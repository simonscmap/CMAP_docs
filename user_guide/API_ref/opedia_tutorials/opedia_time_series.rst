
.. _Jupyter Notebook: https://github.com/mdashkezari/opedia/blob/master/notebooks/Plot_TimeSeries.ipynb



Plot Time Series
================

**Create a Time Series plot using satellite and modeled data**


**Note:**

- Pisces model is a weekly-averaged global model with spatial resolution 1/2° X 1/2° (data is available only at one-week intervals).
- Satellite wind data set is a 6-hourly global product with spatial resolution 1/4° X 1/4° .
- Satellite Altimetry data set is a daily-global product with spatial resolution 1/4° X 1/4° .


Code Tutorial
^^^^^^^^^^^^^


`Jupyter Notebook`_


.. code-block:: python


    from opedia import plotTS as TS

    tables = ['tblSST_AVHRR_OI_NRT', 'tblAltimetry_REP', 'tblPisces_NRT']    # see catalog.csv  for the complete list of tables and variable names
    variables = ['sst', 'sla', 'NO3']                                        # see catalog.csv  for the complete list of tables and variable names
    startDate = '2016-03-29'
    endDate = '2016-05-29'
    lat1, lat2 = 25, 30
    lon1, lon2 = -160, -155
    depth1, depth2 = 0, 5
    fname = 'TS'
    exportDataFlag = False      # True if you you want to download data

    TS.plotTS(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)



.. raw:: html

    <iframe src="../../../_static/tutorial_plots/TS.html"  frameborder = 0  height="1000px" width="100%">></iframe>
