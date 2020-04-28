.. _subset_ST:



Data Subset: Generic Space-Time Cut
===================================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/SpaceTime.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FSpaceTime.ipynb





.. method:: space_time(table, variable, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)


    Returns a subset of data according to the specified space-time constraints (dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2).
    The results are ordered by time, lat, lon, and depth (if exists), respectively.

    |

    :Parameters:

        **table: string**
            Table name (each dataset is stored in a table). A full list of table names can be found in :ref:`Catalog`.
        **variable: string**
            Variable short name which directly corresponds to a field name in the table. A subset of this variable is returned by this method according to the spatio-temporal cut parameters (below). Pass * wild card to retrieve all fields in a table. A full list of variable short names can be found in :ref:`Catalog`.
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
            Start longitude [degree E]. This parameter sets the lower bound of the zonal cut. Note longitude ranges from -180° to 180°.
        **lon2: float**
            End longitude [degree E]. This parameter sets the upper bound of the zonal cut. Note longitue ranges from -180° to 180°.
        **depth1: float**
            Start depth [m]. This parameter sets the lower bound of the vertical cut. Note depth is a positive number (it is 0 at the surface and increases towards the ocean floor).
        **depth2: float**
            End depth [m]. This parameter sets the upper bound of the vertical cut. Note depth is a positive number (it is 0 at the surface and increases towards the ocean floor).


    :returns\:: Pandas dataframe.


|

**Example 1:**

This example retrieves a subset of in-situ salinity measurements by Argo floats.

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.space_time(
                table='tblArgoMerge_REP',
                variable='argo_merge_salinity_adj',
                dt1='2015-05-01',
                dt2='2015-05-30',
                lat1=28,
                lat2=38,
                lon1=-71,
                lon2=-50,
                depth1=0,
                depth2=100
                )


**Example 2:**


Query all variables within the global Mesoscale Eddy dataset (see the wild card at line 10).
The last few lines of code (lines 21-27) makes a couple of simple visualizations showing the eddy radius distribution.

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  %matplotlib inline
  import matplotlib.pyplot as plt
  import pycmap

  api = pycmap.API(token='YOUR_API_KEY>')
  df = api.space_time(
                table='tblMesoscale_Eddy',
                variable='*',
                dt1='2018-01-01',
                dt2='2018-01-01',
                lat1=-90,
                lat2=90,
                lon1=-180,
                lon2=180,
                depth1=0,
                depth2=0
                )

  fig, axes = plt.subplots(nrows=1, ncols=2)
  ax1 = df['eddy_radius'].plot.hist(ax=axes[0], bins=50)
  _ = ax1.set_xlabel('Eddy Radius (km)')
  ax2 = df.plot(kind='scatter', x='lat', y='eddy_radius', ax=axes[1], alpha=0.3)
  ax2.yaxis.tick_right()
  ax2.yaxis.set_label_position('right')
  _ = ax2.set_ylabel('Eddy Radius (km)')





**Example 3:**

This example retrieves a subset of sea surface temperature measured by satellite.
Notice, depth1 and depth2 values are automatically ignored because this is a surface dataset.
A simple plot is made to visualize the retrieved data.

.. code-block:: python


  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  %matplotlib inline
  import matplotlib.pyplot as plt
  import numpy as np
  import pycmap



  def plot(df):
      lat = df.lat.unique()
      lon = df.lon.unique()
      shape = (len(lat), len(lon))
      data = df.sst.values.reshape(shape)
      plt.imshow(data, extent=[np.min(lon), np.max(lon), np.min(lat), np.max(lat)], cmap='coolwarm', origin='bottom', vmin=0, vmax=30)
      plt.title('Sea Surface Temperature')
      plt.colorbar()
      plt.xlabel('Longitude')
      plt.ylabel('Latitude')
      plt.show()


  api = pycmap.API(token='<YOUR_API_KEY>')
  df = api.space_time(
                     table='tblsst_AVHRR_OI_NRT',
                     variable='sst',
                     dt1='2016-04-30',
                     dt2='2016-04-30',
                     lat1=10,
                     lat2=70,
                     lon1=-180,
                     lon2=-80,
                     depth1=0,
                     depth2=0
                     )
  plot(df)

.. figure:: /_static/overview_icons/sql.png
 :scale: 10 %

**SQL Statement**

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.



.. code-block:: sql

  EXEC uspSpaceTime 'tableName', 'variable', 'dt1', 'dt2', 'lat1', 'lat2', 'lon1', 'lon2', 'depth1', 'depth2'

**Example:**

.. code-block:: sql

  EXEC uspSpaceTime 'tblsst_AVHRR_OI_NRT', 'sst', '2016-04-30', '2016-04-30', '10', '70', '-180', '80', '0', '0'
