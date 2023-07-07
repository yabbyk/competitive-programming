def countingValleys(steps, path):
    mount = 0
    valley = 0
    in_vall = []
    for p in path:
        if p == "U":
            mount += 1
        else:
            mount -= 1
        if mount < 0 and not in_vall:  # Enter a valley
            in_vall.append(p)
        elif mount == 0 and in_vall:  # Exit a valley
            in_vall.pop()
            valley += 1
            
    return valley


if __name__ == '__main__':
    steps = int(input().strip())
    path = input().strip()

    result = countingValleys(steps, path)
    print(result)
