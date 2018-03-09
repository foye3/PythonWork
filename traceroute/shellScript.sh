
# > writting to a file, >> append to a file
for ((i = 0; i < 300 ; i++))
do
    traceroute 47.88.107.100 >> traceFile
    echo "~~~" >> traceFile
    echo $i
    sleep 300
done
