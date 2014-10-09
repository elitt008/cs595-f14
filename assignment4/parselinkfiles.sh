#!/bin/bash
echo -e "digraph G {" > linkgraph.dot
echo -e "graph [overlap=false];" >> linkgraph.dot
ls -1 ./URIlinks/ | sed 1d | while read file
do
   basehash=`head -2 "./URIlinks/"$file | tail -1 | md5sum | tr -d " -"`
   base=`head -2 "./URIlinks/"$file | tail -1 | awk -F/ '{print $3}'`
   baseh=`echo $basehash | sed -r 's/.{26}$//'`
   base=$base"/"$baseh
   #echo "base: "$base
   count=0
   echo "\""$base"\""" [color=\"red\",style=\"filled\"];" >> linkgraph.dot
   sed 1,3d "./URIlinks/"$file | while read line
   do
     # echo "\""$base"\""" [color=\"red\",style=\"filled\"];"
      if [ $count -lt 25 ];then
         nodehash=`echo $line | md5sum | tr -d " -"`
         node=`echo $line | awk -F/ '{print $3}'`
         nodeh=`echo $nodehash | sed -r 's/.{26}$//'`
         node=$node"/"$nodeh
         #echo "node: "$node
         echo "\""$base"\" -> \""$node"\";" >> linkgraph.dot 
         #echo "\""$base"\" -> \""$line"\";" >> linkgraph.dot 
         let 'count = count + 1'
      fi
   done 
done
echo "}" >> linkgraph.dot  
