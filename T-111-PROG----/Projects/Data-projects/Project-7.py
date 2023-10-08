"""
reads numbers from file, splits by whitespaces
and adds year and consumer price index to a tuple

"""
def read_numbers_from_file(filename):
    cpi_data_list = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.split()
            year_month = parts[0]
            cpi_value = float(parts[-1])
            data_tuple = (year_month, cpi_value)
            cpi_data_list.append(data_tuple)
    return cpi_data_list

"""
    Computes yearly consumer price index using def read_numbers_from_file
    The dictionary allows me to access a given year and its corresponding value without iterating through the entire file.
"""
def yearly_cpi(cpi_data):
    yearly_cpi_dict = {} 

    for grouped_data in cpi_data:
        year_month, cpi_value = grouped_data
        year = int(year_month[:4])

        if year not in yearly_cpi_dict:
            yearly_cpi_dict[year] = []
        yearly_cpi_dict[year].append(cpi_value)

    return yearly_cpi_dict

"""
computes first and last value for each year using def yearly_cpi compute first and last value using idnexing

"""
def compute_first_last_values(yearly_cpi_dict):
    first_last_cpi = {}
    for year, cpi_values in yearly_cpi_dict.items():
        first_value = cpi_values[0]
        last_value = cpi_values[-1]
        first_last_cpi[year] = (first_value, last_value)

    return first_last_cpi

"""
Computes inflation rate for each year using def compute_first_last_value and returns inflation rate

"""
def compute_inflation_rate(first_last_values_dict):
    inflation_rates = {}
    for year, (first_value, last_value) in first_last_values_dict.items():
        yearly_inflation_rate = ((last_value - first_value) / first_value) * 100
        inflation_rates[year] = yearly_inflation_rate
    return inflation_rates
"""
Prints the result of all functions
"""
def main():
    filename = input() 
    try:
        cpi_data_list = read_numbers_from_file(filename)
        
        yearly_data = yearly_cpi(cpi_data_list)
        first_last_values = compute_first_last_values(yearly_data)
        inflation_rates = compute_inflation_rate(first_last_values)
        
        for year_month, cpi_value in cpi_data_list:
            print(f"('{year_month}', {cpi_value})")

        for year, (first, last) in first_last_values.items():
            print(f"({year}, {first}, {last})")
        
        for year, yearly_inflation_rate in inflation_rates.items():
            print(f"({year}, {round(yearly_inflation_rate, 2)})")
    except FileNotFoundError:
            print()

if __name__ == "__main__":
    main()
