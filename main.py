from abc import ABC, abstractmethod
import csv
import json
import tui  # I also used this because we have 2 functions which have the same name. e.g orbits() which is in tui.py
# and visual.py
from tui import *  # I used this method of importing so i don't need to declare tui. everytime i am calling a function
# from tui.
from visual import *
import warnings

warnings.simplefilter("ignore", UserWarning)

'''
There was a User Warning which was printing in the console in some animation circumstances:
 - UserWarning: Attempting to set identical bottom == top == 0 results in singular transformations; automatically 
    expanding.
The user does not need to see that as it does not effect the operation of the software neither the animation.
'''


# Creating an abstract class in order to save the file
class AbstractWriter(ABC):
    # dictionary is a argument which represents the dictionary to be saved

    # Initializer
    def __init__(self, dictionary):
        self.dictionary = dictionary

    @abstractmethod
    def save_file(self, dictionary):
        self.dictionary = dictionary
        return self


# Created a concrete class that inherits from the AbstractWriter class
class Writer(AbstractWriter):
    # Initializer
    def __init__(self, dictionary):
        super().__init__(dictionary)
        self.dictionary = dictionary

    def save_file(self, dictionary):
        self.dictionary = dictionary
        # Alphabetically sorting the dictionary
        file_save = {x: sorted(self.dictionary[x]) for x in self.dictionary.keys()}
        # Ask the user to choose a file name for the saved json
        sort_data = input("Please enter a file name\n")
        # Getting the current working directory and saving the data as a json
        with open(os.path.join(os.path.dirname(__file__), f'{sort_data}.json'), 'w') as outfile:
            json.dump(file_save, outfile)

        return self


records = []


# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.

