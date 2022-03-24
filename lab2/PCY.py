import math


def main():
    n = int(input())
    s = float(input())
    b = int(input())

    treshold = math.floor(s * n)

    baskets = []
    for i in range(n):
        baskets.append([int(x) for x in input().split(" ")])

    # First pass
    counts = {}
    for basket in baskets:
        for item in basket:
            if item not in counts:
                counts[item] = 0
            counts[item] += 1

    # Second pass
    partition_counter = [0] * b
    for basket in baskets:
        for i in range(len(basket)):
            item1 = basket[i]
            if counts[item1] < treshold:
                continue
            for j in range(i + 1, len(basket)):
                item2 = basket[j]
                if counts[item2] < treshold:
                    continue

                k = (item1 * len(counts) + item2) % b
                partition_counter[k] += 1

    # Third pass
    pairs = {}
    for basket in baskets:
        for i in range(len(basket)):
            item1 = basket[i]
            if counts[item1] < treshold:
                continue
            for j in range(i + 1, len(basket)):
                item2 = basket[j]
                if counts[item2] < treshold:
                    continue

                k = (item1 * len(counts) + item2) % b
                if partition_counter[k] >= treshold:
                    pair = (item1, item2)

                    if pair not in pairs:
                        pairs[pair] = 0
                    pairs[pair] += 1

    m = sum(map(lambda x: x >= treshold, counts.values()))
    a = m * (m - 1) / 2
    print(math.floor(a))

    p = len(pairs)
    print(p)

    occurances = []
    for pair_value in pairs.values():
        if pair_value >= treshold:
            occurances.append(pair_value)

    occurances.sort(reverse=True)

    for occurance in occurances:
        print(occurance)


if __name__ == '__main__':
    main()
