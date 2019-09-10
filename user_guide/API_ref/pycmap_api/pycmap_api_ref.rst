

pycmap API
==========

+-------------------------------+--------------------------------------------------------------+
| :ref:`pycmap_api`             |       Create Instance of API                                 |
+-------------------------------+--------------------------------------------------------------+


Data Retrieval (API)
--------------------


+-------------------------------+--------------------------------------------------------------+
| :ref:`query`                  |       SQL Query                                              |
+-------------------------------+--------------------------------------------------------------+
| :ref:`getcatalog`             |       Retrieve Catalog                                       |
+-------------------------------+--------------------------------------------------------------+
| :ref:`metadata`               |       Retrieve Metadata                                      |
+-------------------------------+--------------------------------------------------------------+
| :ref:`columns`                |       Retrieve Column Names                                  |
+-------------------------------+--------------------------------------------------------------+
| :ref:`dataset_head`           | Retrieve Top Rows of Given Dataset                           |
+-------------------------------+--------------------------------------------------------------+
| :ref:`var_long_name`          | Returns Long Name of Given Variable                          |
+-------------------------------+--------------------------------------------------------------+
| :ref:`var_unit`               | Returns Unit for Given Variable, if applicable               |
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

  pycmap_api
  pycmap_query
  pycmap_catalog
  pycmap_metadata
  pycmap_dataset_columns
  pycmap_dataset_head
  pycmap_variable_long_name
  pycmap_variable_unit
  pycmap_has_field
  pycmap_is_gridded
  pycmap_is_climatology
  pycmap_list_cruises
  pycmap_cruise_details
  pycmap_cruise_ST_bounds
  pycmap_cruise_trajectory
  pycmap_subset_ST
  pycmap_subset_TS
  pycmap_subset_DP
  pycmap_match_datasets
  pycmap_match_cruise_track_datasets


Data Visualization
------------------


+-------------------------------+--------------------------------------------------------------+
| :ref:`histogram`              |       Histogram Plot                                         |
+-------------------------------+--------------------------------------------------------------+
| :ref:`timeSeries`             |       Time Series Plot                                       |
+-------------------------------+--------------------------------------------------------------+
| :ref:`rmCp3d`                 |       Regional Map, Contour Plot, 3D Surface Plot            |
+-------------------------------+--------------------------------------------------------------+
| :ref:`sectionMapContour`      |       Section Map, Section Contour                           |
+-------------------------------+--------------------------------------------------------------+
| :ref:`depthProfile`           | Depth Profile                                                |
+-------------------------------+--------------------------------------------------------------+
| :ref:`cruiseTrackPlot`        | Cruise Track Plot                                            |
+-------------------------------+--------------------------------------------------------------+
| :ref:`corrMatrix`             | Correlation Matrix                                           |
+-------------------------------+--------------------------------------------------------------+
| :ref:`corrMatrixCruise`       | Correlation Matrix Along Cruise Track                        |
+-------------------------------+--------------------------------------------------------------+



.. toctree::
  :maxdepth: 1
  :hidden:

  pycmap_histogram
  pycmap_time_series
  pycmap_rm_cp_3d
  pycmap_section_map_contour
  pycmap_depth_profile
  pycmap_cruise_track
  pycmap_correlation_matrix
  pycmap_correlation_matrix_cruise_track
