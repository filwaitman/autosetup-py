autosetup-py
============

[Because every time I start preparing my projects for PyPI "deployment" I get upset.]

setup.py (and relative files such as MANIFEST.in and setup.cfg) is not simple for the first (second, third) time.

This project aims to provide a *simple* bootstrap for setup.py and other files on common structure (namedly MANIFEST.in, README.rst, LICENSE, requirements.txt and setup.cfg). Again, it's a simple bootsrap. Take a look at some examples of generated output `here <https://github.com/filwaitman/autosetup-py/blob/master/tests/data>`_


Installation:
-------------
.. code:: bash

    pip install autosetup-py


Usage:
-------------

As a python method (with prompts)

.. code:: python

    from autosetup.main import main

    main()
    # Your project data will be prompted

As a python method (with parameters)

.. code:: python

    from autosetup.main import main

    main(
        module_name='potato',
        name='potato',
        version='0.0.1',
        author_name='Filipe Waitman',
        author_email='filwaitman@gmail.com',
        cvs_url='http://github.com/filwaitman/potato',
        tests_module='tests',
        requirements='requirements.txt',
        readme='README.rst',
        license='MIT',
    )

As a CLI (with prompts)

.. code:: bash

    autosetup-py
    # Your project data will be prompted

As a CLI (with parameters)

.. code:: bash

    autosetup-py --module=potato --author_name="Filipe Waitman" --author_email=filwaitman@gmail.com --cvs_url="http://github.com/filwaitman/potato" --license=GPL3 --use-defaults

NOTE: See :code:`autosetup-py --help` for more options and documentation


Contribute
----------
Did you think in some interesting feature, or have you found a bug? Please let me know!

Of course you can also download the project and send me some `pull requests <https://github.com/filwaitman/autosetup-py/pulls>`_.


You can send your suggestions by `opening issues <https://github.com/filwaitman/autosetup-py/issues>`_.

You can contact me directly as well. Take a look at my contact information at `http://filwaitman.github.io/ <http://filwaitman.github.io/>`_ (email is preferred rather than mobile phone).
