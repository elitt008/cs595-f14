#!/bin/bash
loc=`pwd`
cd /home/terminal1/school/cs495/CarbonDate/CarbonDate/
while read line           
do
   address=`echo $line | sed 's/.*,h/h/'`
   python ./local.py $address >> $loc"/temp"  
done < $loc"/mementos.dat"
cd $loc
