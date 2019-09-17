
.. _seaflow dataset: https://cmap.readthedocs.io/en/latest/catalog/datasets/SeaFlow.html#seaflow
.. _Pisces model: https://cmap.readthedocs.io/en/latest/catalog/datasets/Pisces.html#pisces
.. _dataset page: https://cmap.readthedocs.io/en/latest/catalog/datasets/Pisces.html#pisces


.. _matchCruise:

Match (colocalize) Cruise Track with Datasets
=============================================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/MatchCruise.ipynb


.. method:: along_track(cruise, targetTables, targetVars, depth1, depth2, temporalTolerance, latTolerance, lonTolerance, depthTolerance)


    This method colocalizes a cruise trajectory with the specified target variables. The matching results rely on the tolerance parameters because these parameters set the matching boundaries between the cruise trajectory and target datasets. Please note that the number of matching entries for each target variable might vary depending on the temporal and spatial resolutions of the target variable. In principle, if the cruise trajectory is fully covered by the target variable's spatio-temporal range, there should always be matching results if the tolerance parameters are larger than half of their corresponding spatial/temporal resolutions. Please explore the :ref:`Catalog` to find appropriate target variables to colocalize with the desired cruise.
    |
    This method returns a dataframe containing the cruise trajectory joined with the target variable(s).

    |

    :Parameters:

        **cruise: string**
            The official cruise name. If applicable, you may also use cruise "nickname" ('Diel', 'Gradients_1' ...). A full list of cruise names can be retrieved using cruise method.
        **targetTables: list of string**
            Table names of the target datasets to be matched with the source data. Notice source dataset can be matched with multiple target datasets. A full list of table names can be found in the :ref:`Catalog`.
        **targetVars: list of string**
            Variable short names to be matched with the source variable. A full list of variable short names can be found in the :ref:`Catalog`.
        **depth1: float**
            Start depth [m]. This parameter sets the lower bound of the depth cut on the target datasets. 'depth1' and 'depth2' allow matching a cruise trajectory (which is at the surface, hopefully!) with target variables at lower depth. Note depth is a positive number (depth is 0 at surface and grows towards ocean floor).
        **depth2: float**
            End depth [m]. This parameter sets the upper bound of the depth cut on the target datasets. Note depth is a positive number (depth is 0 at surface and grows towards ocean floor).

        **temporalTolerance: list of int**
            Temporal tolerance values between the cruise trajectory and target datasets. The size and order of values in this list should match those of targetTables. If only a single integer value is given, that would be applied to all target datasets. This parameter is in day units except when the target variable represents monthly climatology data in which case it is in month units. Notice fractional values are not supported in the current version.
        **latTolerance: list of float or int**
            Spatial tolerance values in meridional direction [deg] between the cruise trajectory and target datasets. The size and order of values in this list should match those of targetTables. If only a single float value is given, that would be applied to all target datasets. A "safe" value for this parameter can be slightly larger than the half of the target variable's spatial resolution.
        **lonTolerance: list of float or int**
            Spatial tolerance values in zonal direction [deg] between the cruise trajectory and target datasets. The size and order of values in this list should match those of targetTables. If only a single float value is given, that would be applied to all target datasets. A "safe" value for this parameter can be slightly larger than the half of the target variable's spatial resolution.
        **depthTolerance: list of float or int**
            Spatial tolerance values in vertical direction [m] between the cruise trajectory and target datasets. The size and order of values in this list should match those of targetTables. If only a single float value is given, that would be applied to all target datasets.

    :returns\:: Pandas dataframe.


|


Example 1:
----------

This example demonstrates how to colocalize the "Diel" cruise (official name: KM1513) with 2 target variables (lines 8-9):

-  'synecho_abundance' from underway `seaflow dataset`_
-  'NO3' from `Pisces model`_

The last few lines of this snippet plots the colocalized synecho_abundance versus NO3 concentration.

|

**Tip1:**

The official name of this cruise is 'KM1513' and one can use the official name, instead (line 7).

