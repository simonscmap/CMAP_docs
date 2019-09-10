
.. _Jupyter Notebook: https://github.com/mdashkezari/opedia/blob/master/notebooks/Plot_XY.ipynb



Plot XY
=======

**Create an XY plot of two or more variables**


**Note:**

- Satellite SST data set is a daily-global product with spatial resolution 1/4° X 1/4° .
- Satellite Altimetry data set is a daily-global product with spatial resolution 1/4° X 1/4° .


Code Tutorial
^^^^^^^^^^^^^


`Jupyter Notebook`_


.. code-block:: python


    from opedia import plotXY as XY

    tables = ['tblSST_AVHRR_OI_NRT', 'tblAltimetry_REP']
    variables = ['sst', 'sla']                                        # see catalog.csv  for the complete list of tables and variable names
    startDate = '2016-03-29'
    endDate = '2016-05-29'
    lat1, lat2 = 25, 30
    lon1, lon2 = -160, -155
    depth1, depth2 = 0, 5
    fname = 'XY'
    exportDataFlag = False      # True if you you want to download data

    XY.plotXY(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)




.. raw:: html

    <iframe src="../../../../_static/tutorial_plots/XY.html"  frameborder = 0  height="600px" width="100%">></iframe>
