a: int = 3
b: int = 0
c: float


def main() -> None:
    global a
    global b
    print(fun(a,b))


def fun(a: int, b: int) -> list[int]:
    global c
    nums: list[int] = []
    if b == 0:
        while len(nums) < 4:
            c = a + b / 2
            if c % 2 == 0:
                a += 1
                b += 1
            else:
                nums.append(a)
                a += 3
    return nums


def odd_and_even(x: list[int]) -> list[int]:
    i: int = 0
    a_list: list[int] = []
    while i < len(x):
        if x[i] % 2 == 1 and i % 2 == 0:
            a_list.append(x[i])
        i += 1
    return a_list


def vowels_and_threes(x: str) -> str:
    vowels: list = ['a', 'e', 'i', 'o', 'u']
    i: int = 0
    output: str = ""
    while i < len(x):
        if x[i] in vowels:
            output += ""
        else:
            output += x[i]
        i += 3
    return output


def average_grades(x: dict[str, list[int]]) -> dict[str, float]:
    grades: dict[str, float] = {}
    for name in x:
        average: int = 0
        for grade in x[name]:
            average += grade
        grades[name] = average / len(x[name])
    return grades


def tuples():
    Point2D = tuple[float, float]
    Color = tuple[int, int, int]
    Player = tuple[str, float]

    origin: Point2D = (0.0, 0.0)
    gray: Color = (128, 128, 128)
    bacot: Player = ("Bacot", 5)

    for number in gray:
        print(number)


def ranges():
    a_range: range = range(0, 10, 2)
    print(a_range.start)
    print(a_range.stop)
    print(a_range.step)


def find_avg_score(players: dict[str, list[int]]) -> dict[str, int]:
    scores: dict[str, int] = {}
    for name in players:
        average: int = 0
        for score in players[name]:
            average += score
        scores[name] = average / len(players[name])
    return scores


def join_salary_data(players: dict[int, str], salaries: dict[int, int]) -> dict[str, int]:
    joined_dict: dict[str, int] = {}
    for ide in players:
        if ide in salaries:
            joined_dict[players[ide]] = salaries[ide]
    return joined_dict


def highest_and_lowest(items: dict[str, int]) -> dict[str, str]:
    output: dict[str, str] = {'max' : '', 'min' : ''}
    maximum: int = 0
    minimum: int = 0
    for name in items:
        if items[name] > maximum:
            maximum = items[name]
            output['max'] = name
    minimum = maximum
    for name in items:
        if items[name] < minimum:
            minimum = items[name]
            output['min'] = name
    return output


def compare_scores(player: dict[str, list[int]], num_games: int) -> str:
    output: str = ""
    outcomes: dict[str, int] = {}
    i: int = 0
    maximum: int = -1
    while i < num_games:
        for key in player:
            if player[key[i]] > maximum:
                maximum = player[key[i]]
                output = key
        if output not in outcomes:
            outcomes[output] = 1
        else:
            outcomes[output] += 1
        maximum = -1
        output = ""
        i += 1
    return highest_and_lowest(outcomes)["max"]


def maximum(scores: dict[str, int]) -> dict[str, int]:
    output: dict[str, int] = {}
    maximum: int = 0
    for name in scores:
        if scores[name] > maximum:
            maximum = scores[name]
            output['max'] = maximum
    return output


def best_animals(visits: dict[str, list[int]]) -> list[str]:
    result: list[str] = []
    i: int = 0
    while i < 3:
        maximum: int = 0
        animal: str = ""
        for exhibit in visits:
            if visits[exhibit[i]] > maximum:
                maximum = visits[exhibit][i]
                animal = exhibit
        result.append(animal)
        i += 1
    return result


def subset(xs: dict[int, str], a_list: list[int]) -> dict[int, str]:
    result: dict[int, str] = {}
    for key in xs:
        i: int = 0
        while i < len(a_list):
            if key == a_list[i]:
                result[key] = xs[key]
            i += 1
    return result