**Tip2:**

A full list of hosted cruise expeditions can be retrieved using the cruises method.

**Tip3:**

The temporalTolerance parameter is set to [0, 4] (line 12). This means:
-  ±0 day temporal tolerance when matching with 'synecho_abundance' (exact date-time matching)
-  ±4 day temporal tolerance when matching with 'NO3' (Pisces is a weekly averaged dataset)

**Tip4:**

The latTolerance and lonTolerance parameters are set to [0, 0.25] (lines 13-14). This means:
-  ±0 degree spatial tolerances (in meridional and zonal directions) when matching with 'synecho_abundance' (exact lat/lon matching)
-  ±0.25 degrees spatial tolerances (in meridional and zonal directions) when matching with 'NO3'. This dataset has 0.25 degree spatial resolution which means one may reduce the spatial tolerance for this target dataset down to 0.25/2 = 0.125 degrees.

**Tip5:**

The depthTolerance parameter is set to [5, 5] (line 20). This means:
The depthTolerance parameter is set to [5, 5] (line 20). This means: \*
±5 meters vertical tolerances when matching with 'synecho_abundance' \*
±5 meters vertical tolerances when matching with 'NO3'. Note that Pisces
dataset have several depth levels between surface and 5 m. The spacing
between the depth levels is not have uniform. See the `dataset page`_
for more details.




.. code-block:: python

  #!pip install pycmap -q     # uncomment to install pycmap, if necessary

  %matplotlib inline
  import matplotlib.pyplot as plt
  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  df = api.along_track(
                      cruise='diel',
                      targetTables=['tblSeaFlow', 'tblPisces_NRT'],
                      targetVars=['synecho_abundance', 'NO3'],
                      depth1=0,
                      depth2=5,
                      temporalTolerance=[0, 4],
                      latTolerance=[0, 0.25],
                      lonTolerance=[0, 0.25],
                      depthTolerance=[5, 5]
                      )


  plt.plot(df['NO3'], df['synecho_abundance'], '.')
  plt.ylabel('synecho_abundance' + api.get_unit('tblSeaFlow', 'synecho_abundance'))
  plt.xlabel('NO3' + api.get_unit('tblPisces_NRT', 'NO3'))



Example 2:
----------

Imagine you would like to colocalize a 'large' number of variables along track of multiple cruises. Hard-coding the variable names, table names, and tolerance parameters (as is shown in the previous example) is an error-prone process. This example show an alternative approach to implement multi-variable colocalization.

Here we colocalize two open-ocean North-Pacific transect cruises ('KOK1606' [gradient1], 'MGL1704' [gradient2]) with 14 variables from satellite datasets, model outputs, underway cruise measurements, and World-Ocean-Atlas climatology dataset. A full list of variables can be retrieved using the get_catalog() command. Also, please review the tips mentioned in the previous example since they are generally relevant to this case, too. It takes a few minutes to run this script since we are colocalizing two long cruises with multiple target variables. Reduce the number of cruises (line 12), and/or number of target variables (lines 19-36) to save time.


As a simple show case, the colocalized synechococcus abundance is plotted against latitude and is compared with phosphaste concentration from World Ocean Atlas monthly climatology dataset (line 91). The full colocalized dataset is stored in a csv file on local machine.

|

**Tip:**

Once the colocalization is finished, you may add new "calculated"
columns to the final dataframe:
``df['NO3_divided_Fe'] = df['NO3'] / df['Fe']``


