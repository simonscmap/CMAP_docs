.. _pycmapAPI:




API
===


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/API.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FAPI.ipynb

.. class:: API

    To retrieve data, create an instance of the system's API and pass the API key. It is no necessary to pass the API key every time you run a code locally, because it will be stored locally. The API class has other optional parameters to adjust its behavior. All parameters can be updated persistently at any point in the code.

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
