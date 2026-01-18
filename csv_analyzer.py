import os
import csv
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if len(sys.argv) > 1:
    file_path = sys.argv[1] # sample.csv말고 다른 파일 있으면 그 파일
else:
    file_path = os.path.join(BASE_DIR, "sample.csv") # 없으면 sample.csv

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

def extract_key(): # keyword 추출
    keywords = list(extract_columns().keys())
    return keywords

def count_row(): # 행 개수
    row_count = 0
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for _ in reader:
            row_count += 1
            
    return row_count

def find_min(a): # 최솟값 찾기
    values = extract_columns()[extract_key()[a]]
    min_value = min(values)
    return min_value

def find_max(a): # 최댓값 찾기
    values = extract_columns()[extract_key()[a]]
    max_value = max(values)
    return max_value
    
def cal_avg(a): # 평균 계산
    total = 0
    avg = 0
    values = extract_columns()[extract_key()[a]]
    for i in range(len(values)):
        total += values[i]
    
    avg = int(total) / int(len(values))
    return avg

if __name__ == "__main__":
    
    for i in range(len(extract_key())):
        print(f"Column: {extract_key()[i]}")
        print(f" - count: {count_row()}")
        print(f" - min: {find_min(i)}")
        print(f" - max: {find_max(i)}")
        print(f" - avg: {cal_avg(i)}\n")