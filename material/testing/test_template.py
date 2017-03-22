import unittest

from example import gen_dummy_data
from detrend import detrend

class TestDetrend(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_gen_dummy(self):
        x,y = gen_dummy_data()
        self.assertEqual(len(x), len(y))

    def test_detrend(self):
        slope = 6.
        offset = 33.
        x,y = gen_dummy_data(slope=slope, offset=offset, std=0.)
        yn, m, b = detrend(x,y)
        self.assertAlmostEqual(m, slope)
        self.assertEqual(b, offset)
