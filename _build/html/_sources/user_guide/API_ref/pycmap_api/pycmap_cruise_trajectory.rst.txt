.. _cruise_traj:



Cruise Trajectory
=================


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/mdashkezari/pycmapDoc/blob/master/notebooks/CruiseTrajectory.ipynb


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
