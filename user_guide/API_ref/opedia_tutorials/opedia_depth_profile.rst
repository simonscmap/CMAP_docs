
.. _Jupyter Notebook 1: https://github.com/mdashkezari/opedia/blob/master/notebooks/Plot_DepthProfile_01.ipynb
.. _Jupyter Notebook 2: https://github.com/mdashkezari/opedia/blob/master/notebooks/Plot_DepthProfile_02.ipynb

Plot Depth Profile
==================


**Create depth profile plots using model and BGC-Argo float profiles.**

Notes:

- Pisces model is a weekly-averaged global model with spatial resolution  1/2° X 1/2°  (data is available only at one-week intervals).
- Darwin_Climatology is a monthly climatology version of the Darwin model with spatial resolution  1/2° X 1/2° .
- Argo float data set has irregular temporal and spatial resolution.


Code Tutorial
^^^^^^^^^^^^^


**Visualize Argo in-situ data vs modeled data in a mid-depth to surface depth profile**

`Jupyter Notebook 1`_

.. code-block:: python


    from opedia import plotDepthProfile as DEP

    tables = ['tblArgoMerge_REP', 'tblPisces_NRT', 'tblDarwin_Chl_Climatology']     # see catalog.csv  for the complete list of tables and variable names
    variables = ['argo_merge_chl_adj', 'CHL', 'chl01_darwin_clim']
    startDate = '2016-04-30'   # PISCES is a weekly model, and here we are using monthly climatology of Darwin model
    endDate = '2016-04-30'
    lat1, lat2 = 20, 24
    lon1, lon2 = -170, -150
    depth1, depth2 = 0, 1500
    fname = 'DEP'
    exportDataFlag = False      # True if you you want to download data

    DEP.plotDepthProfile(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)



.. raw:: html

    <iframe src="../../../_static/tutorial_plots/dep_01.html"  frameborder = 0  height="1000px" width="100%">></iframe>

|

**Create depth profile plots using model and in-situ measurements at station ALOHA**


Notes:

- Darwin_Climatology is a monthly climatology version of the Darwin model with spatial resolution  12∘×12∘ .
- Pisces model is a weekly-averaged global model with spatial resolution  12∘×12∘  (data is available only at one-week intervals).
- Station ALOHA is a fixed loaction at north of Hawaii:  22∘ 45′ N  158∘ W.

`Jupyter Notebook 2`_

.. code-block:: python


    from opedia import plotDepthProfile as DEP

    tables = ['tblHOT_PP', 'tblDarwin_Chl_Climatology', 'tblPisces_NRT']     # see catalog.csv  for the complete list of tables and variable names
    variables = ['chl_hot', 'chl01_darwin_clim', 'CHL']                  # see catalog.csv  for the complete list of tables and variable names
    startDate = '2015-04-30'   # PISCES is a weekly model, and here we are using monthly climatology of Darwin model
    endDate = '2016-04-30'
    lat1, lat2 = 20, 24
    lon1, lon2 = -159, -157
    depth1, depth2 = 0, 170
    fname = 'DEP'
    exportDataFlag = False      # True if you you want to download data

    DEP.plotDepthProfile(tables, variables, startDate, endDate, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)



.. raw:: html

    <iframe src="../_static/tutorial_plots/dep_02.html"  frameborder = 0  height="1000px" width="100%">></iframe>
