.. _climatology:


Climatology
===========


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Climatology.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FClimatology.ipynb

.. _`catalog`: https://cmap.readthedocs.io/en/latest/user_guide/API_ref/pycmap_api/data_retrieval/pycmap_catalog.html
.. _`API key`: https://cmap.readthedocs.io/en/latest/user_guide/API_ref/pycmap_api/pycmap_api_ref.html
.. _`APIs vizEngine`: https://cmap.readthedocs.io/en/latest/user_guide/API_ref/pycmap_api/pycmap_api_ref.html

.. method:: climatology(table, variable, period, periodVal, lat1, lat2, lon1, lon2, depth1, depth2)


    Computes the climatology of a gridded dataset over a spatial domain delimited by (lat1, lat2, lon1, lon2, depth1, depth2). Note this method does not apply to sparse datasets. The parameter period specifies the climatology interval (e.g weekly, monthly...) and periodVal sets the interval value. For example, to compute the climatology of a variable for the month of October, period is set to 'month' and periodVal is set to 10. Please avoid using periods that are finner than the temporal resolution of the underlying dataset. For instance, if the dataset is a weekly-averaged product, do not set the period to 'dayofyear'.

    |

    The output of this method is a Pandas DataFrame ordered by time, lat, lon, and depth (if exists), respectively.


    |

    :Parameters:
        **table: string**
            Table name (each dataset is stored in a table). A full list of table names can be found in `catalog`_.
        **variable: string**
            Variable short name which directly corresponds to a field name in the table. A subset of this variable's climatology is returned by this method according to the spatio cut parameters (below). A full list of variable short names can be found in `catalog`_.
        **period: string**
            Specifies the aggregation period and can be either one of the following values:
            'd' or 'dayofyear' for day-of-year climatology
            'w' or 'week' or 'weekly' for weekly climatology
            'm' or 'month' or 'monthly' for monthly climatology
            'a' or 'y' or 'yearly' for interannual averaging
        **periodVal: string**
            Sets the value of the climatology interval. For instance, to retrieve the chlorophyll climatology for the month of March period is set to 'month' and periodVal is set to 3 (see example below).
        **lat1: float**
            Start latitude [degree N]. This parameter sets the lower bound of the meridional cut. Note latitude ranges from -90° to 90°.
        **lat2: float**
            End latitude [degree N]. This parameter sets the upper bound of the meridional cut. Note latitude ranges from -90° to 90°.
        **lon1: float**
            Start longitude [degree E]. This parameter sets the lower bound of the zonal cut. Note longitue ranges from -180° to 180°.
        **lon2: float**
            End longitude [degree E]. This parameter sets the upper bound of the zonal cut. Note longitue ranges from -180° to 180°.
        **depth1: float**
            Start depth [m]. This parameter sets the lower bound of the vertical cut. Note depth is a positive number (it is 0 at surface and grows towards ocean floor).
        **depth2: float**
            End depth [m]. This parameter sets the upper bound of the vertical cut. Note depth is a positive number (it is 0 at surface and grows towards ocean floor).


    :returns:

        Pandas dataframe.

|

Example 1:
----------

This example computes and retrieves a subset of `sea surface salinity`_ weekly climatology for the week of 46.

.. _`sea surface salinity`: https://cmap.readthedocs.io/en/latest/catalog/datasets/SSS.html#SSS


.. code-block:: python


  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.climatology(
                  table='tblSSS_NRT',
                  variable='sss',
                  period='week',
                  periodVal=46,
                  lat1=20,
                  lat2=50,
                  lon1=-170,
                  lon2=-120,
                  depth1=0,
                  depth2=0
                  )


Example 2:
----------

This example computes and retrieves a subset of `chlorophyll`_ climatology for the month of March.
Notice, depth1 and depth2 values are automatically ignored because this is a surface dataset.
A simple plot is made to visualize the retrieved data.

.. _`chlorophyll`: https://cmap.readthedocs.io/en/latest/catalog/datasets/Chlorophyll_REP.html#chlorophyll-rep

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
      data = df.chl.values.reshape(shape)
      plt.imshow(data, extent=[np.min(lon), np.max(lon), np.min(lat), np.max(lat)], cmap='viridis', origin='lower', vmin=0, vmax=0.5)
      plt.title('Sea Surface Chlorophyll [mg/m^3]')
      plt.colorbar()
      plt.xlabel('Longitude')
      plt.ylabel('Latitude')
      plt.show()


  api = pycmap.API(token='<YOUR_API_KEY>')
  df = api.climatology(
                       table='tblCHL_REP',
                       variable='chl',
                       period='month',
                       periodVal=3,
                       lat1=10,
                       lat2=70,
                       lon1=-180,
                       lon2=-100,
                       depth1=0,
                       depth2=0
                       )
  plot(df)



.. raw:: html

   <iframe src="../../../../_static/pycmap_tutorial_viz/static/climatology.png"  frameborder = 0  height="550px" width="100%">></iframe>

|

.. figure:: /_static/overview_icons/sql.png
  :scale: 10 %

**SQL Statement**

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block:: sql

  EXEC uspAggregate 'tableName', 'variable', 'period', 'periodVal', 'lat1', 'lat2', 'lon1', 'lon2', 'depth1', 'depth2'

**Example:**

.. code-block:: sql

  EXEC uspAggregate 'tblCHL_REP', 'chl', 'month', '3', '10', '70', '-180', '100', '0', '0'
