import unittest
import sys
import os

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from Section1_Part1 import accepts_string

class TestSection1Part1(unittest.TestCase):
    """Tests for Section1_Part1.py - DFA for strings with number of 1's divisible by 3"""
    
    def test_empty_string(self):
        self.assertTrue(accepts_string(""))
        
    def test_zero_only_strings(self):
        self.assertTrue(accepts_string("000"))
        self.assertTrue(accepts_string("0"))
        self.assertTrue(accepts_string("000000"))
        
    def test_valid_strings(self):
        self.assertTrue(accepts_string("111"))
        self.assertTrue(accepts_string("10101"))
        self.assertTrue(accepts_string("11011"))
        self.assertTrue(accepts_string("111111000"))
        
    def test_invalid_strings(self):
        self.assertFalse(accepts_string("1"))
        self.assertFalse(accepts_string("11"))
        self.assertFalse(accepts_string("1101"))
        self.assertFalse(accepts_string("11111"))
        
    def test_invalid_characters(self):
        self.assertFalse(accepts_string("abc"))
        self.assertFalse(accepts_string("10a1"))
        self.assertFalse(accepts_string("1O1"))  # O instead of 0

if __name__ == '__main__':
    unittest.main()