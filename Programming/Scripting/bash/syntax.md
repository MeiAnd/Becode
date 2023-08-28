# Bash Syntax

## Introduction

It's a good thing to know what a **script** is, it's even better to know how to write one yourself. Hopefully that's exactly what you're going to try here. Follow this [tutorial](https://www.learnshell.org/) (_or others_) on bash scripting then complete the exercises below to ensure fundamental understanding of the syntax. 

Here are some _tips_ to help you out:

* You can append the extension `.sh` to your script for clarity.
* A [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) is needed to indicate to the shell what language to use.
* To make a file executable use [chmod](https://askubuntu.com/questions/229589/how-to-make-a-file-e-g-a-sh-script-executable-so-it-can-be-run-from-a-termi).
* One way to execute your script is to type `./<path to file>`.

> **NOTE**: You can also find more exercises on [Codewars](https://www.codewars.com/)!

## Exercises

### I - prompt user

Write a shell script *prompting* the user for his name, then replying `Hello <name>`.

	#!/bin/bash
	echo Enter your Name:
	read Name
	echo "Hello $Name"


### II - receive arguments

Write a shell script *receiving* a name as *argument*, then replying `Hello <name>`.

	#!/bin/bash
	name=$1
	echo "Hello $name"


### III - path to

Write a shell script receiving a *path* as argument, depending on if it's a file or a directory, display or list its content.

	#!/bin/bash
	
	path=$1
	
	if [ -d $path ] then	
		echo " This is a directory :"
		pwd "$path"
	
	elif [ -f $path ] then
		echo "This is a file"
		cat "$path"

	else
	echo "This isn't a diretory nor file"

	fi

You can complexify the script by only displaying file containing text (ex: `.txt`, `.js`) and returning an error for anything else (ex: `.mp3`, `.pdf`).

### IV - information

Write a shell script to see the current date, time, username, and directory.

	#!/bin/bash
	echo "This is the directory"
	pwd
	
	echo "This is the username"
	whoami
	
	echo "This is the date"
	date
	
	echo "This is the current time"
	date +”%H:%M”
	

### V - list of groups

Write a shell script checking all the [groups](https://www.cyberciti.biz/faq/linux-show-groups-for-user/) a user is part of and for each one display `<username> is part of the group <group>`.

	#!/bin/bash
	
	username=`whoami`
	group=`id -Gn $username`
	
	echo "This is the username : $username"
	echo "This is the group: $group"


## Resources

* [TutorialsPoint](https://www.tutorialspoint.com/unix/shell_scripting.htm)
* [Shellscript](https://www.shellscript.sh/)
****