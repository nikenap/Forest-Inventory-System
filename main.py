
# Initialize Forest Inventory Data with Some Trees
forest = {
    'ACACRA01': {'genus' : 'Acacia', 'species': 'crassicarpa', 'diameter': 20.0, 'height': 16.0, 'age': 4, 'volume': 0.50},
    'ACAMAN01': {'genus' : 'Acacia', 'species': 'mangium', 'diameter': 18.0, 'height': 15.0, 'age': 4, 'volume': 0.38},
    'EUCPEL01': {'genus' : 'Eucalyptus', 'species': 'pellita', 'diameter': 5.2, 'height': 4.8, 'age': 1, 'volume': 0.01},
    'EUCDEG01': {'genus' : 'Eucalyptus', 'species': 'deglupta', 'diameter': 10.0, 'height': 9.4, 'age': 2, 'volume': 0.07},
    'ACAAUR01': {'genus' : 'Acacia', 'species': 'auriculiformis', 'diameter': 10.3, 'height': 11.9, 'age': 3, 'volume': 0.10},
    'EUCALB01': {'genus' : 'Eucalyptus', 'species': 'alba', 'diameter': 8.2, 'height': 9.5, 'age': 2, 'volume': 0.05},
    'ACACRA02': {'genus': 'Acacia', 'species' : 'crassicarpa', 'diameter': 10.6, 'height': 10.4, 'age': 3, 'volume': 0.09},
    'ACAMAN02': {'genus': 'Acacia', 'species' : 'mangium', 'diameter': 4.0, 'height': 4.5, 'age': 1, 'volume': 0.01},
    'EUCPEL02': {'genus': 'Eucalyptus', 'species' : 'pellita', 'diameter': 17.0, 'height': 12.0, 'age': 4, 'volume': 0.27},
    'EUCDEG02': {'genus': 'Eucalyptus', 'species' : 'deglupta', 'diameter': 6.4, 'height': 7.0, 'age': 2, 'volume': 0.02},
    'ACAAUR02': {'genus': 'Acacia', 'species' : 'auriculiformis', 'diameter': 9.5, 'height': 9.8, 'age': 3, 'volume': 0.07},
    'EUCALB02': {'genus' : 'Eucalyptus', 'species': 'alba', 'diameter': 3.5, 'height': 3.6, 'age': 1, 'volume': 0.00}
}

# Helper Functions 
def get_string_input(prompt, allow_numbers=False):
    while True:
        value = input(prompt).strip()
        # Check if the input is empty or contains invalid characters
        if value == "" or (not allow_numbers and not value.isalpha()):
            print("Invalid input. Please enter a valid string.")
        else:
            return value # Return the original input if valid
        
def get_string_int_input(prompt, allow_numbers=True):
    while True:
        value = input(prompt).strip()
        if value == "" or (not allow_numbers and not value.isalnum()):
            print("Invalid input. Please enter a valid string or number combination.")
        else:
            return value

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid float value.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid integer value.") 
    
def calculate_tree_volume(diameter, height):
    # Simplified tree volume calculation
    # Volume = 0.25 x 3.1416 x ((diameter^2)/10000) x height (in cubic meter)
    volume = 0.25 * 3.1416 * ((diameter ** 2)/10000) * height
    return volume

def generate_tree_id(forest, genus, species):
    genus_part = genus[:3].upper()
    species_part = species[:3].upper()
    count = sum(1 for key, value in forest.items() if value['genus'] == genus and value['species'] == species)
    tree_number = str(count + 1).zfill(2)
    return f"{genus_part}{species_part}{tree_number}"

def print_tree(tree_id, tree):
    # Display the searched tree data in table format
    print(f"\n{'ID':<10} {'Genus':<10} {'Species':<15} {'Diameter (cm)':>15} {'Height (m)':>15} {'Age (years)':>12} {'Volume (m³)':>15}")
    print("-" * 90)
    print(f"{tree_id:<10} {tree['genus']:<10} {tree['species']:<15} {tree['diameter']:>15.2f} {tree['height']:>15.2f} {tree['age']:>12} {tree['volume']:>15.2f}")

