



.. _Jupyter_Notebook: https://github.com/mdashkezari/opedia/blob/master/notebooks/Colocalize_Custom_Dataset.ipynb


Colocalize Custom Dataset
=========================

Colocalize a virtual cruise with satellite chlorophyll data and picoeukaryote climatological estimates provided by Darwin model. The trajectory of the virtual cruise is stored in a .csv file.


Notes:

Satellite sea surface temperatue data used in this example is a daily-global near-real-time and optimally interpolated data set with 4km × 4km spatial resolution  1/4° X 1/4° .

Satellite Chlorophyll data used in this example is a daily-global reprocessed and optimally interpolated data set with  4km × 4km  spatial resolution.

Darwin_Climatology is a monthly climatology version of the Darwin model with spatial resolution  1/2° ×1 /2° .



Code Tutorial
^^^^^^^^^^^^^


Jupyter_Notebook_


.. code-block:: python



    from opedia import colocalize as COL

    DB = False                            # < True > if source data exists in the database. < 0 > if the source data set is a spreadsheet file on disk.
    source = './KM1314_ParticulateCobalamins_2018_06_12_vPublished.xlsx'            # the source table name (or full filename)
    temporalTolerance = 1                # colocalizer temporal tolerance (+/- days)
    latTolerance = 0.3                   # colocalizer meridional tolerance (+/- degrees)
    lonTolerance = 0.3                   # colocalizer zonal tolerance (+/- degrees)
    depthTolerance = 5                   # colocalizer depth tolerance (+/- meters)
    tables = ['tblSST_AVHRR_OI_NRT', 'tblPisces_NRT', 'tblDarwin_Plankton_Climatology']    # list of varaible table names
    variables = ['sst', 'Fe', 'picoeukaryote_c03_darwin_clim']                            # list of variable names
    exportPath = './loaded.csv'         # path to save the colocalized data set

    COL.matchSource(DB, source, temporalTolerance, latTolerance, lonTolerance, depthTolerance, tables, variables, exportPath)
