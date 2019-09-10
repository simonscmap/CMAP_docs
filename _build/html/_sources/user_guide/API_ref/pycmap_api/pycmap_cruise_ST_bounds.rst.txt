.. _cruise_ST:



Cruise Spatio-Tempoal Bounds
============================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/mdashkezari/pycmapDoc/blob/master/notebooks/CruiseBounds.ipynb


.. method:: cruise_bounds(cruiseName)



    Returns a dataframe containing the spatio-temporal bounding box accosiated with the specified cruise. Effectively, this method returns a subset of the outputs returend by the cruise_by_name method.

    |

    :Parameters:
        **cruiseName: string**
        The official cruise name. If applicable, you may also use cruise "nickname" ('Diel', 'Gradients_1' ...).
        A full list of cruise names can be retrieved using cruise method.


    :returns\:: Pandas dataframe.



|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.cruise_bounds('KOK1606')