def print_filtered_trees(filtered_trees):
    # Print table headers 
    print(f"\n{'ID':<10} {'Genus':<10} {'Species':<15} {'Diameter (cm)':>15} {'Height (m)':>15} {'Age (years)':>12} {'Volume (m³)':>15}")
    print("-" * 90)
    # Print tree data
    for tree_id in filtered_trees:
        tree_data = forest[tree_id]
        print(f"{tree_id:<10} {tree_data['genus']:<10} {tree_data['species']:<15} {tree_data['diameter']:>15.2f} {tree_data['height']:>15.2f} {tree_data['age']:>12} {tree_data['volume']:>15.2f}")

# Function for The Main Menu
def main_menu():
    while True:
        print("\nPT Sustainable Plantation Forest")
        print("Forest Inventory Data")
        print("\nMain Menu:")
        print("1. Add New Tree")
        print("2. Show Forest Inventory List")
        print("3. Edit Tree Attributes")
        print("4. Delete Dead/Harvested Tree")
        print("5. Display Statistics Summary")
        print("6. Exit Program")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            menu_1()
        elif choice == '2':
            menu_2()
        elif choice == '3':
            menu_3()
        elif choice == '4':
            menu_4()
        elif choice == '5':
            menu_5()  
        elif choice == '6':
            print("Exiting the program. Good bye!")
            break
        else:
            print("\nInvalid choice. Please enter a valid number (1-6).")

# Function for Menu 1: Add New Tree
def menu_1():
    while True:
        print("\nMENU 1: ")
        print("1. Add A New Tree")
        print("2. Back to Main Menu")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == '1':
            genus = get_string_input("Enter Genus: ")
            species = get_string_input("Enter Species: ")
            diameter = get_float_input("Enter Diameter (in cm): ")
            height = get_float_input("Enter Height (in meters): ")
            age = get_int_input("Enter Age (in years): ")

            # Calculate tree volume
            volume = calculate_tree_volume(diameter, height)  

            # Generate ID for the new tree
            tree_id = generate_tree_id(forest, genus, species)
            
            # Show the data in a table format
            print("\nTree Information:")
            print(f"{'ID':<10} {'Genus':<10} {'Species':<15} {'Diameter (cm)':>13} {'Height (m)':>10} {'Age (years)':>12} {'Volume (m³)':>13}")
            print("-" * 90)
            print(f"{tree_id:<10} {genus:<10} {species:<15} {diameter:>13.2f} {height:>10.2f} {age:>12} {volume:>13.2f}")
            
            # Confirm save
            save_choice = input("\nSave data? (yes/no): ").lower()
            if save_choice == 'yes':
                forest[tree_id] = {
                    "genus": genus.capitalize(),
                    "species": species.lower(),
                    "diameter": diameter,
                    "height": height,
                    "age": age,
                    "volume": volume
                }
                print("\nData successfully saved.")
            else:
                print("\nData not saved.")
        
        elif choice == '2':
            print("\nReturning to main menu.")
            break  # Exit to main menu loop
        else:
            print("Invalid choice. Please enter a valid number (1-2).")

