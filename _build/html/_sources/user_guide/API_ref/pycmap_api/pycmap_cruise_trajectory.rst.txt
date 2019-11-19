.. _cruise_traj:



Cruise Trajectory
=================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/CruiseTrajectory.ipynb

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gh/simonscmap/pycmap/master?filepath=docs%2FCruiseTrajectory.ipynb

.. method:: cruise_trajectory(cruiseName)


    Returns a dataframe containing the trajectory of the specified cruise.

    |

    :Parameters:
        **cruiseName: string**
          The official cruise name. If applicable, you may also use cruise "nickname" ('Diel', 'Gradients_1' ...).
          A full list of cruise names can be retrieved using cruise method.


    :returns\:: Pandas dataframe.


|

**Example**


.. code-block:: python

  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.cruise_trajectory('KM1513')


.. figure:: ../../../_static/overview_icons/sql.png
 :scale: 10 %

**SQL Statement**

Here is how to achieve the same results using a direct SQL statement. Please refer to :ref:`query` for more information.

.. code-block::

   EXEC uspCruiseTrajectoryByName 'Cruise Official Name'

**Example:**

.. code-block::

   EXEC uspCruiseTrajectoryByName 'KM1513'