def run():
    # Added try/except to avoid errors that could terminate the program
    try:
        # Since global is declared in the outer scope, it cannot be used inside the function unless called with Global
        global records

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
            # - Read each line from the CSV file and add it to the list 'records'.
            #  You should appropriately handle the case where the file cannot be found
            # TODO: Your code here
            if main_menu == 1:

                started("Data Loading")

                records = planet_list(source_data_path())  # Adding the CSV data to the variable records

                completed("Data Loading")

        # Task 22: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, it is recommended that you create and call one or more separate functions that do the
        # following:
        # - Use the appropriate function in the module tui to display a menu of options for processing the data.
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an entity then
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process
        #       has started.
        #       - Use the appropriate function in the module tui to retrieve the entity name
        #       - Find the record for the specified entity in records.  You should appropriately handle the case
        #       where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve an entity's details then
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve the entity details
        #       - Find the record for the specified entity details in records.  You should appropriately handle the
        #       case where the entity cannot be found.
        #       - Use the appropriate function in the module tui to list the entity
        #       - Use the appropriate function in the module tui to indicate that the entity details retrieval
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their type then
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has started.
        #       - Iterate through each record in records and assemble a dictionary containing a list of planets
        #       and a list of non-planets.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the entity type categorisation
        #       process has completed.
        #
        #   - If the user selected the option to categorise entities by their gravity then
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has started.
        #       - Use the appropriate function in the module tui to retrieve a gravity range
        #       - Iterate through each record in records and assemble a dictionary containing lists of entities
        #       grouped into low (below lower limit), medium and high (above upper limit) gravity categories.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the categorisation by entity gravity
        #       process has completed.
        #
        #   - If the user selected the option to generate an orbit summary then
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       started.
        #       - Use the appropriate function in the module tui to retrieve a list of orbited planets.
        #       - Iterate through each record in records and find entities that orbit a planet in the list of
        #       orbited planets.  Assemble the found entities into a nested dictionary such that each entity can be
        #       accessed as follows:
        #           name_of_dict[planet_orbited][category]
        #       where category is "small" if the mean radius of the entity is below 100 and "large" otherwise.
        #       - Use the appropriate function in the module tui to list the categories.
        #       - Use the appropriate function in the module tui to indicate that the orbit summary process has
        #       completed.
        # TODO: Your code here

            elif main_menu == 2:

                second_menu = process_type()  # Assigning the return of the function to the variable
                started("Data Processing")

                if second_menu == 1:

                    started("Entity retrieval process")
                    check_list(entity_name())
                    completed("Entity retrieval process")
                    completed("Data Processing")

                elif second_menu == 2:

                    started("Entity details retrieval process")
                    list_entities(entity_details())
                    completed("Entity details retrieval process")

                elif second_menu == 3:

                    started("Categorisation process")

                    # Creating 2 list that will be used to store Planets and Non planets
                    planet_lst = []
                    not_planet_list = []

                    for items in records[1:]:  # Starting the iteration excluding titles
                        if items[1] == "TRUE":
                            planet_lst.append(items[0])  # If True, we are adding the planet to the list
                        else:
                            not_planet_list.append(items[0])  # Else we are adding non planets to the non planet list
                    dictionary = {"Planets": planet_lst,
                                  "Not planets": not_planet_list}  # Creating the dictionary of Planets and Not Planets
                    list_categories(dictionary)

                    completed("Categorisation process")

                elif second_menu == 4:

                    started("Categorisation by entity gravity process")

                    # Creating 3 lists for the lower,medium and upper limits
                    lower_limit = []
                    upper_limit = []
                    medium_limit = []

                    # Creating a dictionary which will include lower,medium and upper limits
                    g_dictionary = {}

                    grange = gravity_range()  # Assigning the return of the function to the variable

                    for items in records[1:]:  # Starting iteration excluding titles

                        if float(items[8]) <= grange[0]:
                            lower_limit.append(items[0])  # Adding the planet to the lower limit list
                        elif float(items[8]) >= grange[1]:
                            upper_limit.append(items[0])  # Adding the planet to the upper limit list
                        else:
                            if float(items[8]) >= grange[0] and float(items[8]) <= grange[1]:
                                medium_limit.append(items[0])  # Adding the planet to the medium limit list
                        # Adding all the list created earlier to the dictionary
                        g_dictionary["Lower limits"] = lower_limit
                        g_dictionary["Medium limits"] = medium_limit
                        g_dictionary["Upper limits"] = upper_limit

                    list_categories(g_dictionary)

                    completed("Categorisation by entity gravity process")

                elif second_menu == 5:

                    started("Orbit summary process")

                    orbited = check_list(tui.orbits())  # Assigning the return of the function to the variable

                    # Checking if the return of tui.orbits is None
                    if not orbited:
                        print('Please enter the correct name of the planet')
                        run()
                    else:
                        # Creating a dictionary for the orbited planets
                        orbit_dictionary = {}

                        for orb_item in orbited:
                            # Creating 2 list which will include the small and the large orbits
                            smallish = []
                            largeish = []
                            for rec_item in records:
                                if rec_item[21] == 'NA':  # Checking if the entity is orbiting any planet
                                    continue
                                elif orb_item != rec_item[21]:  # Checking if the entity exist in the database
                                    continue
                                elif orb_item == rec_item[21] and float(rec_item[10]) < 100:
                                    smallish.append(rec_item[0])  # Adding entity to the list
                                elif orb_item == rec_item[21] and float(rec_item[10]) > 100:
                                    largeish.append(rec_item[0])  # Adding entity to the list
                                # Adding the 2 list created earlier to the dictionary
                                orbit_dictionary[orb_item] = {"Small": smallish, "Large": largeish}
                        list_categories(orbit_dictionary)
                    completed("Orbit summary process")

            elif main_menu == 3:

                visual_menu = visualise()  # Assigning the return of the function to the variable

                started("Visualising data")

                if visual_menu == 1:
                    entities_pie(dictionary)

                if visual_menu == 2:
                    entities_bar(g_dictionary)

                if visual_menu == 3:
                    orbits(orbit_dictionary)

                if visual_menu == 4:
                    gravity_animation(g_dictionary)

                completed("Visualizing data")

            elif main_menu == 4:

                started("Saving data process")

                # Checking if the user selected the proper option
                if save() == 1:
                    file_save = Writer(dictionary)
                    file_save.save_file(dictionary)

                completed("Saving data process")

            # Task 28: Check if the user selected the option for saving data.  If so, then do the following:
            # - Use the appropriate function in the module tui to indicate that the save data operation has started.
            # - Save the data (see below)
            # - Use the appropriate function in the module tui to indicate that the save data operation has completed.

            # To save the data, you should demonstrate the application of OOP principles including the concepts of
            # abstraction and inheritance.  You should create an AbstractWriter class with abstract methods and a
            # concrete Writer class that inherits from the AbstractWriter class.  You should then use this to write the
            # records to a JSON file using in the following order: all the planets in alphabetical order followed by
            # non-planets in alphabetical order.
            # TODO: Your code here
            # Task 29: Check if the user selected the option for exiting.  If so, then do the following:
            # # break out of the loop

            elif main_menu == 5:
                print("See you next time!")
                break
            # Task 30: If the user selected an invalid option then use the appropriate function of the module tui to
            # display an error message
            # TODO: Your code here

            else:
                error(main_menu)

    except Exception:
        import sys
        # Assigning the return of the information from exception to the variable
        fatal = str(sys.exc_info()[1]).split()  # Splitting the information

        # Checking if the last word from the exception is:
        if fatal[-1] == 'assignment':
            print(
                "Error! Please load data before trying to visualise data. If you loaded the data, then please process "
                "data afterwards.")
        elif fatal[-1] == 'subscriptable':
            print("Error! Please load data before trying to process data.")
        elif fatal[-1] == 'defined':
            print("Error! Please load data before trying to process data.")
        elif fatal[-1] == 'range':
            print(
                "Error! Please load data before trying to visualise data. If you loaded the data, then please process "
                "data afterwards.")
        # In case there is another unexpected error, add the last word from the error to the function error()
        else:
            error(fatal[-1])
    # If the user choose to exit
    finally:
        if main_menu == 5:
            import time  # Importing time in order to use a small delay before exiting the program
            time.sleep(2)  # 2 seconds delay
            exit(0)
        else:
            run()


if __name__ == "__main__":
    run()
