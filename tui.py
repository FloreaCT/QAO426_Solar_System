import csv
from main import *
import os  # We imported os in order to use relative path when loading/saving files and use current directory


def welcome():
    """
    Task 1: Display a welcome message.

    The welcome message should consist of the title 'Solar Record Management System' surrounded by dashes.
    The number of dashes before and after the title should be equal to the number of characters in the title 
    i.e. 30 dashes before and after.

    :return: Does not return anything.
    """
    # Welcome message

    welcome_message = "Solar Record Management System"

    print("-" * len(welcome_message) + "\n" + welcome_message + "\n" + "-" * len(welcome_message))


def menu():
    """
    Task 2: Display a menu of options and read the user's response.

    A menu consisting of the following options should be displayed:
    'Load Data', 'Process Data', 'Visualise Data', 'Save Data' and 'Exit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Load Data', 2 for 'Process Data' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if invalid selection otherwise an integer corresponding to a valid selection
    """
    # Main menu

    print("Main Menu:\n1.Load Data\n2.Process Data\n3.Visualise Data\n4.Save Data\n5.Exit\n")

    main_option = input()  # Ask the user for input
    # Because the task is specifically asking for an integer, we need to verify if the input is a number
    # The bellow method was used in order to prevent any errors from stopping the script
    if main_option.isnumeric():
        return int(main_option)
    else:
        # Although the task is asking for a None return, i have chosen to return the main_menu in order to show the user
        # an error if a invalid option is selected(e.g A or B instead of 1 or 2)
        return main_option


def started(operation):
    """
    Task 3: Display a message to indicate that an operation has started.

    The function should display a message in the following format:
    '{operation} has started.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being started
    :return: Does not return anything
    """

    print(f"\n{operation} has started.\n")


def completed(operation):
    """
    Task 4: Display a message to indicate that an operation has completed.

    The function should display a message in the following format:
    '{operation} has completed.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being completed
    :return: Does not return anything
    """
    print(f"\n{operation} has completed.\n")


def error(error_msg):
    """
    Task 5: Display an error message.

    The function should display a message in the following format:
    'Error! {error_msg}.'
    Where {error_msg} is the value of the parameter passed to this function

    :param error_msg: A string containing an error message
    :return: Does not return anything
    """
    print(f"Error! {error_msg} is not a valid option")


def source_data_path():
    """
    Task 6: Retrieve a file path to the source data file.

    The function should prompt the user to enter the file path for a data file (e.g. 'data/sol_data.csv').
    If the file path entered by the user does not end in 'csv' then a suitable error message should be displayed
    and the value None should be returned.
    Otherwise, the file path entered by the user should be returned.

    :return: None if the file path does not end in 'csv' otherwise return the file path entered by the user
    """
    # Ask the user for the path of the CSV file
    data_path = input(
        "Please enter the file path for the data file.\n* Do not forget to enter the file extension 'csv' *\n")

    # Verifying if the input is ending with .csv, otherwise show and error
    if data_path.endswith(".csv"):
        return data_path
    else:
        error(data_path)
        return None


def process_type():
    """
    Task 7: Display a menu of options for how the file should be processed. Read in the user's response.

    A menu should be displayed that contains the following options:
        'Retrieve entity', 'Retrieve entity details', 'Categorise entities by type',
        'Categorise entities by gravity', 'Summarise entities by orbit'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Retrieve entity', 2 for 'Retrieve entity details' and so on.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection made otherwise an integer corresponding to a valid option
    """

    # Process data menu

    print(
        "Menu\n1.Retrieve entity\n2.Retrieve entity details\n3.Categorise entities by type\n4.Categorise entities by "
        "gravity\n5.Summarise entities by orbit\n")

    # Ask the user for input
    process_menu = int(input())

    # Checking if the input is correct, otherwise throw an error
    if process_menu in range(1, 6):
        return process_menu
    else:
        error(process_menu)
        return None


def entity_name():
    """
    Task 8: Read in the name of an entity and return the name.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should then read in and return the user's response.

    :return: the name of an entity
    """
    print("Please enter the entity's name:")

    # Ask user for a planet name and capitalize first letter
    planet_name = input().capitalize()

    return planet_name


def entity_details():
    """
    Task 9: Read in the name of an entity and column indexes. Return a list containing the name and indexes.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should also ask the user to enter a list of integer column indexes e.g. 0,1,5,7
    The function should return a list containing the name of the entity and the list of column
    indexes e.g. ['Earth', [0,1,5,7]]

    :return: A list containing the name of an entity and a list of column indexes
    """

    print("\nPlease enter the name of the planet")

    # Ask the user for a planet name and capitalize first letter
    entity = input().capitalize()

    print(f"\nAt which index of the planet we should look?")

    # Defining the index list
    cols = []

    # Ask the user for an index to be shown
    col_nr = input()

    # Checking if the user entered some indexes.
    if len(col_nr) > 0:
        index = col_nr.split(",")  # Splitting the list entered by the user, since its a string and not integers
        print("")
        for i in range(0, len(index)):
            index[i] = int(index[i])  # Converting the strings to integers
        cols.append(index)
        return entity, cols
    # If the user didn't enter any indexes we will return an empty list
    else:
        cols = []
        return entity, cols


