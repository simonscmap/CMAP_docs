.. _corrMatrix:





Correlation Matrix
==================


.. _Chisholm lab: https://chisholmlab.mit.edu/
.. _source dataset: https://cmap.readthedocs.io/en/latest/catalog/datasets/Chisholm_AMT13.html#chisholm-amt13
.. _World Ocean Atlas: https://cmap.readthedocs.io/en/latest/catalog/datasets/WOA_climatology.html#woa-clim
.. _chlorophyll dataset: https://cmap.readthedocs.io/en/latest/catalog/datasets/Chlorophyll_REP.html#chlorophyll-rep
.. _Darwin model: https://cmap.readthedocs.io/en/latest/catalog/datasets/Darwin_3day.html#darwin-3day
.. _dataset page: https://cmap.readthedocs.io/en/latest/catalog/datasets/Chisholm_AMT13.html#chisholm-amt13
.. _Match (colocalize) Datasets: Match.ipynb
.. _API key: pycmap_api.html
.. _APIs parameters: pycmap_api.html

.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/mdashkezari/pycmapDoc/blob/master/notebooks/Viz_CorrelationMatrix.ipynb

.. _Match (colocalize) Datasets: Match.ipynb
.. _catalog: Catalog.ipynb


.. method:: plot_corr_map(sourceTable, sourceVar, targetTables, targetVars, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, temporalTolerance, latTolerance, lonTolerance, depthTolerance, method='spearman', exportDataFlag=False, show=True)



    This function computes and plots the pair-correlation coefficient
    between the source and target variables. The results are visualized in
    form of a correlation matrix. To compute the correlations the source and
    target variables have to be colocalized first (see :ref:`match`). The colocalization procedure relies on the tolerance
    parameters because they set the matching boundaries between the source
    and target datasets. Notice the source has to be a single
    non-climatological variable. In principle, if the source dataset is
    fully covered by the target variable's spatio-temporal range, there
    should always be matching results if the tolerance parameters are larger
    than half of their corresponding spatial/temporal resolutions. Please
    explore the :ref:`Catalog` to find appropriate target variables. Note that,
    currently, this visualization is only supported by plotly visualization
    library.

    Returns the generated correlation graph object using which one may modify the graph properties (see example below).


    .. note::
      This method requires a valid `API key`_. It is not necessary to set the
      API key every time because the API properties are stored locally after
      being called the first time.


    |


    :Parameters:
        **sourceTable: string**
            Table name of the source dataset. A full list of table names can be found in :ref:`Catalog`.
        **sourceVar: string**
            The source variable short name. The target variables are matched (colocalized) with this variable. A full list of variable short names can be found in :ref:`Catalog`.
        **targetTables: list of string**
            Table names of the target datasets to be matched with the source data. Notice source dataset can be matched with multiple target datasets. A full list of table names can be found in :ref:`Catalog`.
        **dt1: string**
            Start date or datetime. Both source and target datasets are filtered before matching. This parameter sets the lower bound of the temporal cut.
        **dt2: string**
            End date or datetime. Both source and target datasets are filtered before matching. This parameter sets the upper bound of the temporal cut.
        **lat1: float**
            Start latitude [degree N]. Both source and target datasets are filtered before matching. This parameter sets the lower bound of the meridional cut. Note latitude ranges from -90 to 90 degrees.
        **lat2: float**
            End latitude [degree N]. Both source and target datasets are filtered before matching. This parameter sets the upper bound of the meridional cut. Note latitude ranges from -90 to 90 degrees.
        **lon1: float**
            Start longitude [degree E]. Both source and target datasets are filtered before matching. This parameter sets the lower bound of the zonal cut. Note longitude ranges from -180 to 180 degrees.
        **lon2: float**
            End longitude [degree E]. Both source and target datasets are filtered before matching. This parameter sets the upper bound of the zonal cut. Note longitude ranges from -180 to 180 degrees.
        **depth1: float**
            Start depth [m]. Both source and target datasets are filtered before matching. This parameter sets the lower bound of the vertical cut. Note depth is a positive number (depth is 0 at surface and grows towards ocean floor).
        **depth2: float**
            End depth [m]. Both source and target datasets are filtered before matching. This parameter sets the upper bound of the vertical cut. Note depth is a positive number (depth is 0 at surface and grows towards ocean floor).
        **temporalTolerance: list of int**
            Temporal tolerance values between pairs of source and target datasets. The size and order of values in this list should match those of targetTables. If only a single integer value is given, that would be applied to all target datasets. This parameter is in day units except when the target variable represents monthly climatology data in which case it is in month units. Notice fractional values are not supported in the current version.
        **latTolerance: list of float or int**
            Spatial tolerance values in meridional direction [deg] between pairs of source and target datasets. The size and order of values in this list should match those of targetTables. If only a single float value is given, that would be applied to all target datasets. A "safe" value for this parameter can be slightly larger than the half of the target variable's spatial resolution.
        **lonTolerance: list of float or int**
            Spatial tolerance values in zonal direction [deg] between pairs of source and target datasets. The size and order of values in this list should match those of targetTables. If only a single float value is given, that would be applied to all target datasets. A "safe" value for this parameter can be slightly larger than the half of the target variable's spatial resolution.
        **depthTolerance: list of float or int**
            Spatial tolerance values in vertical direction [m] between pairs of source and target datasets. The size and order of values in this list should match those of targetTables. If only a single float value is given, that would be applied to all target datasets.

        **method: str, default: 'spearman'**
            Correlation algorithm. 'spearman' is a rank correlation algorithm and is
            a metric for monotonic relationships. Other options involve
            **'pearson'** and **'kendall'**. *'pearson'* is the standard correlation
            coefficient, more favorable for linear correlations. *'kendall'* evaluates Kendall Tau correlation coefficient.

        **exportDataFlag: boolean, default: False**
          If True, the graph data points are stored on the local machine. The export path and file format are set by the `APIs parameters`_.
        **show: boolean, default: True**
          If True, the graph object is returned and is displayed. The graph file is saved on the local machine at the figureDir directory.
          If False, the graph object is returned but not displayed.



    :returns\:: the graph object
      Below are the graph's properties and methods.

      :Properties:
        **x: list of string**
          Correlation matrix column titles (covariate names).
        **y: list of string**
          Correlation matrix row titles (covariate names).
        **z: numpy.ndarray**
          Computed pairwise correlation coefficients.
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
        **title: str**
          The graphs's title.

    :Methods:
      **render()**
        Displays the plot according to the set properties.

