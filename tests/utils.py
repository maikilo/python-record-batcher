import random
import string


def generate_random_sizes(n_records, max_size):
    sizes = [random.randint(1, max_size) for _ in range(n_records)]
    return sizes


def generate_test_data(sizes):
    test_records = [''.join(random.choice(string.ascii_letters + string.digits)
                            for _ in range(N)) for N in sizes]
    return test_records
