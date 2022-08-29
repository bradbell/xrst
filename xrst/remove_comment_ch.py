# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xrst_begin comment_ch_cmd user}
{xrst_spell
   ch
}

Comment Character Command
#########################

Syntax
******
``\{xrst_comment_ch`` *ch* :code:`}`

Purpose
*******
Some languages have a special character that
indicates the rest of the line is a comment.
If you embed sphinx documentation in this type of comment,
you need to inform xrst of the special character so it does
not end up in your ``.rst`` output file.

Command Location
****************
There can be only one occurrence of this command within a file,
it's effect lasts for the entire file, and
it must come before the first :ref:`begin command<begin_cmd>` in the file.
All the other xrst commands must occur between a begin / end command pair.

ch
**
The value of *ch* must be one non white space character.
There must be at least one white space character
between ``xrst_comment_ch`` and *ch*.
Leading and trailing white space around *ch* is ignored.

Input Stream
************
The special character (and one space if present directly after)
is removed from the input stream before any xrst processing; e.g.,
calculating the amount of
:ref:`@indent` for the current section.
For example, if :code:`#` is the special character,
the following input has the heading Factorial
and the ``def`` token indented the same amount:

.. code-block:: py

   # Factorial
   # ---------
   def factorial(n) :
      if n == 1 :
         return 1
      return n * factorial(n-1)


Example
*******
:ref:`comment_ch_example`

{xrst_end comment_ch_cmd}
"""
# ----------------------------------------------------------------------------
import re
import xrst
pattern = dict()
pattern['comment_ch'] = xrst.pattern['comment_ch']
#
# need \{xrst_comment_ch so it does not match comment_ch command
pattern['error']      = re.compile( r'[^\\]\{xrst_comment_ch[^a-z]' )
#
# Removes the beginning of line comment character from file data.
#
# Comment Character:
# The comment character is specified by \{xrst_comment_ch ch} where ch
# is a single character after leading and trailing white space is removed.
#
# data_in:
# is the original data in this file as one disk. Line numbers may, or may not
# have been added.
#
# file_name:
# is the name of this file (used for error reporting).
#
# data_out:
# is a copy of data_in with occurences of the comment character at the
# beginning of each line removed. If there is a space directly after the
# comment character, it is also removed.
#
# data_out =
def remove_comment_ch(data_in, file_name) :
   assert type(data_in) == str
   assert type(file_name) == str
   #
   # m_obj
   m_obj   = pattern['comment_ch'].search(data_in)
   #
   # data_out
   if not m_obj :
      m_error = pattern['error'].search(data_in)
      if m_error :
         msg  = f'syntax_error in xrst comment_ch command'
         line = data_in[: m_error.start() + 1].count('\n') + 1
         xrst.system_exit(msg, file_name = file_name, line = line)
      #
      data_out = data_in
   else :
      #
      # comment_ch
      comment_ch = m_obj.group(2)
      line       = data_in[: m_obj.start() ].count('\n') + 1
      if len( comment_ch ) != 1 :
         msg = 'Expected a single character argument to comment_ch command'
         xrst.system_exit(msg, file_name=file_name, line=line)
      if comment_ch == ']' :
         msg  = 'Cannot use "]" as character in comment_ch command\n'
         xrst.system_exit(msg, file_name=file_name, line=line)
      #
      # m_obj
      data_rest  = data_in[ m_obj.end() : ]
      m_rest     = pattern['error'].search(data_rest)
      if m_rest :
         line = data_in[: m_obj.end() + m_rest.start() ].count('\n') + 1
         msg = 'There are multiple comment_ch commands in this file'
         xrst.system_exit(msg, file_name=file_name, line=line)
      #
      # data_out
      pattern['replace']  = re.compile( r'\n[' + comment_ch + r'] ?' )
      data_out = pattern['replace'].sub(r'\n', data_in)
   return data_out
