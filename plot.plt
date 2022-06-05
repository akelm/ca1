set term x11
set output
set xlabel "Iteration #"
set ylabel "cumulated payoff"
set title 'The cumulated payoff'
plot "results.txt" using 1:4 with points pt 7
pause -1 "Hit any key to continue"