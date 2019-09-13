.. _cruise_details:



Cruise Details by Name
======================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/CruiseByName.ipynb


.. method:: cruise_by_name(cruiseName)


    Returns a dataframe containing some details about the specified cruise.
    The details include cruise official name, nickname, ship name, start/end time/location, etc ...

    |

    :Parameters:
        **cruiseName: string**
          The official cruise name. If applicable, you may also use cruise "nickname" ('Diel', 'Gradients_1' ...). A full list of cruise names can be retrieved using cruise method.



    :returns\:: Pandas dataframe.



|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.cruise_by_name('KOK1606')

  # alternatively, you may pass cruise nickname, if exists.
  # below, "meso_scope" is a nickname, the official name is "KM1709"
  # api.cruise_by_name('meso_scope')
