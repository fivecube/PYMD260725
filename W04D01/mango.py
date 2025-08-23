# Creating Modules
# Package structure
# pip and package management
# Virtual environments
# Important standard library Modules
# Creating and distributing packages
# Documentation and docstrings

from hospitality import moduleA, moduleB

import math

from datetime import datetime, timedelta

import pytz

msg1 = moduleA.say_hello("Mohit Chouhan")

print(msg1)

result_add = math_ops.add(10, 5)

print(f"Addition: {result_add}")

result_subtract = math_ops.subtract(10, 5)

print(f"Subtraction: {result_subtract}")

msg2 = moduleA.say_goodbye("Mohit Chouhan")

print(msg2)

output = math.sqrt(16)

print(f"Square root of 16 is: {output}")

now_time = datetime.now()
print(f"Current date and time: {now_time}")

past_time = now_time - timedelta(days=5)
print(f"Date and time 5 days ago: {past_time}")

past_time_2 = now_time - timedelta(hours=5)
print(f"Date and time 5 hours ago: {past_time_2}")

future_time = now_time + timedelta(days=10)
print(f"Date and time 10 days from now: {future_time}")

asia_timezone = pytz.timezone('Asia/Kolkata')
asia_time = datetime.now(asia_timezone)
print(f"Current date and time in Asia/Kolkata: {asia_time}")

europe_timezone = pytz.timezone('Europe/London')
europe_time = datetime.now(europe_timezone)
print(f"Current date and time in Europe/London: {europe_time}")


# Assignment for learning Python Modules
# 1. Create a module named `string_ops.py` with functions to
#    perform string operations
#    like `to_uppercase`, `to_lowercase`, and `reverse_string`.
#    Then, create a script
#    that imports this module and demonstrates the use of these functions.

# 10:07
