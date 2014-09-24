import operator

def greedy(universal_set, subsets):
    """Greedy algorithm: takes a greedy approach to solving the min set cover problem by choosing the largest subset form a given set to cover the universal set."""
    
    #sort set of subsets based on largest subset
    sorted_set_zips = sorted(subsets.values(), key=operator.attrgetter('num_nearby_stores'), reverse = True)
    min_zipcode = set()                                 #minimum zip code check list
    zip_count = 0

    while len(universal_set) != 0:                      #until universal set is covered

        #select largest subset from set of zip codes
        largest_zip_cover = sorted_set_zips.pop(0)
        subset_stores = largest_zip_cover.nearby_stores

        #delete all elements of subset from universal set
        if universal_set & subset_stores: 

            universal_set = universal_set - subset_stores

            #add subset containing the largest number of uncovered elements to list of zip codes
            min_zipcode.add(largest_zip_cover.name)
            zip_count += 1

    
    
    #return min_zipcode                                 if needed can return min zipcode list 
    
    return zip_count