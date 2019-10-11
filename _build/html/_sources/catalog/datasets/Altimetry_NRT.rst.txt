:orphan:

.. _Altimetry_NRT:



Altimetry Near-Real-Time
************************

.. |globe| image:: /_static/catalog_thumbnails/globe.png
   :scale: 10%
   :align: middle
.. |sat| image:: /_static/catalog_thumbnails/satellite.png
   :scale: 10%
   :align: middle

.. _here: http://marine.copernicus.eu/services-portfolio/access-to-products/?option=com_csw&view=details&product_id=SEALEVEL_GLO_PHY_L4_NRT_OBSERVATIONS_008_046

.. _`Sea Level Quality Information Document`: http://resources.marine.copernicus.eu/documents/QUID/CMEMS-SL-QUID-008-032-062.pdf

+-------------------------------+----------+-------------+------------------------+-------------------+---------------------+---------------------+
| Dataset Name                  |  Sensor  |  Make       | Spatial Resolution     |Temporal Resolution|  Start Date         |  End Date           |
+===============================+==========+=============+========================+===================+=====================+=====================+
| :ref:`Altimetry_NRT`          | |sat|    | Observation |     1/4° X 1/4°        |         Daily     |  2019-01-01         | 2019-04-28          |
+-------------------------------+----------+-------------+------------------------+-------------------+---------------------+---------------------+


Dataset Description
*******************


The near-real-time altimetry dataset in CMAP was provided by CMEMS. It is a 1/4° daily global gridded satellite product of sea level altimetry and derived variables (sla,adt,vgos,vgosa,ugos,ugosa). Sea Level Anomaly (SLA) measurements were calculated with respect to a twenty year average from 2012.
Altimeter satellite gridded Sea Level Anomalies (SLA) computed with respect to a twenty-year 2012 mean. The SLA is estimated by from the along-track Level 3 altimetry product and then Optimal Interpolated to produce a near-real-time altimetry products

A more detailed description of the processing techniques can be found here_. Quality control and sources of error are described in detail in the CMEMS `Sea Level Quality Information Document`_. In summary, the source of error partially depends on the number of satellites per observation. QA checks of the gridded product are done by comparing measurements against in-situ tide gauge readings. With only two altimeters overhead, SLA errors in the low variability areas such as the open ocean can reach 1.4 cm², while the error in high variability areas reaching up to 37.7 cm². Errors within coastal areas (defined as within 200 km of land), are typically 8.2 cm².

The CMEMS internal name for this dataset is: **SEALEVEL_GLO_PHY_L4_NRT_OBSERVATIONS_008_046**.




Table of Variables
******************


.. raw:: html

    <iframe src="../../_static/var_tables/Near-Real-Time%20Altimetry/Near-Real-Time%20Altimetry.html"  frameborder = 0 height = '250px' width="100%">></iframe>





|





Data Source
***********

http://marine.copernicus.eu/

http://marine.copernicus.eu/services-portfolio/access-to-products/?option=com_csw&view=details&product_id=SEALEVEL_GLO_PHY_L4_NRT_OBSERVATIONS_008_046

http://cmems-resources.cls.fr/documents/PUM/CMEMS-SL-PUM-008-032-051.pdf

How to Acknowledge
******************

E.U. Copernicus Marine Service Information

Version History
***************
