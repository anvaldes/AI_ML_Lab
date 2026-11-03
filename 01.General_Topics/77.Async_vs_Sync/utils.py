import math

def cpu_work(n=2_000_000):
    return sum(math.sqrt(i) for i in range(n))