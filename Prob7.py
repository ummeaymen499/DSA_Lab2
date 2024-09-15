import csv
from funcs import BubbleSort, HybridMergeSort, MergeSort, InsertionSort, SelectionSort, RandomArray, ShuffleArray
import time

def read_values_from_file(filename):
    values = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    try:
                        value = int(line)
                        values.append(value)
                    except ValueError:
                        print(f"Warning: Unable to convert '{line}' to an integer.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return values

def main():
    input_filename = 'Nvalues.txt' 
    output_filename = 'RunTimeTable.csv'
    
    ns = read_values_from_file(input_filename)
    
    with open(output_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the table headers matching your format
        writer.writerow(['Value of n', 'Insertion sort (seconds)', 'Merge Sort (seconds)', 
                         'Hybrid Merge Sort (seconds)', 'Selection Sort (seconds)', 'Bubble Sort (seconds)'])
        
        for n in ns:
            print(f"Processing value n = {n}...")
            
            row = [n]
            
            # Insertion Sort
            array = RandomArray(n)
            ShuffleArray(array, 0, len(array))
            start_time = time.time()
            InsertionSort(array, 0, len(array))
            end_time = time.time()
            row.append(end_time - start_time)
            
            # Merge Sort
            array = RandomArray(n)
            ShuffleArray(array, 0, len(array))
            start_time = time.time()
            MergeSort(array, 0, len(array))
            end_time = time.time()
            row.append(end_time - start_time)
            
            # Hybrid Merge Sort
            array = RandomArray(n)
            ShuffleArray(array, 0, len(array))
            start_time = time.time()
            HybridMergeSort(array, 0, len(array))
            end_time = time.time()
            row.append(end_time - start_time)
            
            # Selection Sort
            array = RandomArray(n)
            ShuffleArray(array, 0, len(array))
            start_time = time.time()
            SelectionSort(array, 0, len(array))
            end_time = time.time()
            row.append(end_time - start_time)
            
            # Bubble Sort
            array = RandomArray(n)
            ShuffleArray(array, 0, len(array))
            start_time = time.time()
            BubbleSort(array, 0, len(array))
            end_time = time.time()
            row.append(end_time - start_time)
            
            # Write the row to the CSV
            writer.writerow(row)

if __name__ == "__main__":
    main()
