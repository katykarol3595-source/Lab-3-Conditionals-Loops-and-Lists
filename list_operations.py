# Creates a list of at least 5 integers
numbers = [42, 12, 89, 5, 23]
#Prints the original list
print("Original list:", numbers)
#Uses the built-in sorted() function to print a sorted version of the list without modifying the original list
sorted_version = sorted(numbers)
print("Sorted list (using sorted()):", sorted_version)
print("Original list remains unchanged:", numbers)
#Uses the list’s .sort() method to sort the list in place, then prints the list to show it is now sorted.
numbers.sort()
print("Sorted in place (.sort()):", numbers)
#Adds a new element to the list (append an integer), then prints the updated list.
numbers.append(99)
print("After appending 99:", numbers)
#Removes an element from the list, then prints the list again.
numbers.remove(12)
print("After removing 12:", numbers)
#Uses the reverse() method to reverse the list, then prints the reversed list.
numbers.reverse()
print("Reversed list:", numbers)
