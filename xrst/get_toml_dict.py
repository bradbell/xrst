# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# -----------------------------------------------------------------------------
import toml
# -----------------------------------------------------------------------------
'''
{xrst_begin toml_file user}
{xrst_spell
  macros
  newline
  toml
}

Configuration File for xrst
###########################
A toml file is used to configure xrst.
This file represents a python dictionary

#. Each key, in this dictionary,
   has a default value that is used when the key is not present
   in the toml file.
#. All of the keys are strings and all the values have the same type
   as its corresponding default.
   If a value is has components, all of the comments have the same
   type as the default components.
#. All of the directories mentioned below are relative to the
   :ref:`run_xrst@toml_path@project_directory`;
   i.e.; the directory where the toml file is located.

project_name
************
The value corresponding to this key is a string specifying the
name of this project.
The default value for this key is
{xrst_code toml}'''
project_name = 'project'
'''{xrst_code}

Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_PROJECT_NAME
   # END_PROJECT_NAME
}

root_file
*********
The value corresponding to this key is a dictionary that maps the
:ref:`group names <begin_cmd@group_name>`
to its top level xrst input file.
Note that multiple groups an use the same input file.
The default value for this key is
{xrst_code toml}'''
root_file = { 'default' : 'project.xrst' }
'''{xrst_code}
Note that ``default`` corresponds to the
:ref:`begin_cmd@group_name@Default Group` and ``project.xrst``
is the default root file.

Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_ROOT_FILE
   # END_ROOT_FILE
}

output_directory
****************
The value corresponding to this key is a dictionary that maps the
:ref:`run_xrst@target` to the
directory where the final output is stored .
The default value for this key is
{xrst_code toml}'''
output_directory = {
   'html' : 'html' ,
   'pdf' : 'pdf'   ,
}
'''{xrst_code}
Note that the possible values
for *target* are ``'html'`` and ``'pdf'`` and that the default
uses the same name for the output directory.

Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_OUTPUT_DIRECTORY
   # END_OUTPUT_DIRECTORY
}

rst_directory
*************
The value corresponding to this key is a string specifying the
directory where xrst writes the rst files it extracts from the source code.
For each :ref:`begin_cmd@page_name` , the file

|space| *rst_directory*\ /\ *page_name*\ ``.rst``

is the RST file for the corresponding page. There is one exception
to this rule. If *page_name* ends with ``.rst``, the extra ``.rst``
is not added at the end.
The default value for this key is
{xrst_code toml}'''
rst_directory = 'rst'
'''{xrst_code}

Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_RST_DIRECTORY
   # END_RST_DIRECTORY
}

preamble
********
The value corresponding to this key is a string specifying the
preamble.rst file.
This file is included at the beginning of every xrst output page.
It should only define things, it should not generate any output.
The Latex macros in this file can be used by any page.
There must be one macro definition per line and each such line must match the
following python regular expression:

   ``\n[ \t]*:math:`\\newcommand\{[^`]*\}`[ \t]*``

The default value for this key is
{xrst_code toml}'''
preamble = ''
'''{xrst_code}

Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_PREAMBLE
   # END_PREAMBLE
}

project_dictionary
******************
The value corresponding to this key is list of a strings.
Each string contains a newline separated list of words.
Leading and trailing white space is not part of each word.
These special words are not considered spelling errors for the entire project.
Special words, for a particular page, are specified using the
:ref:`spell command<spell_cmd>`.
The default value for this key is
{xrst_code toml}'''
project_dictionary = []
'''{xrst_code}

Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_PROJECT_DICTIONARY
   # END_PROJECT_DICTIONARY
}

not_in_index
************
The value corresponding to this key is list of a strings.
Each string  contains a newline separated list of patterns.
Leading and trailing white space is not part of each pattern.
These are python regular expression patterns for heading tokens
that are not included in the index.
A heading token is any sequence of non white space characters
with upper case letters converted to lower case.
For example, a heading might contain the token ``The`` but you
might not want to include ``the`` as a entry in the :ref:`genindex`.
In this case you could have a line containing just ``the`` .
For another example, you might want to exclude all tokens that are
integer numbers.
In this case you could have a line containing just ``[0-9]*`` .
The default value for this key is
{xrst_code toml}'''
not_in_index = []
'''{xrst_code}

Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_NOT_KEYWORD
   # END_NOT_KEYWORD
}

{xrst_end toml_file}
-----------------------------------------------------------------------------
'''
#
# key_list
key_list = list()
for key in dir() :
   if not key.startswith( '__' ) :
      key_list.append(key)
#
# {xrst_begin get_toml_dict dev}
# {xrst_comment_ch #}
# {xrst_spell
#     toml
#     dict
# }
#
# Get Configuration Dictionary
# ############################
#
# toml_file
# *********
# is the :ref:`toml_file` corresponding to the configuration.
#
# toml_dict
# *********
# is the python dictionary corresponding to the toml file with the defaults
# filled in. All of the values in the dictionary have been check for
# the proper type. This includes recursive checking; e.g. a list is checked
# to make sure its elements have the proper type.
#
# {xrst_code py}
# toml_dict =
def get_toml_dict(toml_file) :
   assert type(toml_file) == str
   # {xrst_code}
   # {xrst_literal
   #     BEGIN_RETURN
   #     END_RETURN
   # }
   # {xrst_end get_toml_dict}
   #
   # toml_dict
   file_ptr  = open(toml_file, 'r')
   file_data = file_ptr.read()
   toml_dict = toml.loads(file_data)
   #
   # check top level keys in toml_file
   for key in toml_dict :
      if key not in key_list :
         msg  = f'toml_file = {toml_file}\n'
         msg += f'This file has the unexpected top level key {key}'
         xrst.system_exit(msg)
   #
   # toml_dict
   # also check that all the top level values have the correct type
   for key in key_list :
      default = eval(key)
      if key not in toml_dict :
         toml_dict[key] = default
      else :
         value = toml_dict[key]
         if type(value) != type(default) :
            msg  = 'This file  output_directory[{key}] has type '
            msg += str( type(value) )
            xrst.system_exit(msg)
   #
   # root_file
   value = toml_dict['root_file']
   for key in value :
      if type( value[key] ) != str :
         msg  = f'toml_file = {toml_file}\n'
         msg += f'root_file[{key}] has type ' + str(type(value[key]))
         xrst.system_exit(msg)
   #
   # output_directory
   value = toml_dict['output_directory']
   if set( value.keys() ) != { 'html', 'pdf' } :
      msg  = f'toml_file = {toml_file}\n'
      msg += 'output_directory.keys() = '
      msg += str( value.keys() )
      xrst.system_exit(msg)
   for key in value :
      if type( value[key] ) != str :
         msg  = f'toml_file = {toml_file}\n'
         msg += f'output_directory[{key}] has type ' + str(type(value[key]))
         xrst.system_exit(msg)
   #
   # project_dictionary
   value = toml_dict['project_dictionary']
   for (index, entry) in enumerate(value) :
      if type(entry) != str :
         msg  = f'toml_file = {toml_file}\n'
         msg += f'project_dictionary[{index}] has type ' + str(type(entry))
         xrst.system_exit(msg)
   #
   # not_in_index
   value = toml_dict['not_in_index']
   for (index, entry) in enumerate(value) :
      if type(entry) != str :
         msg  = f'toml_file = {toml_file}\n'
         msg += f'not_in_index[{index}] has type ' + str(type(entry))
         xrst.system_exit(msg)
   #
   # BEGIN_RETURN
   assert type(toml_dict) == dict
   return toml_dict
   # END_RETURN
