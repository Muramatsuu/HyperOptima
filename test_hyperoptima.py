# test_hyperoptima.py
"""
Tests for HyperOptima module.
"""

import unittest
from hyperoptima import HyperOptima

class TestHyperOptima(unittest.TestCase):
    """Test cases for HyperOptima class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HyperOptima()
        self.assertIsInstance(instance, HyperOptima)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HyperOptima()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
