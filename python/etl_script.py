import csv
from statistics import mean
import sys


def clean_name(str):
    split_arr = str.split("#")
    return split_arr[1]

def drop_empty_row(arr):
    for row in arr:
        if len(row) == 0:
            arr.remove(row)

results_arr = []
results_dict = {}

with open("python/data.csv") as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        results_arr.append(row)

    drop_empty_row(results_arr)

    i = 1
    for name in results_arr[0][1:]:
        temp_arr = []

        for val in results_arr[1:]:            
            if len(val[i]) != 0:
                temp_arr.append(float(val[i]))
            # if len(val[i]) == 0:
            #     temp_arr.append(None)
            # else:
            #     temp_arr.append(float(val[i]))
        
        results_dict[clean_name(name)] = temp_arr
        i = i + 1

    print(results_dict)