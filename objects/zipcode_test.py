import unittest
from zipcode import Zipcode

class TestZipcode(unittest.TestCase):

    def test_add_store(self):
        print 'testing zipcode add store function'

        z = Zipcode(11801)
        z.add_nearby_store(1)

        s = set([1])

        self.assertEquals(s, z.nearby_stores)
        self.assertEquals(1, z.num_nearby_stores)

if __name__ == '__main__':
    unittest.main()