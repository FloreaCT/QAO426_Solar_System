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


    x = float(len(categories["Planets"]))
    y = float(len(categories["Not planets"]))
    labels = "Planets: " + str(int(x)), "Not Planets: " + str(int(y))
    sizes = [x, y]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')  

    plt.show()

def entities_bar(categories):

    x = float(len(categories["Lower limits"]))
    y = float(len(categories["Medium limits"]))
    z = float(len(categories["Upper limits"]))

    labels = "Lower: " + str(int(x)), "Medium: " + str(int(y)), "Upper: " + str(int(z))
    height = [x, y, z]
    x_pos = (1,2,3)
    plt.xticks(x_pos, labels)

    plt.bar(x_pos, height)

    plt.show()

    """
    Task 25: Display a single subplot that shows a bar chart for categories.

    The function should display a bar chart for the number of 'low', 'medium' and 'high' gravity entities.

    :param categories: A dictionary with entities categorised into 'low', 'medium' and 'high' gravity
    :return: Does not return anything
    """

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


def gravity_animation(categories):
    
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot

    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """

