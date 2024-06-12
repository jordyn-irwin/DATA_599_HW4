# README

1. This repository was cloned: https://github.com/hadoop-sandbox/hadoop-sandbox.git
   
2. The mapper and reducer from https://github.com/cd-public/merrer/ was used and the mapper was edited.
  
4. I used this mapred command:

```
hdfs dfs -rm -r /user/sandbox/words
mapred streaming \
  -input /user/sandbox/books \
  -output /user/sandbox/words \
  -mapper mapper.py \
  -reducer reducer.py \
  -file scripts/mapper.py \
  -file scripts/reducer.py
```
4. The Word Counter was tested on these books:
   *  https://raw.githubusercontent.com/cd-public/books/main/pg1342.txt
   *  https://raw.githubusercontent.com/cd-public/books/main/pg84.txt
   *  https://raw.githubusercontent.com/cd-public/books/main/pg768.txt
