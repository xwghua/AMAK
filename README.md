# Automouse & Autokeyboard(AMAK)
This is a simple Python program for automatic control of mouse movements and actions and keyboard.

## Introduction
<img src="../../blob/master/amak.ico" align="right" height="100">

This program is used to automate the repeatable **two** actions of your mouse, so that the mouse cursor can perform certain actions from one location to the other with a preset time interval. The aim to develope this program is to free my hands from repeating alternated actions and to keep each action at the time interval.
The program could be really useful when you want to control multiple devices at the same triggering period, and it brings much convenience if you want to perform some multi-color imaging when you don't have DAQ controlling for lasers and cameras.

## Requirements
This program should be compatible with Python 3.6+ and PyQt5 environment.

## Install
- Install Python and Pip
- Use `Pip` to indtall `PyQt5` module <br />
```py -m pip install PyQt5```
- Use `Pip` to indtall `pyautogui` module <br />
```py -m pip install pyautogui```
- Use `Pip` to install `keyboard` module <br />
```py -m pip install keyboard```
*Please note that the whole program has only been tested on Windows 10 platform.*

## Usage
After installing all the required packages mentioned above, you may want to run the **amak.py** by the following command: <br />
```
cd <your-.py-file-location>
py .\amak.py
```
Before starting everything, set a reasonable time interval for mouse action triggering.

To initiate a start, clicke the `START` button, then the keyboard will start to take in inputs.

According the instructions, move the mouse to your desired location `1`, then hit your `A` key to take in the left position of the mouse; move the mouse to your desired location `2`, then hit your `D` key to take in the right position of the mouse.

Hit your `W` button to start the automation, with a time interval you set at the beginning.

Hit your `S` button whenever you want to stop the automation.

If you need to make some changes on the user interface, remember to compile the `.ui` file using **compileUI36.bat** and specify the compiler location.


## Limitations
This only limitation is that the time interval cannot be too small since the auto-movement interval cannot process that fast. 
Other ways and solutions would be came up with.
