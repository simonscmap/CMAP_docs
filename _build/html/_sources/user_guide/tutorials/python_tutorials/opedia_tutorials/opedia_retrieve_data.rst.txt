.. _subset:

Retrieve Data
=============




Space-Time
^^^^^^^^^^

This tutorial shows how to retrieve a generic distribution of a variable within a predefined space-time domain. You need to know the variable and table names, both which can be found in the catalog. Data is retrieved in form of a dataframe with time, space, and variable columns.


.. code-block:: python

    from opedia import subset

    ############## set parameters ################
    table = 'tblsst_AVHRR_OI_NRT'
    variable = 'sst'
    dt1 = '2016-06-01'
    dt2 = '2016-06-05'
    lat1, lat2, lon1, lon2 = 23, 24, -160, -158
    depth1, depth2 = 0, 0
    ##############################################

    df = subset.spaceTime(table, variable, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)    # retrieves a DataFrame
    #df.to_csv('data.csv', index=False)      # save the retrieved data into a csv file




|

Time-Series
^^^^^^^^^^^

This tutorial shows how to retrieve time series of a variable within a predefined space-time domain. You need to know the variable and table names, both which can be found in the catalog. The timeSeries function computes the mean and standard deviation of the variable per time period. Data is retrieved in form of a dataframe with time, space, and variable columns.

.. code-block:: python

    from opedia import subset

    ############## set parameters ################
    table = 'tblsst_AVHRR_OI_NRT'
    variable = 'sst'
    dt1 = '2016-06-01'
    dt2 = '2016-07-01'
    lat1, lat2, lon1, lon2 = 23, 24, -160, -158
    depth1, depth2 = 0, 0
    ##############################################

    df = subset.timeSeries(table, variable, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)    # retrieves a DataFrame
    #df.to_csv('data.csv', index=False)      # save the retrieved data into a csv file


|


Depth Profile
^^^^^^^^^^^^^

This tutorial shows how to retrieve depth profile of a variable within a predefined space-time domain. You need to know the variable and table names, both which can be found in the catalog. The depthProfile function computes the mean and standard deviation of the variable per depth period. Data is retrieved in form of a dataframe.

.. code-block:: python

    from opedia import subset

    ############## set parameters ################
    table = 'tblPisces_NRT'
    variable = 'CHL'
    dt1 = '2016-04-30'
    dt2 = '2016-04-30'
    lat1, lat2, lon1, lon2 = 23, 24, -160, -158
    depth1, depth2 = 0, 6000
    ##############################################

    df = subset.depthProfile(table, variable, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)    # retrieves a DataFrame
    #df.to_csv('data.csv', index=False)      # save the retrieved data into a csv file


|

Section Subset
^^^^^^^^^^^^^^

This tutorial shows how to retrieve section profile of a variable within a predefined space-time domain. You need to know the variable and table names, both which can be found in the catalog. Data is retrieved in form of a dataframe with time, space, and variable columns.

.. code-block:: python

    from opedia import subset

    ############## set parameters ################
    table = 'tblPisces_NRT'
    variable = 'Fe'
    dt1 = '2016-04-30'
    dt2 = '2016-04-30'
    lat1, lat2, lon1, lon2 = 22, 50, -160, -158
    depth1, depth2 = 0, 6000
    ##############################################

    subset.section(table, variable, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)    # retrieves a DataFrame
    #df.to_csv('data.csv', index=False)      # save the retrieved data into a csv file
