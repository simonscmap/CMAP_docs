
.. _rmCp3d:



Regional Map, Contour Plot, 3D Surface Plot
===========================================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Viz_RegionalMap.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FViz_RegionalMap.ipynb

.. _API key: pycmap_api.html
.. _APIs parameters: pycmap_api.html
.. _APIs vizEngine: pycmap_api.html



.. method:: plot_map(tables, variables, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, exportDataFlag=False, show=True, levels=0, surface3D=False)


    Creates map graphs for each variable according to the specified space-time constraints (dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2). If the specified space-time domain involves multiple dates and/or depth levels, individual maps are made per date and depth level. To create contour plots, set the contour **levels** parameter to a positive integer number. Also, setting the **surface3D** parameter to True will generate maps in 3D mode. Note that contour and 3D sufrace maps are only supported by plotly visualization library. In the case of sparse dataset, the retrieved data is superimposed on a geospatial map.


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
            Example values: '2016-05-25' or '2017-12-10 17:25:00'
        **dt2: string**
            End date or datetime. This parameter sets the upper bound of the temporal cut.
        **lat1: float**
            Start latitude [degree N]. This parameter sets the lower bound of the meridional cut. Note latitude ranges from -90° to 90°.
        **lat2: float**
            End latitude [degree N]. This parameter sets the upper bound of the meridional cut. Note latitude ranges from -90° to 90°.
        **lon1: float**
            Start longitude [degree E]. This parameter sets the lower bound of the zonal cut. Note latitude ranges from -180° to 180°.
        **lon2: float**
            End longitude [degree E]. This parameter sets the upper bound of the zonal cut. Note latitude ranges from -180° to 180°.
        **depth1: float**
            Start depth [m]. This parameter sets the lower bound of the vertical cut. Note depth is a positive number (it is 0 at surface and grows towards ocean floor).
        **depth2: float**
            End depth [m]. This parameter sets the upper bound of the vertical cut. Note depth is a positive number (it is 0 at surface and grows towards ocean floor).
        **exportDataFlag: boolean, default: False**
          If True, the graph data points are stored on the local machine. The export path and file format are set by the `APIs parameters`_.
        **levels: int, default: 0**
          Number of contour levels. If 0, regional maps are generated (no contour lines). Currently, contour plots are only supported by plotly visualization library.
        **surface3D: boolean, default: False**
          If True, maps are rendered in 3D mode. Currently, 3D map plots are only supported by plotly visualization library.




    :returns\:: list of graph objects
      A list of graph objects. Below are the graph's properties and methods.

      :Properties:
        **data: dataframe**
          Graph data points to be visualized.
        **level: int, default: 0**
          Number of contour levels. Only applicable to plotly.
        **surface3D: boolean, default: False**
          If True, maps are rendered in 3D mode. Only applicable to plotly.
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
          The graphs's x-axis label.
        **ylabel: str**
          The graphs's y-axis label.
        **title: str**
          The graphs's title.

    :Methods:
      **render()**
        Displays the plot according to the set properties.

|

Example 1: Gridded Maps
-----------------------


This example makes two regional maps showing the `phosphate
climatology`_ and `dissolved iron`_, respectively. The graphs are made
using the default visualization library (plotly) which may be changed
by: ``pycmap.API(vizEngine='bokeh')``

.. _phosphate climatology: https://cmap.readthedocs.io/en/latest/catalog/datasets/WOA_climatology.html#woa-clim
.. _dissolved iron: https://cmap.readthedocs.io/en/latest/catalog/datasets/Pisces.html#pisces

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary
  # uncomment the lines below if the API key has not been registered on your machine, previously.
  # import pycmap
  # pycmap.API(token='YOUR_API_KEY>')

  from pycmap.viz import plot_map

  go = plot_map(
               tables=['tblWOA_Climatology', 'tblPisces_NRT'],
               variables=['phosphate_WOA_clim', 'Fe'],
               dt1='2016-04-30',
               dt2='2016-04-30',
               lat1=10,
               lat2=70,
               lon1=-180,
               lon2=-80,
               depth1=0,
               depth2=0.5,
               exportDataFlag=False,
               show=True
               )

