#!/usr/bin/python
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from builtins import *
import sys
import os
python_path = os.environ['PYTHONPATH']
try:
    import clonedigger.clonedigger  
    if not os.path.abspath(clonedigger.clonedigger.__file__).startswith(os.path.abspath(python_path)):
        raise ImportError
except ImportError:
    if not os.path.exists(python_path): 
        os.mkdir(python_path)
    os.chdir(python_path)
    print('Missing Clone Digger')
    print('We will try now to install it to local directory', python_path)
    print('please wait...')
    sys.argv = [sys.argv[0], 'easy_install', '--exclude-scripts', '-U', '--always-copy', '--install-dir', python_path, 'clonedigger']
    try:
	   import setup
    except:
	   import setup
    sys.exit(143)
clonedigger.clonedigger.main()
