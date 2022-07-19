import sys
import unittest

sys.path.append("C:\\Users\\Sam\\Documents\\Programming\\WeatherAppRepo")
from tempchecker import *


class TestCalc(unittest.TestCase):
    def test_find_highest_temp(self):

        self.assertTupleEqual(
            find_highest_temp([["a", 5], ["b", 12], ["c", 643], ["d", 23], ["e", 6]]),
            ("c", 643),
        )

        self.assertTupleEqual(
            find_highest_temp([["a", -5], ["b", 12], ["c", -643], ["d", 23], ["e", 6]]),
            ("d", 23),
        )

        self.assertTupleEqual(
            find_highest_temp(
                [["a", -5], ["b", -12], ["c", -643], ["d", -23], ["e", -6]]
            ),
            ("a", -5),
        )
        self.assertTupleEqual(
            find_highest_temp(
                [["a", -122], ["b", -12], ["c", -643], ["d", -23], ["e", -6]]
            ),
            ("e", -6),
        )

    def test_find_lowest_temp(self):
        self.assertTupleEqual(
            find_lowest_temp(
                [["a", -5], ["b", -12], ["c", -643], ["d", -23], ["e", -6]]
            ),
            ("c", -643),
        )

        self.assertTupleEqual(
            find_lowest_temp([["a", 5], ["b", -12], ["c", 643], ["d", -23], ["e", 6]]),
            ("d", -23),
        )

        self.assertTupleEqual(
            find_lowest_temp([["a", 5], ["b", 12], ["c", 643], ["d", 23], ["e", 6]]),
            ("a", 5),
        )


if __name__ == "__main__":
    unittest.main()
