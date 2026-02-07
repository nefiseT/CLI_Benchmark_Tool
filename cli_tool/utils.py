#data generation nd formattiing

import random

def generate_data(size, mode= "random"):
    if mode == "random":
        result = []
        for _ in range (size):
            result.append(random.randint(0, size * 10))
        return result
    
    elif mode == "sorted":
        return list(range(size))
    elif mode == "reverse":
        return list(range(size, 0, -1))
    return[]

def format_row(name, size, time_ms, memory_kb):
    if isinstance(time_ms, str):
        return f"|{name:<20} | {size:<20} | {time_ms:<15} | {memory_kb:<10} |"
    else:
        return f"|{name:<20} | {size:<20} | {time_ms:>10.4f} ms | {memory_kb:>10.2f} KB |"
