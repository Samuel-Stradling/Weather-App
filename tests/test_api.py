import sys
import unittest

sys.path.append('C:\\Users\\Sam\\Documents\\Programming\\WeatherAppRepo')
from api import get_temp


class TestCalc(unittest.TestCase):
    def test_get_temp_raise(self):
        with self.assertRaises(TypeError): #TypeError
            get_temp(1234)

    def test_get_temp_case(self):
        self.assertEqual(type(get_temp("CheLmsForD")), float)
        self.assertEqual(type(get_temp("CAntERBurY")), float)
    
    def test_get_temp_spelling(self):
        with self.assertRaises(UnboundLocalError):
            get_temp("adsgasdg")
            get_temp("cantrebury")


if __name__ == "__main__":
    unittest.main()