def list_entity(entity, cols=[]):
    """
    Task 10: Display an entity. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for the entity will be displayed.

    The entity is a list of values corresponding to particular Solar System space entity
    E.g. ['Earth', TRUE, 9.8].
    The function should only display those values from the entity list that correspond to the column
    indexes provided as part of cols.
    E.g. if cols is [0, 2] then for the entity ['Earth', TRUE, 9.8] the following will be displayed
    ['Earth', 9.8]
    E.g. if cols is an empty list then all the values will be displayed i.e. ['Earth', TRUE, 9.8]

    :param entity: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: does not return anything
    """
    # Making a copy of the records, because we will alter the list in the current function
    records3 = records2.copy()

    # Verifying if the entity is in the database
    the_entity = check_list(entity[0])

    # If the entity is not in the database, do nothing. An error is printed within the check_list function beforehand.
    if the_entity is None:
        pass
    else:
        # If the user enter indexes in the early function, we will proceed as follow:
        if entity[1] != []:
            for item in records3:
                if the_entity in item[0:1]:  # We need to retrieve the row where we found the entity
                    records3 = item[:]  # records3 is becoming a list of the data from the entities row

            # Creating a list to added the specific indexes from the planet
            lisa = []

            # entity[1] is cols from previous function
            for item in entity[1]:
                for i in item:
                    lisa.append(records3[i])  # Adding the indexes to the list created earlier

            print(f"\nShowing indexes for entity {entity[0]}:")
            print(lisa)
            # Since records3 is now altered we can dispose of it. A new copy will be made when the function will be
            # called again
            del records3
        else:
            for item in records3:
                if entity[0] in item[0:1]:
                    records3 = item[:]
            print(f"\nShowing all the indexes for entity {entity[0]}:")
            print(records3)
            # Since records3 is now altered we can dispose of it. A new copy will be made when the function will be
            # called again
            del records3


def list_entities(entities, cols=[]):
    """
    Task 11: Display each entity in entities. Only the data for the specified column indexes will be displayed.
    If no column indexes have been specified, then all the data for an entity will be displayed.

    The function should have two parameters as follows:
    entities    which is a list of entities where each entity itself is a list of data values
    cols        this is a list of integer values that represent column indexes.
                the default value for this is an empty list i.e. []

    You will need to add these parameters to the function definition.

    The function should iterate through each entity in entities and display the entity.
    An entity is a list of values e.g. ['Earth', TRUE, 9.8]
    Only the columns whose indexes are included in cols should be displayed for each entity.
    If cols is an empty list then all values for the entity should be displayed.

    :param entities: A list of data values related to an entity
    :param cols: A list of integer values that represent column indexes
    :return: Does not return anything
    """
    # TODO: Your code here
    global records2

    divided_list = entities[0].split(",")
    # Using a short code to capitalizing each item inside the list
    divided_list = [item.capitalize() for item in divided_list]

    # Creating a list which will gather all the indexes from the specified planets
    list_of_entities = []

    # Checking ig the list is not empty
    if entities[1] != []:
        for item in records2:
            for items in divided_list:
                if items in item[0:1]:
                    x = item[:]
                    list_of_entities.append(x)

        index_list = entities[1][0]
        # Creating 2 empty list
        lisa = []  # This list will have inside multiple list (lisb)
        lisb = []  # This list will contain only the specified indexes for their respective entity

        for item in index_list:
            for items in list_of_entities:
                lisb.append(items[item])
            lisa.append(lisb)
            lisb = []

        print(f"\nShowing indexes {entities[1][0]} for entity {divided_list}:")
        for item in lisa:  # Displaying every list on a different line
            print(item)

    else:
        # If the list of indexes provided by the user is empty then:
        for item in records2:
            for items in divided_list:
                if items in item[0:1]:
                    x = item[:]  # If we find the item in the list, then we will capture all the indexes here
                    list_of_entities.append(x)  # Adding a list with all the indexes to this list
        print(f"\nShowing all indexes for entity {divided_list}:\n")
        for item in list_of_entities:  # Displaying every list on a different line
            print(item)


