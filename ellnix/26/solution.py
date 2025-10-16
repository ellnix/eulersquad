def rep_seq_len(n):
    subject = 1
    digits = []
    while subject > 0:
        digit, subject = divmod(subject, n)
        if digit > 0:
            try:
                return digits[::-1].index([digit, subject])
            except ValueError:
                hello = "world"

        digits.append([digit, subject])
        subject *= 10

        
    return 0


max_repeats = 0
max_repeat_n = 1
for x in range(1, 1001):
    repeats = rep_seq_len(x)
    if repeats > max_repeats:
        max_repeats = repeats
        max_repeat_n = x


print("Number of repeating digits", max_repeats)
print("Number", max_repeat_n)

