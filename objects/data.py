from json import JSONDecoder
from zipcode import Zipcode

class Data:
    """Extracting relevant data from Jason file for minimum inventory checks problem"""

    def __init__(self):
        self.all_stores = set()                     #set of all all stores (universal set of stores)
        self.zips = {}                              #set of subsets of all stores based upon unique zipcode key


    def extract_data(self, file_name):
        """Extracts data from given JSON file."""

        decoder = JSONDecoder()

        with open(file_name, 'r') as file:
            for line in file:
                feature = decoder.decode(line)

                zipcode_name = feature['zipcode']
                zipcode_name = int(zipcode_name.rsplit("_")[0])  

                store_name = feature['store_id']
                store_name = int(store_name.rsplit("_")[1])        

                self.all_stores.add(store_name)                                #adds store to set universal set of stores


                if zipcode_name in self.zips:
                    self.zips[zipcode_name].add_nearby_store(store_name)        #adds nearby store to zip code if zip exists in dictionary

                else:
                    z = Zipcode(zipcode_name)                                   #creates new zip code if not exist
                    z.add_nearby_store(store_name)
                    self.zips[zipcode_name] = z


    def get_all_stores(self):
        '''Returns the set of all stores.'''

        return self.all_stores

    def get_zips(self):
        '''Returns a set zip codes.'''
        
        return self.zips