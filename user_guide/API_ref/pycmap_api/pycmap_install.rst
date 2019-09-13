.. _pycmapInstall:




Installation
============

.. _plotly: https://plot.ly/
.. _bokeh: https://bokeh.pydata.org/en/latest/index.html
.. _API: API.ipynb
.. _API key: API.ipynb
.. _Binder: https://mybinder.org/
.. _Colab: https://colab.research.google.com/
.. _Anaconda Distribution: https://www.anaconda.com/download/

.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Installation.ipynb


To use pycmap locally, you will need Python installed on your computer. We recommend the `Anaconda Distribution`_


pycmap can be installed using pip:

.. code-block:: shell

  pip install pycmap



In order to use pycmap, you will need to obtain an API key from
SimonsCMAP website: https://simonscmap.com.

.. note::

  You may install pycmap on cloud-based jupyter notebooks (such as
  `Binder`_, or `Colab`_) by running the following command in a
  code-block:



  .. code-block:: shell

    !pip install pycmap




.. code-block:: python

  #!pip install pycmap     #uncomment to install pycmap on Colab

  import pycmap

  pycmap.__version__
