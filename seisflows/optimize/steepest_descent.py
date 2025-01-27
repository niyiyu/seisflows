#
# This is Seisflows
#
# See LICENCE file
#
###############################################################################

# Import system modules
import sys

# Import Numpy
import numpy as np

# Local imports
from seisflows.config import custom_import, ParameterError

try:
    PAR = sys.modules['seisflows_parameters']
    PATH = sys.modules['seisflows_paths']
except:
    print("Check parameters and paths.")

class steepest_descent(custom_import('optimize', 'base')):
    """ Steepest descent method
    """
    restarted = False

    def check(self):
        """ Checks parameters, paths, and dependencies
        """

        if 'LINESEARCH' not in PAR:
            setattr(PAR, 'LINESEARCH', 'Bracket')

        super(steepest_descent, self).check()

    def setup(self):
        super(steepest_descent, self).setup()

    def compute_direction(self):
        super(steepest_descent, self).compute_direction()

    def restart(self):
        # steepest descent never requires restarts
        pass
