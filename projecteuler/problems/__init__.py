"""Allow all the modules in the problems directory to be imported at once."""

import os
import glob

# Code from http://stackoverflow.com/questions/1057431/
modules = glob.glob(os.path.dirname(__file__) + "/*.py")
__all__ = [os.path.basename(module)[: -3] for module in modules]
