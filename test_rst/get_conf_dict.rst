.. _get_conf_dict-name:

!!!!!!!!!!!!!
get_conf_dict
!!!!!!!!!!!!!

xrst input file: ``xrst/get_conf_dict.py``

.. meta::
   :keywords: get_conf_dict, get, configuration, dictionary

.. index:: get_conf_dict, get, configuration, dictionary

.. _get_conf_dict-title:

Get Configuration Dictionary
############################
This routine is called before the current working directory is changed to
the *project_directory* (because it determines the project directory)
so it cannot use the xrst :ref:`system_exit-name` .

.. contents::
   :local:

.. meta::
   :keywords: conf_file

.. index:: conf_file

.. _get_conf_dict@conf_file:

conf_file
*********
is the location of the :ref:`run_xrst@conf_file` specified on
the xrst command line.

.. meta::
   :keywords: conf_dict

.. index:: conf_dict

.. _get_conf_dict@conf_dict:

conf_dict
*********
is the python dictionary corresponding to the toml file with the defaults
filled in. All of the values in the dictionary have been check for
the proper type. This includes recursive checking; e.g. a list is checked
to make sure its elements have the proper type.

.. literalinclude:: ../../xrst/get_conf_dict.py
   :lines: 367-369
   :language: py

.. literalinclude:: ../../xrst/get_conf_dict.py
   :lines: 496-497
   :language: py
