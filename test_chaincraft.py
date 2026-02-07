# test_chaincraft.py
"""
Tests for ChainCraft module.
"""

import unittest
from chaincraft import ChainCraft

class TestChainCraft(unittest.TestCase):
    """Test cases for ChainCraft class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainCraft()
        self.assertIsInstance(instance, ChainCraft)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainCraft()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
