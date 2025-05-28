import matplotlib.pyplot as plt

a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]
c = [5,4,6,2,3,1]
d = [4,5,6,7,8,9]
x = sorted(c)

plt.figure(figsize=(10,8))
plt.subplots_adjust(hspace=0.4, wspace=0.4)

#plot 1

plt.subplot(2,2,1)
plt.plot(a,b, marker=".", linestyle="--", color="red", label="red")
plt.title("Plot 1")
plt.xlabel("x=axis")
plt.ylabel("y=axis")
plt.grid()
plt.legend()

# graph 2

plt.subplot(2,2,2)
plt.plot(c,d, marker="v", linestyle="solid", color="blue", label="blue")
plt.title("graph 2")
plt.xlabel("x=axis")
plt.ylabel("y=axis")
plt.grid()
plt.legend()

# graph 3

plt.subplot(2,2,3)
plt.plot(a,c, marker="o", linestyle="-", color="cyan", label="cyan")
plt.title("Graph 3")
plt.xlabel("x=axis")
plt.ylabel("y=axis")
plt.grid()
plt.legend()

# graph 4

plt.subplot(2,2,4)
plt.plot(b,d, marker="^", linestyle="solid", color="pink", label="pink")
plt.title("Graph 4")
plt.xlabel("x=axis")
plt.ylabel("y=axis")
plt.grid()
plt.legend()

plt.suptitle("This is my first Graph", fontsize=14)

plt.savefig("mygraph.pdf")
plt.show()
