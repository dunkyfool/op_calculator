# job list (list each job's gm week)
jobs = [5,4,3]
jobs.sort()

# define capability
startweek = 2      # calculate week
queue = 2          # the number of handling jobs per week
duration = 2       # how long to finish the job

# counter
ctr = 0            # counter for queue
idx = 0            # index of job
total_diff = 0     # index
roadmap = []
thisweek = []

for gm in jobs:
    diff = gm - (startweek + duration)
    if diff < 0:   # highlight which job cannot finish before GM
      print 'This job:', idx, ' will not finish on time!'
    total_diff += diff
    thisweek += [gm]
    ctr += 1
    idx += 1
    if ctr % queue == 0:
        ctr = 0
        startweek += 1
        roadmap += [thisweek]
        thisweek = []

if len(thisweek) != 0:
    roadmap += [thisweek]
    thisweek = []

print 'Total remain time:', total_diff
print 'Roadmap:'; print roadmap
