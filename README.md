##Min Set Cover
<img src = "./about/minset-cover.png">

##About: 
* name: min_inventory_checks
    * function: determine the _minimum_ number of inventory checks that covers all stores
    * input: stores and zip codes (Jason file)
    * output: minimum number of inventory checks (min list of zip codes)

##Info:
I determined that __zip codes__ are the relevant information in this problem because zip codes are the __keys__ to doing the minimum number of inventory checks at all stores. 

If you are smart in selecting the zip codes to enter into the the company site, you will end up with fewer inventory checks every day at all stores. From the JSON data given in the problem you can improve the number of inventory checks performed every day at specific stores by identifying and storing the minimum number of zip codes that __cover__ the set of __all stores__. 

This problem is known more generally as the __minimum set cover__ problem, which is the mapping of subsets onto a universal set. Every zip code contains a set that maps to the universal set of stores, so minimizing this this will also minimize the number of inventory checks on a daily basis at store websites. 

This problem has been proven to be __NP hard__, so there exist no polynomial time algorithm, but approximation and heuristics can be used to obtain better performance.       


##Problem:
>We do inventory checks on a daily basis for products at physical stores. Walgreens for example has 8042 stores and 22712 unique products so we end up with 182649904 inventory records. They allow checking the inventory of a product at stores near a given zipcode on their website. The check returns at most 5 stores per request. We want to write a program (ideally in Clojure or Python, though Java would also be fine) that determines the minimum number of inventory checks to make that covers all products at all stores. The inputs for an inventory check are zipcode, page number and product id.

>We've posted a JSON-formatted sample inventory reading for a single product at all Walgreens stores to github. The zipcopython min_inventory_checks.py gistfile1.jsonde field in in the inventory reading is encoded like: [zipcode]_[page-number]. You can download it here: https://gist.github.com/nside/199655afe31c1b56b921.

<img src = "./about/minset-cover.png">

* Problem Id:
    * minimum set cover
        * NP hard problem 
        * approximation algorithms and heuristics

* Strategy:
    * greedy
    * overlap look up
    * annealing
    * integer programming
    * weighted set cover 

* Analysis:
    * all subsets are independent and cover same maximum area
    * num(all_stores)/num(zip_stores) = least cover

##Run:
* `cd /dir/of/inventor/location`
* `python min_inventory_checks.py ./data/*`

##TODO LIST:
* annealing
* integer programming
