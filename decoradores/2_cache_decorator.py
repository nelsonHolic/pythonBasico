import  time

def cache(my_func: callable):
    my_cache_dict = {}
    def my_internal(*args, **kwargs):
        key = f"{args}{kwargs}"
        if key in my_cache_dict:
            return my_cache_dict[key]

        result = my_func(*args, **kwargs)

        my_cache_dict[key] = result
        return result

    return my_internal

@cache
def fibonacci_with_memory(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1

    result = fibonacci_with_memory(n - 2) + fibonacci_with_memory(n - 1)
    return result

def fibonacci(n: int):
    if n == 0:
        return 0
    if n == 1:
        return 1

    result = fibonacci(n - 2) + fibonacci(n - 1)
    return result


if __name__ == "__main__":
    begin = time.time()
    print(f"fibonacci(35)={fibonacci(35)}")
    print(f"it takes = {time.time() - begin}")

    begin = time.time()
    print(f"with cache decorated memory, fibonacci(35)={fibonacci_with_memory(35)}")
    print(f"it takes = {time.time() - begin}")
