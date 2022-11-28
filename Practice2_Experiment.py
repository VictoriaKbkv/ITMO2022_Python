import statistics
import csv
import os
from timeit import default_timer as timer


def experiment_results(command, number_of_iterations):
    list = []
    for i in range(0, number_of_iterations):
        start = timer()
        os.system(command)
        end = timer()
        list.append(end - start)
    return list


def write_to_csv(header, list1, list2, list3, output_file):
    output = open(output_file, 'w', newline='')
    writer = csv.writer(output)
    writer.writerow(header)
    for i in range(0, len(list1)):
        row = []
        row.append(f"exp{i :3.0f}")
        row.append(list1[i])
        row.append(list2[i])
        row.append(list3[i])
        writer.writerow(row)
    writer.writerow(['min', min(list1), min(list2), min(list3)])
    writer.writerow(['max', max(list1), max(list2), max(list3)])
    writer.writerow(['mean', statistics.mean(list1), statistics.mean(list2), statistics.mean(list3)])
    writer.writerow(['median', statistics.median(list1), statistics.median(list2), statistics.median(list3)])
    writer.writerow(['standard deviation', statistics.stdev(list1), statistics.stdev(list2), statistics.stdev(list3)])



NUMBER = 50
HEADER = ['Desc', 'JAVA double', 'JAVA BigDecimal', 'Python float']
file_results = r"C:\Users\Victoria\Documents\ITMO_Course\Python\ITMO2022_Python\Files_Practice2\Results.csv"
java_double_command = r'cmd /c "java -cp C:\Users\Victoria\Documents\ITMO_Course\Python\Practice2\JAVA_DGEMM\out\production\JAVA_DGEMM\ Main"'
java_bigdecimal_command = r'cmd /c "java -cp C:\Users\Victoria\Documents\ITMO_Course\Python\Practice2\JAVA_DGEMM\out\production\JAVA_DGEMM\ BigDecimalMain"'
python_float_command = r'cmd /c "C:\Users\Victoria\Documents\ITMO_Course\ITMO2022_Python\Scripts\python.exe C:\Users\Victoria\Documents\ITMO_Course\Python\ITMO2022_Python\Practice2.py"'
java_double_list = experiment_results(java_double_command, NUMBER)
java_bigdecimal_list = experiment_results(java_bigdecimal_command, NUMBER)
python_float_list = experiment_results(python_float_command, NUMBER)
write_to_csv(HEADER, java_double_list, java_bigdecimal_list, python_float_list, file_results)
