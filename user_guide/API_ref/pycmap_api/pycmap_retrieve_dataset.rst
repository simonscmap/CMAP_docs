.. _Retrieve_Dataset:



Retrieve Dataset
================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/RetrieveDataset.ipynb


.. method:: get_dataset(tableName)


    Returns the entire dataset.
    It is not recommended to retrieve datasets with more than 1 million rows using this method.
    For large datasets, please use the  :ref:`subset_ST` method and retrieve the data in smaller chunks.
    Note that this method does not return the dataset metadata. Use the :ref:`metadata` method to get the dataset metadata.

    |

    :Parameters:
        **tableName: string**
          The name of table associated with the dataset. A full list of table names can be found in the :ref:`Catalog` or :ref:`Dataset_list` method.


    :returns\:: Pandas dataframe.



|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.get_dataset('tblKM1906_Gradients3_uway_optics')
