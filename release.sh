#! /bin/bash

export TASKRC=".taskrc"
mkdir ".taskdb"
export TASKDATA=".taskdb"
echo 'uda.priority.type=numeric' >> $TASKRC
echo 'uda.priority.default=1.0' >> $TASKRC
sh demo/tasks.sh
