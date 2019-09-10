

.. _Jupyter Notebook: https://github.com/mdashkezari/opedia/blob/master/notebooks/Plot_Distribution.ipynb


Plot Histogram
==============

**Plot Distribution (Satellite, Core Argo Floats)
Create histograms of sea surface temperature (satellite), and temperature / salinity measurements by Argo floats.**


Note:

- Satellite SST data set is a daily-global product with spatial resolution  14∘×14∘ .
- Argo float data set has irregular temporal and spatial resolution.

Code Tutorial
^^^^^^^^^^^^^


`Jupyter Notebook`_


.. code-block:: python



    from opedia import plotDist as DIS

    tables = ['tblSST_AVHRR_OI_NRT', 'tblArgoMerge_REP', 'tblArgoMerge_REP']           # see catalog.csv  for the complete list of tables and variable names
    variables = ['sst', 'argo_merge_temperature_adj', 'argo_merge_salinity_adj']       # see catalog.csv  for the complete list of tables and variable names
    startDate = '2016-04-30'
    endDate = '2016-04-30'
    lat1, lat2 = 20, 24
    lon1, lon2 = -170, 150
    depth1, depth2 = 0, 1500
    fname = 'DEP'
    exportDataFlag = False      # True if you you want to download data

    DIS.plotDist(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)


.. raw:: html

    <iframe src="../../../../_static/tutorial_plots/hist.html"  frameborder = 0  height="1000px" width="100%">></iframe>
