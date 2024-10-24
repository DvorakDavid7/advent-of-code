
def replace_at(s: str, index: int, new_char: str)-> str:
    return s[:index] + new_char + s[index+1:]


def is_valid_config(s: str, groups: list[int]) -> bool:
    clusters = list(filter(lambda x: x != "", s.split(".")))
    if len(clusters) != len(groups):
        return False

    for i, group_size in enumerate(groups):
        cluster = clusters[i]
        if len(cluster) != group_size:
            return False
    return True


def solve_rec(s: str, groups: list[int]) -> int:
    i = s.find("?")

    if i == -1:
        return 1 if is_valid_config(s, groups) else 0
    
    s_with_dot = replace_at(s, i, ".")
    s_with_hash = replace_at(s, i, "#")

    return solve_rec(s_with_dot, groups) + solve_rec(s_with_hash, groups)


def main():
    with open("input.txt") as f:
        data = f.read()
    
    lines = data.splitlines()

    res = 0
    for line in lines:
        string, groups_s = line.split(" ")
        groups = list(map(lambda x: int(x), groups_s.split(",")))
        res += solve_rec(string, groups)
    print(res)


if __name__ == "__main__":
    main()
