# -*- coding: utf-8 -*-
#title           :  menu.py
#description     :  Menu options
#author          :  Juan Ortiz
#date            :  30 March 2018
#version         :  0.1
#python_version  :  2.7.14
#=======================================================================

import sys, simulation, utils

welcome = True;
mainMenu = True;

Austin = [];
Malasya = [];
Monza = [];
Russia = [];
Silverstone = [];

def inputNumber(message):
  while True:
    try:
       userInput = int(raw_input(message));   
    except ValueError:
       print("Sorry, I didn't understand that. This input not match wiht any option. Try again.");
       continue;
    if userInput < 0 or (userInput > 3 and mainMenu) or (userInput > 6 and userInput != 9 and not mainMenu):
        print("This input not match wiht any option. Try again.");
        continue;
    elif((userInput == 2 or userInput == 3) and (mainMenu)
        and (len(Austin) == len(Malasya) == len(Monza) == len(Silverstone) == len(Russia) == 0)):
        print ("You must first run a simulator");
        continue;
    else:
       return userInput 
       break 

# Main menu
def MainMenu():
    utils.Clear();
    global mainMenu, welcome;
    mainMenu = True;
    
    if (welcome):
        welcome = False;
        utils.Print ("""Welcome, this is a simulator to obtain the optimal values of a race car
     of Formula 1 in diferrents circuits of the World Championship?""", 'blue');

    print("\n")
    utils.Print ("Please choose the option that you want:", 'blue');
    print "1. Run a Simulator";
    print "2. Show stadistics";
    print "3. Save stadistics as .txt file";
    print "\n0. Quit\n";
 
    choice = inputNumber(" >>  ");
    exec_menu(choice);
    return
 
# Execute option
def exec_menu(choice):
    utils.Clear()
    ParseOptions(int(choice))
    return
 
def simulators():

    utils.Print("\nSelect a circuit to start the simulation!\n\n", 'blue');
    print "1. Austin";
    print "2. Malasya";
    print "3. Monza";
    print "4. Russia";
    print "5. Silverstone";
    print "6. Execute all circuits that have not been simulated";
    print "\n9. Back"
    print "0. Quit\n"

    choice = inputNumber(" >>  ")
    exec_menu(choice)
    return
 
def stadistics():
    if (len(Austin) != 0):
        utils.PrintOptimal(Austin, "Austin");
        utils.WaitForSeconds(0.2);

    if (len(Malasya) != 0):
        utils.PrintOptimal(Malasya, "Malasya");
        utils.WaitForSeconds(0.2);

    if (len(Monza) != 0):
        utils.PrintOptimal(Monza, "Monza");
        utils.WaitForSeconds(0.2);

    if (len(Russia) != 0):
        utils.PrintOptimal(Russia, "Russia");
        utils.WaitForSeconds(0.2);

    if (len(Silverstone) != 0):
        utils.PrintOptimal(Silverstone, "Silverstone");
        utils.WaitForSeconds(0.2);

    utils.WaitForSeconds(0.4);
    utils.WaitForInput();

    return
 
def Save():
    utils.Print("Enter the filename", 'red');
    utils.Write(raw_input(' >> '), Austin, Malasya, Monza, Russia, Silverstone);

def exit():
    sys.exit();
 
def ParseOptions(option):
    global mainMenu, Austin, Malasya, Monza, Russia, Silverstone;

    if (option == 0):
        exit();

    if (mainMenu):
        mainMenu = False;

        if (option == 1):
            simulators();
        elif (option == 2):
            stadistics();
            MainMenu();
        elif (option == 3):
            Save();
            MainMenu();

    else:
        if (option == 1):
            if (len(Austin) == 0):
                Austin = simulation.Run("Austin");
            else:
                print("The parameters of the race car for this circuit have already been calculated previously")
                utils.WaitForSeconds(2);

        elif (option == 2):
            if (len(Malasya) == 0):
                Malasya = simulation.Run("Malasya");
            else:
                print("The parameters of the race car for this circuit have already been calculated previously")
                utils.WaitForSeconds(2);

        elif (option == 3):
            if (len(Monza) == 0):
                Monza = simulation.Run("Monza");
            else:
                print("The parameters of the race car for this circuit have already been calculated previously")
                utils.WaitForSeconds(2);

        elif (option == 4):
            if (len(Russia) == 0):
                Russia = simulation.Run("Russia");
            else:
                print("The parameters of the race car for this circuit have already been calculated previously")
                utils.WaitForSeconds(2);

        elif (option == 5):
            if (len(Silverstone) == 0):
                Silverstone = simulation.Run("Silverstone");
            else:
                print("The parameters of the race car for this circuit have already been calculated previously")
                utils.WaitForSeconds(2);

        elif (option == 6):
            if (len(Austin) == 0):
                Austin = simulation.Run("Austin", False);
            if (len(Malasya) == 0):
                Malasya = simulation.Run("Malasya", False);
            if (len(Monza) == 0):
                Monza = simulation.Run("Monza", False);
            if (len(Russia) == 0):
                Russia = simulation.Run("Russia", False);
            if (len(Silverstone) == 0):
                Silverstone = simulation.Run("Silverstone", False);
                
        MainMenu();

    print "Invalid selection, please try again.\n";
    utils.WaitForSeconds(2);
    MainMenu();
