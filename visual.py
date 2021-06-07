import matplotlib.pyplot as plt
import matplotlib.animation as animation
from main import *


def entities_pie(categories):
    """
    Task 24: Display a single subplot that shows a pie chart for categories.

    The function should display a pie chart with the number of planets and the number of non-planets from categories.

    :param categories: A dictionary with planets and non-planets
    :return: Does not return anything
    """
    # Assigning x and y the value of the length of the values of their respective keys
    x = float(len(categories["Planets"]))
    y = float(len(categories["Not planets"]))

    # Creating a list of labels
    labels = "Planets: " + str(int(x)), "Not Planets: " + str(int(y))
    sizes = [x, y]

    # Plotting the figure
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')  # Using autopct in order to display percentage
    ax.axis('equal')

    plt.show()


def entities_bar(categories):
    """
       Task 25: Display a single subplot that shows a bar chart for categories.

       The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

       :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
       :return: Does not return anything
       """

    # Assigning x,y,z the value of the length of the values of their respective keys
    x = len(categories["Lower limits"])
    y = len(categories["Medium limits"])
    z = len(categories["Upper limits"])

    # Creating labels
    labels = "Lower: " + str(x), "Medium: " + str(y), "Upper: " + str(z)
    height = [x, y, z]
    x_pos = (1, 2, 3)

    plt.xticks(x_pos, labels)
    plt.title('Number of orbiting entities by gravity')
    plt.bar(x_pos, height)

    plt.show()



def orbits(summary):
    """
    Task 26: Display subplots where each subplot shows the "small" and "large" entities that orbit the planet.

    Summary is a nested dictionary of the form:
    summary = {
        "orbited planet": {
            "small": [entity, entity, entity],
            "large": [entity, entity]
        }
    }

    The function should display for each orbited planet in summary. Each subplot should show a bar chart with the
    number of "small" and "large" orbiting entities.

    :param summary: A dictionary containing the "small" and "large" entities for each orbited planet.
    :return: Does not return anything
    """
    # Creating 3 empty list
    vsmall = []
    vlarge = []
    planet_name = []

    # Checking if we have any Large entity in the dictionary
    for key, values in summary.items():
        if 'Large' in values:
            # Adding small and large entities to the list
            vsmall.append(len(summary[key]['Small']))
            vlarge.append(len(summary[key]['Large']))
        else:
            vsmall.append(len(summary[key]['Small']))
            vlarge.append(0)
    # Adding all the planets to the list
    for keys in summary.keys():
        planet_name.append(keys)

    fig, axs = plt.subplots(1, len(planet_name))
    fig.suptitle('The number of entities orbiting: ')

    # Using the number of the planets as a range
    for i in range(len(planet_name)):
        x1 = 2
        y1 = vsmall[i]
        x2 = 4
        y2 = vlarge[i]
        plt.subplot(2, 3, i + 1)  # At first iteration i will be 0 and creating a subplot 2,3,0 is not valid.
        plt.bar(x1, y1, color='orange')
        plt.bar(x2, y2, color='blue')
        plt.title(planet_name[i])  # Setting the name of the planet for each subplot
        plt.legend(['Small', 'Large'])

        # Checking if we have 0 planets orbiting, in order to not display 0
        if y1 == 0:
            plt.text(x1, y1, str(y1), color='white', ha='center')  # Setting white so 0 wont be visible
            plt.text(x2, y2 + 0.5, str(y2), color='black', ha='center')
        elif y2 == 0:
            plt.text(x1, y1 / 2, str(y1), color='black', ha='center')
            plt.text(x2, y2 + 0.5, str(y2), color='white', va='center')  # Setting white so 0 wont be visible
        else:
            plt.text(x1, y1 / 2, str(y1), color='black', ha='center')
            plt.text(x2, y2 + 0.5, str(y2), color='black', ha='center')

    plt.tight_layout()
    mng = plt.get_current_fig_manager()  # This is the figure manager
    mng.window.state('zoomed')  # and we use this to open the figure in full screen
    plt.show()


# Created this 2 variables outside of the function in order to called them in the function with global
# This is because we will have a function inside another function and outer scope wont help here

a, b = 0, 0


