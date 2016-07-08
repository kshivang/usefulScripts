# usefulScripts

These are some bash and python scripts.
Most of them are daily hacks.
I documented this for mac users only. Other unix user may also run these script by equivalent command.

## fl

This is a python script for automatically login to fortigate iitk server while using fortigate ip. 
If you run this script you will never have your fortigate login problem in browser. You can also manupulate script with your user name and password, and cron task

## Prerequisite

Install python
### How do I install these formulæ?
`brew install homebrew/python/<formula>`

Or `brew tap homebrew/python` and then `brew install <formula>`.

### How do I install dependencies?
`pip install <package>`

### How do I run these script?
`chmod a+x (yourscriptname)` and then `./(yourscriptname)`

For nicer way to run script see bottom

## bash2048.sh

This is bash version 2048 game

### How do I run these script?
`chmod a+x (yourscriptname)` and then `./(yourscriptname)`

For nicer way to run script see bottom

## countDown

This is bash script to countDown in mac

### How do I run these script?
`chmod a+x (yourscriptname)` and then `./(yourscriptname)`

For nicer way to run script see bottom

## fibonacci

This is bash script to produce fibonacci number. This return nth term of fibonacci number

### How do I run these script?
`chmod a+x (yourscriptname)` and then `./(yourscriptname)`

For nicer way to run script see bottom

## maxInteger

This is a bash script to calculate maximum value that a variable can hold in  bash.
There could be lots of way of doing this but this one is quite efficient.

### How do I run these script?
`chmod a+x (yourscriptname)`and then `./(yourscriptname)`


## nicer way to running script in unix

Make a folder in home where you can store all your script

`mkdir ~/(desiredNameForFolder)`

Add this folder to path variable by adding this line to your .bash_profile 

`PATH = "$PATH:~/(desiredNameForFolder)`

and source your bash by (if you use other shell, then add this line to that shell rc)

`source .bash_profile` Or restart terminal app. (if you use iterm or xterm, then restart that as well)


Now after creating your script you can run it, just by fixing permission by chmod like

`chmod a+x (yoursriptnam)` and running ` $ youscriptname` in terminal.

For more nicer way we can add few lines to text editor rc like for vim add

`au BufWritePost * if getline(1) =~ "^#!" | if getline(1) =~ "/bin/" | silent !chmod +x <afile> `

to automatically fix permission when a script file is saved


