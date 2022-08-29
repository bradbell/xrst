# -----------------------------------------------------------------------------
#                      xrst: Extract Sphinx RST Files
#          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
import re
import toml
import xrst
#
# Replace spelling commands using spell.toml.
#
# tmp_dir:
# is the directory where spell.toml is located; see
# spell_command.py for the spell.toml specifications.
#
def replace_spell(tmp_dir) :
   assert type(tmp_dir) == str
   #
   # spell_toml
   file_ptr  = open( f'{tmp_dir}/spell.toml' )
   file_data = file_ptr.read()
   spell_toml = toml.loads(file_data)
   #
   # file_name
   for file_name in spell_toml :
      #
      # section_list
      section_list = list()
      for section_name in spell_toml[file_name] :
         pair = (section_name , spell_toml[file_name][section_name] )
         section_list.append( pair )
      #
      # section_list
      order_fun    = lambda section_pair : section_pair[1]['begin_line']
      section_list = sorted(section_list, key = order_fun )
      #
      # data_in
      file_ptr = open(file_name, 'r')
      data_in  = file_ptr.read()
      file_ptr.close()
      #
      # comment_ch
      # m_comment.group(1) is checked duriung remove_comment_ch
      m_comment = xrst.pattern['comment_ch'].search(data_in)
      if m_comment :
         comment_ch = m_comment.group(1)
      else :
         comment_ch = None
      #
      # section_list
      # add begin_index, start_index, end_index
      line_number = 0
      for m_newline in re.finditer( r'(^|\n)',  data_in) :
         line_number += 1
         for section_name, section_info in section_list :
            if section_info['begin_line'] + 1 == line_number :
               section_info['begin_index'] = m_newline.start() + 1
            if section_info['start_spell'] == line_number :
               section_info['start_index'] = m_newline.start() + 1
            if section_info['end_spell'] + 1 == line_number :
               section_info['end_index'] = m_newline.start() + 1
      #
      # data_copy
      data_copy = data_in
      data_copy = xrst.add_line_numbers(data_copy)
      data_copy = xrst.remove_comment_ch(data_copy, file_name)
      #
      # data_out
      data_out      = ''
      data_in_index = 0
      #
      # section_name, section_info
      for section_name, section_info in section_list :
         #
         # m_begin
         m_begin = xrst.pattern['begin'].search(data_copy)
         while m_begin.group(3) != section_name :
            m_begin = xrst.pattern['begin'].search(data_copy, m_begin.end())
         #
         # m_end
         m_end = xrst.pattern['end'].search(data_copy, m_begin.end() )
         #
         # section_data
         section_data = data_copy[m_begin.end() : m_end.start() ]
         #
         # indent
         not_used, indent = xrst.remove_indent(
            section_data, file_name, section_name
         )
         if comment_ch != None :
            indent = comment_ch + ' '
         #
         # data_out, data_in_index
         begin_index   = section_info['begin_index']
         data_out     += data_in[data_in_index : begin_index]
         data_in_index = begin_index
         #
         # data_out
         unknown = section_info['unknown']
         if len(unknown) > 0 :
            data_out += indent + '{xrst_spell\n'
            unknown   = sorted(unknown)
            i         = 0
            while i < len(unknown) :
               word = unknown[i]
               if i + 1 < len(unknown) and word == unknown[i+1] :
                  data_out += indent + 3 * ' ' + word + ' ' + word + '\n'
                  i         = i + 2
               else :
                  data_out += indent + 3 * ' ' + word + '\n'
                  i         = i + 1
            data_out += indent + '}\n'
         #
         # data_out, data_in_index
         if 'start_index' in section_info :
            start_index  = section_info['start_index']
            end_index    = section_info['end_index']
            #
            data_out     += data_in[data_in_index : start_index]
            data_in_index = end_index
      #
      # data_out
      data_out += data_in[data_in_index :]
      #
      # file_name
      file_ptr = open(file_name, 'w')
      file_ptr.write( data_out )
      file_ptr.close()
   #
   return
