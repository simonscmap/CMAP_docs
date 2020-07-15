# File Structure <br/>

<a id="toc"></a>
## Table of Contents
1. <a href="#introduction">Introduction</a>
1. <a href="#data_sheet">Data Sheet</a>
    * <a href="#time">time</a>
    * <a href="#lat">lat</a>
    * <a href="#lon">lon</a>
    * <a href="#depth">depth</a>
    * <a href="#vars">vars</a>
1. <a href="#dataset_metadata">Dataset Metadata</a>
    * <a href="#dataset_short_name">dataset_short_name</a>
    * <a href="#dataset_long_name">dataset_long_name</a>
    * <a href="#dataset_version">dataset_version</a>
    * <a href="#dataset_release_date">dataset_release_date</a>
    * <a href="#dataset_make">dataset_make</a>
    * <a href="#dataset_source">dataset_source</a>
    * <a href="#dataset_distributor">dataset_distributor</a>
    * <a href="#dataset_acknowledgement">dataset_acknowledgement</a>
    * <a href="#dataset_history">dataset_history</a>
    * <a href="#dataset_description">dataset_description</a>
    * <a href="#dataset_references">dataset_references</a>
    * <a href="#climatology">climatology</a>
    * <a href="#cruise_names">cruise_names</a>

1. <a href="#variable_metadata">Variable Metadata</a>
    * <a href="#var_short_name">var_short_name</a>
    * <a href="#var_long_name">var_long_name</a>
    * <a href="#var_sensor">var_sensor</a>
    * <a href="#var_unit">var_unit</a>
    * <a href="#var_spatial_res">var_spatial_res</a>
    * <a href="#var_temporal_res">var_temporal_res</a>
    * <a href="#var_discipline">var_discipline</a>
    * <a href="#visualize">visualize</a>
    * <a href="#var_keywords">var_keywords</a>    
    * <a href="#var_comment">var_comment</a>

