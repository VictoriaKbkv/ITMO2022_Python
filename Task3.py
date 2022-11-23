import math
import statistics
import random

sample = [65, 71, 68, 74, 61, 80, 55, 70, 75, 72]

print(f"Sum: {sum(sample)}")
print(f"Average: {statistics.mean(sample): .2f}")
print(f"Median: {statistics.median(sample): .2f}")
print(f"Standard deviation: {statistics.stdev(sample): .2f}")

print()

random_number = random.randint(1, 100)
print(f"Random number: {random_number}")