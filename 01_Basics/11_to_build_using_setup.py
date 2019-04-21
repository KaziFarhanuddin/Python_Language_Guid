""" 
	This script illustrates different ways to install python modules.
	Remember these commands are to be run inside the terminal.
"""

# Most used
pip
# https://pypi.org/
# pip install (module name)
 
wheel
# wheel using pip
pip install (.wheel file)

git
# pip install git+(grporisotry).git
#  Hear the url is the .git url
	
	To also use a specific branch
	# pip install git+(git porisotry).git@(branch / commitID)

	If want to download the ziped repo and install
	#  pip install (git porisotry)/archive/(branch / commitID).zip

#
Set up
# py -3.6 setup.py install
# python setup.py install


easy_install
	# easy_install (module name)