|

Example
-------

In this example the abundance of a prochlorococcus strain (MIT9313PCR,
see lines 37-38) measured by `Chisholm lab`_ during the AMT13 cruise
(Atlantic Meridional Transect Cruise 13) is colocalized with 7 target
variables (lines 7-8):

-  'MIT9312PCR*Chisholm', 'MED4PCR*\ Chisholm', and 'sbact_Chisholm'
   from the same `source dataset`_
-  'phosphate*WOA*\ clim', and 'nitrate*WOA*\ clim' from `World Ocean
   Atlas`_ monthly climatology dataset
-  'chl' from weekly averaged satellite `chlorophyll dataset`_
-  'picoprokaryote' from 3-day averaged `Darwin model`_. Colocalizing
   this variable will take longer time than others as the 3-day averaged
   Darwin dataset is massive (multi-decades global 3D dataset)!


The space-time cut parameters (lines 41-48) have been set in such a way
to encompass the entire source dataset 'tblAMT13_Chisholm' (see the
`dataset page`_ for more details). Notice that the last data point at
the source dataset has been measured at '2003-10-12 12:44:00'. For
simplicity dt2 has been set to '2003-10-13', but you could also use the
exact date-time '2003-10-12 12:44:00'.

Please review the **Example 1** at `Match (colocalize) Datasets`_ page
since all of the mentioned tips directly apply to this example too.



.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary
  # uncomment the lines below if the API key has not been registered on your machine, previously.
  # import pycmap
  # pycmap.API(token='YOUR_API_KEY>', vizEngine='plotly')

  from collections import namedtuple
  from pycmap.viz import plot_corr_map



  def match_params():
      Param = namedtuple('Param', ['table', 'variable', 'temporalTolerance', 'latTolerance', 'lonTolerance', 'depthTolerance'])
      params = []
      ######## self-matching: colocalizing with some other variables in the tblAMT13_Chisholm dataset
      params.append(Param('tblAMT13_Chisholm', 'MIT9312PCR_Chisholm', 0, 0, 0, 0))
      params.append(Param('tblAMT13_Chisholm', 'MED4PCR_Chisholm', 0, 0, 0, 0))
      params.append(Param('tblAMT13_Chisholm', 'sbact_Chisholm', 0, 0, 0, 0))
      ####### WOA: World Ocean Atlas Monthly Climatology
      params.append(Param('tblWOA_Climatology', 'nitrate_WOA_clim', 0, .5, .5, 5))
      params.append(Param('tblWOA_Climatology', 'phosphate_WOA_clim', 0, 0.5, 0.5, 5))
      ####### Satellite
      params.append(Param('tblCHL_REP', 'chl', 4, 0.25, 0.25, 0))
      ####### Darwin Model
      params.append(Param('tblDarwin_Phytoplankton', 'picoprokaryote', 2, 0.25, 0.25, 5))


      tables, variables, temporalTolerance, latTolerance, lonTolerance, depthTolerance = [], [], [], [], [], []
      for i in range(len(params)):
          tables.append(params[i].table)
          variables.append(params[i].variable)
          temporalTolerance.append(params[i].temporalTolerance)
          latTolerance.append(params[i].latTolerance)
          lonTolerance.append(params[i].lonTolerance)
          depthTolerance.append(params[i].depthTolerance)
      return tables, variables, temporalTolerance, latTolerance, lonTolerance, depthTolerance



  targetTables, targetVars, temporalTolerance, latTolerance, lonTolerance, depthTolerance = match_params()
  go = plot_corr_map(
                    sourceTable='tblAMT13_Chisholm',
                    sourceVar='MIT9313PCR_Chisholm',
                    targetTables=targetTables,
                    targetVars=targetVars,
                    dt1='2003-09-14',
                    dt2='2003-10-13',
                    lat1=-48,
                    lat2=48,
                    lon1=-52,
                    lon2=-11,
                    depth1=0,
                    depth2=240,
                    temporalTolerance=temporalTolerance,
                    latTolerance=latTolerance,
                    lonTolerance=lonTolerance,
                    depthTolerance=depthTolerance
                    )

.. raw:: html

   <iframe src="../../../_static/pycmap_tutorial_viz/html/correlation_matrix_annotated_heatmap_MIT9313PCR_Chisholm.html"  frameborder = 0  height="800px" width="100%">></iframe>


.. code-block:: python

  # here is how to modify the graph:
  import numpy as np

  # print correlation values
  # print(go.z)
  # print(go.x)
  # print(go.y)
  go.z = np.abs(go.z)
  go.cmap = 'Greys'
  go.width = 1000
  go.height = 1000
  go.render()

.. raw:: html

   <iframe src="../../../_static/pycmap_tutorial_viz/html/correlation_matrix_modified_annotated_heatmap_MIT9313PCR_Chisholm.html"  frameborder = 0  height="1100px" width="100%">></iframe>
