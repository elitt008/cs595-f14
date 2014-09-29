#!/bin/bash
#read -rep "Enter memento file> " memfile
#read -rep "Enter creation Date file>" crefile
#read -rep "Enter file for output>" outfile

memfile="mementos.dat"
crefile="creation_date.dat"
outfile="creation_vs_mementos.dat"
consolidated="consolidated_data.dat"
while read line
do
   mementos=`echo $line | awk -F, '{print $1}'`
   address=`echo $line | sed 's/.*,h/h/'`
   date=`grep $address$ $crefile | awk -F":;:;" '{print $1}'`

   if [ $mementos -gt 0 ];then
      #address=`echo $line | sed 's/.*,h/h/'`
      #date=`grep $address$ $crefile | awk -F":;:;" '{print $1}'`
      hours=`echo $date | ./convertTime.py`
      #echo $hours
      #echo $date" "$mementos" "$address 
      #echo $date" "$mementos" "$address >> $outfile
      echo $hours" "$mementos" "$address >> $outfile
   fi

   echo $date" "$mementos" "$address >> $consolidated
done < $memfile
