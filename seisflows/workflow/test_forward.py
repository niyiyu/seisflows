#
# This is Seisflows
#
# See LICENCE file
#
###############################################################################

# Import system modules
import sys

# Local imports
from seisflows.config import ParameterError
from seisflows.workflow.base import base

try:
    PAR = sys.modules['seisflows_parameters']
    PATH = sys.modules['seisflows_paths']

    system = sys.modules['seisflows_system']
    solver = sys.modules['seisflows_solver']
except:
    print("Check parameters and paths.")

class test_forward(base):
    """ Tests solver by running forward simulation
    """

    def check(self):
        """ Checks parameters and paths
        """

        # check paths
        if 'SCRATCH' not in PATH:
            raise Exception

        if 'LOCAL' not in PATH:
            setattr(PATH, 'LOCAL', None)

        if 'MODEL' not in PATH:
            raise Exception

        if 'OUTPUT' not in PATH:
            raise Exception


    def main(self):
        """ Generates seismic data
        """

        print('Running solver...')

        system.run('solver', 'generate_data',
                   model_path=PATH.MODEL,
                   model_type='gll',
                   model_name='model')

        print("Finished\n")
