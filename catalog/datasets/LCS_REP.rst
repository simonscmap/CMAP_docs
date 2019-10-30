:orphan:

.. _LCS_REP:



LCS Reprocessed
***************

.. |globe| image:: /_static/catalog_thumbnails/globe.png
   :scale: 10%
   :align: middle
.. |sat| image:: /_static/catalog_thumbnails/satellite.png
   :scale: 10%
   :align: middle



+-------------------------------+----------+-------------+------------------------+-------------------+---------------------+---------------------+
| Dataset Name                  | Sensor   |  Make       |  Spatial Resolution    |Temporal Resolution|  Start Date         |  End Date           |
+===============================+==========+=============+========================+===================+=====================+=====================+
| :ref:`LCS_REP`                | |sat|    | Observation |     0.04° X 0.04°      |         Daily     |  2016-01-01         | 2018-05-27          |
+-------------------------------+----------+-------------+------------------------+-------------------+---------------------+---------------------+


Dataset Description
*******************



.. mdinclude:: ../dataset_descriptions/LCS_desc.md
    :start-line: 0
    :end-line: 12

.. math::
   \begin{equation} \label{Eq:Lyapunov}
   \Lambda = \lim_{|\delta x(t_0)| \to 0}  \lim_{t \to \infty} \frac{1}{t} \log \frac{\delta x(t)}{\delta x(t_0)}
   \end{equation}


such that :math:`\Lambda` is the Lyapunov exponent, and :math:`\delta x(t)`, :math:`\delta x(0)` represent the separation between the tracers at times :math:`t` and :math:`t_0`, receptively.

.. mdinclude:: ../dataset_descriptions/LCS_desc.md
    :start-line: 20




Table of Variables
******************

.. raw:: html

    <iframe src="../../_static/var_tables/LCS_REP/LCS_REP.html"  frameborder = 0 height = '200px' width="100%">></iframe>

|

Data Source
***********

Simons CMAP

https://github.com/mdashkezari/opedia/tree/master/CS

https://github.com/mdashkezari/opedia/tree/master/CS/docs/CS.pdf

How to Acknowledge
******************


Version History
***************
