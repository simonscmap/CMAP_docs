.. _Zenodo: https://zenodo.org/

.. _Dryad: https://datadryad.org/

.. _Figshare: https://figshare.com/

.. _PANGAEA: https://www.pangaea.de/

.. _here: https://github.com/mdashkezari/opedia/tree/master/template

.. _template: https://github.com/mdashkezari/opedia/tree/master/template

.. _Slack: https://join.slack.com/t/simons-cmap/shared_invite/enQtNjQzMTkzMjg0NjQ2LWE4N2FjNDAwMjdiNzU0MGU4OTUzMGE4YWE5MjQwNGY2MjVlZTE2MTE3ZWNiOTAyY2E5ZDUxYzYwMGZhYWUwZjg





Data Submission
===============

If you wish to suggest a dataset be added to the database or have some data that you would like added, please email Raphael (nrhagen@uw.edu).

Dataset Requirements
--------------------

To add your dataset to CMAP and make it usable we have a few data and metadata conventions.

1. Data must be in the format:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+------+-----+-----+-------------------+-----------------+-----+-----------------+
| time | lat | lon | depth {if exists} | <:math:`var_1`> | ... | <:math:`var_n`> |
+------+-----+-----+-------------------+-----------------+-----+-----------------+

Data in CMAP is indexed on space and time. For data to be able to be co-localized, it must be in this format.

2. Data must have supporting meta-data, ie. data about your data.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For other scientist to find and use your data, we need metadata on the dataset and the variables within the dataset.

3. Data should have a DOI (Digital Object Identifier) or a reference.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

CMAP is not a data repository and we do not archive and version control datasets. There are multiple free DOI registers: Zenodo_, Dryad_, Figshare_, PANGAEA_...

|

Data Template and File Structure
--------------------------------

The preferred file format is excel spreadsheet. Data is stored in the first sheet and the sheet title is "data". The second sheet stores the dataset meta-data and is called "dataset_meta_data". Meta-data associated with the variables in the dataset are kept in the third sheet, "vars_meta_data". An example template can be found here_.

A template_ is available.

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

+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------------------------------------+------------------+-----+-----------------+
| time                                                                           | lat                                                                            | lon                                                                              | depth {if exists}                             | <:math:`var_1`>  | ... | <:math:`var_n`> |
+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------------------------------------+------------------+-----+-----------------+
| < Format  %Y-%m-%dT%H:%M:%S,  Time-Zone:  UTC,  example: 2014-02-28T14:25:55 > | < Format: Decimal (not military grid system), Unit: degree, Range: [-90, 90] > | < Format: Decimal (not military grid system), Unit: degree, Range: [-180, 180] > | < Positive value, Unit: [m], example: 10.25 > | < variable 1 >   | ... | < variable n >  |
+--------------------------------------------------------------------------------+--------------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------------------------------------+------------------+-----+-----------------+


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



+------------------------------------------+------------------------------------------+-------------------------------+------------------------------------------+---------------------------------------------------------------------------------------+---------------------------------------------+---------------------------------------------------------------+----------------------------------------+--------------------------------+-----------------------------------------------------+
| dataset_short_name                       |    dataset_long_name                     |       dataset_version         | dataset_release_date                     |      dataset_make                                                                     |  dataset_source                             |    dataset_doi                                                |  dataset_history                       | dataset_description            |        dataset_references                           |
+------------------------------------------+------------------------------------------+-------------------------------+------------------------------------------+---------------------------------------------------------------------------------------+---------------------------------------------+---------------------------------------------------------------+----------------------------------------+--------------------------------+-----------------------------------------------------+
| <short name of your dataset (<50 chars)> | <long name of your dataset (<500 chars)> | <dataset version (<50 chars)> | <Format  %Y-%m-%d,  example: 2018-06-20> | <how dataset is made (fixed options= [assimilation, model, observation]) (<50 chars)> | <name of your lab/institution (<100 chars)> | <digital object identifier (doi) associated with the dataset> | <any note about the dataset evolution> | <a descrption of your dataset> | <list of associated docs/publications (<500chars) > |
+------------------------------------------+------------------------------------------+-------------------------------+------------------------------------------+---------------------------------------------------------------------------------------+---------------------------------------------+---------------------------------------------------------------+----------------------------------------+--------------------------------+-----------------------------------------------------+





**Columns by order**:


1. **dataset_short_name**: dataset short name
    - type: string
    - length: <50 chars
    - Short, human readable name of your dataset. Ex: Darwin_3_Day_Ecosystem

