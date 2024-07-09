import csv

def read_csv_to_set(file_path: str) -> set:
    with open(file_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        return {tuple(row) for row in reader}

def compare_csv_files(file1: str, file2: str) -> bool:
    set1 = read_csv_to_set(file1)
    set2 = read_csv_to_set(file2)
    return set1 == set2

file1 = r'your/file1/location.csv'
file2 = r'your/file2/location.csv'

if compare_csv_files(file1, file2):
    print("The CSV files have the same content.")
else:
    print("The CSV files have different content.")