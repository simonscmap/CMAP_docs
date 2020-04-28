.. _clim:



Is Climatology Product
======================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Climatology.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FClimatology.ipynb

.. method:: is_climatology(tableName)


    Returns True if the specified dataset represents a climatological product; otherwise returns False.

    |

    :Parameters:
        **tableName: string**
            The name of table associated with the dataset. A full list of table names can be found in the :ref:`Catalog`.



    :returns\:: Boolean.



|

**Example**

..Comment: State what the example does.

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.is_climatology('tblDarwin_Plankton_Climatology')
