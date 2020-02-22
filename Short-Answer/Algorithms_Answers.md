#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
    linear time  O(n)- the while loop runs n times, meaning the number of loops increases proportionally compared to n

b)  n(logn) because j is in the body of the while loop, it's not affected by the size of n, it's just doubled


c)
    linear time - even though the function is recursive, it will run for as many times as n, subtracting 1 from each time. But each time the function returns a result, a constant is added to the result, which doesn't increase the number of operations

## Exercise II

    - we are trying to solve for f
    - we start to look at the middle floor = n / 2
    - we try to drop the egg
        - if it breaks, we need to go lower, so we go to floor number *half of what we're on*
            (if we started on floor 4, go to floor 2)
        - we do the same thing. drop the egg. if it breaks, go to half of it and go lower. if not, we can afford to go higher
        - go to the floor halfway between the current floor and the height of the building, and try the drop again 
    this is just like a binary search, time complexity of O(logn)



