ConfigOptions
-------------

Install
=======
To install ConfigOptions, simply do:
    > pip3 install https://github.com/obarisk/configoptions.py/archive/master.zip

Usage
=====
To use ConfigOptions, simply do:

    >>> import configoptions
    >>> confopt = configoptions.ConfigOptions()
    >>> confopt.opts

    >>> import os
    >>> os.getcwd()
    >>> currpwd = configoptions.setpwd()
    >>> os.getcwd()
