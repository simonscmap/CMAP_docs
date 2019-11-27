
.. _searchCatalog:


Search Catalog
==============


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/SearchCatalog.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FSearchCatalog.ipynb


.. method:: search_catalog(keywords)


    Returns a dataframe containing a subset of Simons CMAP catalog of variables.

    All variables at Simons CMAP catalog are annotated with a collection of semantically related keywords.
    This method takes the passed keywords and returns all of the variables annotated with similar keywords.
    The passed keywords should be separated by blank space.
    The search result is not sensitive to the order of keywords and is not case sensitive.
    The passed keywords can provide any 'hint' associated with the target variables. Below are a few examples:

    - the exact variable name (e.g. NO3), or its linguistic term (Nitrate)
    - methodology (model, satellite ...), instrument (CTD, seaflow), or disciplines (physics, biology ...)
    - the cruise official name (e.g. KOK1606), or unofficial cruise name (Falkor)
    - the name of data producer (e.g Penny Chisholm) or institution name (MIT)

    If you searched for a variable with semantically-related-keywords and did not get the correct results, please let us know.
    We can update the keywords at any point.

    |

    :Parameters:
        **keywords: string**
          Search keywords separated by a blank space. The search result is not sensitive to the order of keywords and is not case sensitive.



    :returns\:: Pandas dataframe.



**Example 1:**

List of all measurements by University of Hawaii hosted by Simons CMAP.

.. code-block:: python


  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.search_catalog('University of Hawaii')

**Example 2:**

Returns a list of Nitrite measurements during the Falkor cruise, if exists.

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.search_catalog('nitrite falkor')

**Example 3:**

Returns a list of optical measurements during the Gradients 1 cruise (KOK1606), if exists.

.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.search_catalog('optics KOK1606')

.. figure:: ../../../_static/overview_icons/sql.png
 :scale: 10 %

**SQL Statement**

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block::

   EXEC uspSearchCatalog 'space-separated keywords'

**Example:**

List of satellite Chlorophyll products:

.. code-block::

   EXEC uspSearchCatalog 'chl satellite'
