def num_check(question):

    error = "Please enter a number more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

#Main Routine starts here...

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("Width (m): ")
    height = num_check("Height (m): ")
    cost = num_check("Cost per meter: ")

    # Calculate / perimeter
    perimeter = 2 * (width + height)
    total = perimeter * cost

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Total cost ($): {total:.2f} dollars")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any other key to quit. ")
    print()
