ACCwebsite Project Setup
########################

..  include::   /references.inc

This project is being constructed using :term:`Test-Driven Development`, and
documented using Sphinx_ and the Tut_ extension. Tut_ uses Git_ branches to
mark steps in a tutorial, and I am creating steps for each test set up during
development. The code and documentation are being managed in separate
repositories on GitHub_ and the code is installed as a submodule in the
documentation repository so Sphinx_ can access the code files. (At least that is
the theory!)

Repository Setup
****************

The first thing I do when starting a new project is to create a home for it on
GitHub_. In this case, I set up two projects:

    * `ACCwebsite <http://github.com/rblack42/ACCwebsite.git>`_

    * `ACCwebsite.code <https://github.com/rblack42/ACCwebsite.code.git>`_

Finally, I add the code repository as a submodule of the documentation
repository using this command:

..  code-block:: text

    $ cd ACCwebsite
    $ git submodule add https://github.com/rblack42/ACCwebsite.code.git code

..  vim:filetype=rst spell:
