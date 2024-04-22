
a = input("Enter the elements of box a separated by spaces: ").split()
b = input("Enter the elements of box b separated by spaces: ").split()
c = input("Enter the elements of box c separated by spaces: ").split()

totsum = 0

for box in [a, b, c]:
    box_sum = sum(map(int, box))  
    print("Sum of elements in box:", box_sum)
    totsum += box_sum

print("Total sum of all boxes:", totsum)

