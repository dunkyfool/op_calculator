# job list
jobs = [5,4,3]
jobs.sort()

# define capability
startweek = 2
queue = 2
duration = 2

# counter
ctr = 0
total_diff = 0

for gm in jobs:
    diff = gm - (startweek + duration)
    if diff < 0:
        print gm
    total_diff += diff
    ctr += 1
    if ctr % queue == 0:
        ctr = 0
        startweek += 1

print total_diff
