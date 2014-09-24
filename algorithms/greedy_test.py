from greedy import greedy
from data import Data
import operator
import unittest

class GreedyTest(unittest.TestCase):
    
    def test_greedy(self):
        print 'testing greedy function'

        #my sample data 
        my_data = Data()
        test_data = 'test.json'
        my_data.extract_data(test_data)

        uni_set = my_data.get_all_stores()
        set_sub = my_data.get_zips()
        
        #sorted_set = sorted(set_sub.values(), key=operator.attrgetter('num_nearby_stores'), reverse = True)

        #for zip in sorted_set:
        #   zip.print_nearby_stores()

        min_zip_check = greedy(uni_set, set_sub)

        #test on given input file   
        real_data = Data()
        data_file = 'gistfile1.json'
        real_data.extract_data(data_file)

        uni_set = real_data.get_all_stores()
        set_sub = real_data.get_zips()

        min_zip_check = greedy(uni_set, set_sub)


if __name__ == '__main__':
    unittest.main()