#!/usr/bin/env python3

import random

trainingOptions = ['sit', 'down', 'stay', 'stand', 'recall', 'heel', 'leave it',
'place', 'retrievals', 'counterbalance', 'FMP', 'behavior interruption', 'HR alerts',
'DPT', 'lap', 'go push']
focusCategory = ['duration', 'distance', 'distraction']

#chooses a behavior to work on from the list
command = random.choice(trainingOptions)
#chooses a number between 1 and 30 - number of repetitions to perform
reps = random.randint(1,30)
#chooses something to focus on
focus = random.choice(focusCategory)
print('Work on ' + command + ' for ' + str(reps) + ' repetitions and add ' + focus)
