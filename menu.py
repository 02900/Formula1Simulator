import sys, simulation, utils
from asciimatics.screen import Screen

welcome = True;
mainMenu = True;

Austin = [];
Malasya = [];
Monza = [];
Russia = [];
Silverstone = [];

# Main menu
def main_menu():
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
    print "2. Show stadistics (You must first run a simulator)";
    print "\n0. Quit";
 
    choice = input(" >>  ");
    exec_menu(choice);
    return
 
# Execute option
def exec_menu(choice):
    utils.Clear()
    ParseOptions(int(choice))
    return
 
def simulators():

    utils.Print("\nSelect a circuit to start the simulation!\n", 'blue');
    print "1. Austin";
    print "2. Malasya";
    print "3. Monza";
    print "4. Russia";
    print "5. Silverstone";
    print "6. RUN ALL";
    print "9. Back"
    print "0. Quit"

    choice = raw_input(" >>  ")
    exec_menu(choice)
    return
 
def stadistics():
    if (len(Austin) == 4):
        utils.PrintOptimal(Austin, "Austin");
        utils.WaitForSeconds(0.4);

    if (len(Malasya) == 4):
        utils.PrintOptimal(Malasya, "Malasya");
        utils.WaitForSeconds(0.4);

    if (len(Monza) == 4):
        utils.PrintOptimal(Monza, "Monza");
        utils.WaitForSeconds(0.4);

    if (len(Russia) == 4):
        utils.PrintOptimal(Russia, "Russia");
        utils.WaitForSeconds(0.4);

    if (len(Silverstone) == 4):
        utils.PrintOptimal(Silverstone, "Silverstone");
        utils.WaitForSeconds(0.4);

    if (len(Austin) == len(Malasya) == len(Monza) == len(Silverstone) == len(Russia) == 0):
        print ("You must first run a simulator");

    utils.WaitForSeconds(1);
    print ("\nPress 'ENTER' to continue");    
    raw_input(" >>  ");

    return
 
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
            main_menu();

    else:
        if (option == 1):
            Austin = simulation.Run("Austin");

        elif (option == 2):
            Malasya = simulation.Run("Malasya");

        elif (option == 3):
            Monza = simulation.Run("Monza");

        elif (option == 4):
            Russia = simulation.Run("Russia");

        elif (option == 5):
            Silverstone = simulation.Run("Silverstone");

        elif (option == 6):
            Austin = simulation.Run("Austin");
            Malasya = simulation.Run("Malasya");
            Monza = simulation.Run("Monza");
            Russia = simulation.Run("Russia");
            Silverstone = simulation.Run("Silverstone");

        main_menu();

    print "Invalid selection, please try again.\n";
    utils.WaitForSeconds(2);
    main_menu();
