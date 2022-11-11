#!/usr/bin/env bash
#script that checks for file information

file="school"
if [ -e $file ]
then
    echo "school file exists"
    if [ ! -s $file ]
        then 
            echo "school file is empty"
    else
        echo "school file is not empty"
    fi

    if [ -f $file ]
        then
            echo "school is a regular file"
    fi

else
    echo "school file does not exist"
fi