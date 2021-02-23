#!/bin/bash
#
# This script will install 2 python versions: 2.7 and 3.7 and then it will create 2
# virtualenv environments.
# All names can be inputed from keyboard, or from default values.
# Developed by Andrei Karpyza

# Default values definition
pver1_default='2.7.18'
pver2_default='3.7.10'

venv1_default='Python2_venv'
venv2_default='Python3_venv'


# Installable python versions
pver_1='2.7.18'
pver_2='3.7.10'

# Install first python version
step_installed=-1
while [ $step_installed -ne 0 ]
do
  echo -e "\n\nPlease, input version of python to install. Default is: $pver1_default\nTo install the default version just press ENTER: "
  read pver_1
  [ -z $pver_1 ] && pver_1="$pver1_default"
  pyenv install $pver_1
  step_installed=$?
done

# Install second python version
echo "First python version was successfully installed! Now we're going to install the second one..." 
step_installed=-1
while [ $step_installed -ne 0 ]
do
  echo -e "\n\nPlease, input version of second python to install. Default is: $pver2_default\nTo install the default version just press ENTER: "
  read pver_2
  [ -z $pver_2 ] && pver_2="$pver2_default"
  pyenv install $pver_2
  step_installed=$?
done


# Venv installation section
echo -e "\n\nPython versions are installed. Now we'll create python environments.\n\n"
echo "Standard values are: $venv1_default and $venv2_default. They will be used in case of null-input"
echo "NOTE: In the next inputs you need to write only ONE word. All other words will be skipped."

echo -e "Please, input here environment name for python version $pver_1: "
read venv_1 nothing
[ -z $venv_1 ] && venv_1="$venv1_default" && echo "Will be used standard value: $venv1_default..."
pyenv virtualenv $pver_1 $venv_1

echo -e "\n\nPlease, input here environment name for python version $pver_2: "
read venv_2 nothing
[ -z $venv_2 ] && venv_2="$venv2_default" && echo "Will be used standard value: $venv2_default..."
pyenv virtualenv $pver_2 $venv_2

echo "All done. Get ready for code!"
