import sys
import os

try:
    pass
except ImportError:
    # Add the parent directory of the current file to the path
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
