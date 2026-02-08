#main logic
import sys
from utils import generate_data, format_row
from engine import run_benchmark, run_search_benchmark
from algorithms import quick_sort, bubble_sort, fibonacci, linear_search, binary_search

def main():
    print (" AlgoBench ")
    print ("=" * 60)
    header = format_row("Algorithm", "Size", "Median Time", "Peak Mem")
    print(header)
    print ("-" * len(header))

    sizes = [1000, 10000, 100000]
    for size in sizes:
        # Create data and set target to something not in list or at the end
        data = list(range(size)) 
        target = size - 1 # Worst case for linear
        
        for func in [linear_search, binary_search]:
            t, m = run_search_benchmark(func, data, target)
            print(format_row(func.__name__, size, t, m))

    #test suites
    suites = [
        (quick_sort, [100, 1000, 5000], "random"),
        (bubble_sort, [100, 1000, 2000], "random")

    ]

    for func, sizes, mode in suites:
        for size in sizes:
            data = generate_data(size, mode)
            t, m = run_benchmark(func, data)
            print(format_row(func.__name__, size, t, m))

    #special case
    print("-" * len(header))
    print(format_row("Fibonacci(Rec)", 30, *run_benchmark(fibonacci, 30)))
    print("=" * 60)

if __name__=="__main__":
    main()
