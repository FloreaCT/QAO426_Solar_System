import matplotlib.pyplot as plt
import matplotlib.animation as animation

from main import *
import numpy as np


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
    x_pos = (1, 2, 3)
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

    Summary is a n  ested dictionary of the form:
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

    vsmall = []
    vlarge = []
    planet_name = []
    result = []
    for key, values in summary.items():
        if 'Large' in values:
            vsmall.append(len(summary[key]['Small']))
            vlarge.append(len(summary[key]['Large']))
        else:
            vsmall.append(len(summary[key]['Small']))
            vlarge.append(0)
    for keys in summary.keys():
        planet_name.append(keys)
    for a in planet_name:
        print(a)
        if len(a) > 111:
            b = a.split()[1]
            result.append(b)
        else:
            result.append(a)


    print(result)
    x = np.arange(len(planet_name))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    small = ax.bar(x - width / 2, vsmall, width, label='Small')
    big = ax.bar(x + width / 2, vlarge, width, label='Large')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number of planets')
    ax.set_xticks(x)
    ax.set_xticklabels(result, rotation = 90)

    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate(f'{height}',
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(small)
    autolabel(big)

    fig.tight_layout()
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show()

def gravity_animation(categories):
    """
    Task 27: Display an animation of "low", "medium" and "high" gravities.

    The function should display a suitable animation for the "low", "medium" and "high" gravity entities.
    E.g. an animated line plot



    :param categories: A dictionary containing "low", "medium" and "high" gravity entities
    :return: Does not return anything
    """
    small_list = len(categories['Lower limits'])
    medium_list = len(categories['Medium limits'])
    large_list = len(categories['Upper limits'])

    a = list(range(len(categories['Lower limits'])))
    b = list(range(len(categories['Medium limits'])))
    c = list(range(len(categories['Upper limits'])))

    fig = plt.figure()

    small = fig.add_subplot(221)
    medium = fig.add_subplot(222)
    large = fig.add_subplot(212)

    small.set(xlim=(0, small_list), ylim=(0, small_list))
    medium.set(xlim=(0, medium_list), ylim=(0, medium_list))
    large.set(xlim=(0, large_list), ylim=(0, large_list))

    small.set_title(f'Small gravity planets: {small_list}')
    medium.set_title(f'Medium gravity planets: {medium_list}')
    large.set_title(f'Large gravity planets: {large_list}')

    smallish, = small.plot(range(small_list + 1), range(small_list + 1))
    mediumish, = medium.plot(range(medium_list + 1), range(medium_list + 1))
    largeish, = large.plot(range(large_list + 1), range(large_list + 1))

    def animate(i):
        smallish.set_data(range(i), range(i))
        mediumish.set_data(range(i), range(i))
        largeish.set_data(range(i), range(i))

    a = animation.FuncAnimation(fig, animate, interval=200, frames=small_list)


    print(small_list)
    print(medium_list)
    print(large_list)

    plt.tight_layout()
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')

    plt.show()
