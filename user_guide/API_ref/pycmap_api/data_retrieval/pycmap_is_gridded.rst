.. _gridded:



Is Gridded Product
==================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Grid.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FGrid.ipynb


.. method:: is_grid(tableName, varName)



Returns True if the specified variable represents a gridded product; otherwise returns False. For instance, model outputs or satellite products in form of structured arrays are considered gridded products, while underway cruise measurements with irregular spatial or temporal resolutions are considered "sparse" products.

    :Parameters:
        **tableName: string**
            The name of table associated with the dataset. A full list of table names can be found in the :ref:`Catalog`.
        **varName: string or list of string**
            Variable short name. A full list of variable short names can be found in the :ref:`Catalog`.


    :returns\:: Boolean.



|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.is_grid('tblArgoMerge_REP', 'argo_merge_salinity_adj')
