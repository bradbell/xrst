# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# -----------------------------------------------------------------------------
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
{xrst_begin toml_file user}
{xrst_spell
   booleans
   macros
   newline
   rtd
   toml
}

Configuration File for xrst
###########################
A toml file is used to configure xrst.

#. The location of this file is specified by the xrst
   :ref:`run_xrst@toml_file` argument.
#. This file is a sequence of toml tables,
   if a table can only have one entry, the entry is named data.
#. Each table, has a default value that is used when the table
   is not present in the toml file.
#. All of the entries in the table have the same type
   as its corresponding default.
   If an entry has components, all of the comments have the same
   type as the default components.

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
or a path relative to the location where :ref:`xrst <run_xrst-name>` is run.
All of the other directories are specified relative to this directory.
The other directories may have ``../`` in their specifications; i.e.,
they do not need to be sub-directories of the project directory.

html_directory
==============
This is the directory, relative to the *project_directory*,
where the output files are stored when
:ref:`run_xrst@target` is ``html`` .

pdf_directory
=============
This is the directory, relative to the *project_directory*,
where the output files are stored when
:ref:`run_xrst@target` is ``pdf`` .

rst_directory
=============
This is the directory, relative to the *project_directory*,
where xrst writes the rst files it extracts from the source code.
For each :ref:`begin_cmd@page_name` , the file

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
rst_directory      = 'rst'
html_directory     = 'html'
pdf_directory      = 'pdf'
{xrst_code}
{xrst_suspend}'''
default_dict['directory'] = {
   'project_directory' : '.'    ,
   'rst_directory'     : 'rst'  ,
   'html_directory'    : 'html' ,
   'pdf_directory'     : 'pdf'  ,
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
This table maps the :ref:`group names <begin_cmd@group_name>`
to its root (top) xrst input file.
These file names are relative to the
:ref:`toml_file@directory@project_directory` .
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

preamble
********
This table is used to create a xrst_preamble.rst file that is included
at the beginning of every page.
This table has the following keys:

rst_substitution
================
The value corresponding to this key is a set of rst substitution commands
that get included at the top of every section.

latex_macro
===========
The value corresponding to this key is a list of latex macros.
If :ref:`run_xrst@target` is html, these macros get included at the
top of every page using the sphinx ``:math`` role.
Otherwise *target* is 'pdf' and these macros get included once
at the beginning of the corresponding latex document.
It either case they can be used by every page in the documentation.

Default
=======
{xrst_code toml}
[preamble]
substitution = ''
latex_macro  = []
{xrst_code}
{xrst_suspend}'''
default_dict['preamble'] = {
      'rst_substitution' : ''     ,
      'latex_macro'      : list() ,
}
'''{xrst_resume}


Example
=======
{xrst_literal
   xrst.toml
   # BEGIN_PREAMBLE
   # END_PREAMBLE
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

{xrst_end toml_file}
-----------------------------------------------------------------------------
'''
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
# This routine is called before the current working directory is changed to
# the *project_directory* (because it determines the project directory)
# so it cannot use the xrst :ref:`system_exit-name` .
#
# toml_file
# *********
# is the location of the :ref:`run_xrst@toml_file` specified on
# the xrst command line.
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
   # msg
   msg  = f'toml_file = {toml_file}\n'
   #
   # toml_dict
   file_ptr  = open(toml_file, 'r')
   file_data = file_ptr.read()
   toml_dict = toml.loads(file_data)
   #
   # check top level keys in toml_file
   for table in toml_dict :
      if table not in default_dict :
         msg += f'This file has the unexpected table {table}'
         system_exit(msg)
   #
   # toml_dict
   # also check that all the top keys the correct type
   for table in default_dict :
      default = default_dict[table]
      if table not in toml_dict :
         toml_dict[table] = default
      else :
         table_dict = toml_dict[table]
         if type(table_dict) != dict :
            msg += f'{table} is not a table: it has python type '
            msg += str( type(table_dict) )
            system_exit(msg)
   #
   # directory
   table_dict = toml_dict['directory']
   valid_set = {
      'project_directory',
      'rst_directory',
      'html_directory',
      'pdf_directory',
   }
   if set( table_dict.keys() ) != valid_set :
      msg += 'The directory has the following keys: '
      msg += str( list( table_dict.keys() ) )
      system_exit(msg)
   for key in table_dict :
      value = table_dict[key]
      if type(value) != str :
         msg += f'directory.{key} has python type ' + str(type(value))
         system_exit(msg)
   #
   # root_file
   table_dict = toml_dict['root_file']
   for key in table_dict :
      value = table_dict[key]
      if type(value) != str :
         msg += f'root_file.{key} has python type ' + str(type(value))
         system_exit(msg)
   #
   # html_theme_options
   table_dict = toml_dict['html_theme_options']
   for key in table_dict :
      value = table_dict[key]
      try :
         dict( value )
      except :
         msg += f'html_theme_options.{key} has python type ' + str(type(value))
         system_exit(msg)
   #
   # preamble
   table_dict = toml_dict['preamble']
   if set( table_dict.keys() ) != { 'rst_substitution', 'latex_macro' } :
      msg += 'The preamble has the following keys: '
      msg += str( list( table_dict.keys() ) )
      system_exit(msg)
   value = table_dict['rst_substitution']
   if type( value ) != str :
      msg += f'preamble.rst_substitution has python type '
      msg += str(type(value))
      system_exit(msg)
   value = table_dict['latex_macro']
   if type( value ) != list :
      msg += f'preamble.latex_macro has python type '
      msg += str(type(value))
      system_exit(msg)
   for (index, entry) in enumerate(value) :
      if type(entry) != str :
         msg += f'preamble.latex_macro[{index}] has python type '
         msg += str(type(entry))
         system_exit(msg)
   #
   # project_dictionary, not_in_index
   for table in [ 'project_dictionary', 'not_in_index' ] :
      value = toml_dict[table]['data']
      if type(value) != list :
            msg += f'project_dictionary.data has python type '
            msg += str(type(value))
            system_exit(msg)
      for (index, entry) in enumerate(value) :
         if type(entry) != str :
            msg += f'output_direcory.data[{index}] has python type '
            msg += str(type(entry))
            system_exit(msg)
   #
   # BEGIN_RETURN
   assert type(toml_dict) == dict
   return toml_dict
   # END_RETURN
