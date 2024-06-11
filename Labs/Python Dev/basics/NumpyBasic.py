import numpy as np

data_array = np.array([])

while True:
    print("\nMenu:")
    print("1. Add a number to the array")
    print("2. Remove a number from the array")
    print("3. Display the array")
    print("4. Calculate the mean")
    print("5. Calculate the median")
    print("6. Calculate the mode")
    print("7. Calculate the standard deviation")
    print("8. Sort the array")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        number = float(input("Enter a number to add: "))
        data_array = np.append(data_array, number)
        print(f"{number} has been added to the array.")   
    elif choice == '2':
        number = float(input("Enter a number to remove: "))
        if number in data_array:
            data_array = np.delete(data_array, np.where(data_array == number))
            print(f"{number} has been removed from the array.")
        else:
            print(f"{number} is not in the array.")
    elif choice == '3':
        print("Current array:", data_array)     
    elif choice == '4':
        if data_array.size > 0:
            mean = np.mean(data_array)
            print("Mean:", mean)
        else:
            print("The array is empty.")          
    elif choice == '5':
        if data_array.size > 0:
            median = np.median(data_array)
            print("Median:", median)
        else:
            print("The array is empty.")            
    elif choice == '6':
        if data_array.size > 0:
            values, counts = np.unique(data_array, return_counts=True)
            index = np.argmax(counts)
            mode = values[index]
            if counts[index] > 1:
                print("Mode:", mode)
            else:
                print("No unique mode found.")
        else:
            print("The array is empty.")           
    elif choice == '7':
        if data_array.size > 0:
            std_dev = np.std(data_array)
            print("Standard Deviation:", std_dev)
        else:
            print("The array is empty.")          
    elif choice == '8':
        data_array = np.sort(data_array)
        print("The array has been sorted.")        
    elif choice == '9':
        print("Exiting the program.")
        break     
    else:
        print("Invalid choice. Please select a number between 1 and 9.")
