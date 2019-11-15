.. _subset_DP:



Data Subset: Depth Profile
==========================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/DepthProfile.ipynb


.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FDepthProfile.ipynb


.. method:: depth_profile(table, variable, dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2)


    Returns a subset of data according to the specified space-time constraints (dt1, dt2, lat1, lat2, lon1, lon2, depth1, depth2). The returned data subset is aggregated by depth: at each depth level the mean and standard deviation of the variable values within the space-time constraints are computed. The sequence of these values construct the depth profile. The resulted depth profile is returned in form of a Pandas dataframe ordered by depth.

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



    :returns\:: Pandas dataframe.


|

**Example 1:**

This example retrieves a depth profile of in-situ chlorophyll concentration measurements by Argo Floats. The last few lines of code (lines 22-25) creates a simple plot showing the chlorophyll depth profile (deep chlorophyll maximum near 100 m).

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  %matplotlib inline
  import matplotlib.pyplot as plt
  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  table, variable = 'tblArgoMerge_REP', 'argo_merge_chl_adj'
  df = api.depth_profile(
                        table=table,
                        variable=variable,
                        dt1='2016-04-30',
                        dt2='2016-04-30',
                        lat1=20,
                        lat2=24,
                        lon1=-170,
                        lon2=-150,
                        depth1=0,
                        depth2=1500
                        )




**Example 2:**


This example retrieves depth profile of modeled chlorophyll concentration estimated by Pisces, a weekly 0.5° resolution BioGeoChemical model. The last few lines of code (lines 22-25) creates a simple plot showing the chlorophyll depth profile. The deep chlorophyll maximum (DCM) is approximately near ~100 m, closely matching the in-situ observations by ARGO Floats (see the previous example).

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  %matplotlib inline
  import matplotlib.pyplot as plt
  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  table, variable = 'tblPisces_NRT', 'CHL'
  df = api.depth_profile(
                        table=table,
                        variable=variable,
                        dt1='2016-04-30',
                        dt2='2016-04-30',
                        lat1=20,
                        lat2=24,
                        lon1=-170,
                        lon2=-150,
                        depth1=0,
                        depth2=1500
                        )

  plt.plot(df['depth'], df[variable])
  plt.xlabel('Depth [m]')
  plt.ylabel(api.get_var_long_name(table, variable) + api.get_unit(table, variable))
  plt.show()
