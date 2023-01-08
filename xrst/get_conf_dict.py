# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2020-23 Bradley M. Bell
# -----------------------------------------------------------------------------
import re
import toml
import sys
#
def system_exit(msg) :
   # assert False, msg
   sys.exit(msg)
# -----------------------------------------------------------------------------
default_dict = dict()
#
'''
{xrst_begin config_file user}
{xrst_spell
   booleans
   conf
   epilog
   frist
   prolog
   pyspellchecker
   rtd
   toc
   toml
}

.. _toml file: https://toml.io/en/

Configuration File for xrst
###########################
A `toml file`_ is used to configure xrst.

#. The location of this file is specified by the xrst
   :ref:`run_xrst@config_file` argument.
#. This file is a sequence of toml tables,
   if a table can only have one entry, the entry is named data.
#. Each table has a default value that is used when the table
   is not present in the toml file.
   All of the defaults below will be the same in future versions
   of xrst with the possible exception of the html theme options
   :ref:`config_file@html_theme_options@Default` .
#. All of the entries in a table have the same type
   as its corresponding default.
   If an entry has components, all of the comments have the same
   type as the default components.
   The html theme options default is one exception to this rule; see
   :ref:`config_file@html_theme_options` .

project_name
************
The only value in this table is the name of this project.

Default
=======
{xrst_code toml}
[project_name]
data = 'project'
{xrst_code}
{xrst_suspend}'''
default_dict['project_name'] = { 'data' : 'project' }
'''{xrst_resume}

Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_PROJECT_NAME
   # END_PROJECT_NAME
}

directory
*********
This table specifies the locations of some xrst directories:

project_directory
=================
This *project_directory* can be an absolute path,
or a path relative to the location where the
:ref:`run_xrst@config_file` is located.
All of the other directories are specified relative to this directory.
The other directories may have ``../`` in their specifications; i.e.,
they do not need to be sub-directories of the project directory.
This directory must exists when xrst is run.

html_directory
==============
This is the directory, relative to the *project_directory*,
where the output files are stored when
:ref:`run_xrst@target` is ``html`` .
If *target* is html and this directory does not exist, it will be created.

tex_directory
=============
This is the directory, relative to the *project_directory*,
where the output files are stored when
:ref:`run_xrst@target` is ``tex`` .
If *target* is tex and this directory does not exist, it will be created.

rst_directory
=============
This is the directory, relative to the *project_directory*,
where xrst writes the rst files it extracts from the source code.
For each :ref:`begin_cmd@page_name` , the file
If this  directory does not exist, it will be created.

|space| *rst_directory*\ /\ *page_name*\ ``.rst``

is the RST file for the corresponding page. There is one exception
to this rule. If *page_name* ends with ``.rst``, the extra ``.rst``
is not added at the end.

Other Generated Files
---------------------
See :ref:`auto_file-title` for the other files generated by ``xrst``
and placed in the *rst_directory*.

Default
=======
Note that '.' denotes the directory where
:ref:`xrst <run_xrst-name>` is run.

{xrst_code toml}
[directory]
project_directory  = '.'
rst_directory      = 'build/rst'
html_directory     = 'build/html'
tex_directory      = 'build/tex'
{xrst_code}
{xrst_suspend}'''
default_dict['directory'] = {
   'project_directory' : '.'    ,
   'rst_directory'     : 'build/rst'  ,
   'html_directory'    : 'build/html' ,
   'tex_directory'     : 'build/tex'  ,
}
'''{xrst_resume}

Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_DIRECTORY
   # END_DIRECTORY
}

root_file
*********
This table maps each :ref:`begin_cmd@group_name`
to its root (top) xrst input file.
These file names are relative to the
:ref:`config_file@directory@project_directory` .
Multiple groups can use the same root file.

Default
=======
{xrst_code toml}
[root_file]
default = 'project.xrst'
{xrst_code}
{xrst_suspend}'''
default_dict['root_file'] = { 'default' : 'project.xrst' }
'''{xrst_resume}

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

spell_package
*************
This str is either 'pyspellchecker' or 'enchant' .
These are the only spell checkers support so far.
If you use one spell checker the other one need not be installed
on your system.

Default
=======
{xrst_code toml}
[spell_package]
data = 'pyspellchecker'
{xrst_code}
{xrst_suspend}'''
default_dict['spell_package'] = { 'data' : 'pyspellchecker' }
'''{xrst_resume}

Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_SPELL_PACKAGE
   # END_SPELL_PACKAGE
}

input_files
***********
This table is used to list the files that should be include in the
documentation if they have a :ref:`begin command<begin_cmd-name>`
for a group in :ref:`run_xrst@group_list` .
The only value in this table is a list of program commands.

Each program command is a list of strings.
The list is the program to execute followed by
the program's command line arguments in order.
The standard output for the program should be a space separated
list of file names to be checked.
If a file name has spaces in it, it should be surrounded by single
or double quotes.
The single and double quotes are not part of the file name.
If this list of strings is empty, no files are checked.

Each program is execute, in order, with the *project_directory*
as the current working directory.
The frist program to return without an error is used for the list of files.
The intention here is that different programs
may be intended for different systems.

If the list of program commands is empty,
no checking of input file list is done.
If the list of program commands is non-empty,
and none of the program commands succeed,
a warning is printed.

Default
=======
{xrst_code toml}
[input_files]
data = [
   [ 'git', 'ls-files' ]
]
{xrst_code}
{xrst_suspend}'''
default_dict['input_files'] = { 'data' : [
   [ 'git', 'ls-files'] ,
] }
'''{xrst_resume}

Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_INPUT_FILES
   # END_INPUT_FILES
}

input_files.sh
==============
{xrst_literal
   bin/input_files.sh
}

html_theme_options
******************
This table maps the :ref:`run_xrst@html_theme` to
the corresponding html_theme_options.
This enable building documentation with different themes without
having to change the toml file between builds.
If *html_theme* does not appear in this mapping, no options are set.

For each theme, the corresponding options are in a dictionary.
The keys of this dictionary are strings, but the values do not
necessarily have the same type as he default case.
In the default below, these values are integers and booleans.

Default
=======
The html_theme_options default value below my change in the future.
{xrst_code toml}
[html_theme_options.sphinx_book_theme]
show_toc_level = 4

[html_theme_options.sphinx_rtd_theme]
navigation_depth = -1
titles_only        = true
{xrst_code}
{xrst_suspend}'''
default_dict['html_theme_options'] = {
   'sphinx_book_theme' : {
      'show_toc_level' : 4
   },
   'sphinx_rtd_theme'  : {
      'navigation_depth' : -1   ,
      'titles_only'      : True ,
   },
}
'''{xrst_resume}

Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_HTML_THEME_OPTIONS
   # END_HTML_THEME_OPTIONS
}

include_all
***********
This table is used to create input that is included
at the beginning or end of every page.
This table has the following keys:

rst_epilog
==========
The value corresponding to this key is a set of rst commands
that get included at the end of every section.
This is the same as the rst_epilog variable in the sphinx conf.py file.

rst_prolog
==========
The value corresponding to this key is a set of rst commands
that get included at the beginning of every section.
This is the same as the rst_epilog variable in the sphinx conf.py file
except that the latex macros are added at the end when
:ref:`run_xrst@target` is html.

latex_macro
===========
The value corresponding to this key is a list of latex macros.
If :ref:`run_xrst@target` is ``html``, these macros get included at the
beginning of every page using the sphinx ``:math`` role in the
rst_epilog variable in the sphinx conf.py file.
Otherwise *target* is ``tex`` and these macros get included once
at the beginning of the corresponding latex document.
It either case they can be used by every page in the documentation.

Default
=======
{xrst_code toml}
[include_all]
rst_epilog = ''
rst_prolog = ''
latex_macro  = []
{xrst_code}
{xrst_suspend}'''
default_dict['include_all'] = {
      'rst_epilog'   : ''     ,
      'rst_prolog'   : ''     ,
      'latex_macro'  : list() ,
}
'''{xrst_resume}


Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_INCLUDE_ALL
   # END_INCLUDE_ALL
}

project_dictionary
******************
The only value in this table is a list of strings.
Each string contains a newline separated list of words.
Leading and trailing white space is not part of each word.
These special words are not considered spelling errors for the entire project.
Special words, for a particular page, are specified using the
:ref:`spell command<spell_cmd-name>`.

Default
=======
{xrst_code toml}
[project_dictionary]
data = []
{xrst_code}
{xrst_suspend}'''
default_dict['project_dictionary'] = { 'data' : list() }
'''{xrst_resume}

Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_PROJECT_DICTIONARY
   # END_PROJECT_DICTIONARY
}

not_in_index
************
The only value in this table is a list of strings.
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

Default
=======
{xrst_code toml}
[not_in_index]
data = []
{xrst_code}
{xrst_suspend}'''
default_dict['not_in_index'] = { 'data' : list() }
'''{xrst_resume}

Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_NOT_IN_INDEX
   # END_NOT_IN_INDEX
}

{xrst_end config_file}
-----------------------------------------------------------------------------
'''
def iterable2string(iterable) :
   iterable = sorted( iterable )
   string = ''
   for item in iterable :
      if string != '' :
         string += ', '
      string += str(item)
   return string
