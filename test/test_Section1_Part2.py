import unittest
import sys
import os

# Add src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from Section1_Part2 import is_balanced, is_anbn

class TestSection1Part2(unittest.TestCase):
    """Tests for Section1_Part2.py - Balanced parentheses and a^nb^n strings"""
    
    def test_balanced_parentheses(self):
        self.assertTrue(is_balanced("(())"))
        self.assertTrue(is_balanced("()()"))
        self.assertTrue(is_balanced("(()())"))
        self.assertTrue(is_balanced("(((())))"))
        
    def test_unbalanced_parentheses(self):
        self.assertFalse(is_balanced("(()"))
        self.assertFalse(is_balanced(")("))
        self.assertFalse(is_balanced("())("))
        self.assertFalse(is_balanced("((()"))
        
    def test_valid_anbn_strings(self):
        self.assertTrue(is_anbn("aabb"))
        self.assertTrue(is_anbn("aaabbb"))
        self.assertTrue(is_anbn("ab"))
        self.assertTrue(is_anbn("aaaabbbb"))
        
    def test_invalid_anbn_strings(self):
        self.assertFalse(is_anbn("aab"))
        self.assertFalse(is_anbn("abb"))
        self.assertFalse(is_anbn("ba"))
        self.assertFalse(is_anbn("aaabb"))
        self.assertFalse(is_anbn("aabbb"))

if __name__ == '__main__':
    unittest.main()