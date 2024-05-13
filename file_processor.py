import os
import argparse

from services.file_manager_service import FileReader, CsvOperations
from services.data_processor_service import DataProcessor

OUTPUT_FILE_NAME = "RESULT.csv"

class FileProcessor:
    def __init__(self, input_folder, output_folder):
        """
        Initialize the FileProcessor with input and output folder paths.
        
        Args:
            input_folder (str): The path to the folder containing input files.
            output_folder (str): The path to the folder where output files will be written.
        """
        self.input_folder = os.path.normpath(input_folder)
        self.output_folder = os.path.normpath(output_folder)

    def process_files(self):
        """
        Process input files and perform required operations.
        """
        try: 
            file_reader = FileReader(self.input_folder)
            data = file_reader.read_dat_files()

            output_file_path = os.path.join(self.output_folder, OUTPUT_FILE_NAME)

            data_processor = DataProcessor(data)
            data_processor.calculate_gross_salary()

            headers = ["id", "first_name", "last_name", "email", "job_title", "basic_salary", "allowances", "Gross Salary"]
            
            csv_writer = CsvOperations()
            csv_writer.write_csv_file(data_processor.data, headers, output_file_path)

            second_highest_salary, average_salary = data_processor.get_second_highest_and_average_salary()
            footer = ['second_highest_salary = {}'.format(second_highest_salary), 'average_salary = {}'.format(average_salary) ,'','','','', '']
            csv_writer.append_to_csv(footer, output_file_path)
        except Exception as e:
            print(f"Error occured {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process .dat files and output to CSV")
    parser.add_argument("--input-folder", required=True, help="Path to the folder containing input .dat files")
    parser.add_argument("--output-folder", required=True, help="Path to the folder where output CSV file will be written")
    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder
    # input_folder = r""
    # output_folder = r""
    processor = FileProcessor(input_folder, output_folder)
    processor.process_files()