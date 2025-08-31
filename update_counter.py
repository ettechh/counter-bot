import os
import random
import subprocess

# Read current counter value
if os.path.exists("counter.txt"):
    with open("counter.txt", "r") as f:
        try:
            count = int(f.read().strip())
        except ValueError:
            count = 0
else:
    count = 0

# Random number of increments today
num_commits = random.randint(1, 7)
print(f"Making {num_commits} increments today.")

for i in range(num_commits):
    count += 1

    # Write updated counter
    with open("counter.txt", "w") as f:
        f.write(str(count))

    # Stage, commit, and push immediately
    subprocess.run(["git", "add", "counter.txt"], check=True)
    subprocess.run([
        "git", "commit", "-m",
        f"Automated commit {i+1} of {num_commits} (counter: {count})"
    ], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)

