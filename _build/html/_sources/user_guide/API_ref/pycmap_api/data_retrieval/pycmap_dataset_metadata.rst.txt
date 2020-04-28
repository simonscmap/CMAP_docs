.. _datasetmetadata:




Dataset Metadata
================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/DatasetMetaData.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FDatasetMetaData.ipynb



.. method:: get_dataset_metadata(tableName)



    Returns a dataframe containing the dataset metadata. (such as a list of all variables, data source, distributor, references, and etc..)

    |

    :Parameters:
        **tableName: string**
            The name of the table where the dataset is stored. A full list of table names can be found in the :ref:`Catalog`.

    :returns\:: Pandas dataframe.

|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.get_dataset_metadata('tblArgoMerge_REP')


.. figure:: /_static/overview_icons/sql.png
 :scale: 10 %

**SQL Statement**

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block:: sql

  EXEC uspDatasetMetadata 'tableName'

**Example:**

Metadata associated with the Argo dataset:

.. code-block:: sql

  EXEC uspDatasetMetadata 'tblArgoMerge_REP'
