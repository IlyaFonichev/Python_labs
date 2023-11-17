import json

INPUT_DATA = 'input.json'


def task() -> float:
    with open(INPUT_DATA) as input_:
        json_ = json.load(input_)
        sum_ = sum([i['score'] * i['weight'] for i in json_])
        return round(sum_, 3)


print(task())
