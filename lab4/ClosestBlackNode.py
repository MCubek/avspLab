from collections import deque


def main():
    line = input().split(' ')
    n, e = int(line[0]), int(line[1])

    black_nodes = set()

    closest_black = [(-1, -1)] * n

    for i in range(n):
        if input().strip() == '1':
            black_nodes.add(i)
            closest_black[i] = (i, 0)

    neighbours = {}

    for i in range(e):
        line = input().split(' ')
        a, b = int(line[0]), int(line[1])

        if a not in neighbours:
            neighbours[a] = list()
        if b not in neighbours:
            neighbours[b] = list()

        neighbours[a].append(b)
        neighbours[b].append(a)

    visited = set()
    queue = deque()

    queue.extendleft(black_nodes)

    while len(queue) != 0:
        element = queue.pop()
        visited.add(element)

        curr_black, curr_distance = closest_black[element]

        for node in neighbours[element]:
            if node not in visited:
                node_black, node_distance = closest_black[node]

                if curr_distance + 1 < node_distance or node_distance == -1 or (
                        curr_distance + 1 == node_distance and curr_black < node_black):
                    closest_black[node] = curr_black, curr_distance + 1
                queue.appendleft(node)

    for black, distance in closest_black:
        print(black, distance)


if __name__ == '__main__':
    main()
