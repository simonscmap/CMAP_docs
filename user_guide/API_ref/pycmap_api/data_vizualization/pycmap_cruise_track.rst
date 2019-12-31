.. _cruiseTrackPlot:


Cruise Track Plot
=================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Viz_CruiseTrack.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FViz_CruiseTrack.ipynb


.. _API key: pycmap_api.html
.. _APIs parameters: pycmap_api.html
.. _cruises(): pycmap_list_cruises.html

.. _cruise: Cruises.ipynb

.. method:: plot_cruise_track(cruise)


    Plots the cruise trajectory on a geospatial map.


    .. note::
      This method requires a valid `API key`_. It is not necessary to set the
      API key every time because the API properties are stored locally after
      being called the first time.



    |

    :Parameters:
        **cruiseName: list of string**
            A list of cruise official names. If applicable, you may also use cruise
            "nickname" ('Diel', 'Gradients_1' ...). A full list of cruise names can
            be retrieved using `cruises()`_ method.


    :returns\:: void
        This method has no returns.

|

Example:
--------

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary
  # uncomment the lines below if the API key has not been registered on your machine, previously.
  # import pycmap
  # pycmap.API(token='<YOUR_API_KEY>')


  from pycmap.viz import plot_cruise_track
  plot_cruise_track(['KM1712', 'gradients_1'])


.. raw:: html

   <iframe src="../../../_static/pycmap_tutorial_viz/html/cruise_track_cruiseTrack.html"  frameborder = 0  height="550px" width="100%">></iframe>
