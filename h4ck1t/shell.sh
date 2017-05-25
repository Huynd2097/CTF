#!/bin/sh
a=56
until [ $a -lt 1 ]
do
    cmd="tar -xzf $a"
	$cmd
	cmd="unzip $a"
	$cmd
	cmd="unrar e $a"
	$cmd
    cmd="mv work_folder/* ."
    $cmd
    a=`expr $a - 1`
done
