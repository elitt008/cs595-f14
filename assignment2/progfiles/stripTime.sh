#!/bin/bash
read -rep "Enter the file to parse> " input
read -rep "Enetr the file to save responses in(will append)> " output
mc=`grep -c "URI" $input`
let 'mc = mc + 1'
gc=1
while [ $gc -lt $mc ];do 
   URI=`grep -m $gc "URI" $input | tail -1 | awk -F\" '{print $4}'`
   Time=`grep -m $gc "Estimated" $input | tail -1 | awk -F\" '{print $4}'`
   if [ "x"$Time == "x" ];then
     # echo -n "Hello "
      Time=`grep -m $gc "Topsy.com" $input | tail -1 | awk -F\" '{print $4}'`
    #  echo $Time #" "$URI 
   fi
   
   echo $Time" :;:; "$URI >> $output
   let 'gc=gc+1'
done; 
