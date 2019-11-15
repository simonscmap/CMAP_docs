.. _cruiseVars:



Cruise Variables
================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/CruiseVariables.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FCruiseVariables.ipynb


.. method:: cruise_variables(cruiseName)


    Returns a dataframe containing all registered variables (at Simons CMAP) during the specified cruise.

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
  api.cruise_variables('SCOPE_Falkor1')
