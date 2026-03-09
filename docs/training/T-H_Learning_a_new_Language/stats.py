def average(numbers):
    total = 0
    for number in numbers:
        total += number
    avg = total / len(numbers)
    return avg

def main():
    my_numbers = [3,1,6,3,5,4,6,2]
    my_avg = average(my_numbers)
    print(f"Average = {my_avg}")

if __name__ == "__main__":
    main()