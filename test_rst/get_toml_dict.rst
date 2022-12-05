.. include:: xrst_preamble.rst

.. _get_toml_dict-name:

!!!!!!!!!!!!!
get_toml_dict
!!!!!!!!!!!!!

xrst input file: ``xrst/get_toml_dict.py``

.. meta::
   :keywords: get_toml_dict, get, configuration, dictionary

.. index:: get_toml_dict, get, configuration, dictionary

.. _get_toml_dict-title:

Get Configuration Dictionary
############################
This routine is called before the current working directory is changed to
the *project_directory* (because it determines the project directory)
so it cannot use the xrst :ref:`system_exit-name` .

.. contents::
   :local:

.. meta::
   :keywords: toml_file

.. index:: toml_file

.. _get_toml_dict@toml_file:

toml_file
*********
is the location of the :ref:`run_xrst@toml_file` specified on
the xrst command line.

.. meta::
   :keywords: toml_dict

.. index:: toml_dict

.. _get_toml_dict@toml_dict:

toml_dict
*********
is the python dictionary corresponding to the toml file with the defaults
filled in. All of the values in the dictionary have been check for
the proper type. This includes recursive checking; e.g. a list is checked
to make sure its elements have the proper type.

.. literalinclude:: ../../xrst/get_toml_dict.py
   :lines: 342-344
   :language: py

.. literalinclude:: ../../xrst/get_toml_dict.py
   :lines: 451-452
   :language: py
