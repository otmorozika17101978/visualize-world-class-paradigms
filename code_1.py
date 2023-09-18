
def generate_random_data():
    random_string = 'Cell everything phone much government.'
    random_number = 4

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Cell everything phone much government.")
        print(f"Random Number: 4")

if __name__ == "__main__":
    main()
