## Python String Methods

### capitalize()
Converts the first character to upper case.

The ```capitalize()``` method returns a string where the first character is upper case, and the rest is lower case.

```python
txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x) # Hello, and welcome to my world.
```

### casefold()
The ```casefold()``` method returns a string where all the characters are lower case.

This method is similar to the ```lower()``` method, 
but the ```casefold()``` method is stronger, more aggressive, 
meaning that it will convert more characters into lower case, 
and will find more matches when comparing two strings and both 
are converted using the ```casefold()``` method.

```python
txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x) # hello, and welcome to my world!
```