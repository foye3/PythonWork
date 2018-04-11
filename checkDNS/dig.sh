# > writting to a file, >> append to a file
for ((i = 0; i < 86400 ; i++))
do
    dig @155.246.149.81 www.google.com +norecurse +short >> digfile1
    echo "#"$i >> digfile1
    dig @155.246.149.81 www.bilibili.com +norecurse +short >> digfile2
    echo "#"$i >> digfile2
    dig @155.246.149.81 www.douban.com +norecurse +short >> digfile3
    echo "#"$i >> digfile3
    echo $i
    sleep 1
done

