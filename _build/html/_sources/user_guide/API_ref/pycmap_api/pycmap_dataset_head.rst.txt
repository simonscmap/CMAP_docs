.. _dataset_head:




Dataset Head
============


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Head.ipynb


.. method:: head(tableName, rows=5)


    Returns top rows of a given dataset.

    |

    :Parameters:
        **tableName: string**
            The name of table associated with the dataset. A full list of table names can be found in the :ref:`Catalog`.
        **rows: int, default: 5**
            Number of top rows to be returned (default 5).


    :returns\:: Pandas dataframe.



|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.head('tblFalkor_2018')
