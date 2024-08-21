## Concepts Needed

### Greedy Algorithms
- **Understanding** how greedy algorithms work and why they are suitable for the coin change problem.
- **Recognizing** the limitations of greedy algorithms and identifying scenarios where they might not provide the optimal solution.

### Dynamic Programming
- **Basic Principles** of dynamic programming as a method to solve optimization problems.
- **Overlapping Subproblems & Optimal Substructure**: Understanding these concepts in the context of the coin change problem.

### Algorithmic Complexity
- **Analyzing** the time and space complexity of algorithms.
- **Striving** for solutions with lower complexity to meet runtime constraints.

### Problem-Solving Strategies
- **Breaking Down** the problem into smaller, manageable sub-problems.
- **Iterative vs Recursive Approaches** to dynamic programming.

### Python Programming
- **Manipulating Lists** and using list comprehensions.
- **Implementing Functions** with efficient looping and conditional statements.

## Resources

### Python Official Documentation
- [**More Control Flow Tools**: Deep dive into `for` loops, `if` statements, and other control flow tools in Python.](https://docs.python.org/3/tutorial/controlflow.html)

### GeeksforGeeks Articles
- **[Coin Change | DP-7](https://www.geeksforgeeks.org/coin-change-dp-7/)**: Comprehensive guide on solving the coin change problem using dynamic programming.
- **[Greedy Algorithm to find Minimum number of Coins](https://www.geeksforgeeks.org/greedy-algorithm-to-find-minimum-number-of-coins/)**: Explanation of the greedy approach to minimize the number of coins.

### YouTube Tutorials
- **[Dynamic Programming - Coin Change Problem](https://www.youtube.com/watch?v=jgiZlGzXMBw)**: Visual and step-by-step explanation of the dynamic programming approach to the coin change problem.

---

By thoroughly understanding these concepts and utilizing the provided resources, you will be well-prepared to tackle the coin change problem. You will need to decide whether a greedy algorithm suffices for your particular set of coin denominations or if a more comprehensive dynamic programming approach is necessary to ensure correctness and efficiency. This project not only tests your algorithmic skills


# 0x08. Making Change

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- Prototype: ```def makeChange(coins, total)```
- Return: fewest number of coins needed to meet total
- - If total is 0 or less, return 0
- - If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list
- Your solution’s runtime will be evaluated in this task
