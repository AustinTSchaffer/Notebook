---
tags:
  - OMSCS
  - Algorithms
  - Practice
  - Alg-DC
---
# DC.1 - Modified Binary Search
> Design an O(log(n)) algorithm to find the smallest missing natural number in a given sorted array of length _**n**_. The given array only has _**distinct**_ natural numbers. For example, the smallest missing natural number from $A = [3, 4, 5]$ is 1, and from $A = [1, 3, 4, 6]$ is 2.

## Algorithm
For a given array of length $n$, you need to check the element at index $n/2$.

- If $A[n/2]=n/2$, all of the values in $A[1, ..., (n/2)]$ are correct, and therefore the missing number is located in $A[(n/2)+1, ..., n]$.
- The opposite is true if $A[n/2] \ne n/2$

We then take the half the input and recurse, checking the middle index against the middle value. We need to continue this procedure until we find the boundary condition. We can express this boundary condition for a target index $b$ as $(A[b]=b) \wedge (A[b+1] > (b+1)$). Once we find $b$, the smallest missing natural number is $b+1$.

## Non-Pseudocode Algorithm
The above algorithm is precisely defined, but it contains mathematics notation, which the course instructors consider to be tantamount to pseudocode. This section removes that pseudocode and attempts to explain it in a more storytelling fashion.

For given array of length $n$, we need to check the middle element.

1. If the middle value equals its index, then all of the values below that midpoint are equal to their index. Therefore, the first missing value must be above the midpoint of the array. From here, we take only the top half of the array and apply this same procedure.
2. If the middle value is not equal to its index, then we know that all of the values above the midpoint of the array also cannot be equal to their index. Therefore, the midpoint of the array is located at some point after the first missing value of the array. From here, we take only the bottom half of the array and apply this same procedure.

We continue this procedure until there is only one element remaining in our view of the array. We have arrived at one side of a boundary which falls between 2 elements of the array. The value on the left of the boundary is equal to its index. The value on the right of the boundary is not equal to its index. We first determine which of these 2 cases describe the element that we've arrived at, and then take the value to the left of the boundary and add one. That results in the first value which is missing in the array.

In the special case where the boundary falls directly before the first element of the array, the first missing value is 1. In the special case where the boundary falls directly after the last element of the array, the first missing value is the size of the array plus one.

## Correctness
The trick to this algorithm comes from the facts that
1. The array is sorted.
2. The array only contains distinct values.
3. The array only contains natural numbers: 1, 2, 3, ...

In this scheme, each value of $A$ should equal its own index. We need to find the position where that is no longer the case. For a given element, if its index does not equal its value, the only option is for the value to be more than its index.

- If a specific element equals its index, then all of the elements below that element also equal their own index.
- If a specific element is greater than its index, then all of the elements above that element are also greater than their index.

## Runtime Analysis
This procedure is an adaptation of the binary search algorithm, so the runtime is $O(log \space n)$.