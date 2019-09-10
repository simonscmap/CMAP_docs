
.. _Jupyter Notebook: https://github.com/mdashkezari/opedia/blob/master/notebooks/Plot_ESV.ipynb



Exact Amplicon Sequence Variants
================================

**Query by taxonomy level, clustering thereshold, and size fraction**

The example below retrieves the "topN" number of most abundant sequenced organisms along track of the cruise. One can aggregate and visualize the relative abundance of the organisms according to their taxonomy, clustering levels, and size fractions. The cruise, 'ANT28-5', is an Atlantic latitudinal transect.


Thanks to Jed Fuhrman and Jesse McNichol (USC) for the beautiful dataset!


Code Tutorial
^^^^^^^^^^^^^


`Jupyter Notebook`_


.. code-block:: python


    from opedia import esv

    ############## set parameters ################
    # only plot the top_N number of most abundant organisms
    topN = 5
    # aggregate organisims by their taxa level
    tax = ['domain', 'kingdom', 'phylum', 'class', 'order', 'genus', 'species'][5]
    depth1 = 20
    depth2 = depth1
    cruise_name = 'ANT28-5'
    cluster_level = [89, 92, 96, 97, 98, 99, 100][0]        # minimum similarity precentage to be clustred
    size_frac_lower = [0.2, 3, 8][0]                        # size in micro-meter
    size_frac_upper = [None, 3, 8][1]                       # size in micro-meter
    ##############################################

    esv.plotESVs(topN, tax, depth1, depth2, cruise_name, cluster_level, size_frac_lower, size_frac_upper)



.. raw:: html

    <iframe src="../../../../_static/tutorial_plots/esv.html"  frameborder = 0  height="1000px" width="100%">></iframe>
