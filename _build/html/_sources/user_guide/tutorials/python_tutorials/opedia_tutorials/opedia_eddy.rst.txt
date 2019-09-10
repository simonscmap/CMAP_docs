



.. _Jupyter: https://github.com/mdashkezari/opedia/blob/master/notebooks/Colocalize_Eddy.ipynb


Eddy Sampling
=============

**Colocalize an Eddy path with model and satellite data**

As far as oceanic observation methodology is concerned, one can consider two major class of observations:

- Eulerian
- Lagrangian

Eulerian measurements are made at a fixed frame of reference which means the sensor is fixed at a given location and fluid is passing by. Lagrangian measurements are made from the perspective of water parcels which means the sensor propagates with the flow. This example demonstrates how to advect a passive tracer (massless particle) with the flow and construct a Lagrangian path. We then colocalize the Lagrangian path with other data sets (SST satellite and model-generated diazotroph concentration) to simulate a Lagrangian measurement.

Notes:

- Darwin_Climatology is a monthly climatology version of the Darwin model with spatial resolution 1/2° X 1/2°
- Satellite SST data set is a daily-global product with spatial resolution  1/4° X 1/4° .


Code Tutorial
^^^^^^^^^^^^^


Jupyter_


.. code-block:: python



    from opedia import eddy as EDD

    eddyTable = 'tblChelton'                                              # eddy table name
    startDate = '2014-04-01'                                              # eddy cores within the delimited space-time (start date)
    endDate = '2014-05-01'                                                # eddy cores within the delimited space-time (end date)
    lat1 = 23                                                             # eddy cores within the delimited space-time (start lat)
    lat2 = 29                                                             # eddy cores within the delimited space-time (end lat)
    lon1 = -161                                                           # eddy cores within the delimited space-time (start lon)
    lon2 = -151                                                           # eddy cores within the delimited space-time (end lon)
    fname = 'eddy'                                                        # figure filename (and/or shape filename)
    tables = ['tblSST_AVHRR_OI_NRT', 'tblDarwin_Nutrient_Climatology']    # list of varaible table names
    variables = ['sst', 'DON_darwin_clim']                         # list of variable names
    spatialTolerance = 0.3                                                # colocalizer spatial tolerance (+/- degrees)
    exportDataFlag = False                                                # export the cruise trajectory and colocalized data on disk
    depth1 = 0                                                            # depth range start (m)
    depth2 = 5                                                            # depth range end (m)


    cores = EDD.getEddies(eddyTable, startDate, endDate, lat1, lat2, lon1, lon2)
    EDD.colocalize(tables, variables, cores, spatialTolerance, depth1, depth2, exportDataFlag, fname, marker='-')



.. raw:: html

    <iframe src="../../../../_static/tutorial_plots/eddy.html"  frameborder = 0  height="1000px" width="100%">></iframe>
