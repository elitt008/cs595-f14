#!/bin/bash
count=1
sort -nk2 friends.dat | while read line
do
   numf=`echo $line | awk '{print $2}'`
   pers=`echo $line | awk '{print $1}'`
   if [ $pers != "user" ];then
      echo $count" "$numf >> formatted.dat
   else
      echo $pers" "$numf >> formatted.dat
   fi 
   let 'count= count + 1'
done
