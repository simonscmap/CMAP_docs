.. _Zenodo: https://zenodo.org/
..
.. _Dryad: https://datadryad.org/
..
.. _Figshare: https://figshare.com/
..
.. _PANGAEA: https://www.pangaea.de/
..
.. _Download Data Template: https://github.com/simonscmap/DBIngest/raw/master/template/datasetTemplate.xlsx

.. _Download SeaFlow Example: https://github.com/simonscmap/DBIngest/raw/master/template/SeaFlow_example.xlsx

.. _Download Gradients 1 Fluormetric Chl Example: https://github.com/simonscmap/DBIngest/raw/master/template/Gradients1-KOK1606-FluorometricChlorophyll_2020-03-03_V1.1_example.xlsx

.. _Download Gradients 1 Cobalamin Example: https://github.com/simonscmap/DBIngest/raw/master/template/KOK1606_Gradients1_Cobalamin_example.xlsx

.. _Download Gradients 3 Underway CTD Example: https://github.com/simonscmap/DBIngest/raw/master/template/KM1906_Gradients3_uwayCTD_example.xlsx




.. |template_download| image:: /_static/overview_icons/spreadsheet.png
  :align: middle
  :scale: 35%
  :target: https://github.com/simonscmap/DBIngest/tree/master/template

Data Submission
===============

If you wish to suggest a dataset be added to the database or have some data that you would like added, please email us (cmap-data-submission@uw.edu).

In short the current data submission process is:

1. Contact us about adding a dataset to CMAP.
2. Format your data and metadata in the CMAP format.
3. Submit your dataset via email for feedback and review.
4. Once OK'ed, register a DOI for your dataset.
5. Submit dataset via email with DOI for ingestion into CMAP.


Data Template
-------------

.. table::

    +-----------------------------+
    | |template_download|         |
    +=============================+
    | `Download Data Template`_   |
    +-----------------------------+



Dataset Examples
----------------



* `Download SeaFlow Example`_
* `Download Gradients 1 Fluormetric Chl Example`_
* `Download Gradients 1 Cobalamin Example`_
* `Download Gradients 3 Underway CTD Example`_




Dataset Requirements
--------------------

To add your dataset to CMAP and make it usable we have a few data and metadata conventions.

.. note:: CMAP is not a data repository and we do not archive and version control datasets. We recommend that once your dataset has been approved for submission to CMAP, you register your dataset at a data repository (i.e. Zenodo, Dryad, Figshare, PANGAEA, etc) and obtain a DOI. We will include your DOI when the data is ingested into CMAP.

1. Data must be in the format:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------+-----+-----+-------------------+-----------------+-----+-----------------+
| time | lat | lon | depth {if exists} | <:math:`var_1`> | ... | <:math:`var_n`> |
+------+-----+-----+-------------------+-----------------+-----+-----------------+

Data in CMAP is indexed on space and time. For data to be able to be co-localized, it must be in this format.

2. Data must have supporting meta-data, ie. data about your data.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For other scientist to find and use your data, we need metadata on the dataset and the variables within the dataset.


|

Data Template and File Structure
--------------------------------

The CMAP data template consists of three sections: data, dataset metadata and variable metadata. Data is stored in the first sheet and the sheet title is "data". The second sheet stores the dataset meta-data and is called "dataset_meta_data". Meta-data associated with the variables in the dataset are kept in the third sheet, "vars_meta_data".

The current data template is an excel spreadsheet. If submitting data in the multi-sheet format does not work for you the data, dataset_metadata, and vars_metadata .csv's can be submitted individually.
Note, information from all three sheets is required for a dataset to be added to CMAP.
If you are submitting a dataset that is too large to be stored in a tabular format, the preferred format is netcdf for the data and tabular data for the metadata.



Dataset Filename Convention
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Dataset filename: <dataset_short_name>_<dataset_release_data>_v<dataset_version>.xlxs
Example: seaflow_2018-05-25_v1.0.xlxs

**<dataset_short_name>: short name of the dataset**
- length: less than 50 characters

**<dataset_release_data>: date of dataset release**
- format: %Y-%m-%d
- note: zero padding required

**<dataset_version>: associated dataset version**
- length: less than 50 characters




First Sheet: "data"
~~~~~~~~~~~~~~~~~~~

