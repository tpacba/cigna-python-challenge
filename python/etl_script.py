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

    min_val_unique_host = {}
    max_val_unique_host = {}
    avg_val_unique_host = {}

    for host_key in results_dict:
        min_val_unique_host[host_key] = min(results_dict[host_key])
        max_val_unique_host[host_key] = max(results_dict[host_key])
        avg_val_unique_host[host_key] = round(mean(results_dict[host_key]), 2)

    min_val_all_host = min(min_val_unique_host.values())
    max_val_all_host = max(max_val_unique_host.values())
    avg_val_all_host = round(mean(avg_val_unique_host.values()), 2)

    sys.stdout.write("The minimum value for each unique hostname: " + str(min_val_unique_host) + '\n')
    sys.stdout.write("The maximum value for each unique hostname: " + str(max_val_unique_host) + '\n')
    sys.stdout.write("The average value for each unique hostname: " + str(avg_val_unique_host) + '\n')
    sys.stdout.write("The minimum value for all hostnames: " + str(min_val_all_host) + '\n')
    sys.stdout.write("The maximum value for all hostnames: " + str(max_val_all_host) + '\n')
    sys.stdout.write("The average value for all hostnames: " + str(avg_val_all_host) + '\n')