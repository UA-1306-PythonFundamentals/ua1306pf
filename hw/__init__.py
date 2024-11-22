import os


class BColors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


# print(os.getcwd() + "\\hw")
d = {}


def check_task(tasks: list[str]) -> str:
    all_tasks = [
        "hw02",
        "hw03",
        "hw04",
        "hw05",
        "hw06",
        "hw07",
        "hw08",
        "hw09",
        "hw10",
        "hw11",
    ]
    return [
        (
            f"{BColors.OKGREEN}{task}{BColors.ENDC}"
            if task in tasks
            else f"{BColors.FAIL}{task}{BColors.ENDC}"
        )
        for task in all_tasks
    ]


for path in os.walk(os.getcwd() + "\\hw"):
    s_path = path[0].split("\\")
    if len(s_path) == 7:
        # print(s_path)
        if s_path[6] in d:
            d[s_path[6]].append(s_path[5])
        else:
            d[s_path[6]] = [s_path[5]]
for author, hw in d.items():
    print(f"{author: <20}\t", end="")
    for i in check_task(hw):
        print(i, end=" ")
    print()
