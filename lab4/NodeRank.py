def query_graph(neighbours, b, n, max_iters, r_by_iter):
    for i in range(1, max_iters + 1):
        r_by_iter.append([(1 - b) / n] * n)
        for node, node_neighbours in neighbours.items():
            neighbours_count = len(node_neighbours)
            for node_neighbour in node_neighbours:
                r_by_iter[i][node_neighbour] += b * r_by_iter[i - 1][node] / neighbours_count


def main():
    line = input()

    n, b = line.split(' ')
    n = int(n)
    b = float(b)

    neighbours = {}

    for i in range(n):
        line = input()
        neighbours[i] = list(int(x) for x in line.split(' '))

    q = int(input())

    queries = []

    for i in range(q):
        query_line = input().split(' ')
        node_index = int(query_line[0])
        iteration = int(query_line[1])

        queries.append((node_index, iteration))

    max_iters = 100

    r_by_iter = []

    r_by_iter.append([1.0 / n] * n)

    query_graph(neighbours, b, n, max_iters, r_by_iter)

    for node_index, iteration in queries:
        rank = r_by_iter[iteration][node_index]

        print("{:.10f}".format(rank))


if __name__ == '__main__':
    main()
