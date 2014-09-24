import unittest
from data import Data

class DataTest(unittest.TestCase):

    def test_extract_data(self):
        print 'testing extract data fuction'

        #my sample test
        my_data = Data()
        test_data_file = 'test.json'
        my_data.extract_data(test_data_file)

        print my_data.get_all_stores()

        subset_stores = my_data.get_zips()
        for key in subset_stores.keys():
            print key
            subset_stores[key].print_nearby_stores()
            #print subset_stores[key]


        #test on given input file   
        real_data = Data()
        data_file = 'gistfile1.json'
        real_data.extract_data(data_file)



if __name__ == '__main__':
    unittest.main()