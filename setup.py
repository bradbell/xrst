# -----------------------------------------------------------------------------
#                      xsrst: Extract Sphinx RST Files
#          Copyright (C) 2017-21 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# setup
xsrst_version = "21.09.07"
package_name  = "xsrst"
setup_result = setup(
    name         = 'xsrst',
    version      = xsrst_version,
    license      = 'GPL3',
    description  = 'Exract Sphinx RST Files',
    author       = 'Bradley M. Bell',
    author_email = 'bradbell@seanet.com',
    url          = 'https://github.com/bradbell/xsrst',
    scripts      = [ 'bin/xsrst.py' ],
)
