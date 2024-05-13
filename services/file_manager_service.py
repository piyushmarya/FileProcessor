import csv
import os

from exceptions.custom_exceptions import NoInputDataException


class FileReader:
    def __init__(self, folder_path):
        """
        Initialize the FileReader with the specified folder path.
        """
        self.folder_path = folder_path

    def read_dat_files(self):
        """
        Read data from .dat files in the specified folder.
        Returns:
            list: A list containing data read from the .dat files.
        """
        data = []
        unique_id_set = set()
        try:
            for filename in os.listdir(self.folder_path):
                if not filename.endswith(".dat"):
                    continue
                file_path = os.path.join(self.folder_path, filename)
                with open(file_path, 'r') as file:
                    reader = csv.reader(file,delimiter='\t')
                    next(reader)  # Skip header
                    for row in reader:
                        if row[0] not in unique_id_set:
                            unique_id_set.add(row[0])
                            data.append(row)
        except Exception as e:
            print("Error occured while reading .dat files")
            raise e
        if not data:
            raise NoInputDataException
        return data
    
class CsvOperations:
    def write_csv_file(self, data, headers, file_path):
        """
        Write the data to a CSV file with the specified headers in the specified output folder.
        
        Args:
            data (list): A list containing the data to be written to the CSV file.
            headers (list): A list containing the headers for the CSV file.
            output_folder (str): The path to the output folder where the CSV file will be written.
        """
        try:
            with open(file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(data)
        except Exception as e:
            print(f"Error occured while writing CSV file")
            raise e
        
    def append_to_csv(self, data, file_path):
        """
        Append data to a CSV file.
        
        Args:
            data (list): A list containing the data to be written to the CSV file.
            output_folder (str): The path to the output folder where the CSV file will be written.
        """
        try:
            with open(file_path, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(data)
        except Exception as e:
            print("Error occured while appending to a CSV file")
            raise e