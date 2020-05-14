
.. _getcatalog:


Catalog
=======


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Catalog.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FCatalog.ipynb


.. method:: get_catalog()

    Returns a dataframe containing the details of all variables at Simons CMAP database.
    This method requires no input.

    A static version of the :ref:`Catalog` can be found at the Simons CMAP documentation.

    Alternatively, the catalog may be explored interactively at Simons CMAP website: https://simonscmap.com


    |

    :returns: Pandas dataframe.






**Example**

.. code-block:: python


  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.get_catalog()


.. figure:: /_static/overview_icons/sql.png
 :scale: 10 %

**SQL Statement**

..COMMENT: Icon size is ok. I would put the icon and the "SQL Statement" side by side instead of the icon over the text. 

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block:: sql

  EXEC uspCatalog
