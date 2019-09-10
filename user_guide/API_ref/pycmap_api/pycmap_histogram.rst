.. _histogram:





Histogram Plot
==============


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/mdashkezari/pycmapDoc/blob/master/notebooks/Viz_Histogram.ipynb




.. method:: plot_hist(tables, variables, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, exportDataFlag=False, show=True)


    Creates a histogram graph for each variable according to the specified space-time constraints (dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2). Change the `API's vizEngine`_ parameter if you wish to use a different visualization library.
    Returns the generated graph objects in form of a python list. One may use the returned objects to modify the graph properties.

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
          If True, the graph data points are stored on the local machine. The export path and file format are set by the `API's parameters`_.
        **show: boolean, default: True**
          If True, the graph object is returned and is displayed. The graph file is saved on the local machine at the figureDir directory.
          If False, the graph object is returned but not displayed.





    :returns\:: list of graph objects
      A list of graph objects. Below are the graph's properties and methods.

      :Properties:
        **data: dataframe**
          Graph data points to be visualized.
        **bins: int, default: 50**
          Number of histogram bins.
        **pdf: boolean, default: False**
          If True the histogram shows a probability density function, otherwise absolute counts are displayed.
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

**Example 1:**


This example creates three histogram graphs comparing dissolved oxygen
measured during the Falkor_2018 cruise, estimated by `Darwin climatology
model`_, and `World Ocean Atlas`_. The graphs are made using the default
visualization library (plotly) which may be changed by:
``pycmap.API(vizEngine='bokeh')``

.. _Darwin climatology model: https://cmap.readthedocs.io/en/latest/catalog/datasets/Darwin_clim.html#darwin-clim
.. _World Ocean Atlas: https://cmap.readthedocs.io/en/latest/catalog/datasets/WOA_climatology.html#woa-clim

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary
  # uncomment the lines below if the API key has not been registered on your machine, previously.
  # import pycmap
  # pycmap.API(token='YOUR_API_KEY>')


  from pycmap.viz import plot_hist

  go = plot_hist(
                tables=['tblFalkor_2018', 'tblDarwin_Nutrient_Climatology', 'tblWOA_Climatology'],
                variables=['CTD_Oxygen', 'O2_darwin_clim', 'oxygen_WOA_clim'],
                dt1='2018-03-01',
                dt2='2018-04-30',
                lat1=21,
                lat2=25,
                lon1=-161,
                lon2=155,
                depth1=0,
                depth2=100,
                exportDataFlag=False,
                show=True
                )


.. raw:: html

   <iframe src="../../../_static/pycmap_tutorial_viz/html/histogram_CTD_Oxygen.html"  frameborder = 0  height="420px" width="100%">></iframe>


.. raw:: html

   <iframe src="../../../_static/pycmap_tutorial_viz/html/histogram_O2_darwin_clim.html"  frameborder = 0  height="420px" width="100%">></iframe>

.. raw:: html

   <iframe src="../../../_static/pycmap_tutorial_viz/html/histogram_oxygen_WOA_clim.html"  frameborder = 0  height="420px" width="100%">></iframe>



.. code-block:: python

  # here is how to modify a graph:

  go[0].pdf = False
  go[0].bins = 20
  go[0].xlabel = "new xlable"
  go[0].title= "graph's title"
  go[0].width = 600
  go[0].height = 600
  go[0].render()
