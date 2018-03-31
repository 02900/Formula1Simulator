import os, time, effects;
from termcolor import cprint;
from string import ascii_lowercase;
from colorama import Cursor, Fore, init;
from pyfiglet import Figlet, figlet_format;
from colorama import Cursor, Fore, init; init();

def Clear():
	os.system('cls');

def WaitForSeconds(sec):
	time.sleep(sec);

LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)} 
def AlphabetPosition(text):
    text = text.lower();
    numbers = [LETTERS[character] for character in text if character in LETTERS];
    return int(' '.join(numbers));

def feasibility (coef, power, weight):
	coef = 100 * (coef - 1);
	power = 100 * (power - 1);
	weight = 100 * (1 - weight);

	if(600000*coef + 100000*power + 120000*weight <= 5000000):
		return True;

	return False;

#cybermedium, , graffiti, , eftiwater, larry3d
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