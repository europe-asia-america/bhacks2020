#! /usr/bin/zsh

export TASKRC=$(mktemp)
export TASKDATA=$(mktemp -d)
echo 'uda.priority.type=numeric' >> $TASKRC
echo 'uda.priority.default=1.0' >> $TASKRC
make
