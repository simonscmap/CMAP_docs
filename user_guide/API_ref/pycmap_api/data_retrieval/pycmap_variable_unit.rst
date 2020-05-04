.. _var_unit:




Variable Unit
=============


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Unit.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FUnit.ipynb



.. method:: get_unit(tableName, varName)


    Returns the unit for a given variable, if applicable.

    |

    :Parameters:
        **tableName: string**
            The name of table associated with the dataset. A full list of table names can be found in the :ref:`Catalog`.
        **varName: string or list of string**
            Variable short name. A full list of variable short names can be found in the :ref:`Catalog`.


    :returns: String literal.



|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.get_unit('tblHOT_ParticleFlux', 'silica_hot')

.. figure:: /_static/overview_icons/sql.png
 :scale: 10 %

**SQL Statement**

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block:: sql

  EXEC uspVariableUnit 'tableName', 'varName'

**Example:**

.. code-block:: sql

  EXEC uspVariableUnit 'tblHOT_ParticleFlux', 'silica_hot'
