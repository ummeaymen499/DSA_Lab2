import csv
from funcs import InsertionSort, MergeSort,ShuffleArray
import time

def read_words_from_file(filename):
    Words = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip() 
                if line:
                    Words.extend(line.split())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    return Words
   
if __name__ == "__main__":
    input_filename = 'words.txt'
    words = read_words_from_file(input_filename)

    #Shuffle Words Array Randomly
    array=ShuffleArray(words,0,len(words))
    print(array)
    
    # Sorting with MergeSort
    merge_sort_words = words.copy()
    start_time = time.time()
    MergeSort(merge_sort_words, 0, len(merge_sort_words))
    end_time = time.time()
    merge_sort_runtime = end_time - start_time
    print(merge_sort_words)
    print("Runtime for MergeSort:", merge_sort_runtime, "seconds")
    
    # Sorting with InsertionSort
    insertion_sort_words = words.copy()
    start_time = time.time()
    InsertionSort(insertion_sort_words, 0, len(insertion_sort_words))
    end_time = time.time()
    insertion_sort_runtime = end_time - start_time
    print(insertion_sort_words)
    print("Runtime for InsertionSort:", insertion_sort_runtime, "seconds")