+---------------------------------------------+------------+-------------+-------------------+-----------------------------------+
| time                                        | lat        |   lon       | depth             | <v_1>                             |
+---------------------------------------------+------------+-------------+-------------------+-----------------------------------+
| <corresponding datetime> (%Y-%m-%dT%H:%M:%S)| <latitude> | <longitude> | depth (if exists) | <first variable> (var_short_name) |
+---------------------------------------------+------------+-------------+-------------------+-----------------------------------+




**Columns by order**:

1. **time**: corresponding datetime
    - type: datetime
    - format: %Y-%m-%dT%H:%M:%S [example: 2018-03-29T18:05:55]
    - time zone: UTC
    - note: there is a blank space between date and time
    - note: zero padding required

2. **lat**: latitude
    - type: float
    - format: Decimal (not military grid system)
    - unit: degree north
    - range: [-90, 90]

3. **lon**: longitude
    - type: float
    - format: Decimal (not military grid system)
    - unit: degree east
    - range: [-180, 180]

4. **depth**: depth
    - type: float
    - unit: meters
    - range: [0, ∞]

5. **<v_1>**: first variable (short name)
    - Add more columns similar to the last column, if dataset has more than one variable.



Second Sheet: "dataset_meta_data"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


+------------------------------------------+------------------------------------------+-------------------------------+------------------------------------------+---------------------------------------------------------------------------------------+---------------------------------------------+-------------------------------------------------------------+---------------------------------------------+---------------------------------------------------------------+----------------------------------------+--------------------------------+-----------------------------------------------------+-------------------------------------------+
| dataset_short_name                       |    dataset_long_name                     |       dataset_version         | dataset_release_date                     |      dataset_make                                                                     |  dataset_source                             |    dataset_distributor                                      | dataset_acknowledgement                     |dataset_doi                                                    |  dataset_history                       | dataset_description            |        dataset_references                           | climatology                               |
+------------------------------------------+------------------------------------------+-------------------------------+------------------------------------------+---------------------------------------------------------------------------------------+---------------------------------------------+-------------------------------------------------------------+---------------------------------------------+---------------------------------------------------------------+----------------------------------------+--------------------------------+-----------------------------------------------------+-------------------------------------------+
| <short name of your dataset (<50 chars)> | <long name of your dataset (<500 chars)> | <dataset version (<50 chars)> | <Format  %Y-%m-%d,  example: 2018-06-20> | <how dataset is made (fixed options= [assimilation, model, observation]) (<50 chars)> | <name of your lab/institution (<100 chars)> | <the distributor of the data product (optional <100 chars)> |<the acknowledgment listed for the dataset > |<digital object identifier (doi) associated with the dataset>  | <any note about the dataset evolution> | <a descrption of your dataset> | <list of associated docs/publications (<500chars) > | <null if not climatology, 1 climatology>  |
+------------------------------------------+------------------------------------------+-------------------------------+------------------------------------------+---------------------------------------------------------------------------------------+---------------------------------------------+-------------------------------------------------------------+---------------------------------------------+---------------------------------------------------------------+----------------------------------------+--------------------------------+-----------------------------------------------------+-------------------------------------------+




**Columns by order**:


1. **dataset_short_name**: dataset short name
    - type: string
    - length: <50 chars
    - short, human readable name of your dataset.
    - examples: BATS Bacteria Production

2. **dataset_long_name**: descriptive dataset name
    - type: string
    - length: <500 chars
    - Descriptive human readable name of your dataset
    - examples: Bermuda Atlantic Time-series Study (BATS) Bacteria Production

3. **dataset_version**: dataset version
    - type: string
    - length: <50 chars
    - examples: V1, Version 3.5

4. **dataset_release_date**: dataset release date
    - type: date
    - format: %Y-%m-%d (zero padding required)

5. **dataset_make**: how dataset is made (fixed options= [assimilation, model, observation])
    - type: string
    - length: <50 chars

6. **dataset_source**: name of your lab and/or institution
    - type: string
    - length: <100 chars
    - examples: Bermuda Institute of Ocean Sciences

7. **dataset_distributor**: name of the distributor of the data product (optional: if the dataset source differs from the distributor)
    - type: string
  	- length: <100 chars
  	- examples: Distributed by NASA PODAAC

8. **dataset_acknowledgement**: Any acknowledgement(s) for this dataset
  	- type: string
  	- length: <100 chars

9. **contact_email**: Email address of data submitter. Note: This will be public information in the database.
  	- type: string
  	- length: <100 chars

10. **dataset_doi**: digital object identifier (doi) associated with the dataset.
    - type: string
    - length: no limit

