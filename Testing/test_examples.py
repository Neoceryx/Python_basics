import unittest
from Testing.examples import get_formatted_name

"""
unittest from the Python standard library provides tools for 
testing your code.
"""

"""
ssertEqual(a, b)            Verify that a == b
assertNotEqual(a, b)        Verify that a != b
assertTrue(x)               Verify that x is True
assertFalse(x)              Verify that x is False
assertIn(item, list)        Verify that item is in list
assertNotIn(item, list)     Verify that item is not in list
"""

"""Test from  Testing.examples.py"""
class NamesTestCase(unittest.TestCase):

    """Do names like 'Janis Joplin' work?"""
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()
