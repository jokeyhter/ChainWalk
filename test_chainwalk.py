# test_chainwalk.py
"""
Tests for ChainWalk module.
"""

import unittest
from chainwalk import ChainWalk

class TestChainWalk(unittest.TestCase):
    """Test cases for ChainWalk class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainWalk()
        self.assertIsInstance(instance, ChainWalk)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainWalk()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
