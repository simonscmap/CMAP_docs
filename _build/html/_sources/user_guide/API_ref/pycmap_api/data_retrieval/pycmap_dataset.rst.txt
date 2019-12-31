

.. _Dataset_list:


Datasets
========

.. _documentation: https://cmap.readthedocs.io/en/latest/catalog/catalog.html

.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Datasets.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FDatasets.ipynb

.. method:: datasets()


    Returns a dataframe containing the list of datasets hosted by Simons CMAP database.
    The returned dataframe includes the dataset names and the table names storing the datasets.
    This method requires no input.

    A static version of the dataset list can be found at the Simons CMAP
    documentation_.
    Alternatively, the datasets may be explored interactively at Simons CMAP
    website: https://simonscmap.com/catalog

    |


    :returns\:: Pandas dataframe.

.. _Datasets: Datasets.ipynb



|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.datasets()


.. figure:: /_static/overview_icons/sql.png
 :scale: 10 %

**SQL Statement**

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block:: sql

  EXEC uspDatasets
