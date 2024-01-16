import matplotlib.pyplot as plt
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]

#slope:
m = 8
#intercept:
b = 40
plt.title("Sandra's Lemonade Stand")
plt.xlabel("Months")
plt.ylabel("Revenue (€)")
plt.plot(months, revenue, "o")

y=[]

for i in range(len(months)):
  y_predicted=months[i]*m+b
  y.append(y_predicted)
  print(y)

plt.plot(months, y, "-")
plt.show()


