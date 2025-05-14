import unittest
import sys
import os

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from Section1_Part3 import simulate_tm_ww

class TestSection1Part3(unittest.TestCase):
    """Tests for Section1_Part3.py - Turing Machine for ww language"""
    
    def test_empty_string(self):
        self.assertTrue(simulate_tm_ww(""))
        
    def test_even_length_valid_strings(self):
        self.assertTrue(simulate_tm_ww("00"))
        self.assertTrue(simulate_tm_ww("0101"))
        self.assertTrue(simulate_tm_ww("0000"))
        self.assertTrue(simulate_tm_ww("001100"))
        self.assertTrue(simulate_tm_ww("10101010"))
        
    def test_even_length_invalid_strings(self):
        self.assertFalse(simulate_tm_ww("01"))
        self.assertFalse(simulate_tm_ww("0110"))
        self.assertFalse(simulate_tm_ww("001101"))
        self.assertFalse(simulate_tm_ww("110001"))
        
    def test_odd_length_strings(self):
        self.assertFalse(simulate_tm_ww("0"))
        self.assertFalse(simulate_tm_ww("1"))
        self.assertFalse(simulate_tm_ww("000"))
        self.assertFalse(simulate_tm_ww("010"))
        self.assertFalse(simulate_tm_ww("101"))

if __name__ == '__main__':
    unittest.main()