# Function for Menu 2: Display Forest Inventory List
def menu_2():
    while True:
        print("\nMENU 2: ")
        print("1. Display All Data")
        print("2. Filter Data by Attributes")
        print("3. Search Data by ID")
        print("4. Back to Main Menu")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            # Display all data
            if not forest:
                print("No data available in the forest inventory.")
            else:
                # Print table headers 
                print(f"{'ID':<10} {'Genus':<10} {'Species':<15} {'Diameter (cm)':>15} {'Height (m)':>15} {'Age (years)':>12} {'Volume (m³)':>15}")
                print("-" * 90)  # Separator line
                
                # Print tree data
                for tree_id, tree_data in forest.items():
                    print(f"{tree_id:<10} {tree_data['genus']:<10} {tree_data['species']:<15} {tree_data['diameter']:>15.2f} {tree_data['height']:>15.2f} {tree_data['age']:>12} {tree_data['volume']:>15.2f}")
            
        elif choice == '2':
            print("\nFilter Data by Attributes")
            print("1. Genus")
            print("2. Species")
            print("3. Age")
            print("4. Back to Previous Menu")
            
            filter_choice = input("Enter your filter choice (1-3): ")
            
            if filter_choice == '1':
                # Filter by genus
                genus = get_string_input("Enter Genus: ").capitalize()
                filtered_trees = [tree_id for tree_id, tree_data in forest.items() if tree_data['genus'] == genus]
                if filtered_trees:
                    print_filtered_trees(filtered_trees)
                else:
                    print(f"\nNo trees with genus {genus} were found.")
                
            elif filter_choice == '2':
                # Filter by species
                species = get_string_input("Enter Species: ").lower()
                filtered_trees = [tree_id for tree_id, tree_data in forest.items() if tree_data['species'] == species]
                if filtered_trees:
                    print_filtered_trees(filtered_trees)
                else:
                    print(f"\nNo trees with species {species} were found.")
                
            elif filter_choice == '3':
                # Filter by age
                age = get_int_input("Enter Age to filter by (in years): ")
                filtered_trees = [tree_id for tree_id, tree_data in forest.items() if tree_data['age'] == age]
                if filtered_trees:
                    print_filtered_trees(filtered_trees)
                else:
                    print(f"\nNo trees found with Age {age}.")
            
            elif filter_choice == '4':
                print("\nReturning to previous menu.")
            else:
                print("Invalid choice. Please enter a valid number (1-4).")

        
        elif choice == '3':
            # Search data by ID
            tree_id = get_string_int_input("Enter Tree ID to search for: ").upper().strip()  # Ensure uppercase and remove extra spaces
            # Check if the tree ID exists in the forest dictionary
            if tree_id in forest:
                tree = forest[tree_id]  
                print_tree(tree_id, tree)
            else:
                print(f"No tree with ID {tree_id} was found. Please try again.")
        
        elif choice == '4':
            # Return to the main menu
            print("\nReturning to main menu.")
            break

        else:
            print("\nInvalid choice. Please enter a valid number (1-4).")

# Function for Menu 3: Edit Tree Attributes
def menu_3():
    while True:
        print("\nMENU 3: ")
        print("1. Edit A Specific Tree")
        print("2. Back to Main Menu")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == '1':
            # Update a specific tree
            tree_id = get_string_int_input("Enter Tree ID to search for: ").upper()

            if tree_id in forest:
                tree = forest[tree_id]
                # Display the tree to be edited
                print_tree(tree_id, tree)
                # Display attribute options to be updated
                print("\nChoose an attribute to update:")
                print("1. Diameter")
                print("2. Height")
                print("3. Back to Previous Menu")

                update_choice = input("Enter your choice (1-3): ")
                
                if update_choice == '1':
                    tree['diameter'] = get_float_input("Enter Diameter (in cm): ")
                elif update_choice == '2':
                    tree['height'] = get_float_input("Enter Height (in meters): ")
                elif update_choice == '3':
                    print("\nReturning to previous menu.")
                    continue

                # Recalculate volume
                tree['volume'] = calculate_tree_volume(tree['diameter'], tree['height'])
                print(f"\nUpdated Tree Data:")
                print_tree(tree_id, tree)
                print(f"\nTree data for {tree_id} successfully updated.")
            else:
                print(f"No tree with ID {tree_id} found. Please try again")

        elif choice == '2':
            print("\nReturning to main menu.")
            break
        else:
            print("Invalid choice. Please enter a valid number (1-2).")

