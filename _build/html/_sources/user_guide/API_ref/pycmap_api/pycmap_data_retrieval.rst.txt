

.. _dataRet:

Data Retrieval
==============


**API**



.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/mdashkezari/pycmapDoc/blob/master/notebooks/API.ipynb


.. class:: API

    To retrieve data, we need to create an instance of the system's API and pass the API key. It is no necessary to pass the API key every time you run a code locally, because it will be stored locally. The API class has other optional parameters to adjust its behavior. All parameters can be updated persistently at any point in the code.

    ``class pycmap.API(token=<API KEY>, baseURL='https://simonscmap.com', headers=None, vizEngine='plotly', exportDir='./export/', > exportFormat='.csv', figureDir='./figure/')``
    |

    :Parameters:
        **token: string, required**
            Access token (API Key) required to make client requests. You may get an API key here: https://simonscmap.com
        **baseURL: string, optional, default: https://simonscmap.com**
            Root endpoint of Simons CMAP API.
        **headers: dict, optional, default: None**
            Additional headers to add to the client requests.
        **vizEngine: string, optional, default: 'plotly'**
            Data visualization library used to render the graphs. The other option for visualization library is 'bokeh'. Notice some of the graphs (such as correlation matrix) are only suported by plotly.
        **exportDir: string, optional, default: './export/'**
            Path to local directory where the exported data are stored.
        **exportFormat: string, optional, default: '.csv'**
            File format of the exported files. Currently, only csv format is supported.
        **figureDir: string, optional, default: './figure/'**
            Path to local directory where the figures are stored. The interactive figure objects are stored in form of html files.
            Note: inline graphs (e.g. on jupyter notebook) are not saved.


**Example**

.. code-block:: python


  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>', vizEngine='plotly')


Data Retrieval Methods
----------------------


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
