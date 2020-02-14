# 6.0002 Problem Set 5
# Graph optimization
# Name:
# Collaborators:
# Time:

#
# Finding shortest paths through MIT buildings
#
import unittest
import time
from graph import Digraph, Node, WeightedEdge

#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# Answer: Buildings are nodes, edges are paths between nodes with two weights
#


# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """

    mit_map = Digraph()

    map_file = open(map_filename, 'r')
    print("Loading map from file...")

    for line in map_file:

        line = line.replace('\n','')

        [s, d, total_distance, dis_outdoors] = line.split(' ')
        src = Node(s)
        dst = Node(d)
        w_edge = WeightedEdge(src, dst, int(total_distance), int(dis_outdoors))
        try:
            mit_map.add_node(src)
        except ValueError:
            pass
        try:
            mit_map.add_node(dst)
        except ValueError:
            pass
        mit_map.add_edge(w_edge)
    map_file.close()

    return(mit_map)

# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out


#
# Problem 3: Finding the Shorest Path using Optimized Search Method
#
# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#
# Answer:
#

# Problem 3b: Implement get_best_path
def get_best_path(digraph, start, end, path, max_dist_outdoors, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    path_list = path[0].copy()
    dist_traveled = path[1]
    dist_outdoors = path[2]
    # not sure what best distance is about setting it eq to best path here
    best_dist = best_path[1]

    #print(start, end, path, "best path:", best_path)
    if not digraph.has_node(start) or not digraph.has_node(end):
        #print(start, end, digraph.has_node(start), digraph.has_node(end))
        raise ValueError('Invalid Nodes')
    elif dist_outdoors > max_dist_outdoors or dist_traveled > best_dist:
        # short circut so we don't waste time with long paths
        #
        #print("SHORTED OUT")
        pass
    elif start == end:
        # we made it??
        #print("WE MADE IT WHOOO HOO",dist_traveled, best_dist)
        if dist_traveled <= best_dist:
            #print("WE MADE IT WHOOO HOO121212121", dist_traveled, best_dist)
            #best_dist = dist_traveled # this will not get used
            best_path = path.copy()
    else: ## need to add constraings
        edges = digraph.get_edges_for_node(start)
        for edge in edges:
            #print("trying edge", edge, " with path ", path)
            node = edge.get_destination()
            if node.get_name() in path_list:
                #print("but path_list knocked it out:", path_list)
                pass # already went down this route
            else:
                new_start = node
                new_dist_traveled = dist_traveled + edge.get_total_distance()
                new_dist_outdoors = dist_outdoors + edge.get_outdoor_distance()
                path_list_new = path_list.copy()
                path_list_new.append(new_start.get_name())
                #print(path_list,"dist traveled: ", dist_traveled, edge.get_total_distance(), "start node is", edge.get_source(), "dest node is ", node.get_name())
                new_path = [path_list_new, new_dist_traveled, new_dist_outdoors]
                best_path = get_best_path(digraph, new_start, end, new_path, max_dist_outdoors, best_dist,
                  best_path)

    #print("best_path returned: ", best_path)
    return best_path


# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    # TODO
    start_node = Node(start)
    end_node = Node(end)
    best_path = [['NONE FOUND'],max_total_dist,0]
    best_dist = max_dist_outdoors #never gets used
    starting_path = [[start],0,0]
    best_path = get_best_path(digraph, start_node, end_node, starting_path, max_dist_outdoors,
                  best_dist, best_path)

    if best_path[0][0] == 'NONE FOUND':
        raise ValueError
    else:
        return best_path[0] #looks like the test just want the list
    


# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))



    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)



if __name__ == "__main__":
    unittest.main()
    '''
    testing code below

    digraph = load_map("mit_map.txt")
    #digraph = load_map("mit_map_short.txt")
    best_path = [['1','2'],500,609999999]
    path = [['1'],0,0]
    #digraph.get


    start = time.time() #6 is good test, it is failing be sure to test impossible path
    print(directed_dfs(digraph, Node('1'), Node('4'),1000, 100))
    #print(get_best_path(digraph, Node('14'), Node('50'), path, 1, 500,
    #    best_path))
    print("should return [['1', '4'], 80, 65]")
    end = time.time()
    print("it took:", end-start)
    '''
