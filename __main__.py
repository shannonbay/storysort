import math
import time

import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button

from storysort.storysort import generate_run_array, is_sorted, story_sort


def isEven(x):
    return x % 2 == 0


def isPrime(n):
    if n <= 1:
        return False

    if n == 2:
        return True

    if isEven(n):
        return False

    for m in range(4, n, 2):
        print("  ", m, ": cos(", 2 * np.pi * n / m, ")=", math.cos(2 * np.pi * n / m))
        if math.isclose(math.cos(2 * np.pi * n / m), -1):
            return False

    return True


# Test the isPrime function
for i in range(1, 30):
    print(f"{i} is prime: {isPrime(i)}")

NUM_POINTS = 100


def cos(x, multiplier):
    return np.cos(2 * np.pi * multiplier / x) * (NUM_POINTS - x) / NUM_POINTS


def sin(x, multiplier):
    return np.sin(2 * np.pi * multiplier / x) * (NUM_POINTS - x) / NUM_POINTS


pi = np.pi
points = range(1, NUM_POINTS)
multipliers = np.linspace(1, 1000, num=50000)  # Generate 100 steps from 0 to 1

fig, ax = plt.subplots(figsize=(6, 6))  # Set the figure size

ax.set_xlim(-1.5, 1.5)  # Set x-axis limits
ax.set_ylim(-1.5, 1.5)  # Set y-axis limits

scatter = ax.scatter([], [], c=[], cmap=cm.rainbow)

text_label = ax.annotate(
    "",
    xy=(0, 0),
    xytext=(0.8, 0.8),
    textcoords="axes fraction",
    fontsize=12,
    bbox=dict(boxstyle="round", edgecolor="blue", facecolor="white"),
)

text_labels = []

for _ in range(NUM_POINTS):
    label = ax.text(0, 0, "", fontsize=10, ha="center", va="center")
    text_labels.append(label)

current_frame_idx = 0  # Initialize the current frame index


def update(frame):
    #    frame = current_frame_idx
    xpoints = [cos(p, frame) for p in points]
    ypoints = [sin(p, frame) for p in points]

    colors = np.linspace(0, 1, NUM_POINTS)  # Generate colors based on point index
    scatter.set_offsets(np.column_stack((xpoints, ypoints)))
    scatter.set_array(colors)
    text_label.set_text(str(int(frame)))  # Update the multiplier label

    plt.grid(True)
    for i, label in enumerate(text_labels):
        label.set_text(str(i))
        label.set_position((xpoints[i - 1], ypoints[i - 1]))


def step_forward(event):
    global current_frame_idx
    if current_frame_idx < len(multipliers) - 1:
        current_frame_idx += 1
        update(current_frame_idx)
        ani.event_source.stop()
        fig.canvas.draw()


def step_backward(event):
    global current_frame_idx
    if current_frame_idx > 0:
        current_frame_idx -= 1
        update(current_frame_idx)
        ani.event_source.stop()
        fig.canvas.draw()


ax_step_forward = plt.axes([0.81, 0.01, 0.1, 0.05])
ax_step_backward = plt.axes([0.7, 0.01, 0.1, 0.05])
btn_step_forward = Button(ax_step_forward, "Step Forward")
btn_step_backward = Button(ax_step_backward, "Step Backward")

btn_step_forward.on_clicked(step_forward)
btn_step_backward.on_clicked(step_backward)

ax.grid(which="both")

ani = FuncAnimation(fig, update, frames=multipliers, repeat=False, interval=50)
plt.show()
# Example usage
# input_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
input_array = [4, 1, 7, 2, 9, 3]
print("Starting story sort.  Unsorted:\n", input_array)
run_array = story_sort(input_array)
print("Run array:", run_array)
sorted_array = story_sort(input_array)
print(sorted_array)  # Output: [1, 2, 3, 4, 7, 9]
print("Finished story sort")

random_array = np.random.randint(low=1, high=100000, size=1000000)
print(random_array[1:5])

pre_sorted_array = sorted(random_array)
reverse_sorted_array = sorted(random_array, reverse=True)

print("Finished generating data - starting story_sort")
for array in [random_array]:  # , pre_sorted_array, reverse_sorted_array]:
    start_time = time.time()
    array_sorted = story_sort(array)
    elapsed_time = time.time() - start_time
    print("StorySort time: {:.2f} seconds".format(elapsed_time))
    # assert is_sorted(array_sorted)
    # print(len(array_sorted[1]))

for array in [random_array]:  # , pre_sorted_array, reverse_sorted_array]:
    start_time = time.time()
    array_sorted = sorted(array)
    elapsed_time = time.time() - start_time
    print("TimSort (Python sorted) Time for: {:.2f} seconds".format(elapsed_time))

n = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(n)
print(generate_run_array(n))

is_sorted([])
