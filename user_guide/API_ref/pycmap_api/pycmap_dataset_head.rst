.. _dataset_head:




Dataset Head
============

.. _Datasets: Datasets.ipynb

.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Head.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FHead.ipynb



.. method:: head(tableName, rows=5)


    Returns top rows of a given dataset.

    |

    :Parameters:
      **tableName: string**
        The name of table associated with the dataset. A full list of table names can be found in the :ref:`Catalog` or :ref:`Dataset_list` method.
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


.. figure:: ../../../_static/overview_icons/sql.png
  :scale: 10 %

**SQL Statement**

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block::

  EXEC uspHead 'tableName', 'rows'

**Example:**
Top 5 rows from Falkor data set:

.. code-block::

  EXEC uspHead 'tblFalkor_2018', '5'
