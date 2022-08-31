// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
// ----------------------------------------------------------------------------
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
{xrst_begin literal_example}

Literal Command Example
#######################

factorial
*********
{xrst_literal
   // BEGIN_FACTORIAL
   // END_FACTORIAL
}

square
******
{xrst_literal
   // BEGIN_SQUARE
   // END_SQUARE
}

xrst_literal
************
The file below demonstrates the use of ``xrst_literal`` .

This Example File
*****************
{xrst_literal}

{xrst_end literal_example}
------------------------------------------------------------------------------
*/
