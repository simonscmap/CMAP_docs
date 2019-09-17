:orphan:

.. _Chisholm_bigrapa1:

BiGRAPA1 Cruise
***************

Prochlorococcus Abundance and Metadata for the BigGrapa 1 Cruise
################################################################

.. |cruise| image:: /_static/catalog_thumbnails/sailboat.png
   :scale: 10%
   :align: middle

.. |globe| image:: /_static/catalog_thumbnails/globe.png
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

+-------------------------------+----------+-------------+------------------------+-------------------+---------------------+---------------------+
| Dataset Name                  | Sensor   |  Make       |  Spatial Resolution    |Temporal Resolution|  Start Date         |  End Date           |
+===============================+==========+=============+========================+===================+=====================+=====================+
| :ref:`Chisholm_bigrapa1`      | |cruise| | Observation |     Irregular          |        Irregular  |  2010-11-19         | 2010-12-12          |
+-------------------------------+----------+-------------+------------------------+-------------------+---------------------+---------------------+

Dataset Description
*******************



This dataset contains Prochlorococcus cell concentration measurements from the BiGRAPA1 cruise. For each of the 7 stations along the transect we took a depth profile of 9 samples across the euphotic zone; from these water samples we also preserved samples for other analyses (e.g. ecotype qPCR). In most cases these water samples are not from the same bottles or depths as cruise core measurement casts.  Depths at each station were chosen based on the location of the deep chlorophyll maximum, the mixed layer depth and light attenuation profiles. At station 7 we also participated in two high-resolution deep-chlorophyll maximum casts (63 and 69), and counts for these are included.

Fixed samples for flow cytometry were collected by adding 5 ul of 25% glutaraldehyde to 1 ml whole seawater, mixing, and allowing sample to fix in the dark 10 minutes, followed by flash freezing in liquid nitrogen. The samples were stored in liquid nitrogen or at -80C for 2-4 months before running flow cytometry. Two or three flow cytometry samples were preserved from each Niskin sampled, but only one of these sampling replicates was run.

For each site and depth collected, a sample was run on a BD/Cytopeia Influx flow cytometer with 488 and 457 lasers both illuminating the sample and 2um fluorescent bead standards mixed in. No stains were used. Detector sensitivity ranges were optimized for Prochlorococcus and held constant throughout all runs. Each sample was thawed in the dark and run twice (flow cytometry technical duplicates). Replicates were run back to back, flushing the lines in between, so that samples weren't left thawed for longer than ~ 1hr or put through extra freeze thaw cycles. Values in table are averages of the pair of technical duplicates.  As measurements, these values are good to ~2-3 significant digits (depending on the length of time a sample was run and the number of Prochlorococcus cells actually detected).

Prochlorococcus counts were obtained by gating across chlorophyll fluorescence (680/40) vs. forward scatter using FlowJo software.  Gates were adjusted by hand separately for each sample, since the cell properties change dramatically across this dataset. Concentrations were calculated using sample run times, sample counts and measured flow rates. For surface/mixed layer samples with higher light exposure and smaller cells, many Prochlorococcus populations in this data set were just above or only partly above the fluorescence noise - these counts represent estimates likely on the low side (gating to avoid noise, faintly fluorescing cells undetectable), and they are not as accurate as estimates for the well-separated deeper populations.

At station 1, the mixed layer samples do not have technical replicates. In the first few attempted flow cytometry runs Prochlorococcus cells were not visible - not because their fluorescence was low (these waters are relatively turbid), but because the cells were scarce. Later, the remainders of these samples were used for single, long slow runs, and we were able to detect a small Prochlorococcus population - these counts are not robust, representing small numbers with background noise, but they round out the depth profile for a rough idea.





Table of Variables
******************

CTD Data
########

.. raw:: html

    <iframe src="../../_static/var_tables/tblCTD_Chisholm/tblCTD_Chisholm.html"  frameborder = 0 height = '250px' width="100%">></iframe>

|

Bottle Data
###########

.. raw:: html

    <iframe src="../../_static/var_tables/tblBottle_Chisholm/tblBottle_Chisholm.html"  frameborder = 0 height = '250px' width="100%">></iframe>





Prochlorococcus ecotype qPCR counts for the BiG RAPA cruise
###########################################################



Paul Berube collected and extracted samples,  Allison Coe performed qPCR assay.
PI: Sallie W. Chisholm, MIT Department of Civil and Environmental Engineering

**Sampling**:  Samples for qPCR were collected and preserved as described  (Zinser et al., 2006). Seawater was collected in a triple seawater rinsed HDPE bottle. 100 mL of seawater was filtered onto 25 mm diameter, 0.2 um pore size, polycarbonate filters (in triplicate) and chased with 3 mL of preservation solution (10 mM Tris pH=8, 100 mM EDTA, 500 mM NaCl).  Filters were placed dry inside 2 mL screw cap polypropylene bead beater tubes and stored at -80oC until use.

**DNA Extraction**:  DNA from field samples was extracted from filters as previously described (Zinser et al., 2006). Cells were resuspended by adding 650 ul of 10 mM Tris pH=8 to the bead beater tube containing the filter and bead beated at maximum speed (~4800 rpm) for 2 minutes. 500 ul of the respuspended cells were transfered to a 1.5 mL centrifuge tube and the cells were heat lysed at 95oC for 15 min. DNA samples were then stored at -80oC until analysis.

**Ecotype quantitative PCR**:  The qPCR assay was performed as previously described (Ahlgren et al., 2006; Zinser et al., 2006; Malmstrom et al., 2010; Malmstrom et al., 2013) using the same standards and reaction conditions. Technical duplicates of three replicate filters were analyzed for BiG RAPA (i.e. 6 data points per sample). Data quality was assessed using the percent coefficient of variation for the 6 data points. When cell concentrations fell below the detection limit of the assay (indicated by the associated quality flag), cell concentrations were set to the theoretical detection limit of 0.65 cells/mL.



Data Source
***********

https://chisholmlab.mit.edu/


The data that was not provided by the Chisholm Lab at MIT was downloaded from http://hahana.soest.hawaii.edu/cmoreDS/bextraction.html and http://cmore.soest.hawaii.edu/datasearch/data.php but was cleaned-up and compiled by the Chisholm Lab.

How to Acknowledge
******************

Ahlgren, N. A., G. Rocap, and S. W. Chisholm. 2006. Measurement of Prochlorococcus ecotypes using real-time polymerase chain reaction reveals different abundances of genotypes with similar light physiologies. Environ. Micro- biol. 8: 441–454. doi:10.1111/j.1462-2920.2005.00910.x

Malmstrom, R. R., A. Coe, G. C. Kettler, A. C. Martiny, J. Frias-Lopez, E. R. Zinser, and S. W. Chisholm. 2010. Temporal dynamics of Prochlorococcus ecotypes in the Atlantic and Pacific oceans. ISME J. 4: 1252–1264. doi:10.1038/ ismej.2010.60

Malmstrom, R. R., and others. 2013. Ecology of uncultured Prochlorococcus clades revealed through single-cell genomics and biogeographic analysis. ISME J. 7: 184–198. doi:10.1038/ismej.2012.89

Zinser, E. R., A. Coe, Z. I. Johnson, A. C. Martiny, N. J. Fuller, D. J. Scanlan, and S. W. Chisholm. 2006. Prochlorococcus ecotype abundances in the North Atlantic Ocean as revealed by an improved quantitative PCR method. Appl. Environ. Microbiol. 72: 723–732. doi:10.1128/ AEM.72.1.723-732.2006


Version History
***************
