



.. _Jupyter Notebook: https://github.com/mdashkezari/opedia/blob/master/notebooks/Plot_Section.ipynb


Section Plot
============

**Create a section plot of modeled colored dissolved organic matter**

Notes:

- Darwin_Climatology is a monthly climatology version of the Darwin model with spatial resolution  1/2° X 1/2° .




Code Tutorial
^^^^^^^^^^^^^



`Jupyter Notebook`_


.. code-block:: python



    from opedia import plotSection as SEC

    tables = ['tblDarwin_Nutrient_Climatology']    # see catalog.csv  for the complete list of tables and variable names
    variabels = ['CDOM_darwin_clim']                            # see catalog.csv  for the complete list of tables and variable names



    dt1 = '2016-04-30'   # PISCES is a weekly model, and here we are using monthly climatology of Darwin model
    dt2 = '2016-04-30'
    lat1, lat2 = 23, 55
    lon1, lon2 = -159, -157
    depth1, depth2 = 0, 3597
    fname = 'sectional'
    exportDataFlag = False       # True if you you want to download data

    SEC.sectionMap(tables, variabels, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, fname, exportDataFlag)


.. raw:: html

    <iframe src="../../../_static/tutorial_plots/sectional.html"  frameborder = 0  height="600px" width="100%">></iframe>
