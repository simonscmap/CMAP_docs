:orphan:

.. _Darwin_clim:


Darwin Climatology
******************


.. |globe| image:: /_static/catalog_thumbnails/globe.png
   :scale: 10%
   :align: middle

.. |comp| image:: /_static/catalog_thumbnails/comp_2.png
   :scale: 10%
   :align: middle

.. |rm| image:: /_static/tutorial_pics/regional_map.png
 :align: middle
 :scale: 20%
 :target: ../../tutorials/regional_map_gridded.html

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


+-------------------------------+----------+----------+-------------+------------------------+----------------------+--------------+--------------+
| Dataset Name                  | Coverage | Sensor   |  Make       |     Spatial Resolution | Temporal Resolution  |  Start Date  |  End Date    |
+===============================+==========+==========+=============+========================+======================+==============+==============+
| :ref:`Darwin_clim`            |  |globe| | |comp|   |   Model     |     1/2° X 1/2°        | Monthly Climatology  |              |              |
+-------------------------------+----------+----------+-------------+------------------------+----------------------+--------------+--------------+


Table of Variables
******************

.. raw:: html

    <iframe src="../../_static/var_tables/Darwin-MITgcm%20Climatology/Darwin-MITgcm%20Climatology.html"  frameborder = 0 height = '300px' width="100%">></iframe>

|

.. raw:: html

    <iframe src="../../_static/var_depths/Darwin_depth.html"  frameborder = 0 height = '200px' width="100%">></iframe>

|

.. raw:: html

    <iframe src="../../_static/var_plots/prokaryote_c02_darwin_clim.html"  frameborder = 0  height="500px" width="100%">></iframe>

|



Dataset Description
*******************

This version of the model is modified from Dutkiewicz et al. (2015) and Ward et al. (2012). It includes the biogeochemical cycling of carbon, nitrogen, phosphorus, silica, iron and oxygen, a complex marine ecosystem, incorporating both functional and size diversity of phytoplankton and zooplankton, as well as dissolved organic matter (including an explicit colored component, CDOM), and organic particulate matter. An explicit radiative transfer component and spectral treatment of irradiance provides output that is similar to data provided by ocean color satellite instruments (surface reflectance) and also subsurface optical characteristics such as absorption and scattering.
There are 35 phytoplankton types (2 pico-prokaryotes, 2 pico-eukaryotes, 5 coccolithophore, 5 diazotrophs, 11 diatoms, 10 mixotrophic dinoflagellates) and 16 zooplankton types ranging from 0.6µm to 2500 µm equivalent spherical diameter. Parameters influencing growth, grazing, and sinking are related to size (following Ward et al., 2012) with specific differences between functional groups. This simulation uses Monod kinetics, and C:N:P:Fe stoichiometry are constant over time (though do differ between different phytoplankton groups). The zooplankton preferentially graze on plankton 10 times smaller than themselves with a Holling III function. The distributions of the plankton in this model compare well with both observations based on functional types as well as size distributions. We have incorporated distinct absorption and scattering spectra for the different phytoplankton (as in Dutkiewicz et al., 2015) as well as flattening of the spectra with size for absorption and scattering.


In **Darwin_v0.1_llc90**, this ecosystem model is driven by the physical ocean model of Forget et al, 2015 (ECCO version 4, https://eccov4.readthedocs.io) which runs on a 1-degree, global grid called LLC90 (Forget et al, 2015). This physical ocean model benefits from optimized parameterizations (small- and meso-scale turbulence) and atmospheric boundary conditions (air-sea fluxes). As a result, it matches in-situ observations (T, S, MLD, etc.) and remote sensing data (SST, altimetry, etc.) better than earlier ECCO solutions do (Forget, Ferreira, Liang 2015, Forget and Ponte 2015). Another advantage of this model configuration is that it is easy and inexpensive to rerun in order to produce more output or to experiment with the ecosystem and physical model settings (Forget 2018, 2019, https://cbiomes.readthedocs.io). Results here have been interpolated to a ½ degree grid.

Data Source
***********

http://darwinproject.mit.edu/


How to Acknowledge
******************

- Dutkiewicz, S., A.E. Hickman, O. Jahn, W.W. Gregg, C.B. Mouw, and M.J. Follows, 2015:  Capturing optically important constituents and properties in a marine biogeochemical and ecosystem model. Biogeoscience, 12, 4447-4481 doi:10.5194/bg-12-4447-2015, https://doi.org/10.5194/bg-12-4447-2015
- Forget, G., Campin, J.-M., Heimbach, P., Hill, C. N., Ponte, R. M., and Wunsch, C.: ECCO version 4: an integrated framework for non-linear inverse modeling and global ocean state estimation, Geosci. Model Dev., 8, 3071-3104, https://doi.org/10.5194/gmd-8-3071-2015, 2015
- Forget, G., D. Ferreira, and X. Liang, 2015: On the observability of turbulent transport rates by argo: supporting evidence from an inversion experiment. Ocean Science, 11, 839–853, doi:10.5194/os-11-839-2015
- Forget, G. and R. Ponte, 2015: The partition of regional sea level variability. Progress in Oceanography, 137, 173–195, https://doi.org/10.1016/j.pocean.2015.06.002
- Forget, G., 2018: Initial, preliminary version of the CBIOMES-global model setup and documentation (Version v0.0.1). Zenodo. http://doi.org/10.5281/zenodo.1343303
- Forget, G., 2019: Update MITgcm & DarwinProject elements (Version v0.1.0). Zenodo. http://doi.org/10.5281/zenodo.2653669
- Ward, B.A., S. Dutkiewicz, O. Jahn, and M.J. Follows, 2012: A size-structured food-web model for the global ocean. Limnol. Oceanogr., 57, 1877-1891. https://aslopubs.onlinelibrary.wiley.com/doi/abs/10.4319/lo.2012.57.6.1877


Version History
***************
