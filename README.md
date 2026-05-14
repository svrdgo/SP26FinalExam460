# The Torchbearer

**Student Name:** Santiago Verdugo Carrillo
**Student ID:** 828460068
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  _Calculating the shortest path from S would only give us the shortest distance from S. However, we also need the shortest distances when starting from other nodes._

- **What decision remains after all inter-location costs are known:**
  _Once all inter-location costs are known, we need to determine the order in which to visit each relic chamber so that the total cost is minimized._

- **Why this requires a search over orders (one sentence):**
  _Different orders will yield different total costs, which means a search over orders will allow us to find the minimum._

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source |
|---|---|
| _Start_ | _We need to compute the shortest path from Start to each relic chamber_ |
| _Relic Chamber_ | _We need to compute distance between relics and distance to exit_ |

### Part 2b: Distance Storage

| Property | Your answer |
|---|---|
| Data structure name | 2D Dictionary |
| What the keys represent | i and j = nodes in graph |
| What the values represent | dist[i][j] = distance from i to j|
| Lookup time complexity | O(1) |
| Why O(1) lookup is possible | Uses two constant-time lookups|

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** _k+1_
- **Cost per run:** _O((|V|+|E|)log|V|)_
- **Total complexity:** _O((k+1)(|V|+|E|)log|V|)_
- **Justification (one line):** _Dijkstra is run from the start and each relic chamber, and each run has a cost of O((|V|+|E|)log|V|)_

---

## Part 3: Algorithm Correctness

### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  _The distance recorded is the shortest and it will not change._

- **For nodes not yet finalized (not in S):**
  _The distance recorded is the shortest so far, but can possibly change._

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  _Before the first iteration, the distance to the start node is 0 and the distance to all others is set to infinity._
  _The start node has its correct shortest distance, and all other nodes have valid upper bounds_


- **Maintenance : why finalizing the min-dist node is always correct:**
  _Because all edge weights are nonnegative, the node with the smallest current distance cannot be reached by a shorter path through any unvisited node, which means the distance is correct when finalized._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _When the algorithm ends, all nodes have been finalized, so the shortest path to each node will have been calculated._

### Part 3c: Why This Matters for the Route Planner

_Having the correct shortest distances ensures that each routing decision is a step towards a globally optimal path._

---

## Part 4: Search Design

### Why Greedy Fails

- **The failure mode:** _Greedy fails when a locally optimal choice blocks a globally optimal solution._
- **Counter-example setup:** _Assume we have two search algorithms, one optimal and one greedy, both of which are given the following table (with cheapest inter-location costs already calculated):._

| From → To | B | C | D | T |
|-----------|---|---|---|---|
| S         | 1 | 2 | 2 | --|
| B         | --|100| 1 | 1 |
| C         | 1 | --|100|100|
| D         | 1 | 1 | --|1|

- **What greedy picks:** _Greedy would select the cheapest path available that leads to a node that has not been visited yet. Therefore, it would take the following route: S->B->D->C->T, giving us a total cost of 1+1+1+100=103._
- **What optimal picks:** _The optimal solution would be as follows: S->D->C->B->T, with a total cost of 2+1+1+1=5._
- **Why greedy loses:** _When greedy selects the closest path, it may be stuck selecting a much more expensive path later down the line._

### What the Algorithm Must Explore

- _The algorithm must explore every possible order of relic chambers visited in order to minimize the total cost._

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | current_loc | Node | Current node being visited |
| Relics already collected | relics | Set | Set with relic chambers visited|
| Fuel cost so far | cost_so_far | Int | Total fuel cost for current run |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer |
|---|---|
| Data structure chosen | Set|
| Operation: check if relic already collected | Time complexity: O(1)|
| Operation: mark a relic as collected | Time complexity: O(1)|
| Operation: unmark a relic (backtrack) | Time complexity: O(1)|
| Why this structure fits | Using a set makes relic tracking simple and easy to track, with quick operations|

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** _k!_
- **Why:** _There are k relic chambers that can be visited in any order._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

- **What is tracked:** _Minimum cost among valid routes so far ._
- **When it is used:** _When checking if current route has not exceeded the shortest route found so far._
- **What it allows the algorithm to skip:** _Routes that already exceed the shortest route found so far._

### Part 6b: Lower Bound Estimation

- **What information is available at the current state:** _Relics visited so far, current location and cost so far._
- **What the lower bound accounts for:** _The current cost plus the estimated minimum cost to visit the remaining relics and the exit_
- **Why it never overestimates:** _We assume the cheapest possible route can be taken, meaning the actual cost can be either greater than expected or exactly equal._

### Part 6c: Pruning Correctness

- _Because we never overestimate the cost to continue the route, we only prune when we know for a fact that the current route will be sub-optimal._

---

## References

- _Lecture slides only._


