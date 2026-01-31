import random
import string

def generate_jarm(length=62):
    chars = string.digits + "abcdef"
    return ''.join(random.choices(chars, k=length))

def main(filename, count):
    with open(filename, 'w') as f:
        for _ in range(count):
            f.write(generate_jarm() + '\n')

if __name__ == "__main__":
    for count in [50, 100, 250, 500, 1000, 2000, 2500, 5000, 10000, 15000, 20000, 25000, 30000, 50000, 100000]:
        main(f"./tests/{count}.csv", count)

