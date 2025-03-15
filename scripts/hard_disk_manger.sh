#!/usr/bin/env bash

total_size=$(df | awk 'NR>1 {print $2}')
used=$(df | awk 'NR>1 {print $3}')
available=$(df | awk 'NR>1 {print $4}')
# echo "Total_size: $total_size"
declare -i a=0
for x in $total_size;do
    declare -i x=$x
    a+=$x
done
# echo "Total space: $a"
declare -i b=0
for y in $used;do
    declare -i y=$y
    b+=$y
done
# echo "Used: $b"
declare -i c=0
for z in $available;do
    declare -i z=$z
    c+=$z
done
# echo "Available space: $c"
declare -i t=$b+$c
percent=$(echo "scale=2; ($c / $t) * 100" | bc)
# echo "$percent"
if (( $(echo "$percent > 90" | bc -l) )); then
    echo "More than 90% of the hard disk is used!"
else
    echo "less than 90% of the hard disk is used!"
fi