

.. _Dataset_list:


Datasets
========

.. _documentation: https://cmap.readthedocs.io/en/latest/catalog/catalog.html

.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Datasets.ipynb


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
