import random
import string

def generate_jarm(length=62):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choices(chars, k=length))

def main(filename, count):
    with open(filename, 'w') as f:
        for _ in range(count):
            f.write(generate_jarm() + '\n')

if __name__ == "__main__":
    for count in [50000, 100000]:
        main(f"./tests/{count}.csv", count)

