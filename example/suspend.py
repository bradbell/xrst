# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
default_dict = dict()
'''
{xrst_begin suspend_example}
{xrst_spell
   toml
}

Suspend Command Example
#######################

Discussion
**********
The project_name paragraph below
was taken from the xrst configure file documentation.

#. The documentation for the default table uses toml file format.
#. The python code that implements this default comes directly after
   and is not displayed in the documentation.

project_name
************
The only value in this table is the name of this project.
The default for this table is

{xrst_code toml}
[project_name]
data = 'project'
{xrst_code}
{xrst_suspend}'''
default_dict['project_name'] = { 'data' : 'project' }
'''{xrst_resume}

This Example File
*****************
{xrst_literal}


{xrst_end suspend_example}
'''