.. code-block:: python

  import pandas as pd
  from collections import namedtuple
  import pycmap



  def open_ocean_cruises():
      return ['MGL1704', 'KOK1606']


  def match_params():
      Param = namedtuple('Param', ['table', 'variable', 'temporalTolerance', 'latTolerance', 'lonTolerance', 'depthTolerance'])
      params = []
      ######## ship data (not calibrated)
      params.append(Param('tblCruise_Salinity', 'salinity', 0, 0.1, 0.1, 5))
      params.append(Param('tblCruise_Temperature', 'temperature', 0, 0.1, 0.1, 5))
      ######## underway seaflow
      params.append(Param('tblSeaFlow', 'prochloro_abundance', 0, 0.1, 0.1, 5))
      params.append(Param('tblSeaFlow', 'synecho_abundance', 0, 0.1, 0.1, 5))
      ######## satellite
      params.append(Param('tblCHL_REP', 'chl', 4, 0.25, 0.25, 5))
      params.append(Param('tblModis_AOD_REP', 'AOD', 15, 1, 1, 5))
      params.append(Param('tblAltimetry_REP', 'sla', 1, 0.25, 0.25, 5))
      ####### model
      params.append(Param('tblPisces_NRT', 'Fe', 4, 0.5, 0.5, 5))
      params.append(Param('tblPisces_NRT', 'NO3', 4, 0.5, 0.5, 5))
      params.append(Param('tblPisces_NRT', 'PO4', 4, 0.5, 0.5, 5))
      params.append(Param('tblDarwin_Nutrient_Climatology', 'NH4_darwin_clim', 0, 0.5, 0.5, 5))
      params.append(Param('tblDarwin_Nutrient_Climatology', 'SiO2_darwin_clim', 0, 0.5, 0.5, 5))
      ####### WOA
      params.append(Param('tblWOA_Climatology', 'density_WOA_clim', 0, .75, .75, 5))
      params.append(Param('tblWOA_Climatology', 'phosphate_WOA_clim', 0, 0.75, 0.75, 5))

      tables, variables, temporalTolerance, latTolerance, lonTolerance, depthTolerance = [], [], [], [], [], []
      for i in range(len(params)):
          tables.append(params[i].table)
          variables.append(params[i].variable)
          temporalTolerance.append(params[i].temporalTolerance)
          latTolerance.append(params[i].latTolerance)
          lonTolerance.append(params[i].lonTolerance)
          depthTolerance.append(params[i].depthTolerance)
      return tables, variables, temporalTolerance, latTolerance, lonTolerance, depthTolerance



  def plot(api, df):
      tbl1, tbl2 = 'tblSeaFlow', 'tblWOA_Climatology'
      var1, var2 = 'prochloro_abundance', 'phosphate_WOA_clim'
      fig, ax1 = plt.subplots()
      ax2 = ax1.twinx()
      ax1.plot(df['lat'], df[var1], 'g.', alpha=0.4)
      ax2.plot(df['lat'], df[var2], 'b.', alpha=0.4)
      ax1.set_xlabel('latitude [deg]')
      ax1.set_ylabel(var1 + api.get_unit(tbl1, var1), color='g')
      ax2.set_ylabel(var2 + api.get_unit(tbl2, var2), color='b')
      plt.show()
      return



  def main():
      api = pycmap.API(token='<YOUR_API_KEY>')
      cruises = open_ocean_cruises()
      tables, variables, temporalTolerance, latTolerance, lonTolerance, depthTolerance = match_params()
      df = pd.DataFrame({})
      for cruise in cruises:
          print('\n********************************')
          print('Colocalizing %s cruise...' % cruise)
          print('********************************\n')
          data = api.along_track(
                                cruise=cruise,
                                targetTables=tables,
                                targetVars=variables,
                                temporalTolerance=temporalTolerance,
                                latTolerance=latTolerance,
                                lonTolerance=lonTolerance,
                                depthTolerance=depthTolerance,
                                depth1=0,
                                depth2=5
                                )
          if len(df) < 1:
              df = data
          else:
              df = pd.concat([df, data], ignore_index=True)
          data.to_csv('%s.csv' % cruise, index=False)
      df.to_csv('sfMatch.csv', index=False)
      plot(api, df)
      return df



  if __name__ == '__main__':
      df = main()

  # the results are stored in csv files at the current working address
  # if you are running this script on colab, run the following command to list the generated csv files:
  #!ls
