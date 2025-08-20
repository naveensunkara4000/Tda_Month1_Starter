# Lists, tuples, dicts, sets, functions, lambda, recursion, list comprehensions

def sum_of_squares(nums):
    return sum([x*x for x in nums])

def filter_even(nums):
    return list(filter(lambda x: x % 2 == 0, nums))

def factorial(n):
    if n < 0:
        raise ValueError("n must be non-negative")
    if n in (0,1):
        return 1
    return n * factorial(n-1)

def dict_count(items):
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

if __name__ == "__main__":
    print("Sum of squares:", sum_of_squares([1,2,3,4]))
    print("Even numbers:", filter_even([1,2,3,4,5,6]))
    print("Factorial 5:", factorial(5))
    print("Counts:", dict_count(['a','b','a','c','b','a']))