from objects import Data
from algorithms import greedy
import sys


def min_inventory_check(file_name):
    """Returns a list of the minimum number of inventory checks for an input file."""

    #generates usable data from JSON file
    input_data = Data()
    input_data.extract_data(file_name)

    #runs greedy algorithm on data
    min_number_inventory_checks = greedy(input_data.all_stores, input_data.zips) 

    return min_number_inventory_checks


if __name__ == '__main__':
    args = sys.argv

    print 'min inventory checks: \n'
    for x in range(1 , len(args)):

        file_name = args[x]

        print 'store', x, ':', min_inventory_check(file_name)