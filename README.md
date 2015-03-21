#Let us play your games for you!
##Why do we want to play your games for you?
Because reasons.
##Technical details
 ###Building a Dev environment
* sudo pip install virtualenvwrapper
* export WORKON_HOME=~/Envs
* mkdir -p $WORKON_HOME
* source /usr/bin/local/virtualenvwrapper.sh
* mkvirtualenv --python=/usr/bin/python3 LUPYGFY
* pip install Flask

 ###To make virtualenv load with every instance, add this to ~/.bashrc:
* export WORKON_HOME=$HOME/Envs
* export PROJECT_HOME=$HOME/Devel
* source /usr/local/bin/virtualenvwrapper.sh

###Server Stack
* AWS
* Ubuntu 14.10
* Ngnix 
* Python3.4
* Python.Flask

###Client Side Stack
* Bootstrap 3.3
* Angular.js

###Database Stack 
* AWS
* Ubuntu 14.10
* CouchDB

### Management Software
* Docker
* Piwik
* Travis.ci

##Development Workflow
Generally speaking, this project expects that
* New code is covered by new unit tests
* No unit tests fail
* 10/10 pylint score
* No flake8 errors

###On Dev Workstation
* Make a test
* Show test fails
* Write code
* Make test pass
* Make code pretty
* Make pylint happy
* Push to github

###On Test Server
* Pull new code
* Show unit tests pass

###On Production Server
* Pull new code
* Deploy new code
