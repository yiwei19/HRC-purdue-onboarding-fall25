# HRC Software Onboarding Fall 2025
![Demo](dog.gif)

This document walks you through the onboarding task for HRC Software such that by the end of this onboarding project, you will have created a (semi) walking quadruped simulated on your computer.\
\
For this onboarding project, you will make a mujoco xml specification of a robot dog, simulate it in a python simulation loop, and write a PD controller and walking program for it in simulation.\
\
The goal of this onboarding is for you to get some familiarity with the world of programming legged robots such as thinking about robots and their control physically (kinematics) and the usage of simulation. During this project, you are encouraged to read a bit more about legged locomotion and robotics.


## Experience Assumptions
This project assumes basic familiarity with Python programming, programming with vectors (numpy), git and common software management practices. All the following steps about installation and setting up environments are done on linux terminal. Don’t worry if you are not familiar with these skills, they can be picked up quickly and are always useful.

## System Requirements
Linux based computer, emulator (mac OS), wsl

# Python Environment
Good python programming practice necessitates the use of virtual environments to have a python interpreter that has the packages you need. 

(If you are familiar with python environments, install environments however you like with numpy as mujoco)

In your projects folder, make a python venv with:

```
python3 -m venv [your env name here]
```

This will make a folder of your env name that contains the python interpreter of the virtual environment. You will know it is active in your terminal by the presence of the ([env name]) before your user name and directory. You can activate and deactivate the venv with:
```
source [your env name]/bin/activate // run the bash file to activate the venv
deactivate // deactivate the venv
```
With your venv activated, install mujoco and numpy with
```
pip install mujoco
pip install numpy
```
# Mujoco Snake Example
To help you get started 
