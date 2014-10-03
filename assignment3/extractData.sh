#read -rep "Enter word to search> " term
term="computer"
allpages=40000000000
pageresults=840000000
IDF=`echo "scale=4;$allpages/$pageresults" | bc`
logIDF=`echo "scale=4;l($IDF)/l(2)" | bc -l`

echo -e "TFIDF\t\tTF   \t\tIDF  \t\tURI  " > TFDF.dat
echo -e "-----\t\t-----\t\t-----\t\t-----" >> TFDF.dat

grep -ric " $term " ./processedsites/ | grep -v ":0" > temp.dat 
while read line
do
   hashfilep=`echo $line | awk -F: '{print $1}'`
   hashfile=`echo $hashfilep | sed 's/_processed//' | sed 's/.*\///'`
   file=`grep $hashfile ./hash_table.dat | awk '{print $2}'`
   occur=`echo $line | awk -F: '{print $2}'`
   wordc=`wc $hashfilep | awk '{print $2}'`
   normalTF=`echo "scale=4;$occur/$wordc" | bc`
   TFIDF=`echo "scale=4;$logIDF*$normalTF" | bc `
   echo -e $TFIDF"\t\t"$normalTF"\t\t"$logIDF"\t"$file >> temp1 

done < temp.dat 

sort -r temp1 | head -10 >> TFDF.dat
rm temp1 temp.dat 
