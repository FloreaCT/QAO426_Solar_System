import csv
from visual import *

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

    while True:
      main_option = int(input()) #Ask the user for input
      if main_option not in range(1,6):
         main_option = None
         print("Invalid option. Please select a valid option from 1 to 5!\n1.Load Data\n2.Process Data\n3.Visualise Data\n4.Save Data\n5.Exit\n")
         continue
      elif main_option == 1:
        return main_option
        
      elif main_option == 2:
        return main_option

      elif main_option == 3:
        return main_option

      elif main_option == 4:
        save()
        return main_option

      elif main_option == 5:
        print("Hope to see you soon!")
        return          
      else:
          return None
        

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
    print(f"Error! {error_msg}.")


def source_data_path():
    """
    Task 6: Retrieve a file path to the source data file.

    The function should prompt the user to enter the file path for a data file (e.g. 'data/sol_data.csv').
    If the file path entered by the user does not end in 'csv' then a suitable error message should be displayed
    and the value None should be returned.
    Otherwise, the file path entered by the user should be returned.

    :return: None if the file path does not end in 'csv' otherwise return the file path entered by the user
    """

    print("Please enter the file path for the data file.\n* Do not forget to enter the file extention 'csv' *\n")
    while True:
        data_path =input() #Ask the user for the file path
        if data_path.endswith(".csv"):
            return data_path
        else:
            print("Error! Please DO NOT forget to add the file extension '.csv' at the end\n")
            print("Please enter data path: ") 

            

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
    print("Menu\n1.Retrieve entity\n2.Retrieve entity details\n3.Categorise entities by type\n4.Categorise entities by gravity\n5.Summarise entities by orbit\n")    
    while True:

        second_option = int(input()) #Ask the user for input

        if second_option not in range(6):
            second_option = None
            print("Invalid option. Please select a valid option from 1 to 5.")
            return None
        elif second_option == 1:
            started("Entity retrieval process")
            entity_name()
            completed("Entity retrieval process")
            return second_option
        elif second_option == 2:
            started("Entity details process")
            list_entity(entity_details())
            completed("Entity details process")
            return second_option
        elif second_option == 3:
            started("Categorise entities by type")
            list_categories(0)
            completed("Categorise entities by type")
            return second_option
        elif second_option == 4:
            started("Categorise entities by gravity")
            list_categories(gravity_range())
            completed("Categorise entities by gravity")
            return second_option
        elif second_option == 5:
            started("Summarise entities by orbit")
            list_categories(1)
            completed("Summarise entities by orbit")
            return second_option

def entity_name():
    
    """
    Task 8: Read in the name of an entity and return the name.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should then read in and return the user's response.

    :return: the name of an entity
    """
    print("Please enter the Planet's name:") #Ask the user for the name of the planet

    planet_name = input().capitalize()

    planet_list = records
    while True:
        for item in planet_list:
            if planet_name in item[0:1]:
                planet_list = item[:]
                print(f"\n{planet_name} has been retrieved.")
                return planet_name 
        for item in planet_list:
            if planet_name not in item[0:1]:
                planet_list = item[:]
                print(f"\n{planet_name} is not in the database")
            return None 


def entity_details():
    """
    Task 9: Read in the name of an entity and column indexes. Return a list containing the name and indexes.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should also ask the user to enter a list of integer column indexes e.g. 0,1,5,7
    The function should return a list containing the name of the entity and the list of column
    indexes e.g. ['Earth', [0,1,5,7]]

    :return: A list containing the name of an entity and a list of column indexes
    """

    print("\nPlease enter the name of the planet")  # Ask the user for a planet name

    entity = input().capitalize() 

    print(f"\nAt which index of the planet we should look?")  # Ask the user for an index
    
    cols = []
    col_nr = input()
    if len(col_nr) > 0:
        index = col_nr.split(",")
        print("")
        for i in range(0, len(index)):
          index[i] = int(index[i])
        cols.append(index)
        return (entity), (cols)
    else:
        cols = []
        return (entity), (cols)


  

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
    given_list = records
    if entity[1] != []:
        for item in given_list:
            if entity[0] in item[0:1]:
                given_list = item[:]

        index_list = entity[1]
        lista = []

        for item in index_list:
            for i in item:
                lista.append(given_list[i])
        
        print(f"Showing indexes for entity {entity[0]}:")
        print(lista)
    else:
        for item in given_list:
            if entity[0] in item[0:1]:
                given_list = item[:]
                
        print(f"Showing all the indexes for entity {entity[0]}:")
        print(given_list)


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


