# -*- encoding: utf-8 -*-

import sys
import os


def setpwd() -> str:
    fn = sys.argv[0]
    pn = os.path.dirname(fn)
    cpwd = os.getcwd()
    if (pn == '' or
            pn.startswith('/usr/local/') or
            pn.startswith('/usr/lib/')):
        npwd = cpwd
    else:
        npwd = pn
    os.chdir(npwd)
    return cpwd
