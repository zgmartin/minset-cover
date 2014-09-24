
class Zipcode:
    """a zipcode is associated with a set of nearby stores"""

    def __init__(self, zipcode_name):
        self.name = zipcode_name            #zipcode id name (ie 11801)
        self.num_nearby_stores = 0
        self.nearby_stores = set()          #set of nearby stores related to zipcode                

    def add_nearby_store(self, store_name):
        self.nearby_stores.add(store_name)
        self.num_nearby_stores += 1

    def print_nearby_stores(self):
        print self.nearby_stores