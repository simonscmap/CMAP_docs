.. _cruise_ST:



Cruise Spatio-Temporal Bounds
=============================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/CruiseBounds.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FCruiseBounds.ipynb

.. method:: cruise_bounds(cruiseName)



    Returns a dataframe containing the spatio-temporal bounding box accosiated with the specified cruise. Effectively, this method returns a subset of the outputs returned by the cruise_by_name method.

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


.. figure:: /_static/overview_icons/sql.png
 :scale: 10 %

**SQL Statement**

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block:: sql

  EXEC uspCruiseByName 'KOK1606'
