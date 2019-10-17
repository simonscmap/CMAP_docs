:orphan:


.. _SSS:

Sea Surface Salinity
********************

.. |globe| image:: /_static/catalog_thumbnails/globe.png
   :scale: 10%
   :align: middle
.. |sat| image:: /_static/catalog_thumbnails/satellite.png
   :scale: 10%
   :align: middle



.. _`Technical Documentaion`: https://podaac-tools.jpl.nasa.gov/drive/files/allData/smap/docs/V4/RSS_SMAP-SSS_V4.0_TechnicalDocumentation.pdf

+-------------------------------+----------+-------------+------------------------+-------------------+---------------------+---------------------+
| Dataset Name                  | Sensor   |  Make       |  Spatial Resolution    |Temporal Resolution|  Start Date         |  End Date           |
+===============================+==========+=============+========================+===================+=====================+=====================+
| :ref:`SSS`                    | |sat|    | Observation |     70km x 70km        |         Daily     |  2015-03-31         | 2019-04-21          |
+-------------------------------+----------+-------------+------------------------+-------------------+---------------------+---------------------+



Dataset Description
*******************

The Sea Surface Salinity dataset in CMAP is the the **SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V3_70KM_1** NASA dataset.
This 8-day running mean sea surface salinity product has near-global spatial coverage gridded to ~ 70km x 70km grid cells. While a 40km x 40km product exists, the 70km product has a much higher SNR.
The SSS data is derived from an L-band radiometer atop of the *Soil Moisture Active Pass* (SMAP) satellite mission. SMAP operates in a near-polar orbit with a beam swath of 1000km. Exact repeat overpasses happen every eight days, with near global coverage every three days.

SSS data was referenced against the HYCOM reference salinity field. Multiple QA flags are described on page 38 of the `Technical Documentaion`_.

.. note::
  Two known issues identified by that dataset distributor are:

  | -Satellite retrieval performance was degraded between Apr. 2015 - Aug. 2015, possibly due to instrument calibration issues.
  | -Eight of the total observations days were missing a sea-ice mask. To minimize contamination of salinity samples, these data were excluded from the Level-2 product, therefore some of the level-3 gridded products around these dates may have less total observations. The dates are: 12-03-2015, 12-03-2015, 04-15-2016, 04-16-2016, 09-27-2017, 09-28-2017, 11-25-2017 and 12-16-2018


Table of Variables
******************

.. raw:: html

    <iframe src="../../_static/var_tables/SMAP%20ocean%20surface%20salinity/SMAP%20ocean%20surface%20salinity.html"  frameborder = 0 height = '100px' width="100%">></iframe>



|

Data Source
***********

Remote Sensing Systems, Santa Rosa, CA, USA

http://www.remss.com/missions/smap/

https://podaac.jpl.nasa.gov/dataset/SMAP_RSS_L3_SSS_SMI_8DAY-RUNNINGMEAN_V4

How to Acknowledge
******************

Meissner, T., F. Wentz, A. Manaster, 2018.Remote Sensing Systems SMAP L2C Sea Surface Salinity, Version 3.0 validated release, Remote Sensing Systems, Santa Rosa, CA, USA.

Fore,A.G, S.H. Yueh, W. Tang, B.W. Stiles, and A.K. Hayashi (2016). Combined Active/Passive Retrievals of Ocean Vector Wind and Sea Surface Salinity With SMAP. IEEE TRANSACTIONS ON GEOSCIENCE AND REMOTE SENSING, VOL. 54, NO. 12. p.7396-7404. DOI: 10.1109/TGRS.2016.2601486

SMAP salinity are produced by Remote Sensing Systems and sponsored by NASA. Data are available at www.remss.com

Version History
***************

**4.0**
