###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

COW_FILE = 'ps1_cow_data.txt'
COW_FILE2 = 'ps1_cow_data_2.txt'

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    cow_dict = {}
    cow_file = open(filename,'r')
    for line in cow_file:
        line = line.replace('\n','')
        cow_info = line.split(',')
        cow_dict[cow_info[0]] = int(cow_info[1])
        
    cow_file.close()

    return cow_dict   

 
# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    cow_trips = []
    cows_to_sort = list(cows.keys())
    cow_names = sorted(cows_to_sort, key=cows.__getitem__, reverse = True)

    #max(cows_left key=cows_left.get) #sort be weight
    while len(cow_names) > 0:
    #while cows_names:
        ship_load = []
        trip_limit = limit
        #print("initialised")
        for cow in cow_names.copy():
            #print(cow)
            mass = cows[cow]
            if mass <= trip_limit:
                ship_load.append(cow)
                trip_limit -= mass
                cow_names.remove(cow)
                #print("ship _load is:", ship_load, "limit is:", trip_limit, "cows left is:", cow_names)
                
        cow_trips.append(ship_load)
        
    return cow_trips
  

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # Lets get a list of all permutations 

    best_trips = []
    best_num_trips = len(cows) # maxium possible
    all_combos = get_partitions(cows)
    for trips in all_combos:
        # trips is a list of list
        #
        max_trip_weight = 0 # lowest possible for all 0 weight cows
        for trip in trips:
            trip_weight = 0
            for cow in trip:
                trip_weight += cows[cow]
            if trip_weight > max_trip_weight:
                max_trip_weight = trip_weight
        # Now that we have the maxium trip weight lets choose the trip with
        # the lowest number of trips that doesn't pass the limit
        #
        if ((max_trip_weight <= limit) and (len(trips) <= best_num_trips)):
            best_trips = trips.copy()
            best_num_trips = len(trips)
            
    return best_trips

    

    
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cow_dict = load_cows(COW_FILE)
    
    greedy_start = time.time()
    greedy_num = len(greedy_cow_transport(cow_dict,10))
    greedy_end = time.time()
    greedy_time = greedy_end - greedy_start

    brute_start = time.time()
    brute_num = len(brute_force_cow_transport(cow_dict,10))
    brute_end = time.time()
    brute_time = brute_end - brute_start

    print("Greedy took ", greedy_time, " and gave ", greedy_num)
    print("Brute took ", brute_time, " and gave ", brute_num)

#cow_dict = load_cows(COW_FILE)
#print(cow_dict)
compare_cow_transport_algorithms()


#cow_dict = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5, "Quad": 4}


#print(greedy_cow_transport(cow_dict,10))
#print(brute_force_cow_transport(cow_dict,10))

#print("expected")
#print("[Jesse, Maybel], [Callie, Maggie], [Quad]") # greedy
#print("[Jesse, Quad] [Maybel, Callie, Maggie]") # brute force
