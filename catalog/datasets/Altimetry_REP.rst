:orphan:

.. _Altimetry_REP:


Altimetry Reprocessed
*********************

.. |globe| image:: /_static/catalog_thumbnails/globe.png
   :scale: 10%
   :align: middle
.. |sat| image:: /_static/catalog_thumbnails/satellite.png
   :scale: 10%
   :align: middle


.. _here: http://marine.copernicus.eu/services-portfolio/access-to-products/?option=com_csw&view=details&product_id=SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047

.. _`Sea Level Quality Information Document`: http://resources.marine.copernicus.eu/documents/QUID/CMEMS-SL-QUID-008-032-062.pdf

+-------------------------------+----------+-------------+------------------------+-------------------+---------------------+---------------------+
| Dataset Name                  | Sensor   |  Make       |  Spatial Resolution    |Temporal Resolution|  Start Date         |  End Date           |
+===============================+==========+=============+========================+===================+=====================+=====================+
| :ref:`Altimetry_REP`          | |sat|    | Observation |     1/4° X 1/4°        |         Daily     |  1993-01-01         | 2018-06-10          |
+-------------------------------+----------+-------------+------------------------+-------------------+---------------------+---------------------+


Dataset Description
*******************


The reprocessed altimetry dataset in CMAP was provided by CMEMS. It is a 1/4° daily global gridded satellite product of sea level altimetry and derived variables (sla,adt,vgos,vgosa,ugos,ugosa). The creation of this dataset was possible by taking data from multiple altimetry missions and homogenizing them with the same processing techniques, models and geophysical corrections.
The OSTM/Jason-2 mission was used as a reference dataset, with accompanying data from Jason-3, Sentinel-3A, HY-2A, Saral/AltiKa, Cryosat-2, Jason-2, Jason-1, T/P, ENVISAT, GFO and ERS1/2.

A more detailed description of the processing techniques can be found here_. Quality control and sources of error are described in detail in the CMEMS `Sea Level Quality Information Document`_. In summary, the source of error partially depends on the number of satellites per observation. QA checks of the gridded product are done by comparing measurements against in-situ tide gauge readings. With only two altimeters overhead, SLA errors in the low variability areas such as the open ocean can reach 1.4 cm², while the error in high variability areas reaching up to 37.7 cm². Errors within coastal areas (defined as within 200 km of land), are typically 8.2 cm².

The CMEMS internal name for this dataset is: **SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047**.





Table of Variables
******************


.. raw:: html

    <iframe src="../../_static/var_tables/Reprocessed%20Altimetry/Reprocessed%20Altimetry.html"  frameborder = 0 height = '250px' width="100%">></iframe>




|


Data Source
***********

http://marine.copernicus.eu/

http://marine.copernicus.eu/services-portfolio/access-to-products/?option=com_csw&view=details&product_id=SEALEVEL_GLO_PHY_L4_REP_OBSERVATIONS_008_047

http://cmems-resources.cls.fr/documents/PUM/CMEMS-SL-PUM-008-032-051.pdf

How to Acknowledge
******************

E.U. Copernicus Marine Service Information

Version History
***************
