#!/bin/bash
echo "Hash Table" > hash_table.dat
while read line           
do
   hashv=`echo -n $line | md5sum | sed 's/ -//'`
   echo -n $hashv >> hash_table.dat
   echo -e "\t"$line >> hash_table.dat 
   wget -O  "./rawsites/"$hashv $line
done < unique_links.dat 

for file in `ls ./rawsites/`
do
 echo "Processing $file"
 lynx -dump -force_html ./rawsites/$file > ./processedsites/$file"_processed"
done

