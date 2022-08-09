# -*- coding: utf-8 -*-

from project_name import foo
import unittest


class FooTest(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(foo.return_foo(), f"bar!foo!bar!")


if __name__ == "__main__":
    unittest.main()
