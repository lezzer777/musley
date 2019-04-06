#!/bin/bash

# я ворвался в скрипт и абля

function pipcheck {
	if pip >> /dev/null;
	then echo;
	else echo "can't find pip. Try to install 'python-pip or 'pip' package"
	echo Aborting...
	exit 2;
		fi


}

function sudocheck {
if sudo >> /dev/null;
then cmd=sudo pip;
else cmd=pip
echo
echo
echo
echo can\'t find \'sudo\'. You may have problems with that
echo are you sure, that you want to continue? '(y/n)'
read ans
case $ans in

	y)
		echo
		cmd=pip
		;;
	*)
		echo Aborting...
		exit 2
		;;

esac ;
fi
}

function main {
echo
echo
echo
printf "This script will install dependencies for Musley\nWait a few seconds untill the scripts ends.\n---\n
"

echo checking for sudo...
sudocheck

echo "Installing termcolor - a python libary for text coloring."
pipcheck
if $cmd install termcolor >> /dev/null
then echo;
else echo an error occurred while installing termcolor by pip. Try to install termcolor yourself by '$cmd install termcolor' command.
exit 2;
fi
echo "Success. You can run 'python musley.py' now."
}

main
