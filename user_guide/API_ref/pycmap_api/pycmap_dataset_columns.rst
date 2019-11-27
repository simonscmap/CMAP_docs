.. _columns:


Dataset Columns
===============


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Columns.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FColumns.ipynb



.. method:: columns(table)


    Returns the column names at a given dataset.

    |

    :Parameters:
      **tableName: string**
        The name of table associated with the dataset. A full list of table names can be found in the :ref:`Catalog` or :ref:`Dataset_list` method.




|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.columns('tblAMT13_Chisholm')



.. figure:: ../../../_static/overview_icons/sql.png
 :scale: 10 %

**SQL Statement**

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block:: sql

  EXEC uspColumns 'tableName'

**Example:**

Metadata associated with Argo salinity measurement

.. code-block:: sql

  EXEC uspColumns 'tblAMT13_Chisholm'