def list_categories(categories):
    """
    Task 12: Display the contents of the dictionary categories.

    The function should take a single parameter categories which is a dictionary containing category names
    and a list of entities that belong to the category.

    You will need to add the parameter categories to the function definition.

    :param categories: A dictionary containing category names and a list of entities that are part of that category
    :return: Does not return anything
    """
    # Since the function is used to check 3 different dictionary, i've implemented 3 different displaying options
    # The first one is used for gravity.
    if 'Lower limits' in categories:
        for key, value in categories.items():
            if not value:
                message = f'No {key} exists'
                print('-' * len(message))
                print(message)
                print('-' * len(message), '\n')
            else:
                print('-' * len(key))
                print(key)
                print('-' * len(key), '\n')
                print(value, '\n')
    # The second one is used for planet types
    elif 'Planets' in categories:
        for key, value in categories.items():
            print('-' * len(key))
            print(key)
            print('-' * len(key), '\n')
            print(value, '\n')
    # The third one is used for orbits
    else:
        for key, value in categories.items():
            for keys, values in value.items():
                print('-' * len(key))
                print(key)
                print('-' * len(key), '\n')
                print(keys, values, '\n')


def gravity_range():
    """
    Task 13: Ask the user for the lower and upper limits for gravity and return a tuple containing the limits.

    The function should prompt the user to enter the lower and upper limit for a range of values related to gravity.
    The values will be floats e.g. 5.1 for lower limit and 9.8 for upper limit.
    The function should return a tuple containing the lower and upper limits

    :return: a tuple with the lower and upper limits
    """
    print("Please enter a value for the lower gravity limit")

    lower_gravity = float(input())  # Converting input into float

    print("Please enter a value for the upper gravity limit")

    upper_gravity = float(input())  # Converting input into float

    grav_range = (lower_gravity, upper_gravity)  # Making a tuple for lower and upper gravity

    return grav_range


def orbits():
    """
        Task 14: Ask the user for a list of entity names and return the list.

    The function should prompt the user to enter a list of entity names e.g. Jupiter,Earth,Mars
    The list represents the entities that should be orbited.
    The user may enter as many entity names as they desire.
    The function should return a list of the entity names entered by the user.

    :return: a list of entity names
    """
    print("Please enter the names of the entities you would like to see. e.g Earth,Moon,Venus")

    # Splitting the input by , and converting it into a list
    entities_name = list(input().split(","))
    # Using a short code to capitalizing each item inside the list
    entities_name = [item.capitalize() for item in entities_name]

    # If no entity has been enter we will return None
    if not entities_name:
        return None

    return entities_name


def visualise():
    """
    Task 15: Display a menu of options for how the data should be visualised. Return the user's response.

    A menu should be displayed that contains the following options:
        'Entities by type', 'Entities by gravity', 'Summary of orbits', 'Animate gravities'

    The user's response should be read in and returned as an integer corresponding to the selected option.
    For example, 1 for 'Entities by type', 2 for 'Entities by gravity' and so on.

    If the user enters an invalid option, then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    # Visualise Menu

    print("Visualise Menu\n1.Entities by type\n2.Entities by gravity\n3.Summary of orbits\n4.Animate gravities")

    # Ask user for the input
    visual_menu = int(input())

    # Checking if the user has given a correct option
    if visual_menu not in range(1, 5):
        error(visual_menu)
        return None
    else:
        return visual_menu


def save():
    """
    Task 16: Display a menu of options for how the data should be saved. Return the user's response.

    A menu should be displayed that contains the following option:
         'Export as JSON'

    The user's response should be read in and returned as an integer corresponding to the selected option.

    If the user enters a invalid option then a suitable error message should be displayed and the value
    None should be returned.

    :return: None if an invalid selection is made otherwise an integer corresponding to a valid option
    """
    print("Menu\n1.Export as JSON\n")

    # Ask user for input
    export_menu = int(input())

    # Checking if the user has given a correct option
    if export_menu not in range(1, 2):
        error(export_menu)
        return None
    else:
        return export_menu


def planet_list(path):
    global records2  # We are declaring this global so we can use the variable later on in the program
    """
    This function was created as per Task 21 from main.py request: 
        To load the data, it is recommended that you create and call one or more separate functions that do the
        following
    Its functionality could have been implemented in source_data_path() but that was not a requirement of that function
    """
    # This functions is taking one argument and adds data from a CSV file to a variable

    if path is None:
        print("\nWrong file path.")
        return path

    else:
        # We are using os in order to get the current directory (relative path)
        with open(os.path.join(os.path.dirname(__file__), path), "r") as csvfile:
            csv_reader = csv.reader(csvfile)
            planets = list(csv_reader)
            records2 = planets  # Making a copy of the list that will be used in tui.py

        return planets


def check_list(check):
    """
    Added this function to extend the capabilities of entity_name() because the requirement for entity_name
    was just to return a name. It will be used for orbits() as well.
    """

    # Checking if the argument is a list:
    if type(check) == list:
        clist = []  # Creating an empty list
        for entities in records2:
            for items in check:
                if items == entities[0]:  # Checking if a entity exists in the database
                    print('\n' + items, "has been retrieved.")
                    clist.append(items)
                elif items != entities[0]:
                    continue
        return clist
    # If the argument is not a string, then:
    else:
        for entities in records2:
            if check == entities[0]:  # Checking if the entity exists in the database
                print('\n' + check, "has been retrieved.")
                return check
        print(check, "is not in the database.")
        return None
