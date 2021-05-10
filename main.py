import csv
import json
from tui import *
from visual import *


# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.

records = [] #Defining the list with all the planets

def run():

    welcome()

    while True:
        # Task 20: Using the appropriate function in the module tui, display a menu of options
        # for the different operations that can be performed on the data.
        # Assign the selected option to a suitable local variable
        main_menu = menu()

        # Task 21: Check if the user selected the option for loading data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has started.
        # - Load the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data loading
        # operation has completed.
        #
        # To load the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to retrieve a file path for the CSV data file.  You
        # should appropriately handle the case where this is None.
        # - Read each line from the CSV file and add it to the list 'records'. You should appropriately handle the case
        # where the file cannot be found
        # TODO: Your code here
        if main_menu == 1:

            started("Data Loading\n")
            records.append(records(source_data_path()))
            print()
            completed("Data Loading\n")

        # Task 22: Check if the user selected the option for processing data.  If so, then do the following:
        elif main_menu == 2:

        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
            started("Data Processing")

        # - Process the data (see below).
            process_type()
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
            completed("Data Processing")

        # To process the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to display a menu of options for processing the data.
        # - Check what option has been selected
        elif main_menu == 3:
            started("Visualising data")
        # - Use the appropriate function in the module tui to indicate that the data visualisation operation
        # has started.
            visualise()
        # - Visualise the data (see below).
            completed("Visulaising data")


        #       - Use your code from earlier to assemble a nested dictionary of orbiting planets.

        #       - Use the appropriate function in the module visual to display subplots for the orbits


        #
        #   - if the user selected the option to animate the planet gravities then
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has started.
        #       - Use your code from earlier to assemble a dictionary containing lists of entities grouped into
        #       low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module visual to animate the gravity.
        #       - Use the appropriate function in the module tui to indicate that the gravity animation visualisation
        #       process has completed.
        # TODO: Your code here

        # Task 28: Check if the user selected the option for saving data.  If so, then do the following:
        # - Use the appropriate function in the module tui to indicate that the save data operation has started.
        # - Save the data (see below)
        # - Use the appropriate function in the module tui to indicate that the save data operation has completed.

        # To save the data, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create an AbstractWriter class with abstract methods and a concrete
        # Writer class that inherits from the AbstractWriter class.  You should then use this to write the records to
        # a JSON file using in the following order: all the planets in alphabetical order followed by non-planets 
        # in alphabetical order.
        # TODO: Your code here
        elif main_menu == 4:
            save()
        # Task 29: Check if the user selected the option for exiting.  If so, then do the following:
        # # break out of the loop
        elif menu == 5:
            break
        # Task 30: If the user selected an invalid option then use the appropriate function of the module tui to
        # display an error message
        # TODO: Your code here
if __name__ == "__main__":
    run()

