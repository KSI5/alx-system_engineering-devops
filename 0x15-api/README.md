#  0x15-api :open_book:

## Overview 📜
This project involves working with RESTful APIs in Python to gather, manipulate, and export data. It includes three Python scripts, each designed to perform specific tasks. Below, you'll find a description of each script and its requirements.

## Scripts

### 0-gather_data_from_an_API.py
This script retrieves information about an employee's TODO list progress from a REST API and displays it on the standard output. It accepts an employee ID as a parameter and formats the output in a specific way. Requirements for this script include using the `requests` or `urllib` module and following the specified output format.

### 2-export_to_JSON.py
This script extends the functionality of the previous script by exporting the TODO list information for a given employee to a JSON file. It accepts an employee ID as a parameter, fetches the data from the API, and stores it in a JSON file. The script adheres to the format specified in the task.

### 3-dictionary_of_list_of_dictionaries.py
This script compiles information about multiple employees' TODO lists and organizes it into a specific data structure. It creates a dictionary of lists of dictionaries, where each employee's data is structured in a nested format. The script then exports this data to a JSON file, adhering to the specified format.

## How to Use 🔧
To run each script, follow the provided usage instructions in the script descriptions. The scripts accept command-line arguments, and you should provide the necessary input as per the requirements.

Please note that all scripts have been written with PEP8 style guidelines in mind and should be executed using Python 3.

## Requirements 📝
- Python 3.8.5
- `requests` or `urllib` module
- PEP8 style adherence
- Command-line arguments as specified in each script's description
- Internet connectivity to access the REST API