#
# {xrst_begin get_conf_dict dev}
# {xrst_spell
#     conf
#     config
#     toml
# }
# {xrst_comment_ch #}
#
# Get Configuration Dictionary
# ############################
# This routine is called before the current working directory is changed to
# the *project_directory* (because it determines the project directory)
# so it cannot use the xrst :ref:`system_exit-name` .
#
# config_file
# ***********
# is the location of the :ref:`run_xrst@config_file` specified on
# the xrst command line.
#
# conf_dict
# *********
# is the python dictionary corresponding to the toml file with the defaults
# filled in. All of the values in the dictionary have been check for
# the proper type. This includes recursive checking; e.g. a list is checked
# to make sure its elements have the proper type.
#
# {xrst_code py}
# conf_dict =
def get_conf_dict(config_file) :
   assert type(config_file) == str
   # {xrst_code}
   # {xrst_literal
   #     BEGIN_RETURN
   #     END_RETURN
   # }
   # {xrst_end get_conf_dict}
   #
   # msg
   msg  = f'config_file = {config_file}\n'
   #
   # conf_dict
   file_obj  = open(config_file, 'r')
   file_data = file_obj.read()
   conf_dict = toml.loads(file_data)
   #
   # check top level keys in config_file
   for table in conf_dict :
      if table not in default_dict :
         msg += 'This file has the unexpected table:\n'
         msg += f'   {table}\n'
         msg += 'The value table names are:\n'
         msg += iterable2string( default_dict.keys() )
         system_exit(msg)
   #
   # conf_dict
   # also check that all the top keys the correct type
   for table in default_dict :
      default = default_dict[table]
      if table not in conf_dict :
         conf_dict[table] = default
      else :
         table_dict = conf_dict[table]
         if type(table_dict) != dict :
            msg += f'Table {table} is not a python dictionary\n'
            msg += 'it has python type '+ str( type(table_dict) )
            system_exit(msg)
   #
   # directory
   table_dict = conf_dict['directory']
   valid_set = {
      'project_directory',
      'rst_directory',
      'html_directory',
      'tex_directory',
   }
   if set( table_dict.keys() ) != valid_set :
      msg += 'The directory has the following keys:\n'
      msg += iterable2string( table_dict.keys() ) + '\n'
      msg += 'Expected the following keys:\n'
      msg += iterable2string( valid_set ) + '\n'
      system_exit(msg)
   for key in table_dict :
      value = table_dict[key]
      if type(value) != str :
         msg += f'directory.{key} has python type ' + str(type(value))
         system_exit(msg)
   #
   # spell_package
   value = conf_dict['spell_package']['data']
   if value not in [ 'pyspellchecker', 'enchant' ] :
      msg += 'spell_package has is not pyspellchecker or enchant'
      system_exit(msg)
   #
   # root_file
   p_group_name = re.compile( r'[a-z]+' )
   table_dict = conf_dict['root_file']
   for key in table_dict :
      if key == '' :
         msg += 'root_file uses the empty group name\n'
         msg += 'Use default for the empty group name'
         system_exit(msg)
      m_group_name = p_group_name.fullmatch(key)
      if m_group_name == None :
         msg += f'root_file: "{key}" is not a valid group name\n'
         msg += 'A valid group name is a sequence of the letters a-z.'
         system_exit(msg)
      value = table_dict[key]
      if type(value) != str :
         msg += f'root_file.{key} value has python type '
         msg += str(type(value)) + '\n'
         msg += 'Expected it to have type ' + str( str )
         system_exit(msg)
   #
   # input_files
   table_dict = conf_dict['input_files']
   value      = table_dict['data']
   if type(value) != list :
         msg += f'input_files.data has python type '
         msg += str(type(value)) + '\n'
         msg += 'Expected it to have type ' + str( list )
         system_exit(msg)
   for (index1, entry1) in enumerate(value) :
      if type(entry1) != list :
         msg += f'input_files.data[{index1}] has python type '
         msg += str(type(entry1)) + '\n'
         msg += 'Expected it to have type ' + str( list )
         system_exit(msg)
      for (index2, entry2) in enumerate(entry1) :
         if type(entry2) != str :
            msg += f'input_files.data[{index1}][{index2}] has python type '
            msg += str(type(entry1)) + '\n'
            msg += 'Expected it to have type ' + str( str )
            system_exit(msg)
   #
   # html_theme_options
   table_dict = conf_dict['html_theme_options']
   for key in table_dict :
      value = table_dict[key]
      try :
         dict( value )
      except :
         msg += f'html_theme_options.{key} has python type ' + str(type(value))
         msg += '\nExpected it to have type ' + str( dict )
         system_exit(msg)
   #
   # include_all
   table_dict = conf_dict['include_all']
   valid_set  = {
      'rst_epilog',
      'rst_prolog',
      'latex_macro'
   }
   if set(table_dict.keys()) != valid_set :
      msg += 'The include_all has the following keys:\n'
      msg += iterable2string( table_dict.keys() ) + '\n'
      msg += 'Expected the following keys:\n'
      msg += iterable2string( valid_set ) + '\n'
      system_exit(msg)
   for key in [ 'rst_epilog', 'rst_prolog' ] :
      value = table_dict[key]
      if type( value ) != str :
         msg += f'include_all.{key} has python type '
         msg += str(type(value)) + '\n'
         msg += 'Expected it to have type ' + str( str )
         system_exit(msg)
   value = table_dict['latex_macro']
   if type( value ) != list :
      msg += f'include_all.latex_macro has python type '
      msg += str(type(value)) + '\n'
      msg += 'Expected it to have type ' + str( list )
      system_exit(msg)
   for (index, entry) in enumerate(value) :
      if type(entry) != str :
         msg += f'include_all.latex_macro[{index}] has python type '
         msg += str(type(entry)) + '\n'
         msg += 'Expected it to have type ' + str( str )
         system_exit(msg)
   #
   # project_dictionary, not_in_index
   for table in [ 'project_dictionary', 'not_in_index' ] :
      value = conf_dict[table]['data']
      if type(value) != list :
            msg += f'project_dictionary.data has python type '
            msg += str(type(value)) + '\n'
            msg += 'Expected it to have type ' + str( list )
            system_exit(msg)
      for (index, entry) in enumerate(value) :
         if type(entry) != str :
            msg += f'output_direcory.data[{index}] has python type '
            msg += str(type(entry)) + '\n'
            msg += 'Expected it to have type ' + str( str )
            system_exit(msg)
   #
   # BEGIN_RETURN
   assert type(conf_dict) == dict
   return conf_dict
   # END_RETURN
