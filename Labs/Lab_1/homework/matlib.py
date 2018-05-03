from matplotlib import pyplot

#1 preprare data
machine_counts = [18, 4, 2]

#2 labels
machine_labels = ["PC", "MAC", "linux"]

#3 Draw pie
pyplot.pie(machine_counts, labels = machine_labels, autopct = "%.1f%%", shadow = True, explode = [0.2, 0, 0])
pyplot.axis("equal")
pyplot.title("PC vs MAC vs Linux usage")
#4 Show chart
pyplot.show()