
.. _getcatalog:


Catalog
=======


.. image:: https://colab.research.google.com/assets/colab-badge.svg
   :target: https://colab.research.google.com/github/simonscmap/pycmap/blob/master/docs/Catalog.ipynb


.. method:: get_catalog()

    Returns a dataframe containing the details of all variables at Simons CMAP database.
    This method requires no input.

    A static version of the :ref:`Catalog` can be found at the Simons CMAP documentation.

    Alternatively, the catalog may be explored interactively at Simons CMAP website: https://simonscmap.com


    |

    :returns\:: Pandas dataframe.






**Example**

.. code-block:: python


  #!pip install pycmap -q     #uncomment to install pycmap, if necessary

  import pycmap

  api = pycmap.API(token='<YOUR_API_KEY>')
  api.get_catalog()

..
..
..
.. Optional parameter args
.. -----------------------
..
.. At this point optional parameters `cannot be generated from code`_.
.. However, some projects will manually do it, like so:
..
.. This example comes from `django-payments module docs`_.
..
.. .. class:: payments.dotpay.DotpayProvider(seller_id, pin[, channel=0[, lock=False], lang='pl'])
..
..    This backend implements payments using a popular Polish gateway, `Dotpay.pl <http://www.dotpay.pl>`_.
..
..    Due to API limitations there is no support for transferring purchased items.
..
..
..    :param seller_id: Seller ID assigned by Dotpay
..    :param pin: PIN assigned by Dotpay
..    :param channel: Default payment channel (consult reference guide)
..    :param lang: UI language
..    :param lock: Whether to disable channels other than the default selected above
..
.. .. _cannot be generated from code: https://groups.google.com/forum/#!topic/sphinx-users/_qfsVT5Vxpw
.. .. _django-payments module docs: http://django-payments.readthedocs.org/en/latest/modules.html#payments.authorizenet.AuthorizeNetProvider
