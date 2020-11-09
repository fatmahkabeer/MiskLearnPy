#%%Write a program that outputs the string representation of numbers from 1 to n.
#But for multiples of three it should output “Fizz”
#instead of the number and for the multiples of five output “Buzz.”
#For numbers which are multiples of both three and five output “FizzBuzz.”


def FizzBuzz(x):
    if (x % 3 == 0) & (x % 5 == 0):
        print('FizzBuzz')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 3 == 0:
        print('Fizz')


FizzBuzz(3)


# %% The Fibonacci sequence starts with a one or a zero,
# followed by a one, and proceeds based on the rule that each number
# is equal to the sum of the preceding two numbers,
# e.g. 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, …
# We can generalize this so that the sum of the preceding n numbers form the next term.
#  e.g. with n=3, 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, …
#Write a function that takes two inputs: n and m,
# and returns m values from an n-Fibonacci sequence.

def Fibonacci (x):
    if x <= 0:
        print("unvalid input")
    elif x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        return Fibonacci(x-1) + Fibonacci(x-2)


Fibonacci(9)
# %%
