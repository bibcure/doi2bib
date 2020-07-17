========
Examples
========


Given a DOI number...
---------------------


.. code-block:: bash

    $ doi2bib 10.1038/s41524-017-0032-0

You can easily append a bib into a bibfile, just do


.. code-block:: bash

    $ doi2bib 10.1038/s41524-017-0032-0 >> file.bib

You also can generate a bibtex from a txt file containing a list of DOIs

.. code-block:: bash

    $ doi2bib --input file_with_dois.txt --output refs.bib