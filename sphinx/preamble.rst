.. comment xrst preamble.rst

.. |space| unicode:: 0xA0
.. |tab| replace:: |space| |space| |space| |space|

..  comment: These Latex macros can be used by any section. Each maco must be
    defined on its own line and the line must match the regular expression
    \n[ \t]*:math:`\\newcommand\{[^`]*\}`[ \t]*
    They should all be in a '.. rst-class:: hidden' block of preamble.rst

.. rst-class:: hidden

    :math:`\newcommand{\B}[1]{ {\bf #1} }`
    :math:`\newcommand{\R}[1]{ {\rm #1} }`
