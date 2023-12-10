# Another one down—the Survival of the Fittest!

<div style="border:1pt solid; background-color:#030; padding:1ex;margin:0 0 1ex;">
<span style="border:1px solid;display:inline-block;padding:0 1ex; margin-right:1em; background-color:#ccc;color:#000;">Stuck?</span> [Try this one](http://www.codewars.com/kata/remove-the-minimum).</div>

# A Storm at Sea

Jill the adventurer has seen everything, from the highest mountains, to the most dangerous animals. But today she sailed through a hideous storm and shipwrecked. Left with only a damaged life boat and some supplies, she has carefully balanced out the weight not to capsize. But the weight is too much for the small life boat, she has to get rid of some items.

Beginning from one side of the boat, she starts to remove the `n` smallest items and hopes for the best…

# Task

Given an array of integers, remove the `n` smallest. If there are multiple elements with the same value, remove the ones with a lower index first. If `n` is greater than the length of the array/list, return an empty list/array. If `n` is zero or less, return the original array/list.

Don't change the order of the elements that are left.

### Examples

```javascript
removeSmallest (-10) [1,2,3,4,5] = [1,2,3,4,5]
removeSmallest 0 [1,2,3,4,5] = [1,2,3,4,5]
removeSmallest 2 [5,3,2,1,4] = [5,3,4]
removeSmallest 3 [5,3,2,1,4] = [5,4]
removeSmallest 3 [1,2,3,4,5] = [4,5]
removeSmallest 5 [1,2,3,4,5] = []
removeSmallest 9 [1,2,3,4,5] = []

removeSmallest 2 [1,2,1,2,1] = [2,2,1]
```
```coffeescript
removeSmallest (-10) [1,2,3,4,5] = [1,2,3,4,5]
removeSmallest 0 [1,2,3,4,5] = [1,2,3,4,5]
removeSmallest 2 [5,3,2,1,4] = [5,3,4]
removeSmallest 3 [5,3,2,1,4] = [5,4]
removeSmallest 3 [1,2,3,4,5] = [4,5]
removeSmallest 5 [1,2,3,4,5] = []
removeSmallest 9 [1,2,3,4,5] = []

removeSmallest 2 [1,2,1,2,1] = [2,2,1]
```
```haskell
removeSmallest (-10) [1,2,3,4,5] = [1,2,3,4,5]
removeSmallest 0 [1,2,3,4,5] = [1,2,3,4,5]
removeSmallest 2 [5,3,2,1,4] = [5,3,4]
removeSmallest 3 [5,3,2,1,4] = [5,4]
removeSmallest 3 [1,2,3,4,5] = [4,5]
removeSmallest 5 [1,2,3,4,5] = []
removeSmallest 9 [1,2,3,4,5] = []

removeSmallest 2 [1,2,1,2,1] = [2,2,1]
```
```python
remove_smallest ((-10), [1,2,3,4,5]) = [1,2,3,4,5]
remove_smallest (0, [1,2,3,4,5]) = [1,2,3,4,5]
remove_smallest (2, [5,3,2,1,4]) = [5,3,4]
remove_smallest (3, [5,3,2,1,4]) = [5,4]
remove_smallest (3, [1,2,3,4,5]) = [4,5]
remove_smallest (5, [1,2,3,4,5]) = []
remove_smallest (9, [1,2,3,4,5]) = []

remove_smallest (2, [1,2,1,2,1]) = [2,2,1]
```
```ruby
remove_smallest((-10), [1,2,3,4,5]) = [1,2,3,4,5]
remove_smallest(0, [1,2,3,4,5]) = [1,2,3,4,5]
remove_smallest(2, [5,3,2,1,4]) = [5,3,4]
remove_smallest(3, [5,3,2,1,4]) = [5,4]
remove_smallest(3, [1,2,3,4,5]) = [4,5]
remove_smallest(5, [1,2,3,4,5]) = []
remove_smallest(9, [1,2,3,4,5]) = []

remove_smallest(2, [1,2,1,2,1]) = [2,2,1]
```


[another-one-down-the-survival-of-the-fittest](https://www.codewars.com/kata/563ce9b8b91d25a5750000b6)