def gravity_animation(categories):
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot



    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """
    # Creating 3 variables that will represent the number of lower, medium and upper limits
    small_list = len(categories['Lower limits'])
    medium_list = len(categories['Medium limits'])
    large_list = len(categories['Upper limits'])

    fig = plt.figure()

    # Adding 3 subplots to the figure
    small = fig.add_subplot(221)
    medium = fig.add_subplot(222)
    large = fig.add_subplot(212)

    # Setting the limits of all subplots from 0 to their respective height/length
    small.set(xlim=(0, small_list), ylim=(0, small_list))
    medium.set(xlim=(0, medium_list), ylim=(0, medium_list))
    large.set(xlim=(0, large_list), ylim=(0, large_list))

    # Setting the titles for every subplot
    small.set_title(f'Small gravity planets: {small_list}')
    medium.set_title(f'Medium gravity planets: {medium_list}')
    large.set_title(f'Large gravity planets: {large_list}')

    # Setting the plot sizes
    smallish, = small.plot(range(small_list + 1), range(small_list + 1), "r-")
    mediumish, = medium.plot(range(medium_list + 1), range(medium_list + 1), "b-")
    largeish, = large.plot(range(large_list + 1), range(large_list + 1), "g-")

    # Checking if small_list is the biggest list in order to adjust the other lists
    if small_list > medium_list and small_list > large_list:

        def animate(i):
            global a, b  # Calling the global variables previously declared

            smallish.set_data(range(i), range(i))
            if i > medium_list:
                mediumish.set_data(range(a), range(a))
                if a <= medium_list:
                    a += 1  # Increasing the variable so the plot can continuously grow
                elif a > medium_list:
                    a = 0  # Resetting the plot to 0 so that the animation can start again
            elif i < medium_list:
                mediumish.set_data(range(i), range(i))

            if i > large_list:
                largeish.set_data(range(b), range(b))
                if b <= large_list:
                    b += 1  # Increasing the variable so the plot can continuously grow
                elif b > large_list:
                    b = 0  # Resetting the plot to 0 so that the animation can start again
            elif i <= large_list + 2:
                largeish.set_data(range(i), range(i))

        x = animation.FuncAnimation(fig, animate, interval=200, frames=small_list)
        a, b = 0, 0

    elif medium_list > small_list and medium_list > large_list:

        def animate(i):
            global a, b

            mediumish.set_data(range(i), range(i))
            if i > small_list:
                smallish.set_data(range(a), range(a))
                if a <= small_list:
                    a += 1  # Increasing the variable so the plot can continuously grow
                elif a > small_list:
                    a = 0  # Resetting the plot to 0 so that the animation can start again
            elif i < small_list:
                smallish.set_data(range(i), range(i))

            if i > large_list:
                largeish.set_data(range(b), range(b))
                if b <= large_list:
                    b += 1  # Increasing the variable so the plot can continuously grow
                elif b > large_list:
                    b = 0   # Resetting the plot to 0 so that the animation can start again
            elif i <= large_list + 2:
                largeish.set_data(range(i), range(i))

        x = animation.FuncAnimation(fig, animate, interval=200, frames=medium_list)
        a, b = 0, 0

    elif large_list > small_list and large_list > medium_list:

        def animate(i):
            global a, b

            largeish.set_data(range(i), range(i))
            if i > small_list:
                smallish.set_data(range(a), range(a))
                if a <= small_list:
                    a += 1  # Increasing the variable so the plot can continuously grow
                elif a > small_list:
                    a = 0   # Resetting the plot to 0 so that the animation can start again
            elif i < small_list:
                small_list.set_data(range(i), range(i))

            if i > medium_list:
                mediumish.set_data(range(b), range(b))
                if b <= medium_list:
                    b += 1  # Increasing the variable so the plot can continuously grow
                elif b > medium_list:
                    b = 0   # Resetting the plot to 0 so that the animation can start again
            elif i < medium_list:
                mediumish.set_data(range(i), range(i))

        x = animation.FuncAnimation(fig, animate, interval=200, frames=large_list)
        a, b = 0, 0

    plt.tight_layout()
    mng = plt.get_current_fig_manager()  # This is the figure manager
    mng.window.state('zoomed')  # and we use this to open the figure in full screen

    # In case we need to save the file.
    # fname = input('Please enter the file name')
    # f = f"{fname}.gif\n"
    # writergif = animation.PillowWriter(fps=30)
    # x.save(f, writer=writergif)

    plt.show()
