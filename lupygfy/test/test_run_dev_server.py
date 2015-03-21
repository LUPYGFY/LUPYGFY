""" This is a unit test of the server initiation in run_dev_server.py. """
#! python

__author__ = "Szabolcs Pasztor"
__copyright__ = None
__credits__ = "Szabolcs Pasztor"
__license__ = None
__version__ = "1.0.0"
__maintainer__ = "Szabolcs Pasztor"
__email__ = "blankityblankblankblank@gmail.com"
__status__ = "Development"

import os
import sys
import unittest
import urllib

_LIBRARY_PATH = os.path.abspath('../')
sys.path.insert(0, _LIBRARY_PATH)
import run_dev_server

from flask import Flask
from flask.ext.testing import LiveServerTestCase

class TestRunDevServer(LiveServerTestCase):
    """ Tests the functions in run_dev_server.py """
    def create_app(self):
        """ Required for testing dev server. """
        return run_dev_server.app

    def test_run_server(self):
        """ Tests run_server() in run_dev_server.py. """
        response = urllib.request.urlopen(self.get_server_url())
        self.assertEquals(response.code, 200)

_TEST_SUITE = unittest.TestLoader().loadTestsFromTestCase(TestRunDevServer)
unittest.TextTestRunner(verbosity=2).run(_TEST_SUITE)
