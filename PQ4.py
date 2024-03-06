# Write a Python function to check whether a distinct pair of numbers whose product is odd is present in a sequence of integer values.

def oddproduct(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                product = int(nums[i]) * int(nums[j])
                if product % 2 != 0:
                    return True
    return False

lists = input("Enter a list of numbers separated by space: ")
numbers = lists.split()
print(oddproduct(numbers))
