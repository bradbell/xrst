# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
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
:ref:`indent-0` for the current page.
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
#
# pattern
pattern = dict()
# need \{xrst_comment_ch so it does not match comment_ch command
pattern['error']      = re.compile( r'[^\\]\{xrst_comment_ch[^a-z]' )
pattern['comment_ch'] = xrst.pattern['comment_ch']
#
# Returns the beginning of line comment character for a file.
#
# Comment Character:
# The comment character is specified by \{xrst_comment_ch ch} where ch
# is a single character after leading and trailing white space is removed.
#
# file_data:
# is the original data in this file as one disk. Line numbers may, or may not
# have been added.
#
# file_name:
# is the name of this file (used for error reporting).
#
# comment_ch:
# is a the comment character for this file. It is None when the
# is no comment character command for the file.
#
# comment_ch =
def get_comment_ch(file_data, file_name) :
   assert type(file_data) == str
   assert type(file_name) == str
   #
   # m_obj
   m_obj   = pattern['comment_ch'].search(file_data)
   if not m_obj :
      m_error = pattern['error'].search(file_data)
      if m_error :
         msg  = f'syntax_error in xrst comment_ch command'
         line = file_data[: m_error.start() + 1].count('\n') + 1
         xrst.system_exit(msg, file_name = file_name, line = line)
      #
      # comment_ch
      comment_ch = None
   else :
      #
      # comment_ch
      comment_ch = m_obj.group(2)
      line       = file_data[: m_obj.start() ].count('\n') + 1
      if len( comment_ch ) != 1 :
         msg = 'Expected a single character argument to comment_ch command'
         xrst.system_exit(msg, file_name=file_name, line=line)
      if comment_ch in '.:]' :
         msg  = f'Cannot use {comment_ch} as character in comment_ch command\n'
         xrst.system_exit(msg, file_name=file_name, line=line)
      #
      # m_rest
      data_rest  = file_data[ m_obj.end() : ]
      m_rest     = pattern['error'].search(data_rest)
      if m_rest :
         line = file_data[: m_obj.end() + m_rest.start() ].count('\n') + 1
         msg = 'There are multiple comment_ch commands in this file'
         xrst.system_exit(msg, file_name=file_name, line=line)
   #
   return comment_ch
