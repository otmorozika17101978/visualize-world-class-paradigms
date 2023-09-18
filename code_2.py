
def generate_random_data():
    random_string = 'If six east religious chance foreign.'
    random_number = 100

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: If six east religious chance foreign.")
        print(f"Random Number: 100")

if __name__ == "__main__":
    main()
