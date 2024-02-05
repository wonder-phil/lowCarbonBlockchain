import os
import random

# Get the number of heads needed in a row from the environment variable
num_flips = int(os.environ.get("heads", 10))

# Simulate the coin flips
heads = 0
total_flips = 0
while(heads != num_flips):
    if random.random() < 0.5:
        heads += 1
        total_flips+=1
    else:
        heads = 0
        total_flips+=1

# Print the result
print(f"Number of flips needed: {total_flips}")
