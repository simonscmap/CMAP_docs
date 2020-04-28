

.. _dataRet:

Data Retrieval
==============


The methods below can be used to retrieve metadata and to query, subset, and colocalize datasets. To begin, you must create an instance of the pycmap API. This tutorial can be found below.


+-------------------------------+--------------------------------------------------------------+
| :ref:`pycmapAPI`              |       Create an Instance of the API                          |
+-------------------------------+--------------------------------------------------------------+
| :ref:`query`                  |       Generic SQL Query                                      |
+-------------------------------+--------------------------------------------------------------+
| :ref:`getcatalog`             |       Retrieve Catalog                                       |
+-------------------------------+--------------------------------------------------------------+
| :ref:`searchCatalog`          |       Search Catalog by Keyword                              |
+-------------------------------+--------------------------------------------------------------+
| :ref:`Dataset_list`           |       Retrieve List of Datasets                              |
+-------------------------------+--------------------------------------------------------------+
| :ref:`metadata`               |       Retrieve Variable Metadata                             |
+-------------------------------+--------------------------------------------------------------+
| :ref:`datasetmetadata`        |       Retrieve Dataset Metadata                              |
+-------------------------------+--------------------------------------------------------------+
| :ref:`columns`                |       Retrieve Column Names                                  |
+-------------------------------+--------------------------------------------------------------+
| :ref:`dataset_head`           | Retrieve Top Rows of Given Dataset                           |
+-------------------------------+--------------------------------------------------------------+
| :ref:`var_long_name`          | Returns Long Name of Given Variable                          |
+-------------------------------+--------------------------------------------------------------+
| :ref:`var_unit`               | Returns Unit for Given Variable, if applicable               |
+-------------------------------+--------------------------------------------------------------+
| :ref:`varRes`                 | Returns Spatial and Temporal Resolution of Given Variable    |
+-------------------------------+--------------------------------------------------------------+
| :ref:`varCover`               | Returns Spatial and Temporal Coverage of Given Variable      |
+-------------------------------+--------------------------------------------------------------+
| :ref:`varStat`                | Returns Summary Statistics for Given Variable                |
+-------------------------------+--------------------------------------------------------------+
| :ref:`hasfield`               | Returns True if Column Exists                                |
+-------------------------------+--------------------------------------------------------------+
| :ref:`gridded`                | Returns True if Variable is Gridded Product                  |
+-------------------------------+--------------------------------------------------------------+
| :ref:`clim`                   | Returns True if Dataset is Climatology Product               |
+-------------------------------+--------------------------------------------------------------+
| :ref:`list_cruises`           | Returns Cruise Expedition Details                            |
+-------------------------------+--------------------------------------------------------------+
| :ref:`cruise_details`         | Returns Cruise Specific Details by Name                      |
+-------------------------------+--------------------------------------------------------------+
| :ref:`cruise_ST`              | Returns Cruise Spatio-Temporal Bounds                        |
+-------------------------------+--------------------------------------------------------------+
| :ref:`cruise_traj`            | Returns Trajectory for Specific Cruise                       |
+-------------------------------+--------------------------------------------------------------+
| :ref:`cruiseVars`             | Returns Variables Associated with Specific Cruise            |
+-------------------------------+--------------------------------------------------------------+
| :ref:`Retrieve_Dataset`       | Returns the Entire Dataset                                   |
+-------------------------------+--------------------------------------------------------------+
| :ref:`subset_ST`              | Returns a Subset of Data Defined by Space and Time           |
+-------------------------------+--------------------------------------------------------------+
| :ref:`subset_TS`              | Returns a Subset of Data Aggregated by Time                  |
+-------------------------------+--------------------------------------------------------------+
| :ref:`subset_DP`              | Returns a Subset of Data Aggregated by Depth                 |
+-------------------------------+--------------------------------------------------------------+
| :ref:`match`                  | Colocalizes Variables between Datasets                       |
+-------------------------------+--------------------------------------------------------------+
| :ref:`matchCruise`            | Colocalizes Variables along Cruise Trajectory                |
+-------------------------------+--------------------------------------------------------------+


.. toctree::
  :maxdepth: 1
  :hidden:
  :titlesonly:

  data_retrieval/pycmap_api
  data_retrieval/pycmap_query
  data_retrieval/pycmap_catalog
  data_retrieval/pycmap_search_catalog
  data_retrieval/pycmap_dataset
  data_retrieval/pycmap_metadata
  data_retrieval/pycmap_dataset_metadata
  data_retrieval/pycmap_dataset_columns
  data_retrieval/pycmap_dataset_head
  data_retrieval/pycmap_variable_long_name
  data_retrieval/pycmap_variable_unit
  data_retrieval/pycmap_variable_resolution
  data_retrieval/pycmap_var_coverage
  data_retrieval/pycmap_var_stat
  data_retrieval/pycmap_has_field
  data_retrieval/pycmap_is_gridded
  data_retrieval/pycmap_is_climatology
  data_retrieval/pycmap_list_cruises
  data_retrieval/pycmap_cruise_details
  data_retrieval/pycmap_cruise_ST_bounds
  data_retrieval/pycmap_cruise_trajectory
  data_retrieval/pycmap_cruise_variables
  data_retrieval/pycmap_retrieve_dataset
  data_retrieval/pycmap_subset_ST
  data_retrieval/pycmap_subset_TS
  data_retrieval/pycmap_subset_DP
  data_retrieval/pycmap_match_datasets
  data_retrieval/pycmap_match_cruise_track_datasets
