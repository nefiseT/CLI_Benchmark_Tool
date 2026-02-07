#main logic
import sys
from utils import generate_data, format_row
from engine import run_benchmark
from algorithms import quick_sort, bubble_sort, fibonacci

def main():
    print (" AlgoBench ")
    print ("=" * 60)
    header = format_row("Algorithm", "Size", "Median Time", "Peak Mem")
    print(header)
    print ("-" * len(header))

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