def list_categories(categories):
    """
    Task 12: Display the contents of the dictionary categories.

    The function should take a single parameter categories which is a dictionary containing category names
    and a list of entities that belong to the category.

    You will need to add the parameter categories to the function definition.

    :param categories: A dictionary containing category names and a list of entities that are part of that category
    :return: Does not return anything
    """


    if categories == 0: #Categorising planets and not planets

        planet_list = []
        not_planet_list = []
        dictionary = {}
        for items in records[1:]:
            if items[1] == "TRUE":
                planet_list.append(items[0])
            else:
                not_planet_list.append(items[0])
        dictionary = {"Planets": planet_list, "Not planets": not_planet_list}
        print(dictionary)

        return dictionary

    elif categories == 1:#Used for orbit summary
        global orbit_summary
        orbit_summary = {}
        planet_dict = {}

        for items in records[1:]:
            if items[21] == "NA":
                continue
            else:
                if float(items[10]) < 100:
                    name = str(items[0]) # This is the orbiting entity
                    items[0] = {}
                    items[0].update({items[21]: "Small"})
                    planet_dict = {name: items[0]} #Sub dictionary
                    orbit_summary.update(planet_dict) #Main dictionary
                else:
                    name = str(items[0])
                    items[0] = {}
                    items[0].update({items[21]: "Large"})
                    planet_dict = {name: items[0]}
                    orbit_summary.update(planet_dict)
        print(orbit_summary)
        print("")
        return orbit_summary
    else: #Used for Gravity Range
        global g_dictionary

        lower_limit = []
        upper_limit = []
        medium_limit = []
        g_dictionary = {}

        for items in records[1:]:
            if float(items[8]) <= categories[0]:
                lower_limit.append(items[0])
            elif float(items[8]) >= categories[1]:
                upper_limit.append(items[0])
            else:
                if float(items[8]) >= categories[0] and float(items[8]) <= categories[1]:
                    medium_limit.append(items[0])
        g_dictionary["Lower"] = lower_limit
        g_dictionary["Medium"] = medium_limit
        g_dictionary["Upper"] = upper_limit
        # print("THIS ARE THE UPPER LIMITS\n",upper_limit)
        # print("")
        # print("")
        # print("THIS ARE THE LOWER LIMITS\n",lower_limit)
        # print("")
        # print("")
        # print("THIS ARE THE MEDIUM LIMITS\n",medium_limit)
        print(g_dictionary)
        return g_dictionary


def gravity_range():
    """
    Task 13: Ask the user for the lower and upper limits for gravity and return a tuple containing the limits.

    The function should prompt the user to enter the lower and upper limit for a range of values related to gravity.
    The values will be floats e.g. 5.1 for lower limit and 9.8 for upper limit.
    The function should return a tuple containing the lower and upper limits

    :return: a tuple with the lower and upper limits
    """
    print("Please enter a value for the lower gravity limit")

    lower_gravity = float(input())

    print("Please enter a value for the upper gravity limit")

    upper_gravity = float(input())

    g_range = (lower_gravity, upper_gravity)

    return g_range


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

    entity = list(input().split(","))

    return entity





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
    print("Visualise Menu\n1.Entities by type\n2.Entities by gravity\n3.Summary of orbits\n4.Animate gravities")
    menu = int(input())

    if menu not in range(5):
        menu = None
        print("Invalid option. Please select a valid option from 1 to 4.")
        return None
    elif menu == 1:
        started("Entities by type process")
        entities_pie(list_categories(0))
        completed("Entities by type process")
        return menu
    elif menu == 2:
        started("Entities by gravity process")
        entities_bar(g_dictionary)
        completed("Entities by gravity process")
        return menu
    elif menu == 3:
        started("Summary of orbits process")
        orbits(orbit_summary)
        completed("Summary of orbits process")
        return menu
    elif menu == 4:
        started("Animating gravities process")
        gravity_animation(g_dictionary)
        completed("Animating gravities process")
        return menu
    # else:
        return menu


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

    while True:
        menu = int(input())
        if menu not in range(2) or menu == 0:
            menu = None
            print("Invalid option. Please select a valid option.\n1.Export as JSON\n")
        else:
            print("Please select the output name: ")
            name = input() + ".json"
            with open(name, 'w') as f:
             json.dump(list_categories(categories), f)



