# Sets
Like lists, and tuples, sets are one of the 4 ways to store collections of data in Python. At first glance, one might not know when to use a set over a list or a tuple - so let's remedy that by going over the specific characteristics of the set.

# What are the characteristics of a Set?
Sets have 3 main characteristics:
* Fast performance for adding, removing, and membership tests
* No duplicate information
* The set does not keep values in a specific order, unlike lists and tuples.

So what does this mean for us? Well, sets have use cases that lists and tuples can't cover, such as:
* Finding the unique values in the list
* Providing quick access to unique results
* Performing mathematical set operations such as finding the intersection (which values are the same in two sets) and the union (show all the unique values in both sets)

# So wait, what's this about performance?
Remember when we discussed what Big O notation was in the introduction? Using the unique characteristics of the set, we can make data that is very efficient to search through, by means of a handy thing called **hashing**. By using hashing, we are able to add, remove, and test for membership in O(1) time, instead of O(n).

Let's look at a few examples to help explain this concept.

Suppose we wanted to store all positive numbers from 0 to 9 in a list. How would we get O(1) timing for adding, removing, and membership tests?

If we used the value of the number to find it's number in the list, we might be able to achieve O(1) time.

Let's put this into an expression: `index(n) = n`, where n is the number that we're adding. If we added 7, it would be placed in index 7. If we added 4 it would be placed in idex 4, and so forth. For this to work, we would need the size of our list to be exactly 10.

![](https://github.com/LyrasaurusRose/CSE212Final/blob/8f204c522ab2db1954c98a5f965d75aad48347b2/Sets/setfor1digitnumbers.PNG)

The above shows several numbers added to the list according to the rule `index(n) = n`. In order to determine if a number existed in the list we would only need to use the formula to look up the index. This would result in O(1) perfomance.

We call this a `sparse list` because it's not guranteed to be filled up from the left to the right. Items can be inserted in any order, but there is only one spot for each item. They must be unique.

We call this a set.

# Going further with hashing
The above was quite a simple example, but it has some major flaws that come to mind. First, what happens if we have to store REALLY BIG numbers, such as numbers that are in the millions. Using our current formula, that would take a really big list, too big to be probably with memory.

Instead, let's talk about the modulo (%) operator. If we rewrote our expression as `index(n) = n % 10` instead, we would be able to store bigger values. For example, a value of `553,859,873 % 10` would give us an index of `3`. A value of `678,234,652 % 10` would be placed in index `2`.

Let's put these and some other numbers in a table so that we can visualize this:

![](https://github.com/LyrasaurusRose/CSE212Final/blob/8f204c522ab2db1954c98a5f965d75aad48347b2/Sets/setforbignumbers.PNG)

> If we needed to make the list bigger, we would just add to the modulo at the end of the function. For example, our list size is `10` here, so we `% 10`. If it were 20 we would `% 20`, and so forth.

However, you might notice yet another flaw here. What happens if we try to add another number that ends in a 2, 3, 5 or 8? We call that a conflict.

# Solving Conflicts (both peacefully and non-peacefully)
## Open Addressing
Imagine that you're the manager of a hotel. You have 26 rooms on each floor, and you decide that you will give out the key to each room based on the letter of the alphabet that the client's last name starts with (A gets room 1, B room 2, and so on.) 

Mr. Albert comes in and checks his family into the hotel, you smile and give him the key to the first room, since his last name starts with A. 

However, a few hours later, Ms. August tries to check into the hotel. You start to panic. You've already given out the A key today. So, in an attempt to accommodate her, you put her into the next availible room on the list. The "G" room. Easy enough. But now, when Mr. Green tries to check in, you have to keep looking for the next avalible room. It starts getting messy fast.

This is called `open addressing` if we use our hashing function and find that the spot is already occupied, we look to the right one spot at a time until we find an open spot. However, like we can see from our hotel story, this can quickly result in rapidly growing clusters of conflicts.

## Chaining
Let's return to our hotel story. You may have been shouting at your story-self "But you have more floors! Just move them up a floor!". You were thinking of chaining!

Let's rewind time, and try this scenario again. 

Mr. Albert comes in and checks his family into the hotel, you smile and give him the key to the first room, since his last name starts with A. The same as before.

This time however, when Ms. August tries to check in a few hours later, you hand her the "A" key for the second floor.

If later, Mr. Abode were to check into the hotel, you would give him the "A" key on the third floor.

As mentioned above, this is called `chaining`. It allows us to create lists of values that occupy the same slot of the set.

## The problem
However, with both of these methods we have an adverse effect on our goal of O(1) timing. If we have to search through several positions to find a value, or loop through a list to find a value, we may eventually get to O(n) time if the amount of conflicts is too high.

In order to avoid this, we would have to increase the size of our sparsed list, and reposition all of the values by running the hashing function again with the increased sparsed list size.

# Sets in Python
Now that we've gotten all of the performance out of the way, let's discuss how we actually make a set in Python.

Let's look at the following table:

|Common Set Operation|Description|Python Code|Performance|
|----------------------|-----------|-----------|-----------|
|add(value)|Adds "value" to the set|`my_set.add(value)`|	O(1) - Performance of hashing the value (assuming good conflict resolution) |
|remove(value)|	Removes the "value" from the set|`my_set.remove(value)`|O(1) - Performance of hashing the value (assuming good conflict resolution)|
|member(value)|	Determines if "value" is in the set|`if value in my_set:`|O(1) - Performance of hashing the value (assuming good conflict resolution)|
|size()|Returns the number of items in the set|`length = len(my_set)`|	O(1)|
|union()|Returns every unique value in both sets|`set3 = set1 & set2`|	O(n)|
|intersection()|Returns values that are the same in both sets |`set3 = set1 \| set2`|	O(1)|

# Practice Example
Let's start with a simple example.

[Solution](setsexample.py)

# Prove Example

[Solution](setsprovesolution.py)
