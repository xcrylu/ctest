#!/bin/bash

# This script creates a temporary file, writes some data to it, and then deletes it.
(( line = $1 ))
(( col = $2 ))
(( max = $3 ))
# (( n = line * col ))
echo "$line $col"

for(( i = 0 ; i < line  ; i++ )) ;   do
    for(( j = 0 ; j < col ; j++ )) ; do       
        echo -n "$((RANDOM % max+1 )) " 
    done
    echo  ""
   
done
echo ""