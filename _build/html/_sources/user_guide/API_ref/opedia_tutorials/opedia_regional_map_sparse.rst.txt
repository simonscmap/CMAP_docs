



.. .. _Jupyter Notebook: https://github.com/mdashkezari/opedia/blob/master/notebooks/Plot_RegionalMap.ipynb




Map Sparse Data
===============

Non gridded data from CMAP can now be mapped mapped using **plotRegional** function. This functionally is best for exploring cruise and float data.
CMAP will visualize sparse data values as circular markers with the circle size corresponding to the variables value. A data density heatmap will also be overlaid on the map.
In addition to this web map, CMAP will also create a 'dashboard' of the selected sparse data over time, latitude, longitude and depth.





.. note::
  The mapping library used has limitations on the number of points it can render. If your query is greater than ~10k points, you may consider using the :ref:`subset` functionality of CMAP and plotting locally.



Recommended Data Sets for Sparse Regional Mapping:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------+-------------+-----------------------+----------------+
| :ref:`Flombaum` | :ref:`Argo` | :ref:`Chisholm_AMT13` | :ref:`SeaFlow` |
+-----------------+-------------+-----------------------+----------------+





Code Tutorial
^^^^^^^^^^^^^



.. `Jupyter Notebook`_

.. code-block:: python



  from opedia import plotRegional as REG


  tables = ['tblFlombaum']    # see catalog.csv  for the complete list of tables and variable names
  variables = ['prochlorococcus_abundance_flombaum']                            # see catalog.csv  for the complete list of tables and variable names
  startDate = '1987-09-17'
  endDate = '2008-11-10'
  lat1, lat2 = -90, 90
  lon1, lon2 = -180, 180
  depth1, depth2 = 0, 5
  fname = 'regional'
  exportDataFlag = False       # True if you you want to download data

  REG.regionalMap(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)




.. raw:: html

    <iframe src="../../../_static/tutorial_plots/sparse_map_heatmap_vis.html"  frameborder = 0  height="1000px" width="100%">></iframe>

|

Sparse Regional Map Dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. raw:: html

    <iframe src="../../../_static/tutorial_plots/sparse_map_dashboard_vis.html"  frameborder = 0  height="1000px" width="100%">></iframe>

|
