from abc import ABC, abstractmethod
import csv
import json
import tui
from tui import *
from visual import *


class AbstractWriter(ABC):

    def __init__(self, path):
        self.path = path

    @abstractmethod
    def save_file(self, path):
        self.path = path
        return self


class Writer(AbstractWriter):

    def __init__(self, path):
        self.path = path

    def save_file(self, path):
        self.path = path
        d2 = {x: sorted(self.path[x]) for x in self.path.keys()}
        with open('sorted_data.json', 'w') as outfile:
            json.dump(d2, outfile)

        return self


records = []

# Task 18: Create an empty list named 'records'.
# This will be used to store the date read from the source data file.

def run():
    # try:

        global records
        welcome()

        def check_list(check):
            """
            Added this function to extend the capabilities of entity_name() because the requirement for entity_name
            was just to return a name. It will be used for orbits() from tui.py as well.
            """
            if type(check) == list:
                clist = []
                for entities in records:
                    for items in check:
                        if items == entities[0]:
                            print('\n' + items, "has been retrieved.")
                            clist.append(items)
                        elif items != entities[0]:
                            continue
                return clist
            else:
                for entities in records:
                    if check == entities[0]:
                        print('\n' + check, "has been retrieved.")
                        return check
                print(check, "is not in the database.")
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
                    lower_limit = []
                    upper_limit = []
                    medium_limit = []
                    g_dictionary = {}
                    grange = gravity_range()
                    for items in records[1:]:  # Starting iteration excluding titles

                        if float(items[8]) <= grange[0]:
                            lower_limit.append(items[0])
                        elif float(items[8]) >= grange[1]:
                            upper_limit.append(items[0])
                        else:
                            if float(items[8]) >= grange[0] and float(items[8]) <= grange[1]:
                                medium_limit.append(items[0])
                        g_dictionary["Lower limits"] = lower_limit
                        g_dictionary["Medium limits"] = medium_limit
                        g_dictionary["Upper limits"] = upper_limit
                    list_categories(g_dictionary)
                    completed("Categorisation by entity gravity process")

                elif second_menu == 5:
                    started("Orbit summary process")
                    orbited = check_list(tui.orbits())
                    if not orbited:
                        print('Please enter the correct name of the planet')
                        run()
                    else:
                        orbit_dictionary = {}
                        for orb_item in orbited:
                            smallish = []
                            largeish = []
                            for rec_item in records:
                                if rec_item[21] == 'NA':
                                    continue
                                elif orb_item != rec_item[21]:
                                    continue
                                elif orb_item == rec_item[21] and float(rec_item[10]) < 100:
                                        smallish.append(rec_item[0])
                                elif orb_item == rec_item[21] and float(rec_item[10]) > 100:
                                    largeish.append(rec_item[0])
                                orbit_dictionary[orb_item] = {"Small": smallish, "Large": largeish}
                    list_categories(orbit_dictionary)
                    completed("Orbit summary process")
            elif main_menu == 3:
                visual_menu = visualise()
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
                if save() == 1:
                    file_save = Writer(dictionary)
                    file_save.save_file(dictionary)
                completed("Saving data process")
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


    # except Exception:
    #     import sys
    #     fatal = str(sys.exc_info()[1]).split()
    #
    #     if fatal[-1] == 'assignment':
    #         print("Error! Please load data before trying to visualise data. If you loaded the data, then please process data afterwards.")
    #     elif fatal[-1] == 'subscriptable':
    #         print("Error! Please load data before trying to process data.")
    #     elif fatal[-1] == 'defined':
    #         print("Error! Please load data before trying to process data.")
    #     elif fatal[-1] == 'range':
    #         print("Error! Please load data before trying to visualise data. If you loaded the data, then please process data afterwards.")
    #     else:
    #         error(fatal[-1])
    #
    # finally:
    #     if main_menu == 5:
    #         import time
    #         time.sleep(2)
    #         exit(0)
    #     else:
    #         run()


if __name__ == "__main__":
    run()
