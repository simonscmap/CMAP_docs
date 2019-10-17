:orphan:

.. _Eddy:



Eddy
****

.. |globe| image:: /_static/catalog_thumbnails/globe.png
   :scale: 10%
   :align: middle
.. |sat| image:: /_static/catalog_thumbnails/satellite.png
   :scale: 10%
   :align: middle

.. |sm| image:: /_static/tutorial_pics/sparse_mapping.png
 :align: middle
 :scale: 10%
 :target: ../../tutorials/regional_map_sparse.html


.. |ts| image:: /_static/tutorial_pics/TS.png
  :align: middle
  :scale: 25%
  :target: ../../tutorials/time_series.html

.. |hst| image:: /_static/tutorial_pics/hist.png
  :align: middle
  :scale: 25%
  :target: ../../tutorials/histogram.html

.. |sec| image:: /_static/tutorial_pics/section.png
  :align: middle
  :scale: 20%
  :target: ../../tutorials/section.html

.. |dep| image:: /_static/tutorial_pics/depth_profile.png
  :align: middle
  :scale: 25%
  :target: ../../tutorials/depth_profile.html

.. |edy| image:: /_static/tutorial_pics/eddy_sampling.png
  :align: middle
  :scale: 25%
  :target: ../../tutorials/eddy.html

.. _`[Schlax & Chelton, 2016]`: http://wombat.coas.oregonstate.edu/eddies/Growing_Method_of_Eddy_Identification_and_Tracking.pdf

.. _`Eddy Trajectory Atlas Product Handbook`: https://www.aviso.altimetry.fr/fileadmin/documents/data/tools/hdbk_eddytrajectory_META2018.pdf



+-------------------------------+----------+-------------+------------------------+-------------------+---------------------+---------------------+
| Dataset Name                  | Sensor   |  Make       |  Spatial Resolution    |Temporal Resolution|  Start Date         |  End Date           |
+===============================+==========+=============+========================+===================+=====================+=====================+
| :ref:`Eddy`                   | |sat|    | Observation |       Irregular        |         Daily     |  1993-01-01         | 2018-01-18          |
+-------------------------------+----------+-------------+------------------------+-------------------+---------------------+---------------------+




Dataset Description
*******************

Simons CMAP contains **Eddy** records from  1993-01-01 through 2018-01-18  collected from AVISO+. The dataset was developed and validated in collaboration between Aviso+ and with D.Chelton  and M. Schlax at Oregon State University.
This dataset has a spatial resolution of 1/4° X 1/4° and a daily temporal resolution. Each eddy has associated (cyclonic/anticyclonic), speed, radius metadata.

To detect eddies, this datasets uses ADT and SLA measurements from multiple altimetry satellite missions. Eddy's that may come within proximity to land are filtered out. Details on the detection algorithm can be found in `[Schlax & Chelton, 2016]`_.
More details on detection, filtering and processing can be found in the `Eddy Trajectory Atlas Product Handbook`_.

The AVISO+ product name is: Merged delayed-time version 2.0exp

Table of Variables
******************

.. raw:: html

    <iframe src="../../_static/var_tables/tblMesoscale_Eddy/tblMesoscale_Eddy.html"  frameborder = 0 height = '200px' width="100%">></iframe>

|

Data Source
***********

https://www.aviso.altimetry.fr/en/data/products/value-added-products/global-mesoscale-eddy-trajectory-product.html

How to Acknowledge
******************


The altimeter the Mesoscale Eddy Trajectory Atlas products were produced by SSALTO/DUACS and distributed by AVISO+ (https://www.aviso.altimetry.fr/ ) with support from CNES, in collaboration with Oregon State University with support from NASA


Dudley B. Chelton, Michael G. Schlax, Roger M. Samelson,
Global observations of nonlinear mesoscale eddies,
Progress in Oceanography,
Volume 91, Issue 2,
2011,
Pages 167-216,
ISSN 0079-6611,
https://doi.org/10.1016/j.pocean.2011.01.002.
(http://www.sciencedirect.com/science/article/pii/S0079661111000036)


Version History
***************

Merged delayed-time version 2.0exp
