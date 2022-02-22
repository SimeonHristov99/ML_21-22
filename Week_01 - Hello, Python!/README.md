# Plan of attack

- [ ] Play Kahoot :)
- [ ] Set up Google Colaboratory
- [ ] Complete `Week_01_Hello,_Python.ipynb`
- [ ] Submit your work on the `For home` section by sending an `.ipynb` file or a link to a GitHub repository with such a file to the email address: *s.e.hristov99@gmail.com*. **MAKE SURE TO PUT THE FOLLOWING SUBJECT**: [ML] *your faculty number* *your name*. For example: Subject: [ML] 12345 Simeon Hristov

# For home

## Task 1

Complete the body of the following function according to its docstring. Use a built-in function.

```python
def round_to_two_places(num):
    """Return the given number rounded to two decimal places. 
    
    >>> round_to_two_places(3.14159)
    3.14
    """
    # Replace this body with your own code.
    # "pass" is a keyword that does literally nothing. It is used as a placeholder
    # because after we begin a code block, Python requires at least one line of code
    pass
```

## Task 2

Each cell below contains some commented buggy code. For each line:

  1. Read the code and predict write what the bug is.
  2. Uncomment the code and run it to see what happens. (Tip: You can highlight several lines and press ctrl+/ to toggle commenting.)
  3. Fix the code (so that it accomplishes its intended purpose without throwing an exception)

```python
# ruound_to_two_places(9.9999)
```

```python
# x = -10
# y = 5
# smallest_abs = min(abs(x, y))
# smallest_abs # Should store the variable with the smaller absolute value, i.e. 5.
```

```python
# def f(x):
#     y = abs(x)
# return y
```

## Task 3

Many programming languages have `sign` available as a built-in function. Python doesn't, but we can define our own!

In the cell below, define **TWO** functions `is_neg_if` and `is_neg_ternary` that take a number and return `-1` if it's negative, `1` if it's positive, and `0` if it's 0. The first one should use if-then-else syntax while the second - ternary operators.

Test cases:

```python
is_neg_if(-3) => -1
is_neg_ternary(-3) => -1
```

## Task 4

