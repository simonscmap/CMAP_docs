
cmap4r
======

*cmap4r* is the R package developed for the CMAP project.
The github page can be found here: https://github.com/simonscmap/cmap4r


Prerequisites
~~~~~~~~~~~~~

For Mac operating system, a user needs to install the unixODBC library
and database drivers. We suggest using SQL Server ODBC drivers (Free
TDS). Using Homebrew, run the following commands to install the
suggested module.

-  brew install unixodbc
-  brew install freetds

In case of Linux operating system, first, install `Anaconda
distribition`_, and then run the following commands to install suggested
module.

-  conda install -c anaconda unixodbc
-  conda install -c anaconda freetds

Please follow the `link`_ to see other drivers available for
installation.

R user
~~~~~~

An R user will need the following package to connect to the database: a)
“DBI”, for database interface; b) “odbc” for connecting to the database
using **DBI** interface.

In addition, user may require some additional R package for downloading,
processing and visualizing the data. Run the following commands to
install some of the essential packages.

.. code-block:: shell

  ## Package "DBI" provide interface to the database
  install.packages("DBI")

  ## Driver for the database
  install.packages("odbc")

  ## Package for data processing:
  install.packages("dbplyr")
  install.packages("plyr")

  ## Package for visualization:
  install.packages("ggplot2")
  install.packages("plotly")


Package for visualization:
--------------------------

install.packages(“ggplot2”) install.packages(“plotly”)

.. _Anaconda distribition: https://www.anaconda.com/distribution/#linux
.. _link: https://db.rstudio.com/best-practices/drivers/
