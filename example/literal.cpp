// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: 2020-22 Bradley M. Bell <bradbell@seanet.com>
// ----------------------------------------------------------------------------
// BEGIN_FACTORIAL
template<class T> factorial(const T& n)
// END_FACTORIAL
{   if n == static_cast<T>(1)
      return n;
   return n * factorial(n - 1);
}
//
// BEGIN_SQUARE
template<class T> square(const T& x)
// END_SQUARE
{   return x * x;
}
// BEGIN_TANGENT
template<class T> tangent(const T& x)
// END_TANGENT
{  return sin(x) / cos(x);
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

tangent
*******
{xrst_literal
   example/literal.cpp
   // BEGIN_TANGENT
   // END_TANGENT
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
