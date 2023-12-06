.. _class_example-name:

!!!!!!!!!!!!!
class_example
!!!!!!!!!!!!!

.. meta::
   :keywords: class_example, documenting, class

.. index:: class_example, documenting, class

.. _class_example-title:

Example Documenting a Class
###########################

.. contents::
   :local:

.. _class_example@Syntax:

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

.. meta::
   :keywords: prototype

.. index:: prototype

.. _class_example@Prototype:

Prototype
*********

.. literalinclude:: ../../example/class.cpp
   :lines: 58-58,63-63,68-68,73-73,81-81,89-89,98-98
   :language: cpp

.. meta::
   :keywords: discussion

.. index:: discussion

.. _class_example@Discussion:

Discussion
**********
The class ``ad_double`` implements forward mode Algorithm Differentiation (AD)
for the add, subtract, multiply and divide operations.

.. _class_example@Example:

Example
*******
The function :ref:`example_ad_double-name` is an example for using this class.

.. meta::
   :keywords: test

.. index:: test

.. _class_example@Test:

Test
****
The main program :ref:`test_ad_double-name` runs the example above.

.. csv-table::
   :header: "Child", "Title"
   :widths: 20, 80

   "example_ad_double", :ref:`example_ad_double-title`
   "test_ad_double", :ref:`test_ad_double-title`

.. toctree::
   :maxdepth: 1
   :hidden:

   example_ad_double
   test_ad_double
