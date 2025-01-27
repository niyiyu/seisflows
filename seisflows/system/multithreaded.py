#
# This is Seisflows
#
# See LICENCE file
#
###############################################################################

# Import system modules
import os
import sys
from os.path import abspath, basename, join
from subprocess import Popen
from time import sleep

# Numpy
import numpy as np

# Local imports
from seisflows.tools import unix
from seisflows.tools.tools import call, findpath, nproc, saveobj
from seisflows.config import ParameterError, custom_import

try:
    PAR = sys.modules['seisflows_parameters']
    PATH = sys.modules['seisflows_paths']
except:
    print("Check parameters and paths.")


class multithreaded(custom_import('system', 'multicore')):
    """ An interface through which to submit workflows, run tasks in serial or
      parallel, and perform other system functions.

      By hiding environment details behind a python interface layer, these
      classes provide a consistent command set across different computing
      environments.

      For important additional information, please see
      http://seisflows.readthedocs.org/en/latest/manual/manual.html#system-configuration
    """

    def check(self):
        """ Checks parameters and paths
        """
        print("""
            DEPRECATION WARNING

                SYSTEM.MULTITHREADED has been renamed SYSTEM.MULTICORE

                Please update your parameter file.
        """)

        super(multithreaded, self).check()
