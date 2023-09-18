
def generate_random_data():
    random_string = 'Certain other risk north rest she great.'
    random_number = 15

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Certain other risk north rest she great.")
        print(f"Random Number: 15")

if __name__ == "__main__":
    main()
