Image to ASCII
==============
A python module to easily transform image in ascii art.

.. image:: https://raw.githubusercontent.com/estevaofon/image-to-ascii-pyaoponto/main/zelda_ascii.png

Setup
-----

.. code-block:: bash

    $ pip install image-to-ascii-pyaoponto

Code sample
-----------

.. code-block:: python

    from image_to_ascii import ImageToAscii
    obj = ImageToAscii()
    # Image path
    obj.img_path("link.png")
    # print on screen
    obj.plot()
    # save in a txt file
    obj.save_to_file()