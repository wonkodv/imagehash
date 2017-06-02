from __future__ import (absolute_import, division, print_function)

import unittest
import numpy

from imagehash import ImageHash


class Test(unittest.TestCase):
    def setUp(self):
        self.h1 = ImageHash(numpy.array([[True, False], [True, True]])) # 0b1101
        self.h2 = ImageHash(numpy.array([[True, True], [False, True]])) # 0b1011

    def test_compare(self):
        assert self.h1 == self.h1
        assert self.h1 != self.h2

    def test_hammingdistance(self):
        assert self.h1 - self.h2 == 2
        assert self.h1 - self.h1 == 0

    def test_int(self):
        assert int(self.h1) == 0xD
        assert int(self.h2) == 0xB
        assert ImageHash.from_int(13, 2) == self.h1
        assert ImageHash.from_int(13, 4) != self.h1

    def test_str(self):
        assert str(self.h1) == "D"
        assert ImageHash.from_string("ABCD") == ImageHash.from_int(0xABCD,4)


    def test_xor(self):
        assert numpy.array_equal(self.h1 ^ self.h2, numpy.array([[False, True], [True, False]]))


if __name__ == '__main__':
    unittest.main()

