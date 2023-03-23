import matplotlib.pyplot as plt
import numpy as np

def histogram():
    file = open("list.txt")

    pygotowane = str(file.read().lower())
    pygotowane = pygotowane.strip()
    slownik = {}
    i=0
    for k in pygotowane:
        if not str(k).isalpha():
            continue
        if str(k) not in slownik.keys():
            slownik[k] = 0
        if str(k) in slownik.keys():
            slownik[k] +=1
    slownik= dict(sorted(slownik.items()))
    return dict(slownik)
    file.close()
def poziomo():
    group_data = list((histogram().values()))
    group_names = list(histogram().keys())
    group_mean = np.mean(group_data)
    fig, ax = plt.subplots()
    ax.barh(group_names, group_data)
    plt.show()
def pionowo():
    max_value_of_data = max(histogram().values())

    group_data = list((histogram().values()))
    group_names = list(histogram().keys())
    np.mean(group_data)
    x = group_names
    y = group_data
    fig, ax = plt.subplots()
    plt.style.use('_mpl-gallery')

    ax.bar(x, y, width=0.20, edgecolor="white", linewidth=0)

    ax.set(xlim=(0, 10), xticks=np.arange(0, len(group_names)+1),
           ylim=(0, 10), yticks=np.arange(0, max_value_of_data, 4))

    plt.show()

odp = input("Wyswietl: 1 - pionowo , 2 - poziomo")

if odp == "1":
    pionowo()
elif odp == "2":
    poziomo()
else:
    print("zla wartosc")


