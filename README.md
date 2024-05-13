# File Processor Design Specification

## Overview
The File Processor is a system designed to read data from multiple `.dat` files located in a specified folder. It process the data, and output the result to a CSV file in another folder. The system also calculates the 2nd highest salary and the average salary, adding them as a footer to the output CSV file.

## Components
1. **FileReader**: Responsible for reading data from `.dat` files in the input folder.
2. **DataProcessor**: Processes the input data, calculating the data required for CSV insertion.
3. **CsvOperations**: Consists CSV write & append operations.
4. **custom_exceptions**: Consists of custom exceptions required by FileProcessor
5. **FileProcessor**: Orchestrates the entire process, utilizing instances of the above components.

## Workflow
1. **FileReader** reads data from `.dat` files in the input folder and returns it as a list.
2. **DataProcessor** calculates the gross salary for each entry in the data.
3. **CsvOperations** writes the processed data to a CSV file with the specified headers.
4. **DaraProcessor** Calculates the 2nd highest salary and the average salary.
5. **CsvOperations** Appends the 2nd highest salary and the average salary to the created CSV
6. **FileProcessor** Orchestrates the entire process by calling methods of the above components in the correct sequence.

## Dependencies
- Python 3.x
- Standard Library modules: os, csv, argparse

## Usage
1. python .\file_processor.py --input-folder input_folder_name --output-folder ouput_folder_name
2. Create an instance of `FileProcessor` with input and output folder paths.
3. Call the `process_files()` method of `FileProcessor` to execute the file processing workflow.

## Outcomes
Ensure no duplicate data is present in the output file.
Verify that the calculated 2nd highest salary and average salary in the footer are accurate.
