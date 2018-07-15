# Constraint Satisfaction Problems

Constraint satisfaction problems are problems that can be solved by attempting to assign values to variables X<sub>i</sub>, where the values are often restricted to a finite domain (though can be infinite), and restrictions are imposed upon the variables (e.g. X<sub>i</sub> ~= X<sub>j</sub> for all i ~= j).


### Constraint Types

Two common types of constraints are _unary_ constraints and _binary_ constraints. A unary constraint is a constraint involving only one variable. For example,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
X<sub>2</sub> ~= green.

Binary constraints are constraints relating two variables. For example, for the 4 Queens problem, where Q<sub>i</sub>∈{1,2,3,4}, 1 ≤ i ≤ 4, we have the following constraints relating Q<sub>1</sub> and Q<sub>2</sub>:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
(Q<sub>1</sub>, Q<sub>2</sub>) ∈ {(1, 3), (1, 4), (2, 4), (3, 1), (4, 1), (4, 2)}

The above is an example of an _explicit_ constraint. An example of an _implicit_ constraint would be

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
alldiff(Q<sub>1</sub>, Q<sub>2</sub>, Q<sub>3</sub>, Q<sub>4</sub>)

implying no two Q<sub>i</sub>'s can have the same value. Another example of an implicit constraint would be

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
Σ<sub>i,j</sub> X<sub>i,j</sub> = n

A _binary CSP_ is a CSP where each constraint involves at most two variables (or can be reformulated as such).

### Connection with Backtracking

These problems can be naively solved recursively through backtracking by assigning a value to a variable, and seeing if a solution exists with this assigned value. If a solution exists, we are done. If it does not exist, we try a different value and repeat. If no values can be assigned, then we fail.

### Search Formulation

To solve a CSP, then in one way or another we make use of the following:

- **States**: values assigned so far
- **Initial State**: The empty assignment {}
- **Successor Function**: A method to select an unassigned variable and assign a value to it that does not violate any constraints, or fail if no such assignment is possible.
- **Goal Test**: Check if the assignment is complete and violates no constraints.

#### Complexity

If we have n variables and m values, then the total number of assignments (including ones that could violate constraints) is m<sup>n</sup>. However, when we are naively searching for solutions, we start with one variable, assign a value and continue with the remaining n-1 variables. As such, the *depth* of our solution is never greater than n, and so DFS is a popular way to solve CSP problems.

But consider trying every path in the search tree. At the top level, we assign one of the m values to one of our n variables, giving n•m choices. For each of these choices, we have n-1 variables remaining, all of which can take m values, or (n-1)•m choices, and so on. As such, the total number of possible paths in the tree is (n)m * (n-1)m * ... * (1)m, or * **n!•m<sup>n</sup>**, which is greater than the total number of possible assignments!

We can easily reduce this by noticing that *variable assignments are commutative*. That is, assigning X<sub>i</sub>=0, followed by X<sub>j</sub>=1 is the same as assigning X<sub>j</sub>=1 and then X<sub>i</sub>=0. So by *restricting the order of variable assignments*, we can reduce the total number of possible paths back down to m<sup>n</sup>.

### Recursive Backtracking Algorithm

```python
def recursive_backtracking(assignment, csp):
    if assignment is complete:
        return assignment
    var = select_unassigned_variable(csp[variables], assignment, csp)
    for value in order_domain_values(csp[variables], assignment, csp):
        if consistent(value, csp[constraints]):
            assignment.update(var = value)
            result = recursive_backtracking(assignment, csp)
            if result != failure:
                return result
            assignment.remove(var = value)
    return failure
```

## Improvements on Backtracking

To see how we might improve the efficiency of our algorithm, we ask ourselves:

- Which variable should be assigned next?
- In what order should values be tried?
- Can we detect failure early?

### Most Constrained Variable

To decide which variable to assign to next, we choose the variable with the fewest possible legal assignments. This is also known as the **minimum remaining values (MRV)** heuristic, or the **fail first** heuristic, as it assigns first to the variables that are most likely to fail.

### Most Constraining Variable

In the case that we have a tie when employing the MRV heuristic, we choose the variable that **imposes the most constraints on the remaining variables**. For example, at the beginning of a graph coloring problem, one is free to assign any of m colors to any of n vertices, so MRV does not help us at this stage. So we can instead color the vertex that has the highest degree, which in turn has the greatest effect on possible assignments to the remaining vertices.

### Least Constraining Value

We now have our next variable to assign, but what value should be choose? We want to leave ourselves with the most possible valid paths after our assignment, so we should choose a value that eliminates the fewest values amongst the remaining variables, hence the least constraining value.

Of course, if we are interested in finding all solutions, or there are no solutions to our problem, then there is no advantage in employing LCV as we will end up trying all values anyways.

### Forward Checking

After we assign a value to a variable, we want to keep track of all possible values for the remaining variables. If a variable has no more legal values at any point in our search, we can backtrack immediately from our current assignment.

### Constraint Propagation

Forward checking will not  rule out all of the invalid assignments. For example, in the middle of a vertex coloring, we may come to a point where two adjacent vertices only have the colour blue to be assigned. Forward checking will say this is fine, but we already know any variable assignments made from our current state will be invalid.

#### Arc Consistency

The simplest form of constraint propagation makes each pair of variables consistent. We say that the _arc X<sub>i</sub> → X<sub>j</sub> is **consistent** iff for **every** value of X<sub>i</sub>, there is **some** legal value of X<sub>j</sub>_.

Essentially, we start with a queue of all arcs of our problem (all pair of variables connected by a constraint) and check if they are consistent. If the arc X<sub>i</sub> → X<sub>j</sub> is found to be inconsistent, we remove all values from domain(X<sub>i</sub>) to make the arc consistent. However, once this is done we are no longer guaranteed that arcs of the form X<sub>k</sub> → X<sub>i</sub> are consistent, so we must add these back to the queue.

Arc consistency will detect failures earlier than forward checking and can be run after every assignment.

With n variables, there are at most n choose 2 arcs, or O(n<sup>2</sup>). Checking if an arc is consistent is O(m<sup>2</sup>), and could end up adding an arc back onto the queue up to m times (an arc X<sub>i</sub> → X<sub>j</sub> will be put back onto the queue whenever one of the m values in domain[X<sub>j</sub>] are removed). As such, the running time of the algorithm is O(n<sup>2</sup>m<sup>3</sup>).

**AC-3: An Arc Consistency Algorithm:**

```python
def AC3(csp):
   # (Possibly) update variables in csp to have reduced domains
   arcs = queue(all valid arcs of csp)
   while arcs is not empty:
       (X_i, X_j) = arcs.pop()
       if remove_inconsistent_values(X_i, X_j):
           for X_k in neighbours[X_i]:
               arcs.add((X_k, X_i))

def remove_inconsistent_values(X_i, X_j):
    removed = False
    for vi in domain[X_i]:
        constraint_ij_satisfied = False
        for vj in domain[X_j]:
            if valid_assignment(X_i, X_j, vi, vj):
                constraint_ij_satisfied = True
                break
        if not constraint_ij_satisfied:
            domain[X_i].remove(vi)
            removed = True
    return removed
```


#### References:

https://www.cs.unc.edu/~lazebnik/fall10/lec07_csp.pdf

https://www.cs.unc.edu/~lazebnik/fall10/lec08_csp2.pdf
