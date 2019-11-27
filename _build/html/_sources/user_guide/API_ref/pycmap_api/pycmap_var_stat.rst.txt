.. _varStat:




Variable Stat
=============


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Stat.ipynb


.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FStat.ipynb

.. method:: get_var_stat(tableName, varName)


    Returns summary statistics involving the min, max, mean, standard deviation, count, and quantiles for the given variable.


    |

    :Parameters:
        **tableName: string**
            The name of table associated with the dataset. A full list of table names can be found in the :ref:`Catalog`.
        **variable: string or list of string**
            Variable short name. A full list of variable short names can be found in the :ref:`Catalog`.


    :returns\:: Pandas dataframe.



|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.get_var_stat('tblHOT_LAVA', 'Prochlorococcus')

.. figure:: ../../../_static/overview_icons/sql.png
 :scale: 10 %

**SQL Statement**

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block:: sql

  EXEC uspVariableStat 'tableName', 'varName'

**Example:**

List of satellite Chlorophyll products:

.. code-block:: sql

  EXEC uspVariableStat 'tblHOT_LAVA', 'Prochlorococcus'
