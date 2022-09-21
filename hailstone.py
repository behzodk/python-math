from sqlite3 import Cursor
from turtle import color
import matplotlib.pyplot as plt
from matplotlib.widgets import Cursor

a = input("Enter anumber: ")

s = []
numbers = []

x = eval(a)
if x ==1:
    print(1)
    exit()
while x!=1:
    s.append(int(x))
    if x%2==0:
        x=x/2
    else:
        x=x*3+1
print(f"Number: {eval(a)}\nHailstone sequence: {s}\nMoves to get 1: {len(s)}\nHighest: {max(s)}")
for i in range(len(s)):
    numbers.append(i+1)

fig = plt.figure()
ax = fig.subplots()
ax.plot(numbers, s, color='b')
ax.grid()
cursor = Cursor(ax, horizOn=True, vertOn=True, useblit=True, color='r', linewidth=1)
annot = ax.annotate("", xy=(0,0), xytext=(-40,40),textcoords="offset points", bbox=dict(boxstyle="round4",fc='linen', ec='k', lw=1),arrowprops = dict(arrowstyle='-|>'))
annot.set_visible(False)
coord=[]
def onclick(event):
    global coord
    coord.append((event.xdata, event.ydata))
    x = event.xdata
    y = event.ydata
    print([x,y])
    annot.xy=(x,y)
    text=f'{x,y}'
    annot.set_text(text)
    annot.set_visible(True)
    fig.canvas.draw()
fig.canvas.mpl_connect("button_press_event", onclick)
plt.show()
