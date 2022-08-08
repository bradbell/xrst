// --------------------------------------------------------------------------
//                      xrst: Extract Sphinx RST Files
//          Copyright (C) 2020-22 Bradley M. Bell (bradbell@seanet.com)
//              This program is distributed under the terms of the
//              GNU General Public License version 3.0 or later see
//                    https://www.gnu.org/licenses/gpl-3.0.txt
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
{xrst_begin file_example}

File Command Example
####################

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

xrst_file
*********
The file below demonstrates the use of ``xrst_file`` .

This Example File
*****************
{xrst_file}

{xrst_end file_example}
------------------------------------------------------------------------------
*/
