import os
import unittest

from launch.utils.utils import PATH

class TestLaunch(unittest.TestCase):
    
    def test_directory(self):
        launch_folder = PATH()
        self.assertTrue(os.path.isdir(launch_folder))