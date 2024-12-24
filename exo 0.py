import math


people = int(input("How many people need a ride? "))
taxi_capacity = int(input("How many people can fit in one taxi? "))


taxis_needed = math.ceil(people / taxi_capacity)


print(f"You will need {taxis_needed} taxis to transport {people} people.")