1. <a href="#bibliography">Bibliography</a>
    * [References](#references)
------------------------------------------



<br/><br/>
<br/><br/>
<br/><br/>

<a id="introduction"></a>
## Introduction
<div style="text-align: right"><a href="#toc" title="Table of Contents">Table of Contents</a></div>   
This document describes the specifications of the data and metadata fields required for submitting datasets to the Simons CMAP database. The submitted data can be in any file format such as netCDF, parquet, plain text, CSV, or Excel files. The only requirement is that information for all required fields (specified by <sup>*</sup> ) is provided. For simplicity, we have created an empty dataset template in Excel format that can be found <a href="https://github.com/simonscmap/DBIngest/raw/master/template/datasetTemplate.xlsx">here</a>. You can use this template to load and submit your dataset. The data and metadata field names (e.g. time, lat, lon, short_name, long_name, ...) used in the template file are based on the CF and COARDS naming conventions [<a href="#ref1">1</a>, <a href="#ref1">2</a>, <a href="#ref1">3</a>].


The CMAP data template consists of three sheets: data, dataset metadata, and variable metadata. Data is stored in the first sheet called “data”. Metadata that describes the dataset is entered in the second sheet called “dataset_meta_data”. Metadata associated with the variables in the dataset are entered in the third sheet called “vars_meta_data”. Information must be provided for all columns except those specifcally noted as optional. For those datasets that use the Excel template, a web-based tool is available through <a href="https://simonscmap.com/datasubmission">Simons CMAP</a> to validate and modify a given  dataset  to ensure it conforms to structure requirements for dataset submission. Below are a few example datasets that have been prepared using the specifications described in this document:

* [Gradients 1 Cobalamin](https://github.com/simonscmap/DBIngest/raw/master/template/KOK1606_Gradients1_Cobalamin_example_2020_07_15.xlsx)

* [AMT01 Extracted Chlorophyll](https://github.com/simonscmap/DBIngest/raw/master/template/amt01_extracted_cholorphyll_2020_07_25.xls)

------------------------------------------

<br/><br/>
<br/><br/>
<br/><br/>



<a id="data_sheet"></a>
## Data Sheet
<div style="text-align: right"><a href="#toc" title="Table of Contents">Table of Contents</a></div>

| time   |      lat     |  lon |  depth [if exists] | var<sub>1</sub> | ... | var<sub>n</sub>
|:----------:|:-------------:|:------:|:------:|:------:|:------:|:------:|
| example: 2016-5-01T15:02:00 | 25  | -158 | 5 | value | ... | value |

All data points are stored in the "Data" sheet. Each data point must have time and location information. The exact name and order of the time and location columns are shown in the table above. If a dataset does not have depth values (e.g., sea surface measurements), you may remove the depth column. If your dataset represents results of a `Laboratory` study (see <a href="#dataset_make">dataset_make</a>) fill these fields with the time of study and the location of your laboratory. The columns var<sub>1</sub>  ...  var<sub>n</sub> represent the dataset variables (measurements). Please rename var<sub>1</sub>  ...  var<sub>n</sub> to names appropriate to your data. The format of "time", "lat", "lon", and "depth" columns are described in the following sections. Please review the example datasets listed in the <a href="#introduction">introduction</a> for more detailed information.
<br/><br/>

<a id="time"></a>
+ **time<sup>*</sup>**<br/>
This column holds datetime values with the following format: %Y-%m-%dT%H:%M:%S<br/>
The date and time sections are separated by a "T" character.<br/>
Example: 2010-02-09T18:15:00
    * Year (%Y) is a four-digit value: example 2010
    * Month (%m) is a two-digit value: example 02 (for Feburary)
    * Day (%d) is a two-digit value: example 09
    * Hour (%H) is a two-digit value from 00 to 23: example 18
    * Minute (%M) is a two-digit value from 00 to 59: example 15
    * Second (%S) is a two-digit value from 00 to 59: example 00
    * Time zone: UTC
<br/><br/>

<a id="lat"></a>
+ **lat<sup>*</sup>**<br/>
This column holds the latitude values with the following characteristics:<br/>
    * Type: Numeric values from -90 to 90
    * Format: Decimal (not military grid system)
    * Unit: degree North
<br/><br/>

<a id="lon"></a>
+ **lon<sup>*</sup>**<br/>
This column holds the longitude values with the following characteristics:<br/>
    * Type: Numeric values from -180 to 180
    * Format: Decimal (not military grid system)
    * Unit: degree East
<br/><br/>

<a id="depth"></a>
+ **depth**<br/>
This column holds the depth values with the following characteristics:<br/>
    * Type: Positive numeric values. It is 0 at surface with increased values with depth.
    * Format: Decimal
    * Unit: meter
<br/><br/>

<a id="vars"></a>
+ **var<sub>1</sub>  ...  var<sub>n</sub>**<br/>
These columns represent the dataset variables (measurements). Please rename
them to names appropriate for your data. Note that  these names should be identical to the names defined as <a href="#var_short_name">var_short_name</a> in the
<a href="#variable_metadata">Variable Metadata</a> sheet.
Please do not include units in these columns; units are recorded in the <a href="#variable_metadata">Variable Metadata</a> sheet. Leave a given cell empty for those instances when data was not taken and a value is missing. Do not replace the missing data with arbitrary values such as "99999", "0", "UNKNOWN", etc. Please review the example datasets listed in the <a href="#introduction">introduction</a> for more information.
------------------------------------------

<br/><br/>
<br/><br/>
<br/><br/>





<a id="dataset_metadata"></a>
## Dataset Metadata
<div style="text-align: right"><a href="#toc" title="Table of Contents">Table of Contents</a></div>   
This sheet holds a list of top-level attributes about the dataset such as the dataset name and description. Below are the list of these attributes along with their descriptions. Please review the example datasets listed in the <a href="#introduction">introduction</a> for more information.
<br/><br/>

<a id="dataset_short_name"></a>
+ **dataset_short_name<sup>*</sup>**<br/>
This name is meant to be used in programming codes and scripts. It should only contain a combination of letters, numbers, and underscores (the first character can not be a number). Do not use space, dash, or special characters such as <, +, %, etc. The name must be shorter than 50 characters and is a required field. <br/>

    * Required: Yes
    * Constraint: Less than 50 characters
<br/><br/>    

<a id="dataset_long_name"></a>
+ **dataset_long_name<sup>*</sup>**<br/>
 A descriptive and human-readable name for the dataset. This name will identify your dataset in the CMAP catalog (<a href="#fig_dataset_long_name_cat">Fig.1</a>) and visualization search dialog (<a href="#fig_dataset_long_name_viz">Fig.2</a>). Any Unicode character can be used here, but please avoid names longer than 200 characters as they may get trimmed when displayed on graphical interfaces. A full textual description of your dataset, with no length limits, is entered in "<a href="#dataset_description">dataset_description</a>" .
 If your dataset is associated with a cruise, we recommend including the official cruise and and the cruise nickname in the dataset_long_name. For example: Underway CTD Gradients 3 KM1906. <br/>  

    * Required: Yes
    * Constraint: Less than 200 characters
<br/><br/>    

<figure>
  <img id="fig_dataset_long_name_cat" src="../_static/data_submission_pics/dataset_long_name_cat.png" alt="Dataset Long_name in Catalog">
  <figcaption>Figure 1. A sample dataset shown in the Simons CMAP catalog. The "dataset_long_name" is enclosed in the red rectangle.</figcaption>
</figure>

<figure>
  <img id="fig_dataset_long_name_viz" src="../_static/data_submission_pics/dataset_long_name_viz_search.png" alt="Dataset Long_name in Visualization Page">
  <figcaption>Figure 2. The "dataset_long_name" appears in the visualization page search dialog.</figcaption>
</figure>

<br/><br/>  


<a id="dataset_version"></a>
+ **dataset_version<sup>*</sup>**<br/>
Please assign a version number or an identifier to your dataset such as "1.0.0" or "Final". Version identifiers will help track the evolution of a dataset over time. <br/>  

    * Required: Yes
    * Constraint: Less than 50 characters
    * Example: 1.0
<br/><br/>    


<a id="dataset_release_date"></a>
+ **dataset_release_date<sup>*</sup>**<br/>
Indicates the release date of the dataset. If your dataset has been previously published or released publicly, please specify that date. Otherwise, use the date the dataset was submitted to CMAP. <br/>

    * Required: Yes
    * Constraint: Less than 50 characters
    * Example: 2020-06-22
<br/><br/>  


<a id="dataset_make"></a>
+ **dataset_make<sup>*</sup>**<br/>
This is a required field that provides a broad category description of how a dataset was produced (also referred to as `dataset make`). Each dataset requires a single descriptor from a fixed set of options (observation, model, assimilation, laboratory), which are described below. This field will help in discovery of data in CMAP by categorizing datasets according to their `Make` class. Please contact us if you believe your dataset Make is not consistent with any of the categories below:<br/>

    * **Observation**: refers to any in-situ or remote sensing measurements such as measurements made during a cruise expedition, data from an in-situ sensor, or satellite observations. Observations made as part of laboratory experiments have their own distinct category and do not fall in this category.

    * **Model**: refers to the outputs of numerical simulations.  

    * **Assimilation**: refers to  products that are a blend of observations and numerical models.

    * **Laboratory**: refers to the observations made in a laboratory setting such as culture experiment results. <!--- comment for Mohammad: if we include at-sea experiments, this "make" could be Experimental (or Experiments). -->
<br/><br/>  


<a id="dataset_source"></a>
+ **dataset_source<sup>*</sup>**<br/>
Specifies the group and/or the institute name of the data owner(s). It can also include any link (such as a website) to the data producers. This information will be visible in the CMAP catalog as shown in <a href="#fig_dataset_source_cat">Fig.3</a>. Also, dataset_source will be annotated to any visualization made using the dataset (<a href="#fig_dataset_source_viz">Fig. 4</a>). This is a required field and its length must be less than 100 characters. <br/>

    * Required: Yes
    * Constraint: Less than 100 characters
    * Example: Armbrust Lab, University of Washington
<br/><br/>  

<figure>
  <img id="fig_dataset_source_cat" src="../_static/data_submission_pics/dataset_source_cat.png" alt="Dataset Source in Catalog">
  <figcaption>Figure 3. A sample dataset shown in the Simons CMAP catalog. The "dataset_source" is enclosed in the red rectangle.</figcaption>
</figure>

<figure>
  <img id="fig_dataset_source_viz" src="../_static/data_submission_pics/dataset_source_viz.png" alt="Dataset Source in Visualizations">
  <figcaption>Figure 4. The "dataset_source" appears in visualizations made using the corresponding dataset (enclosed in the red rectangle).</figcaption>
</figure>

<!--- Comment For Raphael: data source in plots (see figure above) seem to be data distributor not data source. Ask Mike to correct it. -->
<br/><br/>


<a id="dataset_distributor"></a>
+ **dataset_distributor**<br/>
If your dataset has already been published by a data distributor provide a link to the data distributor. Otherwise, leave this field empty. This is not a required field.<br/>

    * Required: No (optional)
    * Constraint: Less than 100 characters
    * Example: http://marine.copernicus.eu/
<br/><br/>  


<a id="dataset_acknowledgement"></a>
+ **dataset_acknowledgement**<br/>
Specify how your dataset should be acknowleged. You may mention your funding agency, grant number, or you may ask those that use your data to acknowledge your dataset with a particular statement. Dataset acknowlegment will be visible in the catalog page (<a href="#fig_dataset_ack_cat">Fig. 5</a>). This is not a required field.<br/>

    * Required: No (optional)
    * Constraint: No length limits    
<br/><br/>  

<figure>
  <img id="fig_dataset_ack_cat" src="../_static/data_submission_pics/dataset_ack_cat.png" alt="Dataset Acknowledgment in Catalog">
  <figcaption>Figure 5. A sample dataset shown in the Simons CMAP catalog. The "dataset_acknowledgement" is enclosed in the red rectangle.</figcaption>
</figure>


<br/><br/>


<a id="dataset_history"></a>
+ **dataset_history**<br/>
Use this field if your dataset has evolved over time and you wish to add notes about the history of your dataset. Otherwise, leave this field empty. This is not a required field.
<br/><br/>  


<a id="dataset_description"></a>
+ **dataset_description<sup>*</sup>**<br/>
Include any description that you think will help a reader  better understand your dataset. This description can include information about data acquisition, processing methods, figures, and links to external content. This field serves as the dataset documentation that is visible in the Simons CMAP catalog (<a href="#fig_dataset_description_cat">Fig. 6</a>). This field is required.<br/>  

    * Required: Yes
    * Constraint: No length limits
<br/><br/>    

<figure>
  <img id="fig_dataset_description_cat" src="../_static/data_submission_pics/dataset_description_cat.png" alt="Dataset description in Catalog">
  <figcaption>Figure 6. A sample dataset shown in the Simons CMAP catalog. The "dataset_description" is accessible using the "Dataset Details" button, enclosed in the red rectangle.</figcaption>
</figure>

<br/><br/>  


<a id="dataset_references"></a>
+ **dataset_references**<br/>
List any publications or documentation that one may cite in reference to the dataset. If there are more than one reference, please put them in separate cells under the dataset_reference column. Leave this field empty if there are no publications associated with this dataset. This is not a required field.
<br/><br/>  


<a id="climatology"></a>
+ **climatology**<br/>
This is a flag indicating whether the dataset represents a climatological product. If your dataset is a climatological product fill this field with "1". Otherwise, leave this field blank. This is not a required field.
<br/><br/>  


<a id="cruise_names"></a>
+ **cruise_names**<br/>
If your dataset represents measurements made during a cruise expedition (or expeditions), provide a list of cruise official names here. If your dataset is associated with more than one cruise, please put them in separate cells under the cruise_names column. If the cruises have any nicknames, please include them in the same cell as the official cruise name separated by a comma(s). Leave this field blank if your dataset is not associated with a cruise expedition. This is not a required field.<br/>

    * Required: No (optional)
    * Constraint: No length limits
    * Example: KOK1606, Gradients 1
<br/><br/>  
------------------------------------------


<br/><br/>
<br/><br/>
<br/><br/>





<a id="variable_metadata"></a>
## Variable Metadata
<div style="text-align: right"><a href="#toc" title="Table of Contents">Table of Contents</a></div>  
A dataset can contain multiple different measurements (variables). This sheet (labeled as "vars_meta_data") holds a list of top-level attributes about these variables such as the variable name, unit, and description. Each variable along with its attributes (metadata) is stored in separate rows. Below is the list of these attributes along with their descriptions. Please review the example datasets listed in the <a href="#introduction">introduction</a> for more information.
<br/><br/>



<a id="var_short_name"></a>
+ **var_short_name<sup>*</sup>**<br/>
This name is meant to be used in programming codes and scripts. It should only contain a combination of letters, numbers, and underscores (the first character can not be a number). Do not use space, dash, or special characters such as <, +, %, etc. Finally, there must be a one-to-one match between the short_names listed here and the variable column names in the "Data" sheet (see <a href="#vars">vars</a>). `var_short_name` will be seen in the CMAP catalog (<a href="#fig_var_short_name_cat">Fig. 7</a>), and will appear as the title of the generated figures (<a href="#fig_var_short_name_viz">Fig. 8</a>). This a required field and must be shorter than 50 characters. <br/>

    * Required: Yes
    * Constraint: Less than 50 characters
<br/><br/>    

<figure>
  <img id="fig_var_short_name_cat" src="../_static/data_submission_pics/var_short_name_cat.png" alt="Variable short name in catalog">
  <figcaption>Figure 7. A sample dataset shown in the Simons CMAP catalog. The "var_short_name" is highlighted in the red rectangle.</figcaption>
</figure>


<figure>
  <img id="fig_var_short_name_viz" src="../_static/data_submission_pics/viz_short_name.png" alt="Variable short name in a figure">
  <figcaption>Figure 8. A sample figure generated in the Simons CMAP catalog. The "var_short_name" appears as the figure title and is highlighted in the red rectangle.</figcaption>
</figure>

<br/><br/>    



<a id="var_long_name"></a>
+ **var_long_name<sup>*</sup>**<br/>
 A descriptive and human-readable label for the variable in accordance with the CF and COARDS conventions [<a href="#ref1">1</a>, <a href="#ref1">2</a>, <a href="#ref1">3</a>]. This name will present your variable in the CMAP catalog (<a href="#fig_var_long_name_cat">Fig. 9</a>) and visualization search dialog (<a href="#fig_var_long_name_search_viz">Fig. 10</a>). `var_long_name` can contain any unicode character, but please avoid names longer than 200 characters as they may get trimmed while displayed on graphical interfaces. Please use <a href="#var_comment">var_comment</a> if you would like to add a full textual description (with no length limits) for your variable. <br/>  

    * Required: Yes
    * Constraint: Less than 200 characters
<br/><br/>    

<figure>
  <img id="fig_var_long_name_cat" src="../_static/data_submission_pics/var_long_name_cat.png" alt="Variable long name in catalog">
  <figcaption>Figure 9. A sample dataset shown in the Simons CMAP catalog. The "var_long_name" is highlighted in the red rectangle.</figcaption>
</figure>

<figure>
  <img id="fig_var_long_name_search_viz" src="../_static/data_submission_pics/var_long_name_viz_search.png" alt="var long name in visualization page">
  <figcaption>Figure 10. The "var_long_name" appears in the visualization page search dialog.</figcaption>
</figure>

<br/><br/>  



<a id="var_sensor"></a>
+ **var_sensor<sup>*</sup>**<br/>
This is a required field that refers to the instrument used to produce the measurements such as `CTD`, `fluorometer`, `flow cytometer`, `sediment trap`, etc. If your dataset is the result of a field expedition but you are not sure about the name of the instrument used for the measurements, use the term "in-situ" to fill out this field. If your dataset is the output of a numerical model or a combination of model and observation, use the term "simulation" and "blend", respectively. This field will significantly help to find and categorize data generated using a similar class of instruments. `var_sensor` will be visible in the Simons CMAP catalog.

<br/><br/>  


<a id="var_unit"></a>
+ **var_unit**<br/>
Specifies  variable units, if applicable. Leave this field blank if your variable is unitless (e.g. "station numbers" or "quality flags"). Units may contain unicode characters such as subscripts and superscripts. `var_unit` will be visible in the Simons CMAP catalog (see <a href="#fig_var_long_name_cat">Fig. 9</a>) and in the generated visualizations (see <a href="#fig_var_short_name_viz">Fig. 8</a>). This field is not required.<br/>  

    * Required: No (optional)
    * Constraint: Less than 50 characters
    * Example: ug L<sup>-1</sup>
<br/><br/>    



<a id="var_spatial_res"></a>
+ **var_spatial_res<sup>*</sup>**<br/>
Specifies the spatial resolution of the variable. Typically, gridded products have uniform spatial spacing (such as 0.25&deg; X 0.25&deg;) while field expeditions do not have a regular spatial resolution. If your variable does not have a regular spatial resolution, use the term "irregular" to fill out this field. Note that if samples are taken at a series of distinct but spatially-non-uniform stations, the spatial resolution is considered irregular. `var_spatial_res` may contain unicode characters such as degree symbol ( &deg; ) and will be visible in the Simons CMAP catalog (see <a href="#fig_var_long_name_cat">Fig. 9</a>). This field is required.<br/>  

    * Required: Yes
    * Constraint: Less than 50 characters
    * Example: irregular
<br/><br/>    



<a id="var_temporal_res"></a>
+ **var_temporal_res<sup>*</sup>**<br/>
Specifies the temporal resolution of measurements (such as daily, hourly, 3-minutes, etc). If the measurements do not have a regular temporal spacing, use the term "irregular" to fill out this field. `var_temporal_res` will be visible in the Simons CMAP catalog (see <a href="#fig_var_long_name_cat">Fig. 9</a>). This field is required.<br/>  

    * Required: Yes
    * Constraint: Less than 50 characters
    * Example: irregular
<br/><br/>    



<a id="var_discipline"></a>
+ **var_discipline<sup>*</sup>**<br/>
Indicates in which disciplines (such as Physics, Biology ...) this variable is commonly studied. You can specify more than one discipline. If you list multiple disciplines per variable, please separate them by comma. `var_discipline` will be visible in the Simons CMAP catalog (referred to as "Study Domain" in <a href="#fig_var_long_name_cat">Fig. 9</a>). This field is required.<br/>  

    * Required: Yes
    * Constraint: Less than 100 characters
    * Example: Physics, BioGeoChemistry
<br/><br/>    



<a id="visualize"></a>
+ **visualize**<br/>
This is a flag field and can only be 0 or 1. Fill this field with 1, if you think this variable can be visualized on a graph by Simons CMAP. In principle, any variable with numeric values can be visualized while variables with string values, station numbers, or quality flags may not be the best candidates for visualization in CMAP. Please consult with the data curation team if you have any questions. This is not a required field. <br/>  
<br/><br/>    


<a id="var_keywords"></a>
+ **var_keywords<sup>*</sup>**<br/>
Every variable in CMAP is annotated with a range of semantically related keywords to ensure a variable can be easily discovered. For example, use of keywords allows you to search using the term "PO4" and retrieve a list of all phosphate data even if "PO4" was not used as the var_long_name for a given dataset. Similarly, if one searches for "MIT", CMAP returns all variables generated by MIT groups, or if one looks for "model", only model outputs are returned. These "semantic" searches are made possible using the keywords that are added to each variable. We would like to have keywords to cover the following areas described below (where applicable). Please note that there is no limit to the number of keywords used for a variable. The keywords are case-insensitive and you may add/remove them at any point (even after data ingestion). This is a required field.

    * Alternative names: other official, unofficial, abbreviation, technical (or jargon) names or notations associated with the variable. <br/>
    Examples: Nitrate, NO3, NO_3
    <!--- Mohammad - do you want to include an example that illustrates that you don't need to include "subset" keywords like Pro, Proch, Prochlor, Prochlorococcus -->

    * Method and Instrument: Keywords related to the method and instruments used for the variable measurements. <br/>
    Examples: observation, in-situ, model, satellite, remote sensing, cruise, CTD, cytometry, ....<br/><br/>
    Note these keywords are not mutually exclusive. For example, a CTD temperature measurement made during a cruise can have all of the following keywords: observation, in-situ, cruise, CTD

    * Data Producers: Keywords associated with the lead scientist/lab name/institute name.<br/>
    Examples: UW, University of Washington, Virginia Armbrust, Ginger

    * Cruise: The official/unoffical name of the cruise(s) during which the variable was measured, if applicable.<br/>
    Examples: KOK1606, Gradients_1, diel

    * Project name: If your data are in the context of a project, include the project name.<br/>
    Examples: HOT, Darwin, SeaFlow

<br/><br/>    


<a id="var_comment"></a>
+ **var_comment**<br/>
Use this field to communicate any detailed information about this particular variable with the users. This could include, for example, description of method(s) used to process the raw measurements. `var_comment` is visible in the Simons CMAP catalog (<a href="#fig_var_comment_cat">Fig. 11</a>). This field is not required.<br/>  

    * Required: No (optional)
    * Constraint: No length limits
<br/><br/>    

<figure>
  <img id="fig_var_comment_cat" src="../_static/data_submission_pics/var_comment_cat.png" alt="Variable description in Catalog">
  <figcaption>Figure 11. A sample dataset shown in the Simons CMAP catalog. The "var_commentn" is accessible using the "Comment" button, highlighted in the red rectangle.</figcaption>
</figure>

<br/><br/>
------------------------------------------





<a id="bibliography"></a>
## Bibliography
<div style="text-align: right"><a href="#toc" title="Table of Contents">Table of Contents</a></div>   

### References
1. <a id="ref1"></a>[NetCDF Climate and Forecast (CF) Metadata Conventions](http://cfconventions.org/cf-conventions/cf-conventions.html)
2. <a id="ref2"></a>[Conventions for the standardization of NetCDF files](https://ferret.pmel.noaa.gov/noaa_coop/coop_cdf_profile.html)
3. <a id="ref3"></a>[COARDS NetCDF Conventions](https://ferret.pmel.noaa.gov/Ferret/documentation/coards-netcdf-conventions)
