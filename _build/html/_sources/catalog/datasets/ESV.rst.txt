:orphan:

.. _ESV:

ESV - Exact Sequence Variants
*****************************

Exact Amplicon Sequence Variant Abundances from the ANT28-5 Latitudinal Transect of the Atlantic Ocean
######################################################################################################

.. |cruise| image:: /_static/catalog_thumbnails/sailboat.png
   :scale: 10%
   :align: middle


+-------------------------------+----------+-------------+------------------------+-------------------+---------------------+---------------------+
| Dataset Name                  | Sensor   |  Make       |  Spatial Resolution    |Temporal Resolution|  Start Date         |  End Date           |
+===============================+==========+=============+========================+===================+=====================+=====================+
|:ref:`ESV`                     ||cruise|  | Observation |     Irregular          |        Irregular  |  2012-04-11         | 2012-05-11          |
+-------------------------------+----------+-------------+------------------------+-------------------+---------------------+---------------------+

Dataset Description
*******************

.. mdinclude:: ../dataset_descriptions/ESV_desc.md
    :start-line: 0



Table of Variables
******************

.. raw:: html

    <iframe src="../../_static/var_tables/tblESV/tblESV.html"  frameborder = 0 height = '300px' width="100%">></iframe>

|


Dataset reprocessing for CMAP:
##############################

In order to generate exact amplicon sequence variants (eASVs), publicly accessible amplicon data from Milici et al. (2016) was reanalyzed with qiime2 (2018.8). In brief, primers were trimmed with cutadapt, amplicons were merged with VSEARCH, and subsequently quality-filtered. eASVs were generated with deblur denoise-16s with a trim length of 231 base pairs. Taxonomic classification was carried out with the “qiime feature-classifier classify-sklearn” against the SILVA 132 database (NR99) subsetted to the amplicon region (807F = GGATTAGATACCCBRGTAGTC ; 1064R = AGYTGDCGACRRCCRTGCA). eASVs were also clustered into operational taxonomic units (OTUs) with VSEARCH at different percent sequence similarity thresholds approximately corresponding to existing taxonomic ranks (99, 98, 97, 96, 92, 89). Scripts and ancillary data are available at : https://osf.io/g7xsj/.

Data were then transformed into relative abundances and collated with metadata provided in Milici et al (2016a, b, c) prior to ingestion into CMAP (as long as depths recorded for metadata and sequence data differed by ≤ 10 m; https://github.com/jcmcnch/OTUandMetadata2CMAP). The resulting dataset allows the user to retrieve relative abundances and environmental covariates for both individual eASVs and OTU clusters. As with all other data in CMAP, each relative abundance measurement is associated with unique time/space coordinates. Whether a given abundance is from an eASV or OTU is clearly denoted in the columns “ESV_ID_or_Cluster_Centroid”, “Clustering_Level” and “Cluster_Type”. Raw sequences of eASVs and tab-separated files are also available as part of the ancillary data allow the user to manually connect individual eASVs with OTU clusters.

Notes on data:
##############

The primers used by Milici et al. (2016) are prokaryotic-specific, and do have mismatches to some important marine taxa (e.g. SAR11 group I). Despite these potential biases, SAR11 remain a high proportion of the total reads, and thus this bias is likely to have been small in practice. As noted in the original paper, these primers also do amplify chloroplast sequences, which are particularly abundant in the SPA and LPA fractions. In some of the particle-associated samples, there were some putatively eukaryotic sequences amplified, but they were excluded from this dataset by the positive filter of deblur.





Data Source
***********

Data provided by: Jesse McNichol (mcnichol@alum.mit.edu) & Jed Fuhrman lab, USC



How to Acknowledge
******************
Milici, M., Tomasch, J., Wos-Oxley, M.L., Wang, H., Jáuregui, R., Camarinha-Silva, A., Deng, Z.-L., Plumeier, I., Giebel, H.-A., Wurst, M., Pieper, D.H., Simon, M., Wagner-Döbler, I., 2016a. Low diversity of planktonic bacteria in the tropical ocean. Scientific Reports 6, 19054. https://doi.org/10.1038/srep19054

Milici, M., Deng, Z.-L., Tomasch, J., Decelle, J., Wos-Oxley, M.L., Wang, H., Jáuregui, R., Plumeier, I., Giebel, H.-A., Badewien, T.H., Wurst, M., Pieper, D.H., Simon, M., Wagner-Döbler, I., 2016b. Co-occurrence Analysis of Microbial Taxa in the Atlantic Ocean Reveals High Connectivity in the Free-Living Bacterioplankton. Front. Microbiol. 7. https://doi.org/10.3389/fmicb.2016.00649

Milici, M., Tomasch, J., Wos-Oxley, M.L., Decelle, J., Jáuregui, R., Wang, H., Deng, Z.-L., Plumeier, I., Giebel, H.-A., Badewien, T.H., Wurst, M., Pieper, D.H., Simon, M., Wagner-Döbler, I., 2016c. Bacterioplankton Biogeography of the Atlantic Ocean: A Case Study of the Distance-Decay Relationship. Front. Microbiol. 7. https://doi.org/10.3389/fmicb.2016.00590


Version History
***************
