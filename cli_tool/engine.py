#timing & stats

import time
import statistics
import tracemalloc

def run_benchmark(func, data, iterations=5):
    # Warm up
    if isinstance(data, list):
        func(data.copy())
    else:
        func(data)

    times = []
    memory_usage = []

    for _ in range(iterations):
        if isinstance(data, list):
            sample_data = data.copy()
        else:
            sample_data = data

        tracemalloc.start()
        start_t = time.perf_counter_ns()

        func(sample_data)
        end_t = time.perf_counter_ns()
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        times.append((end_t - start_t) / 1_000_000)  # conversion to ms
        memory_usage.append(peak / 1024)

    return statistics.median(times), statistics.median(memory_usage)
