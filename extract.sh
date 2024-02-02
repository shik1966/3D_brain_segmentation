#!/bin/bash

path='BraTS2021'

cd $path
for i in `ls -1b`; 
do 
    c=`find $i -type f |wc -l`; 
    #echo “$c $i”; 
    cd $i
    `gunzip -- *.gz`
    echo "$i extracted"
    cd ..
done;



