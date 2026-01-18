import os
import csv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "sample.csv")

def extract_columns(): # 숫자 column 값
    columns = {}
    
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            for key, value in row.items():
                try:
                    value = float(value)
                    columns.setdefault(key, []).append(value)
                except ValueError:
                    pass
                
    return columns

def extract_key():
    keywords = list(extract_columns().keys())
    return keywords

def count_row(): # 행 개수
    row_count = 0
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for _ in reader:
            row_count += 1
            
    return row_count

def find_min(a):
    values = extract_columns()[extract_key()[a]]
    min_value = min(values)
    return min_value

def find_max(a):
    values = extract_columns()[extract_key()[a]]
    max_value = max(values)
    return max_value
    
def cal_avg():
    total = 0
    avg = 0
    return 0

if __name__ == "__main__":
    for i in range(3):
        print(f"Column: {extract_key()[i]}\n")
        print(f" - count: {count_row()}\n")
        print(f" - min: {find_min(i)}\n")
        print(f" - max: {find_max(i)}\n")
        print(f" - avg: {cal_avg()}")