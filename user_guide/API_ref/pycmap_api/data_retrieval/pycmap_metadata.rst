.. _metadata:



Metadata
========


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/MetaData.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FMetaData.ipynb



.. method:: get_metadata(table, variable)



    Returns a dataframe containing the associated metadata of a variable (such as data source, distributor, references, and etc.).
    The inputs can be string literals (if only one table, and variable is passed) or a list of string literals.

    |

    :Parameters:
        **table: string or list of string**
            The name of table where the variable is stored. A full list of table names can be found in the :ref:`Catalog`.
        **variable: string or list of string\:**
            Variable short name. A full list of variable short names can be found in the :ref:`Catalog`.


    :returns: Pandas dataframe.

|

**Example**

Retrieve dataset metadata for the satellite SST and Argo salinity datasets.

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.get_metadata(['tblsst_AVHRR_OI_NRT', 'tblArgoMerge_REP'], ['sst', 'argo_merge_salinity_adj'])


.. figure:: /_static/overview_icons/sql.png
 :scale: 10 %

**SQL Statement**

..COMMENT: I would align the SQL icon and "SQL Statement" side by side. 

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block:: sql

  EXEC uspVariableMetaData 'table', 'variable'

**Example:**

Metadata associated with Argo salinity measurements:

.. code-block:: sql

  EXEC uspVariableMetaData 'tblArgoMerge_REP', 'argo_merge_salinity_adj'