Modify the definition in the cell below to correct the grammar of our print statement. (If there's only one candy, we should use the singular "candy" instead of the plural "candies"). Use f-strings.

```python
def to_smash(total_candies):
    """Return the number of leftover candies that must be smashed after distributing
    the given number of candies evenly between 3 friends.
    
    >>> to_smash(91)
    Splitting 91 candies
    1

    >>> to_smash(1)
    Splitting 1 candy
    0
    """
    print("Splitting total_candies candies")
    return total_candies % 3

to_smash(91)
to_smash(1)
```

## Task 5

The boolean variables ketchup, mustard and onion represent whether a customer wants a particular topping on their hot dog. We want to implement a number of boolean functions that correspond to some yes-or-no questions about the customer's order. For example:

```python
def onionless(ketchup, mustard, onion):
    """Return whether the customer doesn't want onions.
    """
    pass
```

For the next three functions, fill in the body to match the English description in the docstring.

```python
def wants_all_toppings(ketchup, mustard, onion):
    """Return whether the customer wants "the works" (all 3 toppings)
    """
    pass
```

```python
def wants_plain_hotdog(ketchup, mustard, onion):
  """Return whether the customer wants a plain hot dog with no toppings.
  """
  pass
```

```python
def exactly_one_sauce(ketchup, mustard, onion):
    """Return whether the customer wants either ketchup or mustard, but not both.
    (You may be familiar with this operation under the name "exclusive or")
    """
    pass
```

## Task 6

We’ve seen that calling `bool()` on an integer returns `False` if it’s equal to 0 and `True` otherwise. What happens if we call `int()` on a bool? Try it out in the notebook cell below.

Can you take advantage of this to write a succinct function that corresponds to the English sentence "does the customer want exactly one topping?"?

```python
def exactly_one_topping(ketchup, mustard, onion):
  """Return whether the customer wants exactly one of the three available toppings
  on their hot dog.
  """
  pass
```

## Task 7

Complete the function according to the docstring.

```python
def select_second(l):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    pass
```

## Task 8

You are analyzing sports teams. Members of each team are stored in a list. The Coach is the first name in the list, the captain is the second name in the list, and other players are listed after that. These lists are stored in another list, which starts with the best team and proceeds through the list to the worst team last.  Complete the function below to select the **captain** of the worst team.

```python
def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    pass
```

## Task 9

The next iteration of Mario Kart will feature an extra-infuriating new item, the *Purple Shell*. When used, it warps the last place racer into first place and the first place racer into last place. Complete the function below to implement the Purple Shell's effect.

> **The solution should be on one line!**

```python
def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    pass
```

## Task 10

We're using lists to record people who attended our party and what order they arrived in. For example, the following list represents a party with 7 guests, in which Adela showed up first and Ford was the last to arrive:

```python
arrivals = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']
```

A guest is considered `fashionably late` if they arrived after at least half of the party's guests. However, they must not be the very last guest. In the above example, Mona and Gilbert are the only guests who were fashionably late.

Complete the function below which takes a list of party attendees as well as a person, and tells us whether that person is fashionably late.

```python
def is_fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    pass
```

## Task 11

The following program has a bug. Try to identify the bug and fix it.

```python
def has_lucky_number(nums):
    """Return whether the given list of numbers is lucky. A lucky list contains
    at least one number divisible by 7.
    """
    for num in nums:
        if num % 7 == 0:
            return True
        else:
            return False
```

## Task 12

Python has some libraries (like numpy and pandas) that compare each element of a list to a number (i.e. do an 'element-wise' comparison) and return a list of booleans like [False, False, True, True].

Implement a function that reproduces this behaviour, returning a list of booleans corresponding to whether the corresponding element is greater than n.

```python
def elementwise_greater_than(l, thresh):
  """Return a list with the same length as l, where the value at index i is 
  True if l[i] is greater than thresh, and False otherwise.
  
  >>> elementwise_greater_than([1, 2, 3, 4], 2)
  [False, False, True, True]
  """
  pass
```

## Task 13

Complete the body of the function below according to its docstring.

```python
def menu_is_boring(meals):
  """Given a list of meals served over some period of time, return True if the
  same meal has ever been served two days in a row, and False otherwise.
  """
  pass
```

## Task 14

There is a saying that "Data scientists spend 80% of their time cleaning data, and 20% of their time complaining about cleaning data." Let's see if you can write a function to help clean US zip code data. Given a string, it should return whether or not that string represents a valid zip code. For our purposes, a valid zip code is any string consisting of exactly 5 digits.

HINT: `str` has a method that will be useful here. Use `help(str)` to review a list of string methods.

```python
def is_valid_zip(zip_code):
  """
  Returns whether the input string is a valid (5 digit) zip code

  Examples:
  >>> is_valid_zip('1234')
  False

  >>> is_valid_zip('12345')
  True
  """
  pass
```

## Task 15

A researcher has gathered thousands of news articles. But she wants to focus her attention on articles including a specific word. Complete the function below to help her filter her list of articles.

Your function should meet the following criteria:

- Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.” 
- She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.” would be included when the keyword is “closed”
- Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is “closed”. But you can assume there are no other types of punctuation.

```python
def word_search(doc_list, keyword):
  """
  Takes a list of documents (each document is a string) and a keyword. 
  Returns list of the index values into the original list for all documents 
  containing the keyword.

  Example:
  >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
  >>> word_search(doc_list, 'casino')
  [0]
  """
  pass
```

## Task 16

Now the researcher wants to supply multiple keywords to search for. Complete the function below to help her.

(You're encouraged to use the `word_search` function you just wrote when implementing this function. Reusing code in this way makes your programs more robust and readable - and it saves typing!)

```python
def multi_word_search(doc_list, keywords):
  """
  Takes list of documents (each document is a string) and a list of keywords.  
  Returns a dictionary where each key is a keyword, and the value is a list of indices
  (from doc_list) of the documents containing that keyword

  >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
  >>> keywords = ['casino', 'they']
  >>> multi_word_search(doc_list, keywords)
  {'casino': [0, 1], 'they': [1]}
  """
  pass
```

## Task 17

Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.

Ex: Given the following strings...

```text
"level", return true
"algorithm", return false
"A man, a plan, a canal: Panama.", return true
```

## Task 18

Implement a function named `generateRange(min, max, step)`, which takes three arguments and generates a range of integers from min to max, with the step. The first integer is the minimum value, the second is the maximum of the range and the third is the step. `min` will always be less than max.

```python
generate_range(2, 10, 2) # should return list of [2,4,6,8,10]
generate_range(1, 10, 3) # should return list of [1,4,7,10]
generate_range(2, 10, 2) # should return array of [2, 4, 6, 8, 10]
generate_range(1, 10, 3) # should return array of [1, 4, 7, 10]
```

## Task 19

Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

Ex: Given the following strings...

```text
"LR", return true
"URURD", return false
"RUULLDRD", return true
```

## Task 20

Given a array of numbers representing the stock prices of a company in chronological order, write a function that calculates the maximum profit you could have made from buying and selling that stock once. You must buy before you can sell it.

For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars.

## Task 21

Let us begin with an example:

Take a number: `56789`. Rotate left, you get `67895`.

Keep the first digit in place and rotate left the other digits: `68957`.

Keep the first two digits in place and rotate the other ones: `68579`.

Keep the first three digits and rotate left the rest: `68597`. Now it is over since keeping the first four it remains only one digit which rotated is itself.

You have the following sequence of numbers:

`56789 -> 67895 -> 68957 -> 68579 -> 68597`

and you must return the greatest: `68957`.

Write function which given a positive integer `n` returns the maximum number you got doing rotations similar to the above example.
