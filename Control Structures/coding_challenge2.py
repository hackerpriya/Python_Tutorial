"""
Coding challenge part 2.

Create a list of your favorite food items, the list should have minimum 5 elements.
List out the 3rd element in the list.
Add additional item to the current list and display the list.
Insert an element named tacos at the 3rd index position of the list and print out the list elements.
"""

food =["Pizza","Pasta","Dosa","Rajma","Noodles"]
print("Third element=",food[2])
food.append("Momos")
print("Display list=",food)
food.insert(3,'tacos')
print("Display list=",food)
