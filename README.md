# SecretSanta

This is my solution to the Secret Santa’s challenge proposed by Debora Cornetta (@deboracornetta).

The challenge was to create a program to pick a secret Santa for everybody in a list. You need to make sure no one was assigned to themselves and that everybody got a secret Santa. The interesting part about the challenge was that Debora suggested solving it in one cycle. 

Soon it became clear that I should start by shuffling the names in the list. This way we could assign the current name in the list to the next name and so on, and the result would be different every time we run the program. Also, I wanted to save the result as a key-value pair in a dictionary.

Now, if you ever tried to assign something in a current index to the next index, you know you would eventually get an Index Error. One way to deal with this is implementing a try and except, where you manually assign the last index to the first one, and avoid getting the error.

However, since the beginning I was sure I had to solve a problem involving cycling through elements before I knew what a try and except was. 

And then suddenly it came to me: Caesar Cypher!

The Caesar Cypher algotithm uses the modulo (%) operator to circle through the indices of the letters. If ‘A’ becomes ‘B’, ‘Z’ will become ‘A’.
This is how it works:
The modulo operator determines the remainder of a division operation.
You’ll need the length of your list to use the module, it will be your divisor.
For this example, let’s assume our list have four friends.
When the dividend is smaller than the divisor, the modulo will be equal to the dividend.
When the dividend is the same as the divisor, the result is 0.

Let’s have a look at this in the shell:
```
>>> 0 % 4
0
>>> 1 % 4
1
>>> 2 % 4
2
>>> 3 % 4
3
>>> 4 % 4
0
```
As we start counting from 0, the name at index 0 will be assigned the name at index (0 + 1) % 4, which is the element in index 1. The for loop keeps assigning the current name to the name at the next index. When your next index is 4 (that’s the length of our example list) you get 0 as a result of the modulo operation. We won’t get an Index error, because when i = 3 (the last element) it will be assigned the item in index (4 % 4), and that is the index 0!

I completed the challenge with two methods to print the dictionary. The first prints all the names assignments, which is good for debugging.
The other method prints only the result for the given name.
