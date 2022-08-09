# -*- coding: utf-8 -*-

from project_name.submodule import bar
import unittest


class BarTest(unittest.TestCase):
    def test_bar(self):
        self.assertEqual(bar.return_bar(), "bar!")


if __name__ == "__main__":
    unittest.main()
