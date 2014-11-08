#!/bin/bash
echo -e "\"links\": ["
type=0
while read line
do
   if [ "x`echo $line | grep "<edge"`" != "x" ];then 
   	type=1
   	source=`echo $line | awk '{print $2}' | awk -F\" '{print $2}' | tr -d 'n'`
   	target=`echo $line | awk '{print $3}' | awk -F\" '{print $2}' | tr -d 'n'`
      echo -n "{\"source\": $source," "\"target\": $target, \"weight\": "
  elif [ $type -eq 1 ];then
   	weight=`echo $line | awk -F\> '{print $2}' | tr -d "</data"`
      echo "$weight },"
      type=0
   fi
done < karate.GraphML 

echo -e "]\n}"
