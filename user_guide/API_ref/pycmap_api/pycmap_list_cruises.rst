.. _list_cruises:



List of Cruises
===============


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Cruises.ipynb


.. method:: cruises()



    Returns a dataframe containing the details of all cruise expeditions stored at Simons CMAP database. This method requires no input.


    |

    :returns\:: Pandas dataframe.



|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.cruises()