2. **dataset_long_name**: descriptive dataset name

    - type: string
    - length: <500 chars
    - Descriptive human readable name of your dataset: Darwin 3 Day Averaged Ecosystem Characteristics

3. **dataset_version**: dataset version

    - type: string
    - length: <50 chars
    - ex: V1

4. **dataset_release_date**: dataset release date

    - type: date
    - format: %Y-%m-%d (zero padding required)

5. **dataset_make**: how dataset is made (fixed options= [assimilation, model, observation])

    - type: string
    - length: <50 chars

6. **dataset_source**: name of your lab and/or institution

    - type: string
    - length: <100 chars

7. **dataset_doi**:

    - type: string
    - length

8. **dataset_history**: notes regarding the evolution of the dataset with respect to the previous versions, if applicable

    - type: string
    - length: <100 chars

9. **dataset_description**: A description of your dataset detailing collection and processing methodology.

    - type: string
    - length: no limit

10. **dataset_references**: links/citations associated with the dataset documentations/publications (enter each ref. in a separate row)

    - type: string
    - length: <500 chars per item



Third Sheet: "vars_meta_data"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




+-----------------------------------+-----------------------------------+--------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------+--------------------------------+
|var_short_name                     |    var_long_name                  |     var_standard_name    | var_sensor                                                                                             |  var_unit                   | var_spatial_res                                                                     |      var_temporal_res                                                  | var_missing_value                                                                | var_discipline                                                                                            | var_keywords                       |  var_comment                   |
+-----------------------------------+-----------------------------------+--------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------+--------------------------------+
| <variable short name (<50 chars)> | <variable long name (<500 chars)> | <variable standard name> | <device by which variable is measured (<50 chars) examples: [satellite, cruise_name, simulation, ...]> | <variable unit (<50 chars)> | <variable spatial resolution (examples: [1/25° X 1/25° , 50km X 50km, Irregular] )> | <variable temporal resolution (examples: [Hourly, Daily, Irregular] )> | <placeholder for missing values (examples: empty cell, "nan", "unknown", #FFFF)> | <associated discipline(s) (<100 chars) (examples: [Physics, Chemistry, Biology, BioGeoChemistry, etc..])> | <associated keywords (<500 chars)> | <variable comment/description> |
+-----------------------------------+-----------------------------------+--------------------------+--------------------------------------------------------------------------------------------------------+-----------------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------+----------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------+------------------------------------+--------------------------------+


**Columns by order**:


1. **var_short_name**: variable short name

    - type: string
    - length: <50 chars
    - Computer-readable short name. Should not contain any leading numbers, special characters (ex: '&') or spaces. Ex: SST

2. **var_long_name**: descriptive variable name

    - type: string
    - length: <500 chars
    - Human readable variable name. Think of this as a common name for the variable. Ex: Sea Surface Temperature

3. **var_standard_name**: standard variable name (more details in CF Conventions and COARDS Conventions)

    - type: string
    - length: <500 chars

4. **var_unit**: variable unit

    - type: string
    - length: <50 chars
    - Prefer symbols to descriptions. Ex: "/" is better than "per"

5. **var_sensor**: device by which variable is measured

    - type: string
    - length: <50 chars
    - examples: [satellite, in-situ, blen, flow cytometry, CTD, underway CTD, Optical, Float, Drifter, AUV etc..]

6. **var_spatial_res**: variable spatial resolution

    - type: string
    - length: <50 chars
    - examples: [1/25° X 1/25° , 50km X 50km, Irregular, ...]

7. **var_temporal_res**: variable temporal resolution

    - type: string
    - length: <50 chars
    - examples: [Hourly, Daily, Irregular, ...]

8. **var_missing_value**: placeholder for missing values

    - type: string
    - length: <50 chars
    - examples: [empty cell, "nan", "unknown", #FFFF, -999, ...]

9. **var_discipline**: the closest discipline(s) associated with the variable

    - type: string
    - length: <100 chars
    - examples: [Physics, Chemistry, Biology, BioGeoChemistry, ...]

10. **var_keywords**: keywords pertinent to the variable (separated by comma).

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


    **Keyword Example for <proprochloro_abundance> variable in the SeaFlow Dataset:**

    - pro, prochloro, prochlorococcus, seaflow, flow, cytometry, flow-cytometry, insitu, in-situ, cruise,  observation, rep, reprocessed, bio, biology, armbrust, UW, University of Washington, abundance,cell abundance


11. **var_comment**: any other comment about the variable

    - type: string
    - length: no limit
