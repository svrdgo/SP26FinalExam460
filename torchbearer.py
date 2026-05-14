"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Santiago Verdugo Carrillo
Student ID:   828460068

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return"""Why a single shortest-path run from S is not enough: Calculating the shortest path from S would only give us the shortest distance from S. However, we also need the shortest distances when starting from other nodes.

What decision remains after all inter-location costs are known: Once all inter-location costs are known, we need to determine the order in which to visit each relic chamber so that the total cost is minimized.

Why this requires a search over orders (one sentence): Different orders will yield different total costs, which means a search over orders will allow us to find the minimum."""

# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    sources = [spawn]
    for node in relics:
        if node not in sources:
            sources.append(node)

    return sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').
    TODO
    """
    #Initialize list to all infinite values
    dist = {node: float('inf') for node in graph}
    #Set source distance to itself to 0
    dist[source] = 0
    #Declare priority queue
    pq = [(0,source)]
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        if curr_dist>dist[curr_node]: #Prune longer distances
            continue 
        for neighbor, cost in graph[curr_node]:
            if neighbor not in dist: #Edge case: neighbor in edge but not in graph
                dist[neighbor] = float('inf')
            if (curr_dist+cost<dist[neighbor]): #Check if distance is shorter
                dist[neighbor] = curr_dist+cost
                heapq.heappush(pq, (dist[neighbor],neighbor))

    return dist


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    dist_table = {}
    #Calculate distances
    dist_table [spawn] = run_dijkstra(graph, spawn)
    for node in relics:
        if node != spawn:
            dist_table[node] = run_dijkstra(graph, node)
    return dist_table




# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return """Part 3a: What the Invariant Means
For nodes already finalized (in S): The distance recorded is the shortest and it will not change.

For nodes not yet finalized (not in S): The distance recorded is the shortest so far, but can possibly change.

Part 3b: Why Each Phase Holds

Initialization : why the invariant holds before iteration 1: Before the first iteration, the distance to the start node is 0 and the distance to all others is set to infinity. The start node has its correct shortest distance, and all other nodes have valid upper bounds

Maintenance : why finalizing the min-dist node is always correct: Because all edge weights are nonnegative, the node with the smallest current distance cannot be reached by a shorter path through any unvisited node, which means the distance is correct when finalized.

Termination : what the invariant guarantees when the algorithm ends: When the algorithm ends, all nodes have been finalized, so the shortest path to each node will have been calculated.

Part 3c: Why This Matters for the Route Planner

Having the correct shortest distances ensures that each routing decision is a step towards a globally optimal path."""

# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return """Why Greedy Fails

The failure mode: Greedy fails when a locally optimal choice blocks a globally optimal solution.
Counter-example setup: Assume we have two search algorithms, one optimal and one greedy, both of which are given the following table (with cheapest inter-location costs already calculated):.
From → To	B	C	D	T
S	1	2	2	--
B	--	100	1	1
C	1	--	100	100
D	1	1	--	1
What greedy picks: Greedy would select the cheapest path available that leads to a node that has not been visited yet. Therefore, it would take the following route: S->B->D->C->T, giving us a total cost of 1+1+1+100=103.
What optimal picks: The optimal solution would be as follows: S->D->C->B->T, with a total cost of 2+1+1+1=5.
Why greedy loses: When greedy selects the closest path, it may be stuck selecting a much more expensive path later down the line.
What the Algorithm Must Explore

The algorithm must explore every possible order of relic chambers visited in order to minimize the total cost.
"""

# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    best = [float('inf'),[]] #Initialize best
    _explore(dist_table=dist_table,
             current_loc=spawn,
             relics_remaining=set(relics),
             relics_visited_order=[],
             cost_so_far=0,
             exit_node=exit_node,
             best=best)
    return (best[0],best[1])

def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    #If exit node is last one left
    if not relics_remaining:
        total_cost = cost_so_far + dist_table[current_loc][exit_node]
        if total_cost < best[0]:
            best[0] = total_cost
            best[1] = relics_visited_order.copy() #Update route order
        return
    #Prune
    if (cost_so_far >= best[0]):
        return
    
    for relic in relics_remaining:
        new_remaining = relics_remaining - {relic}
        #Calculate cost if we visited this relic next
        new_cost = cost_so_far + dist_table[current_loc][relic]
        if(new_cost>=best[0]): #All edges are nonnegative, so total cost can only increase as the route extends. Therefore, if the current cost is equal or higher to best cost, this route is safe to prune
            continue
        #Recursive step
        _explore(
            dist_table=dist_table,
            current_loc=relic,
            relics_remaining = new_remaining,
            relics_visited_order=relics_visited_order + [relic],
            cost_so_far=new_cost,
            exit_node=exit_node,
            best=best)

# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    dist_table = precompute_distances(graph,spawn,relics,exit_node)
    return find_optimal_route(dist_table,spawn,relics,exit_node)


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
