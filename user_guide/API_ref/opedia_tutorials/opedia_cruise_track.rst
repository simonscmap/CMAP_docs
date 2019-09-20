

.. _Jupyter Notebook 1: https://github.com/mdashkezari/opedia/blob/master/notebooks/Colocalize_Cruise.ipynb
.. _Jupyter Notebook 2: https://github.com/mdashkezari/opedia/blob/master/notebooks/Colocalize_Virtual_Cruise.ipynb



Colocalize Cruise
=================



Example 1: Field Expedition
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Colocalize Darwin model and satellite data with cruise.
Compare the underway (in-situ) picoeukaryote abundance measurements performed during the "Gradient1.0" (aka SCOPE_16) with satellite chlorophyll data and picoeukaryote climatological estimates provided by Darwin model.


Notes:

- In-Situ picoeukaryote abundance measurements are results of the SeaFlow data set with 3-minute temporal resolution and irregular spatial resolution
- Satellite Chlorophyll data used in this example is a daily-global reprocessed and optimally interpolated data set with  4 km×4 km  spatial resolution.
- Darwin_Climatology is a monthly climatology version of the Darwin model with spatial resolution  12∘×12∘ .

Code Tutorial
-------------

`Jupyter Notebook 1`_


.. code-block:: python


  from opedia import plotCruise as CRS

  DB_Cruise = True                 # < True > if cruise trajectory already exists in DB. < False > if arbiturary cruise file (e.g. virtual)
  source = 'tblSeaFlow'            # cruise table name or path to csv trajectory file
  cruise = 'TN292'          # cruise name, or file name of the csv trajectory file
  resampTau = '6H'                 # resample the cruise trajectory making trajectory time-space resolution coarser: e.g. '6H' (6 hourly), '3T' (3 minutes), ... '0' (ignore)
  fname = 'alongTrack'             # figure filename
  tables = ['tblSeaFlow', 'tblDarwin_Plankton_Climatology', 'tblCHL_OI_REP']    # list of varaible table names
  variables = ['picoeuk_abundance', 'picoeukaryote_c03_darwin_clim', 'chl']               # list of variable names
  spatialTolerance = 0.3           # colocalizer spatial tolerance (+/- degrees)
  exportDataFlag = False           # export the cruise trajectory and colocalized data on disk
  depth1 = 0                       # depth range start (m)
  depth2 = 5                       # depth range end (m)


  df = CRS.getCruiseTrack(DB_Cruise, source, cruise)
  df = CRS.resample(df, resampTau)
  loadedTrack = CRS.plotAlongTrack(tables, variables, cruise, resampTau, df, spatialTolerance, depth1, depth2, fname, exportDataFlag, marker='-', msize=30, clr='darkturquoise')

|


.. raw:: html

    <iframe src="../../../_static/tutorial_plots/alongTrack.html"  frameborder = 0  height="1000px" width="100%">></iframe>

|

Example 2: Virtual Cruise
^^^^^^^^^^^^^^^^^^^^^^^^^

Colocalize Darwin model, satellite data with a virtual cruise.
Colocalize a virtual cruise with satellite chlorophyll data and picoeukaryote climatological estimates provided by Darwin model. The trajectory of the virtual cruise is stored in a .csv file.


Notes:

- Satellite sea surface temperatue data used in this example is a daily-global near-real-time and optimally interpolated data set with 4km × 4km spatial resolution  14∘×14∘ .
- Satellite Chlorophyll data used in this example is a daily-global reprocessed and optimally interpolated data set with  4 km×4 km  spatial resolution.
- Darwin_Climatology is a monthly climatology version of the Darwin model with spatial resolution  1/2° X 1/2° .


Code Tutorial
-------------

`Jupyter Notebook 2`_


.. code-block:: python

    from opedia import plotCruise as CRS
    import os

    DB_Cruise = False                                  # < True > if cruise trajectory already exists in DB. < False > if arbiturary cruise file (e.g. virtual)
    source = './virtual_parity_scope_2.csv'            # cruise table name or path to csv trajectory file
    cruise = os.path.splitext(source)[0]               # cruise name, or file name of the csv trajectory file
    resampTau = '6H'                                   # resample the cruise trajectory making trajectory time-space resolution coarser: e.g. '6H' (6 hourly), '3T' (3 minutes), ... '0' (ignore)
    fname = 'alongTrack'                               # figure filename
    tables = ['tblSST_AVHRR_OI_NRT', 'tblCHL_OI_REP', 'tblDarwin_Plankton_Climatology']    # list of varaible table names
    variables = ['sst', 'chl', 'picoeukaryote_c03_darwin_clim']                            # list of variable names
    spatialTolerance = 0.3                             # colocalizer spatial tolerance (+/- degrees)
    depth1 = 0.3                                       # depth range start (m)
    depth2 = 5                                         # depth range end (m)
    exportDataFlag = False                             # export the cruise trajectory and colocalized data on disk



    df = CRS.getCruiseTrack(DB_Cruise, source, cruise)
    df = CRS.resample(df, resampTau)
    loadedTrack = CRS.plotAlongTrack(tables, variables, cruise, resampTau, df, spatialTolerance, depth1, depth2, fname, exportDataFlag, marker='-', msize=30, clr='darkturquoise')
