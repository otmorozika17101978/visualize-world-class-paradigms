
def generate_random_data():
    random_string = 'National professor too nice the food put.'
    random_number = 13

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: National professor too nice the food put.")
        print(f"Random Number: 13")

if __name__ == "__main__":
    main()
