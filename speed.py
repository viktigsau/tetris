from threading import Thread
import psutil


def split(list, n):
    return [list[i:i+n] for i in range(0, len(list), n)]

def thread(list, func, num_threads: int | None=None, max_usage: float=90.0, use_threads: bool=True, args=()):
    if not num_threads:
        total_threads = psutil.cpu_count(logical=True)
        num_threads = int(round(total_threads * (max_usage / 100))) 

    list_len = len(list)
    calculated = list_len // num_threads
    parts = split(list, calculated + 1 if calculated != 0 else 1)
    part_len = len(parts[0])
    out = [None] * list_len
    threads = []

    for i, part in enumerate(parts):
        def calc(part):
            for j, item in enumerate(part):
                out[i * part_len + j] = func(item, *args)

        if use_threads:
            thread = Thread(target=calc, args=(part,))
            thread.start()
            threads.append(thread)

            while psutil.cpu_percent() > max_usage:
                ...
        else:
            calc(part)
    
    for thread in threads:
        thread.join()

    return out