import json

def task(json):

    total_sum = 0
    for item in json:
        if isinstance(item, dict) and "score" in item and "weight" in item:
            total_sum += item["score"] * item["weight"]
    return round(total_sum, 3)

json = [
    {"score": 1.148, "weight": 2},
    # {"score": 0.1, "weight": 1},
    # {"score": 0.2, "weight": 1},
    # {"score": 0, "weight": 0}
]

result = task(json)
print(result)



