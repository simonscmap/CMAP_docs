

.. _pycmap: https://cmap.readthedocs.io/en/latest/user_guide/API_ref/pycmap_api/pycmap_api_ref.html

.. _`Simons CMAP website`: https://simonscmap.com/register


matcmap API
===========


.. _here: https://github.com/simonscmap/pycmap/archive/master.zip



matcmap is the MATLAB client for Simons CMAP project.
It provides access to the Simons CMAP database where various ocean data sets are hosted.
These data sets include multi decades of remote sensing observations (satellite),
numerical model estimates, and field expeditions.

This package is adopted from pycmap_ which is the python client of Simons CMAP ecosystem.


Usage
*****

Clone or download the repository. The source code is in the src directory.
The CMAP.m file abstracts the Simons CMAP API and provides the user with several
methods to query the database and extract subsets of data.
In order to make API requests, you need to get an API key from `Simons CMAP website`_.
Once you got your API key run the following command (in the MATLAB Command Window)
to store the API key on your local machine:

.. code-block:: MATLAB

    CMAP.set_api_key('your api key');

Documentation
*************

In the MATLAB Command Window run the following command to see the docs:

.. code-block:: MATLAB

    doc CMAP

Examples
********

1. Get the list of data sets:

.. code-block:: MATLAB

    CMAP.datasets()

2. Retrieve a subset of sea surface temperature measured by satellite. A simple plot is made to visualize the retrieved data.

.. code-block:: MATLAB

  tbl = CMAP.space_time(...
                    'tblsst_AVHRR_OI_NRT',... % table
                    'sst',... % variable
                    '2016-04-30',... % dt1
                    '2016-04-30',... % dt2
                    10,... % lat1
                    70,... % lat2
                    -180,... % lon1
                    -80,... % lon2
                    0,... % depth1
                    0);   % depth2

  lat = unique(tbl.lat);
  lon = unique(tbl.lon);
  sst = reshape(tbl.sst, length(lon), length(lat));
  imagesc(lon, lat, sst');
  axis xy;
  title('Sea Surface Temperature');
  colorbar();
