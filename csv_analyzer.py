import os
import csv
import statistics

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "sample.csv")

def is_number(value): # 숫자인지 확인
    try:
        float(value)
        return value
    except ValueError:
        return False
    
def extract_colums(): # colums 값 추출
    columns = {}
    
    with open("sample.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            for key, value in row.items():
                try:
                    value = float(value)
                    columns.setdefault(key, []).append(value)
                except ValueError:
                    pass
                
    return columns

def count_row(): # 행 수 세기
    row_count = 0
    with open("sample.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        if reader != {}:
            next(reader) # 헤더 스킵
            for _ in reader:
                row_count += 1
    
        else:
            return False
        
    return row_count      

def find_min(): # 최솟값 찾기
    value = extract_colums().values()
    min_value = int(value[0]) # type: ignore
    for i in range(len(value)):
        if min_value > int(value[i]): # type: ignore
            min_value = int(value[i]) # type: ignore
        else:
            continue
        
    return min_value

def find_max(): # 최댓값 찾기
    value = extract_colums().values()
    max_value = int(value[0]) # type: ignore
    for i in range(len(value)):
        if max_value < int(value[i]): # type: ignore
            max_value = int(value[i]) # type: ignore
        else:
            continue
        
    return max_value

def cal_avg(): # 평균 계산
    value = extract_colums().values()
    total = 0
    average = 0
    for i in range(len(value)):
        total += int(value[i]) # type: ignore

    average = int(total / len(value))
    
    return average

if __name__ == "__main__":
    print(cal_avg())