# Function for Menu 4: Delete Harvested/Dead Tree
def menu_4():
    while True:
        print("\nMENU 4: ")
        print("1. Delete A Specific Tree")
        print("2. Back to Main Menu")
        
        choice = input("Enter your choice (1-2): ")
        
        if choice == '1':
            # Delete a specific tree
            tree_id = get_string_int_input("Enter Tree ID to delete: ").upper()
            if tree_id in forest:
                # Display the tree to be deleted
                print_tree(tree_id, forest[tree_id])
                # Confirm deletion
                confirm = input(f"Are you sure you want to delete tree {tree_id}? (yes/no): ").lower()
                if confirm == 'yes':
                    del forest[tree_id]
                    print(f"Tree {tree_id} deleted successfully.")
                else:
                    print("Deletion canceled. Returning to menu")
            else:
                print(f"No tree with ID {tree_id} found. Please try again")

        elif choice == '2':
            # Return to the main menu
            print("\nReturning to main menu.")
            break

        else:
            print("\nInvalid choice. Please enter a valid number (1-2).")

# Funtion for Menu 5: Display Statistics Summary
def menu_5():
    while True:
        print("\nMENU 5: ")
        print("1. Statistics Summary")
        print("2. Back to Main Menu")
        
        choice = input("Enter your choice (1-2): ")

        if choice == '1':
            if not forest:
                print("\nNo data available in the forest inventory to calculate statistics.")
                continue

            else:
                # Choose the attribute to calculate statistics on
                print("\nChoose an attribute to calculate statistics:")
                print("1. Diameter")
                print("2. Height")
                print("3. Age")
                print("4. Tree Volume")
                print("5. Back to Previous Menu")
                
                attribute_choice = input("Enter your choice (1-5): ")

                if attribute_choice == '1':
                    attribute = 'diameter'
                elif attribute_choice == '2':
                    attribute = 'height'
                elif attribute_choice == '3':
                    attribute = 'age'
                elif attribute_choice == '4':
                    attribute = 'volume'
                elif attribute_choice == '5':
                    print("\nReturning to previous menu.")
                    continue
                else:
                    print("\nInvalid choice for attribute.")
                    continue  # Return to the main loop

                # Proceed with statistics calculation only for valid attributes
                if attribute in ['diameter', 'height', 'age', 'volume']:
                    print("\nChoose the statistic to calculate:")
                    print("1. Average")
                    print("2. Maximum")
                    print("3. Minimum")
                    print("4. Sum (only for Tree Volume)")
                    statistic_choice = input("Enter your choice (1-4): ")

                    # Handle sum operation only for volume
                    if statistic_choice == '4' and attribute != 'volume':
                        print("\nSum is only valid for Tree Volume. Please select a different statistic.")
                        continue  # Return to the statistics selection

                    if statistic_choice == '1':
                        # Calculate average
                        total_value = sum(tree[attribute] for tree in forest.values())
                        average_value = total_value / len(forest)
                        print(f"\nAverage {attribute.capitalize()} for all trees: {average_value:.2f}")
                    
                    elif statistic_choice == '2':
                        # Calculate maximum
                        max_value = max(tree[attribute] for tree in forest.values())
                        print(f"\nMaximum {attribute.capitalize()} for all trees: {max_value:.2f}")
                    
                    elif statistic_choice == '3':
                        # Calculate minimum
                        min_value = min(tree[attribute] for tree in forest.values())
                        print(f"\nMinimum {attribute.capitalize()} for all trees: {min_value:.2f}")
                    
                    elif statistic_choice == '4' and attribute == 'volume':
                        # Sum tree volume (valid only for volume)
                        total_volume = sum(tree['volume'] for tree in forest.values())
                        print(f"\nSum of tree volumes: {total_volume:.2f} cubic meters")

                    else:
                        print("\nInvalid choice or incompatible statistic for the selected attribute.")
                else:
                    print("\nInvalid attribute selected. Please try again.")
            
        elif choice == '2':
            # Return to the main menu
            print("\nReturning to main menu.")
            break

        else:
            print("\nInvalid choice. Please enter a valid number (1-2).")
            
# Run The Main Menu
main_menu()
