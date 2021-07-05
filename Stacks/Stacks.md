# Stacks

Stacks are a linear data structure in python that operate using a Last In/First Out basis. They're similar to a stack of plates in a cupboard, the last plate you stack on top, is the first plate you grab when you open up the cupboard.

# How do stacks work?
Let's continue with our plate analogy from before. If we have a place in the cupboard to stack our plates, we would start stacking plates from the bottom. This action is called a **push** operation. While it might be logical for us to think that we're adding new items to the top of the stack, in Python, we say that we're adding it to the **back** of the stack.

When we remove a plate from the stack to use it, we call this a **pop** operation. Take note that we **push** and **pop** from the back of the stack. Generally, removing from the middle isn't done (you wouldn't do this to a stack of plates either, would you?).

Because of this, the first plate (the one at the **front**) won't be used for a while. 

![](Stacks/platestack.PNG)

While this might seem weird at first, let's look at one of the best examples of a stack: the undo stack.

## The "Undo" Stack
Without realizing it, you use stacks almost every day that you use a computer! If you've ever used the "undo" functionality of a editor or word processor, you've made use of a stack!

In order to understand, let's break it down a bit.

Consider the phrase "Jenny went to the market to buy apples". If we assume that each word is a plate on our stack, the stack would look as follows:

![](Stacks/undostack1.png)

If we then used the **pop()** operation three times, then the stack would look like this:

![](Stacks/undostack2.png)

Notice how we removed the top most three "plates", and the back of the stack became the word "market".

Finally, let's add more words using the **push()** operation. We'll add "and", "bought", and "pears". Now our stack looks like this:

![](Stacks/undostack3.png)

Since the stack is maintaining a history of what we typed, we know that we're going to get the commands in the order that we entered them in. Notice that the 5 commands at the start stayed the same throughout all three examples. If we pressed the undo button enough times, those would eventually be removed.

Stacks are useful for when we need to maintain a history, and perform operations backwards.

# Stack Performance
Recall back to what we learned in the introduction about Big O notation. In order to test the efficiency of our algorithms, we assign them a notation. How do stacks fit in this? Let's take a look at the following table:


|Common Stack Operation|Description|Python Code|Performance|
|----------------------|-----------|-----------|-----------|
|push(value)|	Adds "value" to the **back** of the stack.|	`my_stack.append(value)`|	O(1) |
|pop()|	Removes and returns the item from the **back** of the stack.|	`value = my_stack.pop()`|	O(1)|
|size()|	Return the size of the stack.|	`length = len(my_stack)`|	O(1)|
|empty()|	Returns true if the length of the stack is zero.|	`if len(my_stack) == 0`|	O(1)|

Each of these operations is O(1) notation, meaning that it takes a consistant time to perform the operation, and doesn't change with the size of the data.
>Something very important to note, is that ***there is no .push() function in python***! Instead we use **.append(value)**.

# Practice Example
Let's start with a simple example. 

I will provide you some code with .append() and .pop() operations. Using your knowledge, you must figure out the state of the stack when the code finishes. 
`Hint: write down the stack on a piece of paper!`


```python
stack = []
stack.append("9")
stack.append("8")
stack.append("7")
stack.pop()
stack.pop()
stack.append("apple")
stack.pop()
stack.append("72")
stack.append("85")
stack.append("fruit")
stack.pop()
stack.pop()
stack.append("87")
stack.append("92")
stack.append("banana")
stack.pop()
stack.pop()
print(stack)
```
[Solution](Stacks/stackexample.py)

# Prove Example
Requirements:
* Allow the user to input a phrase
* Reverse the letters in the phrase using a stack
* Print out the original phrase, and the reversed prase:

Example run:
```
Please enter a phrase: The racecar zooms into the sunset

The phrase you entered was: The racecar zooms into the sunset
The reversed phrase is: tesnus eht otni smooz racecar ehT
```

Have fun with this!
[Solution](Stacks/stackprovesolution.py)
