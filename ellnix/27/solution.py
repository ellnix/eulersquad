# brute force

from math import ceil, sqrt

def is_prime(n):
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            return False

    return True


def prime_sequence_len(a, b):
    seq_len = 0

    for n in range(0, 10000):
        res = n**2 + n * a + b

        if is_prime(abs(res)):
            seq_len += 1
        else:
            break

    return seq_len

max_seq_len = 0
max_seq_len_res = 1
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        seq_len = prime_sequence_len(a, b)

        if seq_len > max_seq_len:
            max_seq_len = seq_len
            max_seq_len_res = a * b


print(max_seq_len)
print(max_seq_len_res)
