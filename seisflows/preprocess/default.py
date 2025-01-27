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


class default(custom_import('preprocess', 'base')):
    """ Default preprocesing class

      Provides data processing functions for seismic traces, with options for
      data misfit, filtering, normalization and muting
    """
    # currently identical to base class
    pass
