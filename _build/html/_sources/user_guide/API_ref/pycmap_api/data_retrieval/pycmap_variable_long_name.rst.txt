.. _var_long_name:




Variable Long Name
==================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/LongName.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FLongName.ipynb


.. method:: get_var_long_name(tableName, varName)




    Returns the long name of a given variable.

    |

    :Parameters:
        **tableName: string**
            The name of the table associated with the dataset. A full list of table names can be found in the :ref:`Catalog`.
        **variable: string or list of string**
            Variable short name. A full list of variable short names can be found in the :ref:`Catalog`.


    :returns: String literal.



|

**Example**

Returns the long name of the short name variable, adt, in the Altimetry Reprocessed dataset.

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.get_var_long_name('tblAltimetry_REP', 'adt')


.. figure:: /_static/overview_icons/sql.png
 :scale: 10 %

**SQL Statement**

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block:: sql

  EXEC uspVariableLongName 'tableName', 'varName'

**Example**

Returns the long name of the short name variable, adt, in the Altimetry Reprocessed dataset.

.. code-block:: sql

  EXEC uspVariableLongName 'tblAltimetry_REP', 'adt'
