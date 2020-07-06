
Retrieve Data Catalog
=====================

Dataset descriptions and variables names can be accessed through the :ref:`Catalog` or through the getCatalog.py script.

This short Python script will pull all of the variables in the opedia database and write them to a .csv file in ./data/catalog.csv.


.. code:: python

    # Pull catalog from opedia database:
    In [1]: from opedia import getCatalog
