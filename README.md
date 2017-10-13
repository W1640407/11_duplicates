# Anti-Duplicator

Search duplicate files in define folder and its subfolders.  
Duplicates are files which names and sizes are equal

#### Run script:
```
python duplicates.py <filename>
```
where  `<filename>` - file name

#### Output:
List of all duplicate files with relative path and size in kb sorted in asc order

#### Run script example:
```
python duplicates.py test
```
#### Output example:
```
Following duplicates found:
File: test\a\a.txt with size: 0.33 kb
File: test\b\a.txt with size: 0.33 kb
File: test\a\b.txt with size: 0.33 kb
File: test\b\b.txt with size: 0.33 kb
File: test\c.txt with size: 0.06 kb
File: test\a\c.txt with size: 0.06 kb
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
