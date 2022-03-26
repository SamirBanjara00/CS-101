# Accepts stake (int), goal (int), and trials (int) as command-line arguments; runs trials
# experiments (dollar bets) that start with stake dollars and terminate on 0 dollars or goal; and
# writes the percentage of wins and the average number of bets per experiment to standard output.

import stdio
import sys
import stdrandom

stake = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])
bets = 0
wins = 0
for t in range(trials):
    cash = stake
    while 0 < cash < goal:
        bets += 1
        if stdrandom.bernoulli():
            cash += 1
        else:
            cash -= 1
    if cash == goal:
        wins += 1
stdio.writeln(str(100 * wins // trials) + '% wins')
stdio.writeln('Avg # bets: ' + str(bets // trials))
