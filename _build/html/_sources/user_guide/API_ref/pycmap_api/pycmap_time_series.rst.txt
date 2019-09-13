
.. _timeSeries:



Time Series Plot
================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Viz_TimeSeries.ipynb




.. method:: plot_timeseries(tables, variables, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, exportDataFlag=False, show=True, interval=None)


    Creates a timeseries graph for each variable according to the specified space-time constraints (dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2). By definition, timeseries data points are aggregated by time: at each time interval the mean and standard deviation of the variable values within the space-time constraints are computed. The sequence of these values construct the timeseries. If the **interval** parameter is set, timeseries can be binned weekly, monthly, quarterly, or annually, (this feature is not applicable to climatological datasets).

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
          If True, the graph data points are stored on the local machine. The export path and file format are set by the `API's parameters`_.
        **show: boolean, default: True**
          If True, the graph object is returned and is displayed. The graph file is saved on the local machine at the figureDir directory.
          If False, the graph object is returned but not displayed.
        **interval: None or string, default: None**
          The timeseries bin size. If None, the native dataset time resolution is
          used as the bin size. Below is a list of interval values for other
          binning options:

          -  **'w'** or **'week'** for weekly timeseries.
          -  **'m'** or **'month'** for monthly timeseries.
          -  **'s'** or **'q'** for seasonal/quarterly timeseries.
          -  **'a'** or **'y'** for annual/yearly timeseries.




    :returns\:: list of graph objects
      A list of graph objects. Below are the graph's properties and methods.

      :Properties:
        **data: dataframe**
          Graph data points to be visualized.
        **line: boolean, default: True**
          If True, line plot is superimposed on markers.
        **color: string**
          Line and marker colors (e.g. 'red', 'green', ..) or rgb hex '#FF0023'.
        **msize: int**
          Marker size.
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

**Example:**


This example generates two timeseries graphs showing remotly sensed `sea
level anomaly`_, and `sea surface salinity`_ over a weekly-binned
one-year period. The graphs are made using the default visualization
library (plotly) which may be changed by:
``pycmap.API(vizEngine='bokeh')``

.. _sea level anomaly: https://cmap.readthedocs.io/en/latest/catalog/datasets/Altimetry_REP.html#altimetry-rep
.. _sea surface salinity: https://cmap.readthedocs.io/en/latest/catalog/datasets/SSS.html#sss

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary
  # uncomment the lines below if the API key has not been registered on your machine, previously.
  # import pycmap
  # pycmap.API(token='YOUR_API_KEY>')


  from pycmap.viz import plot_timeseries

  go = plot_timeseries(
                      tables=['tblAltimetry_REP', 'tblSSS_NRT'],
                      variables=['sla', 'sss'],
                      dt1='2016-04-30',
                      dt2='2017-04-30',
                      lat1=30,
                      lat2=32,
                      lon1=-160,
                      lon2=-158,
                      depth1=0,
                      depth2=0,
                      exportDataFlag=False,
                      show=True,
                      interval='w'
                      )



.. raw:: html

   <iframe src="../../../_static/pycmap_tutorial_viz/html/time_series_sla.html"  frameborder = 0  height="420px" width="100%">></iframe>


.. raw:: html

   <iframe src="../../../_static/pycmap_tutorial_viz/html/time_series_sss.html"  frameborder = 0  height="420px" width="100%">></iframe>



.. code-block:: python

  # here is how to modify a graph:

  go[0].pdf = False
  go[0].bins = 20
  go[0].xlabel = "new xlabel"
  go[0].title= "graph's title"
  go[0].width = 600
  go[0].height = 600
  go[0].render()

.. raw:: html

   <iframe src="../../../_static/pycmap_tutorial_viz/html/time_series_modified_sla.html"  frameborder = 0  height="600px" width="100%">></iframe>
