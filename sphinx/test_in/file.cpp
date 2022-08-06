// --------------------------------------------------------------------------
//                      xrst: Extract Sphinx RST Files
//          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
/*
------------------------------------------------------------------------------
{xrst_begin_parent file_example}

File Command Example
####################
{xrst_file}

{xrst_end file_example}
------------------------------------------------------------------------------
*/
// BEGIN_FACTORIAL
template<class T> factorial(const T& n)
{   if n == static_cast<T>(1)
        return n;
    return n * factorial(n - 1);
}
// END_FACTORIAL
//
// BEGIN_SQUARE
template<class T> square(const T& x)
// END_SQUARE
{   return x * x;
}
/*
------------------------------------------------------------------------------
{xrst_begin file_start_stop}

File Start and Stop Example
###########################

factorial
*********
{xrst_file
    // BEGIN_FACTORIAL
    // END_FACTORIAL
}

square
******
{xrst_file
    // BEGIN_SQUARE
    // END_SQUARE
}

{xrst_end file_start_stop}
------------------------------------------------------------------------------
*/
