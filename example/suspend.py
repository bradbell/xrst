# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
# ----------------------------------------------------------------------------
"""
{xrst_begin suspend_example}
{xrst_spell
   toml
}

Suspend Command Example
#######################
This example was taken from the xrst configure file documentation.
It displays a default value using toml file format and
implements this default using python that is not in the documentation.

output_directory
****************
The value corresponding to this key is a dictionary that maps the
*target* command line argument to
the directory where the final output is stored .
The default value for this key is

{xrst_code toml}
output_directory.html = 'html'
output_directory.pdf  = 'pdf'
{xrst_code}
{xrst_suspend}"""
default_dict['output_directory'] = {
   'html' : 'html' ,
   'pdf' : 'pdf'   ,
}
"""{xrst_resume}

Note that the possible values
for *target* are ``'html'`` and ``'pdf'`` and that the default
uses the same name for the output directory.

This Example File
*****************
{xrst_literal}


{xrst_end suspend_example}
"""
