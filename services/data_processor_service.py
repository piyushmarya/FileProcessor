class DataProcessor:
    def __init__(self, data):
        """
        Initialize the DataProcessor with the data.
        """
        self.data = data

    def calculate_gross_salary(self):
        """
        Calculate the gross salary for each entry in the data.
        Args:
            data (list): A list containing the input data.
        Returns:
            list: A list containing the processed data with gross salary calculated.
        """
        for row in self.data:
            try:
                basic_salary = float(row[5])
                allowances = float(row[6])
                gross_salary = basic_salary + allowances
                row.append(int(gross_salary))
            except Exception as e:
                print(e)
    
    def get_second_highest_and_average_salary(self):
        """
        Calculates second highest and average salaries
        Returns:
            list: A list containing the 2nd highest salary and average salary
        """
        gross_salaries = [row[7] for row in self.data]
        gross_salaries.sort(reverse=True)
        second_highest_salary = gross_salaries[1]
        average_salary = sum(gross_salaries) / len(gross_salaries)

        return second_highest_salary, average_salary