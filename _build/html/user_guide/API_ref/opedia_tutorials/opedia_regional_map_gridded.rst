


.. _Jupyter Notebook: https://github.com/mdashkezari/opedia/blob/master/notebooks/Plot_RegionalMap.ipynb





Map Gridded Data
================



Gridded data from CMAP can be mapped using **plotRegional** function. This functionally is best for mapping gridded datasets such as satellite or model products.
Multiple datasets and variables can be queried in one request.



Recommended Data Sets for Gridded Regional Mapping:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

+-----------------+------------------------+--------------------+---------------+
| :ref:`SST`      | :ref:`Chlorophyll_REP` | :ref:`Darwin_3day` | :ref:`Pisces` |
+-----------------+------------------------+--------------------+---------------+


Code Tutorial
^^^^^^^^^^^^^



`Jupyter Notebook`_

.. code-block:: python



    from opedia import plotRegional as REG


    tables = ['tblsst_AVHRR_OI_NRT', 'tblPisces_NRT']    # see catalog.csv  for the complete list of tables and variable names
    variables = ['sst', 'Fe']                            # see catalog.csv  for the complete list of tables and variable names
    startDate = '2016-04-30'
    endDate = '2016-04-30'
    lat1, lat2 = 10, 70
    lon1, lon2 = -180, -80
    depth1, depth2 = 0, 0.5
    fname = 'regional'
    exportDataFlag = False       # True if you you want to download data

    REG.regionalMap(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)




.. raw:: html

    <iframe src="../../../_static/tutorial_plots/regional.html"  frameborder = 0  height="1000px" width="100%">></iframe>
