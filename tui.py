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

    print("-" * len(welcome_message))
    print(welcome_message)
    print("-" * len(welcome_message))


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
      if main_option not in range(6) or main_option == 0:
        main_option = None
        print("Invalid option. Please select a valid option from 1 to 5!\n1.Load Data\n2.Process Data\n3.Visualise Data\n4.Save Data\n5.Exit\n")
        continue
      elif main_option == 1:
        source_data_path()

      elif main_option == 2:
        process_type()

      elif main_option == 3:
        visualise()

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
    
    print(f"{operation} has started.")


def completed(operation):
    """
    Task 4: Display a message to indicate that an operation has completed.

    The function should display a message in the following format:
    '{operation} has completed.'
    Where {operation} is the value of the parameter passed to this function

    :param operation: A string indicating the operation being completed
    :return: Does not return anything
    """
    print(f"{operation} has completed.")


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

    data_path = input() #Ask the user for the file path

    if ".csv" in data_path:
        return data_path
    else:
        print("Error! Please DO NOT forget to add the file extension '.csv' at the end")
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
    print("Menu\n1.Retrieve entity\n2.Retrieve entity details\n3.Categorise entities by type\n4.Categorise entities by gravity\n5.Summarise entities by orbit\n")

    second_option = int(input()) #Ask the user for input

    if second_option not in range(6):
        second_option = None
        print("Invalid option. Please select a valid option from 1 to 5.")
        return None
    else:
        return second_option

def entity_name():
    """
    Task 8: Read in the name of an entity and return the name.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should then read in and return the user's response.

    :return: the name of an entity
    """
    print("Please enter the Planet's name") #Ask the user for the name of the planet

    planet = input()

    return planet

def entity_details():
    """
    Task 9: Read in the name of an entity and column indexes. Return a list containing the name and indexes.

    The function should ask the user to enter the name of an entity e.g. 'Earth'
    The function should also ask the user to enter a list of integer column indexes e.g. 0,1,5,7
    The function should return a list containing the name of the entity and the list of column
    indexes e.g. ['Earth', [0,1,5,7]]

    :return: A list containing the name of an entity and a list of column indexes
    """
    entity = []

    print("Please enter the name of the planet")  # Ask the user for a planet name
    planet = input()
    entity.append(planet)

    print(f"At which index of the planet {planet} we should look?")  # Ask the user for an index
    index = input().split(",")
    for i in range(0, len(index)):
        index[i] = int(index[i])
    entity.append(index)
    return entity


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

    # TODO: Your code here

def list_entities():
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
    with open('planets.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            print(row[categories])


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
    print("Please enter the name/names of the entities you would like to see. e.g Earth,Moon,Venus")

    entity = input().split(",")

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
    else:
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

            return menu

menu()