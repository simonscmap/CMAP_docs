.. _query:



Query
=====

.. _`Azure Data Studio`: https://docs.microsoft.com/en-us/sql/azure-data-studio/download?view=sql-server-ver15
.. _`Plotly Falcon`: https://plot.ly/free-sql-client-download/
.. _`CMAP database repository`: https://github.com/simonscmap/DB


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Query.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FQuery.ipynb


.. method:: query(query)



    ``This is an 'optional' page. If you are not planning and/or not interested in SQL coding, simply ignore this page please!``

    Simons CMAP datasets are hosted in a SQL database and pycmap package provides the user with a number of pre-developed methods to extract and retrieve subsets of the data. The rest of this documentation is dedicated to explore and explain these methods. In addition to the pre-developed methods, we intend to leave the database open to custom scan queries for interested users. This method takes a custom SQL query statement and returns the results in form of a Pandas dataframe. The full list of table names and variable names (fields) can be obtained using the
    :ref:`getcatalog` method. In fact, one may use this very method to retrieve the table and field names:
    ``query(‘EXEC uspCatalog’)``. A Dataset is stored in a table and each table field represents a variable. All data tables have the following fields:

    * [time] [date or datetime] NOT NULL,
    * [lat] [float] NOT NULL,
    * [lon] [float] NOT NULL,
    * [depth] [float] NOT NULL,

    .. note::



      Tables which represent a climatological dataset, such as 'tblDarwin_Nutrient_Climatology', will not have a 'time' field.
      Also, if a table represents a surface dataset, such as satellite products, there would be no 'depth' field. 'depth' is a positive number in meters;
      it is zero at the surface and increasing towards the ocean's floor. 'lat' and 'lon' are in degrees units, ranging from -90° to 90° and -180° to 180°, respectively.


      Please keep in mind that some of the datasets are massive in size (10s of TB), avoid queries without WHERE clause (``SELECT * FROM TABLENAME``).
      Always try to add some constraints on time, lat, lon, and depth fields (see the basic examples below).


      Moreover, the database hosts a wide range of predefined stored procedures and functions to streamline nearly all CMAP data services.
      For instance, retrieving the catalog information is achieved using a single call of this procedure: uspCatalog.
      These predefined procedures can be called using the pycmap package (see Example 3).
      Alternatively, one may use any SQL client to execute these procedures to retrieve and visualize data (examples: `Azure Data Studio`_, or `Plotly Falcon`_).
      Using the predefined procedures, all CMAP data services are centralized at the database layer which dramatically facilitates
      the process of developing apps with different programming languages (pycmap, web app, cmap4r, ...).
      Please note that you can improve the current procedures or add new procedures by contributing at the `CMAP database repository`_.
      Below is a selected list of stored procedures and functions, their arguments will be described in more detail subsequently:


        * uspCatalog
        * uspSpaceTime
        * uspTimeSeries
        * uspDepthProfile
        * uspSectionMap
        * uspCruises
        * uspCruiseByName
        * uspCruiseBounds
        * uspWeekly
        * uspMonthly
        * uspQuarterly
        * uspAnnual
        * uspMatch
        * udfDatasetReferences
        * udfMetaData_NoRef

    |

    :Parameters:
      **query: string**
        Generic scan SQL statement. A full list of tables can be found in the :ref:`Catalog`.

    :returns: Pandas dataframe.





Example 1:
----------


A generic query returning dissolved iron (Fe) from Pisces model dataset.

.. code-block:: python

  # !pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.query(
           '''
           SELECT [time], lat, lon, depth, Fe FROM tblPisces_NRT
           WHERE
           [time] BETWEEN '2017-06-03' AND '2017-06-03' AND
           lat BETWEEN 10 AND 55 AND
           lon BETWEEN -180 AND 100 AND
           depth BETWEEN 0 AND 0.5
           ORDER BY [time], lat, lon, depth
           '''
           )


Example 2:
----------

A sample query returning the timeseries of sea surface temperature (sst).

.. code-block:: python

  # !pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.query(
           '''
           SELECT [time], AVG(lat) AS lat, AVG(lon) AS lon, AVG(sst) AS sst FROM tblsst_AVHRR_OI_NRT
           WHERE
           [time] BETWEEN '2016-06-01' AND '2016-10-01' AND
           lat BETWEEN 23 AND 24 AND
           lon BETWEEN -160 AND -158
           GROUP BY [time]
           ORDER BY [time]
           '''
           )





Example 3:
----------

A sample query calling a predefined stored procedure.

.. code-block:: python


  # !pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.query('EXEC uspCatalog')
