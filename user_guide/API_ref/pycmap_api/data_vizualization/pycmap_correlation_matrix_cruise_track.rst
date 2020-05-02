.. _corrMatrixCruise:




Correlation Matrix Along Cruise Track
=====================================

.. _Match (colocalize) Cruise Track with Datasets: MatchCruise.ipynb
.. _cruise: Cruises.ipynb
.. _Match (colocalize) Cruise Track with Datasets: MatchCruise.ipynb
.. _Match (colocalize) Datasets: Match.ipynb
.. _API key: pycmap_api.html
.. _APIs parameters: pycmap_api.html

.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Viz_CruiseCorrelationMatrix.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FViz_CruiseCorrelationMatrix.ipynb


.. _SeaFlow dataset: https://cmap.readthedocs.io/en/latest/catalog/datasets/SeaFlow.html#seaflow
.. _catalog: Catalog.ipynb

.. method:: plot_cruise_corr_map(cruise, targetTables, targetVars, depth1, depth2, temporalTolerance, latTolerance, lonTolerance, depthTolerance, method='spearman', exportDataFlag=False, show=True)


    This function colocalizes the target variables along track of a cruise
    (see `Match (colocalize) Cruise Track with Datasets`_). It then computes
    and visualizes a correlation matrix showing the pairwise correlation
    coefficients between the colocalized variables. The colocalization
    procedure relies on the tolerance parameters because they set the
    matching boundaries between the cruise track and target datasets. Currently, this graph is only supported by plotly library.

..COMMENT: The above 'Match (colocalize) Cruise Track with Datasets' link is not working. 

    Returns the generated correlation graph object. One may modify the graph properties (see example below).


    .. note::
      This method requires a valid `API key`_. It is not necessary to set the
      API key every time because the API properties are stored locally after
      being called the first time.

..COMMENT: The above 'API key' link is not working. 

    |



    :Parameters:
        **cruise: string**
            The official cruise name. If applicable, you may also use cruise "nickname" ('Diel', 'Gradients_1' ...). A full list of cruise names can be retrieved using `cruise`_ method.
            
..COMMENT: The above 'cruise' link is not working. 

        **targetTables: list of string**
            Table names of the target datasets to be matched with the source data. Note source dataset can be matched with multiple target datasets. A full list of table names can be found in :ref:`Catalog`.
        **targetVars: list of string**
            Variable short names to be matched with the source variable. A full list of variable short names can be found in :ref:`Catalog`.
        **depth1: float**
            Start depth [m]. This parameter sets the lower bound of the depth cut on the target datasets. 'depth1' and 'depth2' allow matching a cruise trajectory (which is at the surface, hopefully!) with target varaiables at lower depth. Note depth is a positive number (depth is 0 at the surface and increases towards the ocean floor).
        **depth2: float**
            End depth [m]. This parameter sets the upper bound of the depth cut on the target datasets. Note depth is a positive number (depth is 0 at the surface and increases towards the ocean floor).
        **temporalTolerance: list of int**
            Temporal tolerance values between pairs of source and target datasets. The size and order of values in this list should match those of targetTables. If only a single integer value is given, that would be applied to all target datasets. This parameter is in day units except when the target variable represents monthly climatology data in which case it is in month units. Note fractional values are not supported in the current version.
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
     
..COMMENT: The above 'APIs parameters' link is not working.

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

..COMMENT: Not obvious that there are two links given above in my browser. Add some space. 

        **vmin: float**
          This parameter defines the lower bound of the colorbar.
        **vmax: float**
          This parameter defines the upper bound of the colorbar.
        **height: int**
          Graph's height in pixels.
        **width: int**
          Graph's width in pixels.
        **title: str**
          Graphs's title.

    :Methods:
      **render()**
        Displays the plot according to the set properties.

|

Example
-------

This example colocalizes the Gradient 2 cruise (MGL1704) with 12
variables, including underway measurements of prochlorococcus,
synechococcus, and picoeukaryote abundances by `SeaFlow dataset`_,
satellite products (adt, chl, sst), and model estimates (see the
``match_params()`` function below for more details). Please explore the
`catalog`_ to find more appropriate target variables.

..COMMENT: The above 'catalog' link is not working.

Returns the generated correlation graph object. One may
modify the graph properties (see example below).

Review `Match (colocalize) Cruise Track with Datasets`_, and `Match
(colocalize) Datasets`_ pages for more details and tips!

..COMMENT: The two links in the previous sentence are not working. 

.. note::
  This method requires a valid `API key`_. It is not necessary to set the
  API key every time because the API properties are stored locally after
  being called the first time.

..COMMENT: The above 'API key' link is not working.



.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary
  # uncomment the lines below if the API key has not been registered on your machine, previously.
  # import pycmap
  # pycmap.API(token='YOUR_API_KEY>', vizEngine='plotly')

  from collections import namedtuple
  from pycmap.viz import plot_cruise_corr_map


  def match_params():
      Param = namedtuple('Param', ['table', 'variable', 'temporalTolerance', 'latTolerance', 'lonTolerance', 'depthTolerance'])
      params = []
      ######## seaflow
      params.append(Param('tblSeaFlow', 'prochloro_abundance', 0, 0.1, 0.1, 5))
      params.append(Param('tblSeaFlow', 'synecho_abundance', 0, 0.1, 0.1, 5))
      params.append(Param('tblSeaFlow', 'picoeuk_abundance', 0, 0.1, 0.1, 5))
      ####### WOA: World Ocean Atlas Monthly Climatology
      params.append(Param('tblWOA_Climatology', 'silicate_WOA_clim', 0, .5, .5, 5))
      params.append(Param('tblWOA_Climatology', 'oxygen_WOA_clim', 0, 0.5, 0.5, 5))
      ####### Satellite
      params.append(Param('tblSST_AVHRR_OI_NRT', 'sst', 1, 0.25, 0.25, 5))
      params.append(Param('tblSSS_NRT', 'sss', 1, 0.25, 0.25, 5))
      params.append(Param('tblAltimetry_REP', 'adt', 1, 0.25, 0.25, 5))
      params.append(Param('tblCHL_REP', 'chl', 4, 0.25, 0.25, 0))
      ####### Models
      params.append(Param('tblPisces_NRT', 'NO3', 4, 0.5, 0.5, 5))
      params.append(Param('tblDarwin_Plankton_Climatology', 'prokaryote_c01_darwin_clim', 0, 0.5, 0.5, 5))
      params.append(Param('tblDarwin_Plankton_Climatology', 'prokaryote_c02_darwin_clim', 0, 0.5, 0.5, 5))

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
  go = plot_cruise_corr_map(
                           cruise='MGL1704', # Gradients_2
                           targetTables=targetTables,
                           targetVars=targetVars,
                           depth1=0,
                           depth2=5,
                           temporalTolerance=temporalTolerance,
                           latTolerance=latTolerance,
                           lonTolerance=lonTolerance,
                           depthTolerance=depthTolerance
                           )

.. raw:: html

  <iframe src="../../../../_static/pycmap_tutorial_viz/html/correlation_matrix_cruise_track_annotated_heatmap_Along_Track_MGL1704.html"  frameborder = 0  height="800px" width="100%">></iframe>





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

|

.. raw:: html

   <iframe src="../../../../_static/pycmap_tutorial_viz/html/correlation_matrix_cruise_track_modified_annotated_heatmap_Along_Track_MGL1704.html"  frameborder = 0  height="1100px" width="100%">></iframe>
