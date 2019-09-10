.. _metadata:




Metadata
========


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/mdashkezari/pycmapDoc/blob/master/notebooks/MetaData.ipynb


.. method:: get_metadata(table, variable)



    Returns a dataframe containing the associated metadata of a variable (such as data source, distributor, references, and etc..).
    The inputs can be string literals (if only one table, and variable is passed) or a list of string literals.

    |
    
    :Parameters:
        **table: string or list of string**
            The name of table where the variable is stored. A full list of table names can be found in the :ref:`Catalog`.
        **variable: string or list of string\:**
            Variable short name. A full list of variable short names can be found in the :ref:`Catalog`.


    :returns\:: Pandas dataframe.


|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.get_metadata(['tblsst_AVHRR_OI_NRT', 'tblArgoMerge_REP'], ['sst', 'argo_merge_salinity_adj'])
