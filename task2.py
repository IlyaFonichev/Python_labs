import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as input_, open(OUTPUT_FILENAME, 'w') as output_:
        result = []
        for row in csv.DictReader(input_):
            result.append(dict(row.items()))
        json.dump(result, output_, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
