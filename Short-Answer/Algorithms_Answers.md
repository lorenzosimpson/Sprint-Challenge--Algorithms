#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    linear time  O(n)- the while loop runs n times, meaning the number of loops increases proportionally compared to n

b)  quadratic time O(n^2) because the while loop has to run once for every jumber from 1 to j


c)
    linear time - even though the function is recursive, it will run for as many times as n, subtracting 1 from each time. But each time the function returns a result, a constant is added to the result, which doesn't increase the number of operations

## Exercise II

    - Since there's no indication of where f needs to lie in relation to n, we can assume f just has to be between 0 and n
    - egg breaks at f or higher
    - egg doesn't break at lower than f
    - f can just be n, because we can assume it won't break at any floor lower than the building
    this means no matter how tall the building, there will only be one floor (the top one) where the egg will break

    f = n 

    the time complexity is O(1) because no matter how high the building is, f is just equal to n


