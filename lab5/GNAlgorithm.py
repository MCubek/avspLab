def read_input():
    graph = {}

    line = input()
    while len(line.strip()) > 0:
        left, right = (int(x) for x in line.split(" "))

        if left not in graph:
            graph[left] = []
        if right not in graph:
            graph[right] = []

        graph[left].append(right)
        graph[right].append(left)

        line = input()

    graph_features = {}

    line = input()
    while len(line.strip()) > 0:
        split = list(int(x) for x in line.split(" "))
        number = split[0]
        features = split[1:]

        graph_features[number] = features

        try:
            line = input()
        except EOFError:
            break

    return graph, graph_features


def calculate_non_similarity(graph_features):
    non_similarity = {}

    for left in graph_features.keys():
        features_left = graph_features[left]

        num_of_features = len(features_left)

        for right in graph_features.keys():
            if not right > left:
                continue

            features_right = graph_features[right]

            similarity = 0
            for i in range(num_of_features):
                if features_left[i] == features_right[i]:
                    similarity += 1

            non_similarity[(left, right)] = num_of_features - (similarity - 1)

    return non_similarity


def add_starting_weights_to_graph(graph, non_similarity):
    weighed_graph = {}

    for left in graph.keys():
        for right in graph[left]:
            if not right > left:
                continue
            key = (left, right)
            weighed_graph[key] = non_similarity[key]

    return weighed_graph


def calculate_total_weights(graph_weights):
    count = 0
    for weight in graph_weights.values():
        count += weight

    return count


def get_edge_weight(graph: dict, first_node: int, second_node: int):
    if first_node > second_node:
        temp = first_node
        first_node = second_node
        second_node = temp

    if (first_node, second_node) not in graph:
        return -1
    return graph[(first_node, second_node)]


def add_edge_weight(graph: dict, first_node: int, second_node: int, weight: float):
    if first_node > second_node:
        temp = first_node
        first_node = second_node
        second_node = temp

    graph[(first_node, second_node)] += weight


def zero_weights_on_graph(graph: dict):
    for node in graph.keys():
        graph[node] = 0
    return graph


def find_shortest_paths(graph_input: dict):
    pass


def calculate_centralises(graph_input: dict):
    graph = zero_weights_on_graph(graph_input)

    for first_node in graph_input.keys():
        for second_node in graph_input.keys():
            if first_node >= second_node:
                continue

            shortest_paths = find_shortest_paths(graph_input)

            num_shortest_paths = len(shortest_paths)
            for path in shortest_paths:
                for i in range(len(path) - 1):
                    first_node = path[i]
                    second_node = path[i + 1]

                    add_edge_weight(graph, first_node, second_node, 1.0 / num_shortest_paths)


def get_node_weights(graph_weights: dict, node: int):
    weights = 0
    for node1, node2 in graph_weights.keys():
        if node1 == node or node2 == node:
            weights += graph_weights[(node1, node2)]

    return weights


def calculate_modularity(graph_weights: dict, graph_centralities: dict):
    q = 0
    m = calculate_total_weights(graph_weights)


def get_graph_groups(source_graph: dict, current_weighed_graph: dict):
    groups = {}
    visited = []

    for node in source_graph.keys():
        if node in visited:
            continue
        groups[node] = []

        for next_node in source_graph[node]:
            if not (node, next_node) or not (next_node, node) in current_weighed_graph:
                continue
            groups[node].append(next)

    return groups.values()


def get_current_graph_string(source_graph: dict, current_weighed_graph: dict):
    groups = get_graph_groups(source_graph, current_weighed_graph)

    return ' '.join('-'.join(x) for x in groups)


def remove_highest_edges_from_graph_and_print(graph: dict):
    max_weight = 0
    for weight in graph.values():
        if max_weight < weight:
            max_weight = weight

    for key, value in graph.items():
        if value == max_weight:
            print(f"{key[0]} {key[1]}")
            del graph[key]


def main():
    graph_input, graph_features = read_input()

    non_similarity = calculate_non_similarity(graph_features)

    graph_weights = add_starting_weights_to_graph(graph_input, non_similarity)

    communities_over_iterations = {}

    graph = {}

    while True:
        graph_centralities = calculate_centralises(graph_input)

        modularity = calculate_modularity(graph_weights, graph_centralities)

        communities_over_iterations[get_current_graph_string(graph_input, graph_centralities)] = modularity

        graph_centralities = remove_highest_edges_from_graph_and_print(graph_centralities)

        if len(graph.keys()) == 0:
            break

    communities_over_iterations = dict(sorted(communities_over_iterations.items()))

    print("%s %s".format(communities_over_iterations.items()[0]))


if __name__ == '__main__':
    main()
