# usefulScripts

These are some bash and python scripts.
Most of them are daily hacks.
I documented this for mac users only. Other unix user may also run these script by equivalent command.

## fl

This is python script for automatically login to fortigate iitk server while using fortigate ip.

## Prereqisite

Install python
### How do I install these formulæ?
`brew install homebrew/python/<formula>`

Or `brew tap homebrew/python` and then `brew install <formula>`.

### How do I install dependencies?
`pip install <package>`

### How do I run these script?
`chmod a+x (yourscriptname)` and then `./(yourscriptname)`

## bash2048.sh

This is bash version 2048 game

### How do I run these script?
`chmod a+x (yourscriptname)` and then `./(yourscriptname)`


## countDown

This is bash script to countDown in mac

### How do I run these script?
`chmod a+x (yourscriptname)` and then `./(yourscriptname)`

## fibonacci

This is bash script to produce fibonacci number

### How do I run these script?
`chmod a+x (yourscriptname)` and then `./(yourscriptname)`

## maxInteger

This is a bash script to calculate maximum value that a variable can hold in  bash.
There could be lots of way of doing this but this one is quite efficient.

### How do I run these script?
`chmod a+x (yourscriptname)`and then `./(yourscriptname)`


## nicer way to running script in unix

Make a folder in home where you can store all your script

`mkdir ~/(desiredNameForFolder)`

Add this folder to path variable by adding this line to your .bash_profile and source you bash (if you use other shell add this line to that shell rc)

`PATH = "$PATH:~/(desiredNameForFolder)`

Now after creating your script you can run it, just by fixing permission by chmod like

`chmod a+x (yoursriptnam)` and running ` $ youscriptname` in terminal.

For more nicer way we can add few lines to text editor rc like for vim add

`au BufWritePost * if getline(1) =~ "^#!" | if getline(1) =~ "/bin/" | silent !chmod +x <afile> `

to automatically fix permission when a script file is saved


