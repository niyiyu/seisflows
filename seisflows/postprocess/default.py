#
# This is Seisflows
#
# See LICENCE file
#
###############################################################################

# Import system modules
import sys

# Local imports
from seisflows.config import custom_import

try:
    PAR = sys.modules['seisflows_parameters']
    PATH = sys.modules['seisflows_paths']
except:
    print("Check parameters and paths.")


class default(custom_import('postprocess', 'base')):
    """ Default postprocesing option

      Provides default image processing and regularization functions for models
      or gradients
    """
    # currently identical to base class
    pass
