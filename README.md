##Minimum Inventory Check

###About: 
This is a program to determine the minimum number of inventory checks that covers ALL PRODUCTS at ALL STORES.

#####input:
stores and zip codes (Jason file)

#####output:
minimum number of inventory checks (min list of zip codes)

###Run:
cd /dir/of/inventor/location

python min_inventory_checks.py ./data/*

###Info:
I determined that zip codes are the relevant information in this problem because zip codes are the keys to doing the minimum number of inventory checks at all stores. 

If you are smart in selecting the zip codes to enter into the the company site, you will end up with fewer inventory checks every day at all stores. From the JSON data given in the problem you can improve the number of inventory checks performed every day at specific stores by storing and identifying the minimum number of zip codes that cover the set of all stores. 

This problem is known as a more generalized problem called the minimum set cover problem, which is the mapping of subsets onto a universal set. Every zip code contained a set that maps to the universal set of stores, so minimizing this this will also minimize the number of inventory checks on a daily basis at store websites. 

This problem has been proven to be NP hand, so there exist no polynomial time algorithm, but approximation and heuristics can be used to obtain better performance.       


###Real World Problem:
We do inventory checks on a daily basis for products at physical stores. Walgreens for example has 8042 stores and 22712 unique products so we end up with 182649904 inventory records. They allow checking the inventory of a product at stores near a given zipcode on their website. The check returns at most 5 stores per request. We want to write a program (ideally in Clojure or Python, though Java would also be fine) that determines the minimum number of inventory checks to make that covers all products at all stores. The inputs for an inventory check are zipcode, page number and product id.

We've posted a JSON-formatted sample inventory reading for a single product at all Walgreens stores to github. The zipcopython min_inventory_checks.py gistfile1.jsonde field in in the inventory reading is encoded like: [zipcode]_[page-number]. You can download it here: https://gist.github.com/nside/199655afe31c1b56b921.


####Problem Id:
minimum set cover

info known:
NP hard problem (approximation algorithms and heuristics)

####Example:
<img src = "./minset-cover.svg">

###Strategy:
greedy
overlap look up
annealing
integer programming
weighted set cover 



Best Case:
all subsets are independent and cover same maximum area
num(all_stores)/num(zip_stores) = least cover



###TODO LIST:
annealing
integer programming
