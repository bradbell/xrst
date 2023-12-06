// SPDX-License-Identifier: GPL-3.0-or-later
// SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
// SPDX-FileContributor: 2020-23 Bradley M. Bell
/*
-----------------------------------------------------------------------------
{xrst_begin_parent class_example}
{xrst_spell
   var
}

Example Documenting a Class
###########################

Syntax
******
| ``ad_double`` *var* ( *value* , *derivative* )
| ``ad_double`` *other* ( *value* , *derivative* )
| *var*.\ ``value``\ ()
| *var*.\ ``derivative``\ ()
| *var* + *other*
| *var* - *other*
| *var* * *other*
| *var* / *other*

Prototype
*********
{xrst_literal ,
   // BEGIN CTOR, END CTOR
   // BEGIN VALUE, END VALUE
   // BEGIN DERIVATIVE, END DERIVATIVE
   // BEGIN ADD, END ADD
   // BEGIN SUB, END SUB
   // BEGIN MUL, END MUL
   // BEGIN DIV, END DIV
}

Discussion
**********
The class ``ad_double`` implements forward mode Algorithm Differentiation (AD)
for the add, subtract, multiply and divide operations.


Example
*******
The function :ref:`example_ad_double-name` is an example for using this class.

Test
****
The main program :ref:`test_ad_double-name` runs the example above.

{xrst_end class_example}
*/
# include <iostream>

class ad_double {
private:
   const double value_;
   const double derivative_;
public:
   // BEGIN CTOR
   ad_double(double value, double derivative)
   // END CTOR
   : value_(value), derivative_(derivative)
   { }
   // BEGIN VALUE
   double value(void) const
   // END VALUE
   {  return value_; }
   //
   // BEGIN DERIVATIVE
   double derivative(void) const
   // END DERIVATIVE
   {  return derivative_; }
   //
   // BEGIN ADD
   ad_double operator+(const ad_double& other) const
   // END ADD
   {  double value      = value_      + other.value_;
      double derivative = derivative_ + other.derivative_;
      return ad_double(value, derivative);
   }
   //
   // BEGIN SUB
   ad_double operator-(const ad_double& other) const
   // END SUB
   {  double value       = value_      - other.value_;
      double derivative  = derivative_ - other.derivative_;
      return ad_double(value, derivative);
   }
   //
   // BEGIN MUL
   ad_double operator*(const ad_double& other) const
   // END MUL
   {  double value       = value_      * other.value_;
      double derivative  = value_      * other.derivative_
                         + derivative_ * other.value_;
      return ad_double(value, derivative);
   }
   //
   // BEGIN DIV
   ad_double operator/(const ad_double& other) const
   // END DIV
   {  double value       = value_      / other.value_;
      double derivative  = derivative_ / other.value_
         - value_ * other.derivative_ /(other.value_ * other.value_);
      return ad_double(value, derivative);
   }
};

/*
------------------------------------------------------------------------------
{xrst_begin example_ad_double}
{xrst_spell
   ay
   dx
   dy
   ok
}

An Example Using the ad_double Class
####################################
This example mixes the documentation and the example code.
Another choice is to put the documentation and the beginning
an then just have comments in the code.

Begin Function
**************
This function has no arguments and returns a boolean that is true,
if all it's tests pass, and false otherwise.
{xrst_code cpp} */
bool test_ad_double(void)
{
   bool ok = true;
/* {xrst_code}

Independent Variable
********************
{xrst_code cpp} */
   double x  = 2.0;
   double dx = 3.0;
   ad_double ax(x, dx);
/* {xrst_code}

Addition
********
{xrst_code cpp} */
   {  ad_double ay = ax + ax;
      double    dy = ay.derivative();
      ok          &= dy == 2.0 * dx;
   }
/* {xrst_code}

Subtraction
***********
{xrst_code cpp} */
   {  ad_double ay = ax - ax;
      double    dy = ay.derivative();
      ok          &= dy == 0.0;
   }
/* {xrst_code}

Multiplication
**************
{xrst_code cpp} */
   {  ad_double ay = ax * ax;
      double    dy = ay.derivative();
      ok          &= dy == 2.0 * x * dx;
   }
/* {xrst_code}

Division
********
{xrst_code cpp} */
   {  ad_double ay = ax / ax;
      double    dy = ay.derivative();
      ok          &= dy == 0.0;
   }
/* {xrst_code}

End Function
************
ok is true if all the test above pass and false otherwise.
{xrst_code cpp} */
   return ok;
}
/* {xrst_code}
{xrst_end example_ad_double}
------------------------------------------------------------------------------
{xrst_begin test_ad_double}

Run ad_double Example and Check its Result
##########################################
{xrst_literal
   BEGIN MAIN
   END MAIN
}
{xrst_end test_ad_double}
*/
// BEGIN MAIN
int main(void)
{  bool ok = test_ad_double();

   if( ! ok )
   {  std::cerr << "test_ad_double: Error\n";
      return 1;
   }
   std::cout << "test_ad_double: OK\n";
}
// END MAIN