.. raw:: html

  <iframe src="../../../../_static/pycmap_tutorial_viz/html/gridded_map_phosphate_WOA_clim.html"  frameborder = 0  height="550px" width="100%">></iframe>



.. raw:: html

  <iframe src="../../../../_static/pycmap_tutorial_viz/html/gridded_map_Fe.html"  frameborder = 0  height="550px" width="100%">></iframe>



.. code-block:: python

  # here is how to modify a graph:

  go[1].cmap = 'PRGn'
  go[1].vmin = 0
  go[1].vmax = 5e-5
  go[1].width = 900
  go[1].height = 700
  go[1].render()



.. raw:: html

  <iframe src="../../../_static/pycmap_tutorial_viz/html/gridded_map_modified_Fe.html"  frameborder = 0  height="750px" width="100%">></iframe>


Example 2: Sparse Maps
----------------------

This example visualizes an example of sparse data: synechococcus
abundance from `Global Pikophytoplankton`_ dataset.

.. _Global Pikophytoplankton: https://cmap.readthedocs.io/en/latest/catalog/datasets/Picoeuk.html#pikophytoplankton



.. code-block:: python


  #!pip install pycmap -q     #uncomment to install pycmap, if necessary
  # uncomment the lines below if the API key has not been registered on your machine, previously.
  # import pycmap
  # pycmap.API(token='YOUR_API_KEY>')

  from pycmap.viz import plot_map

  plot_map(
          tables=['tblGlobal_PicoPhytoPlankton'],
          variables=['synechococcus_abundance'],
          dt1='1990-01-30',
          dt2='1995-12-30',
          lat1=10,
          lat2=70,
          lon1=-180,
          lon2=80,
          depth1=0,
          depth2=100,
          exportDataFlag=False,
          show=True
          )

.. raw:: html

   <iframe src="../../../_static/pycmap_tutorial_viz/html/sparse_map_heatMap.html"  frameborder = 0  height="550px" width="100%">></iframe>

|

Example 3: Contour Plot
-----------------------

This example creates a contour plot using the satellite `Sea Surface
Temperature (SST)`_. Notice the **levels** parameter sets the number of
contour levels. Currently, contour plots are only supported by the
plotly library.

.. _Sea Surface Temperature (SST): https://cmap.readthedocs.io/en/latest/catalog/datasets/SST.html#sst

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary
  # uncomment the lines below if the API key has not been registered on your machine, previously.
  # import pycmap
  # pycmap.API(token='YOUR_API_KEY>')

  from pycmap.viz import plot_map

  go = plot_map(
               tables=['tblsst_AVHRR_OI_NRT'],
               variables=['sst'],
               dt1='2016-04-30',
               dt2='2016-04-30',
               lat1=10,
               lat2=70,
               lon1=-180,
               lon2=-80,
               depth1=0,
               depth2=0,
               exportDataFlag=False,
               show=True,
               level

.. raw:: html

  <iframe src="../../../_static/pycmap_tutorial_viz/html/contour_map_sst.html"  frameborder = 0  height="550px" width="100%">></iframe>

Example 4: 3D Surface
---------------------

This example creates a 3D map using model estimates of `dissolved
nitrate (NO3)`_. Notice the **surface3D** parameter is set to True.
Currently, 3D map plots are only supported by the plotly library.

.. _dissolved nitrate (NO3): https://cmap.readthedocs.io/en/latest/catalog/datasets/Pisces.html#pisces

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary
  # uncomment the lines below if the API key has not been registered on your machine, previously.
  # import pycmap
  # pycmap.API(token='YOUR_API_KEY>')

  from pycmap.viz import plot_map

  go = plot_map(
               tables=['tblPisces_NRT'],
               variables=['NO3'],
               dt1='2016-04-30',
               dt2='2016-04-30',
               lat1=-90,
               lat2=90,
               lon1=-180,
               lon2=180,
               depth1=0,
               depth2=0.5,
               exportDataFlag=False,
               show=True,
               surface3D=True
               )


.. raw:: html

 <iframe src="../../../_static/pycmap_tutorial_viz/html/3D_surface_NO3.html"  frameborder = 0  height="550px" width="100%">></iframe>