11. **dataset_history**: notes regarding the evolution of the dataset with respect to the previous versions, if applicable.
  	- type: string
  	- length: <100 chars

12. **dataset_description**: A description of your dataset detailing collection and processing methodology.
  	- type: string
  	- length: no limit

13. **dataset_references**: links/citations associated with the dataset documentations/publications (enter each ref. in a separate row)
    - type: string
    - length: <500 chars per item


14. **climatology**: is the dataset a climatology product? (<null if not climatology, 1 climatology>)
  	- type: string
  	- length: <10 chars


Third Sheet: "vars_meta_data"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


+-----------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+---------------------------------------------------+-----------------------------------+----------------------------------+
|var_short_name                     |    var_long_name                  | var_sensor                                                                                             |  var_unit                   | var_spatial_res                                                                     |      var_temporal_res                                                  | var_discipline                                                                                              |       visualize                                   | var_keywords                      |  var_comment                     |
+-----------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+---------------------------------------------------+-----------------------------------+----------------------------------+
| <variable short name (<50 chars)> | <variable long name (<500 chars)> | <device by which variable is measured (<50 chars) examples: [satellite, cruise_name, simulation, ...]> | <variable unit (<50 chars)> | <variable spatial resolution (examples: [1/25° X 1/25° , 50km X 50km, Irregular] )> | <variable temporal resolution (examples: [Hourly, Daily, Irregular] )> | <associated discipline(s) (<100 chars) (examples: [Physics, Chemistry, Biology, BioGeoChemistry, etc..])> ↓ |  <0 is not visualizable, 1 is visualizable >      |<associated keywords (<500 chars)> | <variable comment/description>   |
+-----------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+---------------------------------------------------+-----------------------------------+----------------------------------+



**Columns by order**:


1. **var_short_name**: variable short name
    - type: string
    - length: <50 chars
    - Computer-readable short name. Should not contain any leading numbers, special characters (ex: '&') or spaces. Ex: SST

2. **var_long_name**: descriptive variable name
    - type: string
    - length: <500 chars
    - Human readable variable name. Think of this as a common name for the variable. Ex: Sea Surface Temperature


3. **var_sensor**: device by which variable is measured
    - type: string
    - length: <50 chars
    - examples: [satellite, in-situ, blen, flow cytometry, CTD, underway CTD, Optical, Float, Drifter, AUV etc..]

4. **var_unit**: variable unit
    - type: string
    - length: <50 chars
    - Prefer symbols to descriptions. Ex: "/" is better than "per"

5. **var_spatial_res**: variable spatial resolution
    - type: string
    - length: <50 chars
    - examples: [1/25° X 1/25° , 50km X 50km, Irregular, ...]

6. **var_temporal_res**: variable temporal resolution
    - type: string
    - length: <50 chars
    - examples: [Hourly, Daily, Irregular, ...]

7. **var_discipline**: the closest discipline(s) associated with the variable
    - type: string
    - length: <100 chars
    - examples: [Physics, Chemistry, Biology, BioGeoChemistry, ...]

8. **visualize**: Is this variable visualizable? If not, it can be excluded from the Simons CMAP web application.
    - type: int
    - length: <2 chars
    - examples: [0 is not visualizable, 1 is visualizable]. ex: station # = 0 (non visualize), prochlorococcus abundance = 1 (visualize)

9. **var_keywords**: keywords pertinent to the variable (separated by comma).
    - type: string
    - length: <500 chars
    - delimiter = ','
    - examples: [field sample, Biology, abundance, synechococcus, ...]

    .. note:: **Keywords are variable-specific and case-insensitive. Please separate each keyword by comma. The suggested format for each variable keyword list is:**

      - Example keywords related to any official or unofficial variable names:   pro / prochloro / ...
      - Example keywords related to sensor/apparatus:  cruise / satellite / computer (in case of mode) / SeaFlow / ....
      - Example keywords related to official or unofficial cruise names (if applicable): KM1427 / Gradients 2.0 / ....
      - Example keywords related to data owners institution:  UW / University of Washington / ...
      - Example keywords related to data production techniques: cytometry / flow cytometry / ...
      - Example keywords related to the research context: omics / 16s / ...
      - Example keywords related to the associated discipline(s): chemistry / biology / physics / biogeochemical / biogeography ...
      - Any other keywords you think are relevant



10. **var_comment**: any other comment about the variable.
  	- type: string
  	- length: no limit
