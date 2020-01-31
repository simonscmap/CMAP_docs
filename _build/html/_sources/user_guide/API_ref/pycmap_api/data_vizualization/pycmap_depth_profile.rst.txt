

.. _depthProfile:



Depth Profile
=============


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Viz_DepthProfile.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FViz_DepthProfile.ipynb


.. _API key: pycmap_api.html
.. _APIs parameters: pycmap_api.html
.. _APIs vizEngine: pycmap_api.html


.. method:: plot_depth_profile(tables, variables, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, exportDataFlag=False, show=True)



    Creates a depth profile graph for each variable according to the
    specified space-time constraints (dt1, dt2, lat1, lat2, lon1, lon2,
    depth1, depth2). By definition, depth profile data points are aggregated
    by depth: at each depth level the mean and standard deviation of the
    variable values within the space-time constraints are computed. The
    sequence of these values construct the depth profile.


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
        **show: boolean, default: True**
          If True, the graph object is returned and is displayed. The graph file is saved on the local machine at the figureDir directory.
          If False, the graph object is returned but not displayed.




    :returns\:: list of graph objects
      A list of graph objects. Below are the graph's properties and methods.

      :Properties:
        **data: dataframe**
          Graph data points to be visualized.
        **line: boolean, default: True**
          If True, line plot is superimposed on markers.
        **color: string**
          Line and marker colors (e.g. 'red', 'green', ..) or rgb hex '#FF0023'.
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

Example:
--------

This example compares the depth profile of chlorophyll concentration
retrieved from `Argo Floats`_ observations, `Pisces model`_ estimations,
and `Darwin model`_ calculations. The depth profiles from the two models
demonstrate close consistency with the Argo measurements. The graphs are
made using the default visualization library (plotly) which may be
changed by: ``pycmap.API(vizEngine='bokeh')``

.. _Argo Floats: https://cmap.readthedocs.io/en/latest/catalog/datasets/Argo.html#argo
.. _Pisces model: https://cmap.readthedocs.io/en/latest/catalog/datasets/Pisces.html#pisces
.. _Darwin model: https://cmap.readthedocs.io/en/latest/catalog/datasets/Darwin_3day.html#darwin-3day

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary
  # uncomment the lines below if the API key has not been registered on your machine, previously.
  # import pycmap
  # pycmap.API(token='YOUR_API_KEY>')


  from pycmap.viz import plot_depth_profile

  go = plot_depth_profile(
                         tables=['tblArgoMerge_REP', 'tblPisces_NRT', 'tblDarwin_Ecosystem'],
                         variables=['argo_merge_chl_adj', 'CHL', 'CHL'],
                         dt1='2014-04-25',
                         dt2='2014-04-30',
                         lat1=20,
                         lat2=24,
                         lon1=-170,
                         lon2=-150,
                         depth1=0,
                         depth2=1500,
                         exportDataFlag=False,
                         show=True
                         )

.. raw:: html

  <iframe src="../../../../_static/pycmap_tutorial_viz/html/depth_profile_argo_merge_chl_adj.html"  frameborder = 0  height="450px" width="100%">></iframe>

|

.. raw:: html

  <iframe src="../../../../_static/pycmap_tutorial_viz/html/depth_profile_CHL.html"  frameborder = 0  height="450px" width="100%">></iframe>



.. code-block:: python

  # here is how to modify a graph:

  go[1].cmap = 'PRGn'
  go[1].vmin = 0
  go[1].vmax = 5e-5
  go[1].width = 900
  go[1].height = 700
  go[1].render()

|

.. raw:: html

   <iframe src="../../../../_static/pycmap_tutorial_viz/html/depth_profile_modified_argo_merge_chl_adj.html"  frameborder = 0  height="650px" width="100%">></iframe>






.. figure:: /_static/overview_icons/sql.png
  :scale: 10 %

**SQL Statement**

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block:: sql

  EXEC uspDepthProfile 'tableName', 'variable', 'dt1', 'dt2', 'lat1', 'lat2', 'lon1', 'lon2', 'depth1', 'depth2'

**Example:**

.. code-block:: sql

  EXEC uspDepthProfile 'tblPisces_NRT', 'CHL', '2016-04-30', '2016-04-30', '20', '24', '-170', '-150', '0', '1500'
