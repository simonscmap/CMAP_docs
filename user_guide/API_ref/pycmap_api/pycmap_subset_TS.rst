.. _subset_TS:



Data Subset: Time Series
========================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/TimeSeries.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FTimeSeries.ipynb


.. method:: time_series(table, variable, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2, interval=None)


    Returns a subset of data according to the specified space-time constraints (dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2). The returned data subset is aggregated by time: at each time interval the mean and standard deviation of the variable values within the space-time constraints are computed. The sequence of these values construct the timeseries. The timeseries data can be binned weekly, monthly, quarterly, or annually, if the interval parameter is set (this feature is not applicable to climatological datasets). The resulted timeseries is returned in form of a Pandas datframe ordered by time.

    |

    :Parameters:

        **table: string**
            Table name (each dataset is stored in a table). A full list of table names can be found in :ref:`Catalog`.
        **variable: string**
            Variable short name which directly corresponds to a field name in the table. A subset of this variable is returned by this method according to the spatio-temporal cut parameters (below). A full list of variable short names can be found in :ref:`Catalog`.
        **dt1: string**
            Start date or datetime. This parameter sets the lower bound of the temporal cut.
            Example values: '2016-05-25' or '2017-12-10 17:25:00'
        **dt2: string**
            End date or datetime. This parameter sets the upper bound of the temporal cut.
        **lat1: float**
            Start latitude [degree N]. This parameter sets the lower bound of the meridional cut. Note latitude ranges from -90° to 90°.
        **lat2: float**
            End latitude [degree N]. This parameter sets the upper bound of the meridional cut. Note latitude ranges from -90° to 90°.
        **lon1: float**
            Start longitude [degree E]. This parameter sets the lower bound of the zonal cut. Note latitude ranges from -180° to 180°.
        **lon2: float**
            End longitude [degree E]. This parameter sets the upper bound of the zonal cut. Note latitude ranges from -180° to 180°.
        **depth1: float**
            Start depth [m]. This parameter sets the lower bound of the vertical cut. Note depth is a positive number (it is 0 at surface and grows towards ocean floor).
        **depth2: float**
            End depth [m]. This parameter sets the upper bound of the vertical cut. Note depth is a positive number (it is 0 at surface and grows towards ocean floor).
        **interval: None or string, default: None**
            The timeseries bin size. If None, the native dataset time resolution is used as the bin size. Below is a list of interval values for other binning options:
            -  **'w'** or **'week'** for weekly timeseries.
            -  **'m'** or **'month'** for monthly timeseries.
            -  **'s'** or **'q'** for seasonal/quarterly timeseries.
            -  **'a'** or **'y'** for annual/yearly timeseries.


    :returns\:: Pandas dataframe.


|

**Example 1:**

This example retrieves the timeseries of SiO4 measurements conducted by HOT team at University of Hawaii, spanning from 1988 to 2016.

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.time_series(
                 table='tblHOT_Bottle',
                 variable='SiO4_bottle_hot',
                 dt1='1988-12-01',
                 dt2='2016-10-15',
                 lat1=22,
                 lat2=23,
                 lon1=-159,
                 lon2=-157,
                 depth1=0,
                 depth2=0
                 )


**Example 2:**


This example retrieves a 24-year long timeseries of absolute dynamic topography (closely related to sea surface height) measured by satellite.
Notice, depth1 and depth2 values are automatically ignored because this is a surface dataset. The 'interval' parameter (line 24) has to 'y' indicating yearly binning (inter-annual timeseres). This example takes a few moments to run as the altimetry dataset is very large (multi-decade daily-global remote sensing).
The last few lines of code (lines 28-32) makes a simple plot to visualize the retrieved data.

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  %matplotlib inline
  import matplotlib.pyplot as plt
  import numpy as np
  import pycmap




  api = pycmap.API(token='<YOUR_API_KEY>')
  table, variable = 'tblAltimetry_REP', 'adt'
  df = api.time_series(
                     table=table,
                     variable=variable,
                     dt1='1994-01-01',
                     dt2='2017-12-31',
                     lat1=30,
                     lat2=32,
                     lon1=-160,
                     lon2=-158,
                     depth1=0,
                     depth2=0,
                     interval='y'
                     )


  plt.errorbar(df['year'], df['adt'], yerr=df['adt_std'], fmt='ob', capsize=3, alpha=0.4)
  plt.fill_between(df['year'], df['adt']-df['adt_std'], df['adt']+df['adt_std'], color='gray', alpha=0.2)
  plt.xlabel('Year')
  plt.ylabel(api.get_var_long_name(table, variable) + api.get_unit(table, variable))
  plt.show()


.. figure:: ../../../_static/overview_icons/sql.png
 :scale: 10 %

**SQL Statement**

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block::

   EXEC uspTimeSeries 'tableName', 'variable', 'dt1', 'dt2', 'lat1', 'lat2', 'lon1', 'lon2', 'depth1', 'depth2'

**Examples (different intervals):**

.. code-block::

   EXEC uspTimeSeries 'tblsst_AVHRR_OI_NRT', 'sst', '2016-01-01', '2016-12-31', '20', '25', '-160', '-158', '0', '0'

.. code-block::

   EXEC uspWeekly 'tblsst_AVHRR_OI_NRT', 'sst', '2016-01-01', '2016-12-31', '20', '25', '-160', '-158', '0', '0'

.. code-block::

   EXEC uspMonthly 'tblsst_AVHRR_OI_NRT', 'sst', '2016-01-01', '2016-12-31', '20', '25', '-160', '-158', '0', '0'

.. code-block::

   EXEC uspQuarterly 'tblsst_AVHRR_OI_NRT', 'sst', '2016-01-01', '2016-12-31', '20', '25', '-160', '-158', '0', '0'

.. code-block::

   EXEC uspAnnual 'tblsst_AVHRR_OI_NRT', 'sst', '2015-01-01', '2018-12-31', '20', '25', '-160', '-158', '0', '0'

   
