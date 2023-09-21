
def generate_random_data():
    random_string = 'Deep small behavior month only probably culture.'
    random_number = 60

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Deep small behavior month only probably culture.")
        print(f"Random Number: 60")

if __name__ == "__main__":
    main()
