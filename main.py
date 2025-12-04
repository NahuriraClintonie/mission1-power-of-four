import sys

def sum_fourth_powers(nums):
    if not nums:
        return 0
    head, *tail = nums
    return ((head ** 4) if head <= 0 else 0) + sum_fourth_powers(tail)

def process_cases(lines, index, remaining):
    if remaining == 0:
        return [], index

    if index >= len(lines):
        return ["-1"], index

    try:
        x = int(lines[index].strip())
    except:
        return ["-1"], index + 1

    index += 1
    if index >= len(lines):
        return ["-1"], index

    raw_nums = lines[index].strip().split()
    index += 1

    if len(raw_nums) != x:
        result = "-1"
    else:
        try:
            nums = list(map(int, raw_nums))
            result = str(sum_fourth_powers(nums))
        except:
            result = "-1"

    rest_results, new_index = process_cases(lines, index, remaining - 1)
    return [result] + rest_results, new_index

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return

    try:
        n = int(data[0].strip())
    except:
        print("-1")
        return

    results, _ = process_cases(data, 1, n)
    print("\n".join(results))

if __name__ == "__main__":
    main()
