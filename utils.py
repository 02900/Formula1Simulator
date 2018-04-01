# -*- coding: utf-8 -*-
#title           :  utils.py
#description     :  Multiple utility fuctions
#author          :  Juan Ortiz
#date            :  30 March 2018
#version         :  0.1
#python_version  :  2.7.14
#=======================================================================

import os, time;
from termcolor import cprint;
from string import ascii_lowercase;
from pyfiglet import Figlet, figlet_format;
from colorama import Cursor, Fore, init; init();

def Clear():
	os.system('cls');

def WaitForSeconds(sec):
	time.sleep(sec);

def WaitForInput():
	print ("\nPress 'ENTER' to continue");    
	raw_input(" >>  ");

def Write(file, Austin, Malasya, Monza, Russia, Silverstone):
	with open(file + '.txt', 'w') as f:
		print >> f, 'CIRCUIT: [Coef. Aerodinamic, Power, Weight, Time Lap, Remaining Money]';
		print >> f, 'Austin:', Austin;
		print >> f, 'Malasya:', Malasya;
		print >> f, 'Monza:', Monza;
		print >> f, 'Russia:', Russia;
		print >> f, 'Silverstone:', Silverstone;

LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 
def AlphabetPosition(text):
	text = text.lower();
	numbers = [LETTERS[character] for character in text if character in LETTERS];
	return int(' '.join(numbers));

def Expensive (coef, power, weight):
	coef = 100 * (coef - 1);
	power = 100 * (power - 1);
	weight = 100 * (1 - weight);
	return 5000000 - (600000*coef + 100000*power + 120000*weight);

def msgCool (track):
	figletText = figlet_format('\n'+track + " circuit", "cybermedium");
	cprint(figletText, 'blue', attrs=['dark']);
	return

def Print(msg, color):
	fore = {'red': Fore.RED, 'blue': Fore.BLUE, 'green': Fore.GREEN}
	print(fore[color] + msg + Fore.WHITE);

def PrintOptimal(optimalConfig, track=""):
	if (track != ""):
		msgCool (track);
	print(Fore.RED + "The optimal initial setup is: " + Fore.WHITE);
	print("Coef. Aerodinamic", optimalConfig[0]);
	print("Power", optimalConfig[1]);
	print("Weight", optimalConfig[2]);
	print("Time Lap", optimalConfig[3]);
	print("Remaining Money", optimalConfig[4]);
