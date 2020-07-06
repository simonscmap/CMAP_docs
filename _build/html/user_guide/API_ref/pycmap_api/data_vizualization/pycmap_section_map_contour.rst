
.. _sectionMapContour:



Section Map, Section Contour
============================


.. _API key: https://simonscmap.com/apikeymanagement
.. _APIs parameters: https://cmap.readthedocs.io/en/latest/user_guide/API_ref/pycmap_api/pycmap_api_ref.html
.. _`APIs vizEngine`: https://cmap.readthedocs.io/en/latest/user_guide/API_ref/pycmap_api/pycmap_api_ref.html




.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Viz_Section.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FViz_Section.ipynb



.. method:: plot_section(tables, variables, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, exportDataFlag=False, show=True, levels=0)


    Creates section maps for each variable according to the specified
    space-time constraints (dt1, dt2, lat1, lat2, lon1, lon2, depth1,
    depth2). If the specified space-time domain involves multiple dates,
    individual maps are made per date. Prior to creating the section graph,
    the retrieved data is averaged along the meridional direction if
    longitude range is larger than latitude range ( (lon2-lon1) >
    (lat2-lat1) ); otherwise data is averaged along the zonal axis. To
    create contour plots, set the contour **levels** parameter to a positive
    integer number. Note that contour plot is only supported by plotly
    visualization library. Also, ``plot_section()`` function only applies to
    gridded datasets with depth component (e.g. model outputs) and does not
    apply to sparse datasets.


    Change the `APIs vizEngine`_ parameter if you wish to use a different
    visualization library. Returns the generated graph objects in form of a
    python list. One may use the returned objects to modify the graph
    properties.


    .. note::
      This method requires a valid `API key`_. It is not necessary to set the
      API key every time because the API properties are stored locally after
      being called the first time.


    |


    :Parameters:
        **tables: list of string**
            Table names (each dataset is stored in a table). A full list of table names can be found in :ref:`Catalog`.
        **variable: list of string**
            Variable short name which directly corresponds to a field name in the table. A full list of variable short names can be found in :ref:`Catalog`.
        **dt1: string**
            Start date or datetime. This parameter sets the lower bound of the temporal cut.

            Example values: '2016-05-25' or '2017-12-10 17:25:00'.
        **dt2: string**
            End date or datetime. This parameter sets the upper bound of the temporal cut. Example values: '2016-05-25' or '2017-12-10 17:25:00'.
        **lat1: float**
            Start latitude [degree N]. This parameter sets the lower bound of the meridional cut. Note latitude ranges from -90° to 90°.
        **lat2: float**
            End latitude [degree N]. This parameter sets the upper bound of the meridional cut. Note latitude ranges from -90° to 90°.
        **lon1: float**
            Start longitude [degree E]. This parameter sets the lower bound of the zonal cut. Note longitude ranges from -180° to 180°.
        **lon2: float**
            End longitude [degree E]. This parameter sets the upper bound of the zonal cut. Note longitude ranges from -180° to 180°.
        **depth1: float**
            Start depth [m]. This parameter sets the lower bound of the vertical cut. Note depth is a positive number (it is 0 at the surface and increases towards the ocean floor).
        **depth2: float**
            End depth [m]. This parameter sets the upper bound of the vertical cut. Note depth is a positive number (it is 0 at the surface and increases towards the ocean floor).
        **exportDataFlag: boolean, default: False**
          If True, the graph data points are stored on the local machine. The export path and file format are set by the `APIs parameters`_.


        **show: boolean, default: True**
          If True, the graph object is returned and is displayed. The graph file is saved on the local machine at the figureDir directory.
          If False, the graph object is returned but not displayed.
        **levels: int, default: 0**
          Number of contour levels. If 0, regional maps are generated (no contour lines). Currently, contour plots are only supported by plotly visualization library.




    :returns: list of graph objects

      A list of graph objects. Below are the graph's properties and methods.

      :Properties:
        **data: dataframe**
          Graph data points to be visualized.
        **level: int, default: 0**
          Number of contour levels. Only applicable to plotly.
        **cmap: str or cmocean colormap**
          Colormap name. Any matplotlib (e.g. 'viridis', ..) or cmocean (e.g. cmocean.cm.thermal, ..) colormaps can be passed to this property. A full list of matplotlib and cmocean color palettes can be found at the following links:
          https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html

          https://matplotlib.org/cmocean/


        **vmin: float**
          This parameter defines the lower bound of the colorbar.
        **vmax: float**
          This parameter defines the upper bound of the colorbar.
        **height: int**
          Graph's height in pixels.
        **width: int**
          Graph's width in pixels.
        **xlabel: str**
          Graph's x-axis label.
        **ylabel: str**
          Graph's y-axis label.
        **title: str**
          Graphs's title.

    :Methods:
      **render()**
        Displays the plot according to the set properties.

|

Example 1: Section Map
----------------------

This example makes a meridional section map showing the `dissolved
nitrate`_. The retrieved data is averaged along the zonal direction
because the selected region is elongated along the meridional direction:
(lat2-lat1) > (lon2-lon1). The graphs are made using the default
visualization library (plotly) which may be changed by:
``pycmap.API(vizEngine='bokeh')``

.. _dissolved nitrate: https://cmap.readthedocs.io/en/latest/catalog/datasets/Pisces.html#pisces


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary
  # uncomment the lines below if the API key has not been registered on your machine, previously.
  # import pycmap
  # pycmap.API(token='YOUR_API_KEY>')

  from pycmap.viz import plot_section

  go = plot_section(
                   tables=['tblPisces_NRT'],
                   variables=['NO3'],
                   dt1='2016-04-30',
                   dt2='2016-04-30',
                   lat1=10,
                   lat2=60,
                   lon1=-160,
                   lon2=-158,
                   depth1=0,
                   depth2=5000,
                   exportDataFlag=False,
                   show=True
                   )

.. raw:: html

  <iframe src="../../../../_static/pycmap_tutorial_viz/html/section_map_NO3.html"  frameborder = 0  height="550px" width="100%">></iframe>





.. code-block:: python

  # here is how to modify a graph:

  import cmocean

  go[0].cmap = cmocean.cm.balance
  go[0].vmin = 0
  go[0].vmax = 60
  go[0].width = 700
  go[0].height = 800
  go[0].render()

.. raw:: html

  <iframe src="../../../../_static/pycmap_tutorial_viz/html/section_map_modified_NO3.html"  frameborder = 0  height="850px" width="100%">></iframe>




Example 2: Section Contour
--------------------------

This example makes a cross-basins section map showing estimates of `SIO2
concentration`_ calculated by Darwin model.

.. _SIO2 concentration: https://cmap.readthedocs.io/en/latest/catalog/datasets/Darwin_3day.html#darwin-3day


.. code-block:: python


  #!pip install pycmap -q     #uncomment to install pycmap, if necessary
  # uncomment the lines below if the API key has not been registered on your machine, previously.
  # import pycmap
  # pycmap.API(token='YOUR_API_KEY>')

  from pycmap.viz import plot_section

  plot_section(
              tables=['tblDarwin_Nutrient'],
              variables=['SIO2'],
              dt1='2008-01-05',
              dt2='2008-01-05',
              lat1=-50,
              lat2=-46,
              lon1=-180,
              lon2=180,
              depth1=0,
              depth2=2000,
              exportDataFlag=False,
              show=True,
              levels=10
              )

.. raw:: html

   <iframe src="../../../../_static/pycmap_tutorial_viz/html/section_contour_SIO2.html"  frameborder = 0  height="550px" width="100%">></iframe>
