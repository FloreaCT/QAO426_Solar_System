import csv
import json
from tui import *
from visual import *

records = []
# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.

def run():
    try:
        global records

        welcome()

        def check_list(check):  # Added function to check if the entity exist in the list

            for item in records:
                if check == item[0]:
                    print(check, "has been retrieved.")
                    return check

            print(check , "is not in the database.")
            return None

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

                started("Data Loading")

                records = planet_list(source_data_path())

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
                second_menu = process_type()
                started("Data Processing")

                if second_menu == 1:
                    started("Entity retrieval process")
                    check_list(entity_name())
                    completed("Entity retrieval process")
                    completed("Data Processing")

                elif second_menu == 2:
                    started("Entity details retrieval process")
                    list_entity(entity_details())
                    completed("Entity details retrieval process")

                elif second_menu == 3:
                    started("Categorisation process")

                    planet_lst = []
                    not_planet_list = []
                    dictionary = {}

                    for items in records[1:]:  # Starting the iteration excluding titles
                        if items[1] == "TRUE":
                            planet_lst.append(items[0])
                        else:
                            not_planet_list.append(items[0])
                    dictionary = {"Planets": planet_lst,
                                  "Not planets": not_planet_list}  # The dictionary of Planets and Not Planets

                    list_categories(dictionary)

                    completed("Categorisation process")

                elif second_menu == 4:
                    started("Categorisation by entity gravity process")
                    list_categories(g_range(gravity_range()))
                    completed("Categorisation by entity gravity process")

            elif main_menu == 3:
                started("Visualising data")
                visualise()
                completed("Visulaising data")



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
            elif main_menu == 5:
                break
            # Task 30: If the user selected an invalid option then use the appropriate function of the module tui to
            # display an error message
            # TODO: Your code here
            else:
                error(main_menu)
    except Exception:
        import sys
        fatal = str(sys.exc_info()[1]).split()
        error(fatal[-1])


    finally:
        run()
if __name__ == "__main__":
    run()

