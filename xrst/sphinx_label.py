# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
import re
import xrst
#
pattern_declare = re.compile(
   r'\n\.\. _([^:\n]+):([^\n]*)\{xrst_line ([0-9]+)@'
)
pattern_use = re.compile(
   r'`([^<\n]+)(<[^>\n]*>)`_[^\n]*\{xrst_line ([0-9]+)@'
)
# ----------------------------------------------------------------------------
# {xrst_begin sphinx_label dev}
#
# Get Labels Declared Using Sphinx Commands
# #########################################
#
# {xrst_comment_ch #}
#
# data_in
# *******
# is the data for one page.
# Line numbers have been added to this data; see
# :ref:`add_line_numbers` .
#
# file_name
# *********
# is the name of the xrst input file corresponding to data_in
# (only used for error reporting).
#
# page_name
# *********
# is the page name corresponding to data_in
# (only used for error reporting).
#
# external_line
# *************
# For each label declared in data_in using sphinx commands,
# and that links to an external web site,
# *external_line* [ *label*.lower() ] is the line number in
# *file_name* where the label was defined.
#
# internal_line
# *************
# For each label declared in data_in using sphinx commands,
# and that links to a page in this web site,
# *internal* [ *label* ] is the line number in
# *file_name* where the label was defined.
#
# Errors
# ******
# If two or external labels have the same lower case value,
# an error is reported using :ref:`system_exit` .
#
# {xrst_code py}
# external_line, internal_line =
def sphinx_label(data_in, file_name, page_name) :
   assert type(data_in) == str
   assert type(file_name) == str
   assert type(page_name) == str
   # {xrst_code}
   # {xrst_literal
   #     BEGIN_return
   #     END_return
   # }
   # {xrst_end sphinx_label}
   #
   # external_line, internal_line
   external_line  = dict()
   internal_line  = dict()
   #
   # pattern
   for pattern in [ pattern_declare, pattern_use ] :
      #
      # m_label
      m_label    = pattern.search(data_in)
      while m_label :
         #
         # label_lower, line
         label       = m_label.group(1).strip(' ')
         label_lower = label.lower()
         destination = m_label.group(2).strip(' ')
         line        = m_label.group(3)
         #
         if label_lower == page_name :
            msg  = 'A label has the same lower case value as the page_name\n'
            msg += f'label.lower() = {label_lower}'
            xrst.system_exit(
               msg, file_name = file_name, page_name = page_name, line = line
            )
         #
         if label_lower in external_line :
            previous_line = external_line[label_lower]
            msg  = 'A previous label has the same lower case value\n'
            msg += f'label.lower() = {label_lower}\n'
            msg += f'previous_line = {previous_line}'
            xrst.system_exit(
               msg, file_name = file_name, page_name = page_name, line = line
            )
         #
         # external_line, internal_line
         external =  destination != ''
         if external :
            external_line[label_lower] = line
         else :
            internal_line[label] = line
         #
         # m_label
         m_label = pattern.search(data_in, m_label.end())
   # BEGIN_return
   for result in [ external_line, internal_line ] :
      assert type(result) == dict
      for key in result.keys() :
         assert type( result[key] ) == str
   #
   return external_line, internal_line
   # END_return
