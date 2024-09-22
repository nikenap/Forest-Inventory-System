# Forest Inventory System Utilizing CRUD Approach in Python

This system is designed to efficiently manage tree inventories in a forest plantation by utilizing the CRUD (Create, Read, Update, Delete) approach. It enables users to add, update, delete, and view tree data, along with calculating essential statistics based on key attributes like diameter, height, age, and volume.

The primary objective of this project is to streamline forest data management processes while providing insightful analyses to support decision-making regarding forest conditions and growth.

## Key Features

This forest inventory system includes six main features:

	• Feature 1: Add New Trees 
 Users can add a new tree by entering attributes such as genus, species, diameter, height, and age. The system automatically generates a unique tree ID and calculates the tree’s volume using a simplified volume formula.
 
	• Feature 2: Display Tree Inventory)
 The system displays all trees in the inventory with options to filter by specific attributes like genus, species, or age. This feature ensures easy navigation and quick retrieval of relevant data.
 
	• Feature 3: Edit Tree Data 
 Users can modify the attributes of an existing tree, such as updating its diameter or height. The system will automatically recalculate the tree’s volume based on these changes to ensure data consistency.
 
	• Feature 4: Delete Trees 
 Trees can be removed from the inventory, typically when they have been harvested or no longer exist. The system ensures that users confirm deletions before proceeding to prevent accidental removals.
 
	• Feature 5: Summary Statistics 
 The system provides summary statistics such as the average, maximum, and minimum values for tree attributes (diameter, height, age, and volume). Additionally, it calculates the total volume of trees in the inventory, helping plantation managers make informed decisions.
 
	• Feature 6: Exit Program 
 Users can exit the program at any time, with their data being preserved until the next session.

 ## Technical Highlights

	•	ID Generation:
Each tree is automatically assigned a unique ID based on the first three letters of its genus and species, followed by a sequential number to ensure that each ID is distinct.

	•	Volume Calculation:
Tree volume is calculated using the formula:
Volume = 0.25 × π × (diameter² / 10000) × height
This provides a basic estimate of tree volume in cubic meters, aiding in forestry resource assessments.

	•	Input Validation:
The system includes robust input validation for string, integer, and float inputs to ensure that only valid data is stored in the inventory. This improves the integrity of the system and prevents errors caused by incorrect data entries.

## Project Objective

This project was developed as part of a capstone requirement for the Digital Talent Incubator Data Science and Machine Learning program at Purwadhika Digital Technology School. The aim was to create a functional and efficient tree inventory management system that automates data handling while incorporating fundamental concepts of data science and software development.

