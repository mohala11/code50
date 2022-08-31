import sys
import csv


def main():
    check_csv_file()
    create_csv_file()
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                lastname, name = row['name'].split(", ")
                house = row['house']
                with open(sys.argv[2], 'a', newline='') as file1:
                    fieldnames = ['first', 'last', 'house']
                    writer = csv.DictWriter(file1, fieldnames=fieldnames)
                    writer.writerow({'first': name, 'last': lastname, 'house': house})
    except FileNotFoundError:
        sys.exit(f"could not read {sys.argv[1]}")


def check_csv_file():
        if len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv) > 3:
            sys.exit("Too many command-line arguments")
        elif sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv") == False:
            sys.exit("Not a CSV file")


def create_csv_file():
    with open(sys.argv[2], 'w') as file:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()


if __name__ == "__main__":
    main()