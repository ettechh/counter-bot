import os

# Read the current counter
if os.path.exists("counter.txt"):
    with open("counter.txt", "r") as f:
        try:
            count = int(f.read().strip())
        except ValueError:
            count = 0
else:
    count = 0

# Increment the counter
count += 1

# Write it back to the file
with open("counter.txt", "w") as f:
    f.write(str(count))
