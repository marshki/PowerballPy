PowerballPy :8ball:
========================================================================================
|travis| |codacy| |maintained| |python| |mit| |open source|

.. |travis| image:: https://app.travis-ci.com/marshki/PowerballPy.svg?branch=master
    :target: https://app.travis-ci.com/marshki/PowerballPy
    :alt: Travis

.. |codacy| image:: https://api.codacy.com/project/badge/Grade/7f03d830dacb4b5cbf229739510fc1a2
   :target: https://www.codacy.com/manual/marshki/PowerballPy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=marshki/PowerballPy&amp;utm_campaign=Badge_Grade
   :alt: Codacy

.. |maintained| image:: https://img.shields.io/badge/Maintained%3F-yes-green.svg
   :target: https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity
   :alt: Maintained

.. |python| image:: https://img.shields.io/badge/Made%20with-Python-1f425f.svg
   :target: https://www.python.org/
   :alt: Python

.. |mit| image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://lbesson.mit-license.org/
   :alt: MIT

.. |open source| image:: https://badges.frapsoft.com/os/v3/open-source.svg?v=103
   :target: https://github.com/ellerbrock/open-source-badges/
   :alt: Open Source

Powerball Number Generator
--------------------------

Pseudo-random number generator for Powerball_ lottery in Python 3.

.. _Powerball: https://www.powerball.com/games/home 


Requirements
------------
Install Python3 requirements:

.. code-block:: Python3

    pip3 install -r requirements.txt

Usage
-----
Run directly from a shell in Python3:

.. code-block:: Python3

    python3 powerballPy.py --n 5

or:

.. code-block:: Python3 

    python3 powerballPy.py --num_sets 5
    
Program generates the following set:

* five (5) distinct pseudo-random numbers between 1 and 69, and
* one (1) pseudo-random number between 1 and 26.

to a PrettyTable_ .

.. _PrettyTable: https://pypi.org/project/PrettyTable

User designates the number of sets they'd like to create. Default is one (1) set.

Sample Output
-------------
+--------------------+-------+
| White #s           | Red # | 
+====================+=======+
| 12, 49, 22, 18, 20 | 18    | 
+--------------------+-------+
| 27, 20, 25, 13, 3  | 14    | 
+--------------------+-------+
| 20, 47, 64, 5, 26  | 11    | 
+--------------------+-------+
| 10, 54, 40, 39, 6  | 20    | 
+--------------------+-------+
| 30, 23, 63, 3, 25  | 8     | 
+--------------------+-------+

Change Log
----------
CHANGELOG_

.. _CHANGELOG: https://github.com/marshki/PowerballPy/blob/master/CHANGELOG.rst

License
-------
LICENSE_

.. _LICENSE: https://github.com/marshki/PowerballPy/blob/master/LICENSE 
