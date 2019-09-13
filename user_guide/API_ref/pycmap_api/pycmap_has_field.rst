.. _hasfield:




If Column Exists
================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target:https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/HasField.ipynb


.. method:: has_field(tableName, varName)


    Returns True if the specified column (field) exists in the table; otherwise returns False.

    |

    :Parameters:
        **tableName: string**
            The name of table associated with the dataset. A full list of table names can be found in the :ref:`Catalog`.
        **variable: string or list of string**
            Variable short name. A full list of variable short names can be found in the :ref:`Catalog`.


    :returns\:: String literal.



|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.has_field('tblAltimetry_REP', 'sla')
