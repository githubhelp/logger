#!/usr/bin/env gnuplot
set title "Temperature"
set xlabel "Datetime"
set ylabel "Celcius"

set terminal png
set output "/var/www/temp.png"
set datafile separator "|"
set style data lines
set grid
set yrange [0:*]
set xdata time
set timefmt x "%H:%M"
set format x "%H:%M"
plot "< sqlite3 sensors.db \"SELECT time, value from sensors where date = date('now', 'localtime') and name = 'outdoor';\"" using 1:2 title "outdoor", "< sqlite3 sensors.db \"SELECT time, value from sensors where date = date('now', 'localtime') and name = 'indoor';\"" using 1:2 title "indoor"
