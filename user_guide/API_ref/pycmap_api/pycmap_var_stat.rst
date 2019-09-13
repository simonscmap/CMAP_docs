.. _varStat:




Variable Stat
=============


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Stat.ipynb


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
