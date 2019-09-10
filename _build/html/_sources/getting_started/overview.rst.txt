


.. _Simons: https://www.simonsfoundation.org/




Overview
========


Oceanography is a multidisciplinary field which involves synthesizing physical, chemical and biological data. Analyzing these observations often requires harmonizing data such as satellite measurements with model estimates. Handling satellite and model data sets is particularly challenging for the following reasons.

* Are scattered all over the web and might not be trivial to retrieve or discover

* Are massive in size

* Have varying spatial and temporal dimensions and resolutions.



This project's goal is to establish a unifying data structure and streamline the process of subsetting, extracting, and visualizing data. We propose that the space and time information should act as the linking chain between data sets, as every single data point must be annotated with its own space and time data. Therefore, all data sets hosted in Simons CMAP have the following simple data structure:


+------+-----+-----+-------------------+-----------------+-----+-----------------+
| time | lat | lon | depth {if exists} | <:math:`var_1`> | ... | <:math:`var_n`> |
+------+-----+-----+-------------------+-----------------+-----+-----------------+



Project Process Flow
^^^^^^^^^^^^^^^^^^^^

Simons Foundation supports various ocean research programs and cruise expeditions. The results of these endeavors are shared with the scientific community and general public through Simons CMAP. All data sets are first registered in formal digital archive repositories (such as zenodo.org) and obtain academically citable Digital Object Identifiers (DOI). The atlas also encompass a wide range of external data sets such as global satellite data and model outputs (see  :ref:`Catalog`). We then ingest all data sets into a database system using the data structure mentioned above.  Finally, the API and application layers provide the user with the access to the database system where data set subsets can be retrieved and visualized.

.. figure:: ../_static/overview_icons/process_flow.png
   :scale: 60 %
   :align: center
