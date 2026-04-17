score = {
    "first":2,
    "second":6,
    "third":7,
    "fourth":68,
    "fifth":8,
    "sixth": -7
}

porog = 7

for key,value in score.items():
    if value > porog:
        print(f"{key} : {value}")