from __future__ import absolute_import
try:
    import util
except ImportError:
    import os, sys
    curr_path = os.path.abspath(os.path.dirname(__file__))
    p = os.path.join(curr_path, "../src/")
    sys.path.append(p)
    import util

util.log.init_logger()

import time

import numpy as np

import logging
