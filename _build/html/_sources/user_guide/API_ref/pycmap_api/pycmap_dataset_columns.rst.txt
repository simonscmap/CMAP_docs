.. _columns:


Dataset Columns
===============


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/mdashkezari/pycmapDoc/blob/master/notebooks/Columns.ipynb


.. method:: columns(table)


    Returns the column names at a given dataset.

    |

    :Parameters:
      **table: string:**
        The name of table associated with the dataset. A full list of table names can be found in the :ref:`Catalog`.


    :returns\:: Pandas dataframe.

|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.columns('tblAMT13_Chisholm')
