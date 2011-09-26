"""
Unit tests for the referenced exercise
"""
import unittest
import exercise1

class TestExercise1(unittest.TestCase):
    """
    Ensures the student writes correct code. It's essential to make sure that
    asserts also return a useful comment / description in the case of a fail.
    """

    def test_has_wibble(self):
        f = foo(wibble="foo")
        self.assertEqual(f.wibble, "foo", "A useful comment")
