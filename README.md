
## Text-Commands

Purpose: A script that reads the unread emails sent as text messages from the phone, and then updates the calendar, and excel spreadsheet based on the parameters. 

## Getting Started

First create a directory where you would like to download the script to. Name it whatever you like, but make sure to remember the path.
For the purposes of this guide, I created my directory on my desktop.

Next download the textcommands.py into your newly created directory.

You can open the python project in any text editor and IDE of your choice to edit.


### Prerequisites

To run this quickstart, you'll need:
Python 2.6 or greater.
The pip package management tool.
A Google account with Google Calendar enabled.
`

### Installing

## Step 1
First you will need to download python according to your OS.

# Mac
Mac already comes with python. To check to see what version of python your mac is running, open the Terminal application, and enter the following command:
```
python
```
You should receive a prompt stating the version of python.
Enter the following command to exit the python program in terminal.
```
quit()
```
# Windows

In your PowerShell (Terminal) program, run python. You run things in Terminal by just typing the name and pressing Enter.
If you run python and it's not there (python is not recognized..). Install it from http://python.org/download.
Make sure you install Python 2.7 or above. I prefer Python2 over Python3
You may be better off with ActiveState Python especially when you do not have Administrative rights
If after you install it python still isn't recognized then in PowerShell enter this:
[Environment]::SetEnvironmentVariable("Path", "$env:Path;C:\Python27", "User")
Close PowerShell and then start it again to make sure Python now runs. If it doesn't, restart may be required.
Type quit() and press Enter to exit python.

# Linux

Linux is a varied operating system with a bunch of different ways to install software. I'm assuming if you are running Linux then you know how to install packages so here are your instructions:
Run your Terminal program. It won't look like much.
In your Terminal program, run python. You run things in Terminal by just typing the command name and pressing Enter.
If you run python and it's not there, install it. 
Type quit() and press Enter to exit python.
You should be back at a prompt similar to what you had before you typed python. If not, find out why.

## Step 2
# Do I need to install pip?
# Python 2.7.9+ and 3.4+
Good news! Python 3.4 (released March 2014) and Python 2.7.9 (released December 2014) ship with Pip. This is the best feature of any Python release. It makes the community's wealth of libraries accessible to everyone. Newbies are no longer excluded from using community libraries by the prohibitive difficulty of setup. In shipping with a package manager, Python joins Ruby, Node.js, Haskell, Perl, Go--almost every other contemporary language with a majority open-source community. Thank you Python.
Of course, that doesn't mean Python packaging is problem solved. The experience remains frustrating. I discuss this in Stack Overflow question Does Python have a package/module management system?.
And, alas for everyone using Python 2.7.8 or earlier (a sizable portion of the community). There's no plan to ship Pip to you. Manual instructions follow.
# Python 2 ≤ 2.7.8 and Python 3 ≤ 3.3
Flying in the face of its 'batteries included' motto, Python ships without a package manager. To make matters worse, Pip was--until recently--ironically difficult to install.
# Official instructions
Per https://pip.pypa.io/en/stable/installing/#do-i-need-to-install-pip:
Download get-pip.py, being careful to save it as a .py file rather than .txt. Then, run it from the command prompt:
python get-pip.py
You possibly need an administrator command prompt to do this. Follow Start a Command Prompt as an Administrator (Microsoft TechNet).
This installs the pip package, which (in Windows) contains ...\Scripts\pip.exe that path must be in PATH environment variable to use pip from the command line (see the second part of 'Alternative Instructions' for adding it to your PATH,
# Alternative instructions
The official documentation tells users to install Pip and each of its dependencies from source. That's tedious for the experienced and prohibitively difficult for newbies.
For our sake, Christoph Gohlke prepares Windows installers (.msi) for popular Python packages. He builds installers for all Python versions, both 32 and 64 bit. You need to:
Install setuptools
Install pip
For me, this installed Pip at C:\Python27\Scripts\pip.exe. Find pip.exe on your computer, then add its folder (for example, C:\Python27\Scripts) to your path (Start / Edit environment variables). Now you should be able to run pip from the command line. 

## Install the following packages using pip in terminal
```
pip install --upgrade google-api-python-client
```

For windows, you might have to type the following

```
python -m pip install --upgrade google-api-python-client
```

You will also need to install the following package using this command
```
pip install --upgrade oauth2client
```

Fow windows you might have to enter ‘python -m’ before the previous command. 

## Step 3
Turn on the Google Calendar API
Use this wizard to create or select a project in the Google Developers Console and automatically turn on the API. Click Continue, then Go to credentials.
On the Add credentials to your project page, click the Cancel button.
At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
Select the Credentials tab, click the Create credentials button and select OAuth client ID.
Select the application type Other, enter the name "Google Calendar API Quickstart", and click the Create button.
Click OK to dismiss the resulting dialog.
Click the file_download (Download JSON) button to the right of the client ID.
Move this file to your working directory and rename it client_secret.json.

## Step 4

Open the python file in you selected editor, and update the gmail_username, and gmail_password with your email, and password. Save the file.

### Running the tests

 Send an email to the account using the following format:
If you would like to update the calendar, send the message starting with 1 followed by the first name, and last name of the client, and how many days from the current date you would like to create an event for. For example            1 Jon Doe 10
If you would like to update the paid and unpaid account on excel, send the message starting with 2 followed by first name, last name, amount, and if it’s paid, or unpaid.                                 2 Jon Doe 100 Paid
Open your terminal, and set the working directory to where textcommands.py file is located. Then run it using the following command
```
python textcommands.py
```
If you tried to update the calendar, it will give you a prompt stating that the event has been created. You can open your google calendar to check if it went through.
