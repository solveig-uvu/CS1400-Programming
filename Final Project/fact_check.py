"""
This module was created to make a simplified data sheet of presidents provided in a file formatted to work with it, calculate the job market's growth in their term of office, 
and output the data it creates either to the console or to a specified text file.

How to use: Open a command prompt, and use 'python3 fact_check.py <presidents_file> <term_datasheet> [output_file]' (output_file is NOT required for it to function.)
"""

import csv
import sys

# Function to read provided file's list of presidents, as long as the file is formatted correctly, return a list of dictionaries about each president.
def read_presidents(filename:str='presidents.txt') -> list:
    presidents = []
    
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()

            # Splits president name and party information from their term start and end dates.
            pres_info, pres_term = line.split(' | ')
            pres_name, pres_party = pres_info.split(' (')
            pres_party = pres_party.strip(')')
            if pres_party == 'R': pres_party = 'Republican'
            else: pres_party = 'Democrat'

            # Formatting president's term beginning to it's end.
            pres_start, pres_end = pres_term.split(' - ')
            pres = {'name': pres_name, 'party': pres_party, 'term_start': pres_start, 'term_end': pres_end}
            presidents.append(pres)
    return presidents

# Read a provided CSV file's datasheet, as long as the file is formatted correctly, returns a list of data about jobs produced for each year.
def read_data(filename:str='BLS_private.csv') -> list:
    data = []

    # Using a DictReader from python's built-in CSV functionality to return each year as a dictionary, and appending the dictionary to the list of data.
    with open(filename, 'r') as f:
        if filename.endswith('.csv'):
            reader = csv.DictReader(f)
            for line in reader:
                data.append(line)
            return data        
        else:
            return None
        
# Helper function for getting jobs produced from a specific president's term.
def term_produced_jobs(datasheet:list, term_start:str, term_end:str) -> list:
    produced_jobs = []
    months = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
    start_month, start_year = term_start.split(' ')
    end_month, end_year = term_end.strip().split(' ')
    try:
        for num_month, month_name in months.items():
            if month_name == start_month:
                start_month_num = num_month        
        for num_month, month_name in months.items():
            if month_name == end_month:
                end_month_num = num_month
    except Exception as exception:
        print(f"Error: {exception}")

    for row in datasheet:
        year = row['Year']
        # Skips the outside range of years
        if year < start_year or year > end_year:
            continue
        
        # Skips the outside range for months
        for month in range(12):
            month_pos = month + 1
            months_name = months[month_pos]
            if year == start_year and month_pos < start_month_num:
                continue
            if year == end_year and month_pos > end_month_num:
                continue
            value = int(row.get(months_name))
            if value is not None:
                produced_jobs.append(value)       
    return produced_jobs

# Helper function for calculating how much the job market has grown in a term.
def calculate_term_growth(job_production:list) -> dict:
    if not job_production:
        return None
    # Calculations for growth
    growth = job_production[-1] - job_production[0]
    percent_growth = (growth / job_production[0]) * 100 if job_production[0] > 0 else 0
    average_growth = sum(job_production) / len(job_production)
    return {'average_growth': average_growth, 'starting_jobs': job_production[0], 'ending_jobs': job_production[-1], 'growth': growth, 'growth_percent': percent_growth, 'data_points': len(job_production)}

# Function to write all the data to a file, will write to console if no file is specified.
def write_to_file(presidents:list, datasheet:list, output_file=None) -> None:
    lines = []
    lines.append("Analysis on Jobs Created in Selected Time Frame")
    lines.append("=" * 50 + "\n")

    results = []
    # Calculating each president's produced jobs and formatting it for writing.
    for president in presidents:
        lines.append(f"\n{president['name']} ({president['party']}) - {president['term_start']} to {president['term_end']}")

        produced_jobs = term_produced_jobs(datasheet, president['term_start'], president['term_end'])
        calculations = calculate_term_growth(produced_jobs)

        if calculations:
            lines.append(f"   Term Period: {president['term_start']} to {president['term_end']}")
            lines.append(f"   Average Growth: {calculations['average_growth']:,.0f}")
            lines.append(f"   Starting Jobs: {calculations['starting_jobs']:,.0f}")
            lines.append(f"   Ending Jobs: {calculations['ending_jobs']:,.0f}")
            lines.append(f"   Net Change: {calculations['growth']:,.0f} - {calculations['growth_percent']:.2f}%")
            lines.append(f"   Months in Office: {calculations['data_points']} months")

            results.append({'President': president['name'], 'Party': president['party'], 'Avg Employment': calculations['average_growth'], 'Start': calculations['starting_jobs'], 'End': calculations['ending_jobs'], 'Net Change': calculations['growth'], 'Percent Change': calculations['growth_percent']})
        else:
            lines.append("   No data available for this period.")
        
        # Summary Comparison for quick analysis
    lines.append('\n' + '=' * 50)
    lines.append('Summary Comparison\n' + '=' * 50)

    if results:
        lines.append('\n Job Market Growth by President')
        lines.append(f"{'President':<30} {'Party':<12} {'Net Change':>15} {'% Change':>12}\n" + '-' * 70)
        for result in results:
            lines.append(f'{result['President']:<30} {result['Party']:<12} {result['Net Change']:>15,.0f} {result['Percent Change']:>11.2f}%')
    
    # Calculating average job market growth by party
    lines.append('\n\nAverage Growth by Party:')

    republican_results = [result for result in results if result['Party'] == 'Republican']
    democrat_results = [result for result in results if result['Party'] == 'Democrat']

    if republican_results:
        avg_growth = sum(result['Net Change'] for result in republican_results) / len(republican_results)
        avg_percent = sum(result['Percent Change'] for result in republican_results) / len(republican_results)
        lines.append(f"   Republican: {avg_growth:,.0f} -- {avg_percent:.2f}%")
    if democrat_results:
        avg_growth = sum(result['Net Change'] for result in democrat_results) / len(democrat_results)
        avg_percent = sum(result['Percent Change'] for result in democrat_results) / len(democrat_results)
        lines.append(f"   Democrat: {avg_growth:,.0f} -- {avg_percent:.2f}%")
    
    # Outputting the analysis
    analysis_text = '\n'.join(lines)

    if output_file:
        with open(output_file, 'w') as f:
            f.write(analysis_text)
        print(f"Analysis saved to {output_file}.")
    else:
        print(analysis_text)

def main():    
    if len(sys.argv) >= 5 or len(sys.argv) < 3:
        print("Usage: python3 fact_check.py <presidents_file> <term_datasheet> [output_file]")
        sys.exit(1)
    elif len(sys.argv) == 4:
        try:
            # Loading arguments given
            presidents = read_presidents(sys.argv[1])
            datasheet = read_data(sys.argv[2])
            write_to_file(presidents, datasheet, sys.argv[3])
        # Handling exceptions
        except FileNotFoundError as exception:
            print(f"Error: Couldn't find file - {exception}")
        except Exception as exception:
            print(f"Error: {exception}")
    elif len(sys.argv) == 3:
        try:
            presidents = read_presidents(sys.argv[1])
            datasheet = read_data(sys.argv[2])
            write_to_file(presidents, datasheet, None)

        except FileNotFoundError as exception:
            print(f"Error: Couldn't find file - {exception}")
        except Exception as exception:
            print(f"Error: {exception}")


if __name__ == '__main__':
    main()