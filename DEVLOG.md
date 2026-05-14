# Development Log – The Torchbearer

**Student Name:** Santiago Verdugo Carrillo
**Student ID:** 828460068

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [05/11/2026]: Initial Plan

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

_Reviewed assignment requirements. The plan is to work on README document first, in order to have a strategy in place before writing any code. I believe the implementation of the code may be more difficult than the analysis, since the problem implies the solution for it may be somewhat complex. Once the solution is implemented, I plan to start testing by using simple inputs, and then moving on to edge cases to ensure those are properly handled. ._

---

## Entry 2 – [05/12/2026]: [Trouble with Dijkstra logic]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_When writing the code for Part 2, I rushed through the Dijkstra algorithm logic, which I did not notice until I tried visualizing my code. Instead of calculating the closest distance from each node to all other nodes, I was only doing it for the source node, which gave me an incomplete distances list. By writing some pseudocode and re-reading Part 2 in the README, I was able to change the logic to properly implement the algorithm._

---

## Entry 3 – [05/13/2026]: [Finished parts 5+6]

_Finished implementations of the code and all tests have passed. When first writing the README, I had decided to use a bitmask to track the relics visited. However, I decided a set would be much simpler to implement and could still coomplete operations in constant time. One of the concerns was the unordered nature of sets, but that was not an issue since the solution order was being tracked as well._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | .5hrs |
| Part 2: Precomputation Design | 1hr |
| Part 3: Algorithm Correctness | .5hrs |
| Part 4: Search Design | .5hrs |
| Part 5: State and Search Space | 1hr |
| Part 6: Pruning | 1hr |
| Part 7: Implementation | .5hrs|
| README and DEVLOG writing | 2hrs |
| **Total** | 7hrs |
