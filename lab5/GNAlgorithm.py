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


def find_full_paths_recursive(current_edges_graph, weight_graph, current_node, finish_node, source_path, source_cost):
    current_path = source_path.copy()
    cost = source_cost

    current_path.append(current_node)

    if current_node == finish_node:
        result = (current_path, cost)
        result_list = []
        result_list.append(result)
        return result_list

    full_paths = []

    for first_node, second_node in current_edges_graph.keys():
        if first_node != current_node and second_node != current_node:
            continue

        if first_node == current_node:
            next_node = second_node
        else:
            next_node = first_node

        if next_node in current_path:
            continue

        additional_cost = get_edge_weight(weight_graph, current_node, next_node)

        full_paths.extend(find_full_paths_recursive(current_edges_graph, weight_graph
                                                    , next_node, finish_node, current_path, cost + additional_cost))

    return full_paths


def find_shortest_paths(current_edges_graph: dict, weight_graph: dict, first_node: int, second_node: int):
    current_path = []
    current_cost = 0

    paths_counts = find_full_paths_recursive(current_edges_graph, weight_graph, first_node, second_node, current_path,
                                             current_cost)

    if len(paths_counts) == 0:
        return list()

    shortest_path = min(x[1] for x in paths_counts)

    shortest_paths = (x[0] for x in paths_counts if x[1] == shortest_path)

    return list(shortest_paths)


def calculate_centralises(graph: dict, input_graph: dict, source_weight_graph: dict):
    graph = zero_weights_on_graph(graph)

    for first_node in input_graph.keys():
        for second_node in input_graph.keys():
            if first_node >= second_node:
                continue

            shortest_paths = find_shortest_paths(graph, source_weight_graph, first_node, second_node)

            num_shortest_paths = len(shortest_paths)
            for path in shortest_paths:
                for i in range(len(path) - 1):
                    path_node_first = path[i]
                    path_node_second = path[i + 1]

                    add_edge_weight(graph, path_node_first, path_node_second, 1.0 / num_shortest_paths)

    return graph


def get_node_weights(graph_weights: dict, node: int):
    weights = 0
    for node1, node2 in graph_weights.keys():
        if node1 == node or node2 == node:
            weights += graph_weights[(node1, node2)]

    return weights


def calculate_modularity(graph_input: dict, graph_weights: dict, graph_centralises: dict):
    q = 0
    m = calculate_total_weights(graph_weights)
    groups = get_graph_groups(graph_input, graph_centralises, graph_weights)

    for group in groups:
        for first_node in group:
            for second_node in group:
                a = get_edge_weight(graph_weights, first_node, second_node)
                if a < 1:
                    a = 0
                ku = get_node_weights(graph_weights, first_node)
                kv = get_node_weights(graph_weights, second_node)
                sum_part = (a - (ku * kv / (2.0 * m)))
                q += sum_part

    return q / (2 * m)


def get_graph_groups(source_graph: dict, graph_centralises: dict, weight_graph: dict):
    groups = {}
    visited = set()

    for node in source_graph.keys():
        if node in visited:
            continue
        groups[node] = set()
        groups[node].add(node)
        visited.add(node)

        for second_node in source_graph.keys():
            if second_node in visited:
                continue
            paths = find_shortest_paths(graph_centralises, weight_graph, node, second_node)
            for path in paths:
                groups[node] = groups[node].union(path)
                visited = visited.union(path)

    return groups.values()


def get_current_graph_string(source_graph: dict, graph_centralises: dict, weight_graph: dict):
    groups = get_graph_groups(source_graph, graph_centralises, weight_graph)

    group_strings = []
    for group in groups:
        group_strings.append("-".join(str(x) for x in group))

    group_strings.sort(key=lambda x: len(x))

    return " ".join(group_strings)


def remove_highest_edges_from_graph_and_print(graph: dict):
    max_weight = max(graph.values())

    graph_mod = graph.copy()

    items = list(graph.items())

    items.sort(key=lambda x: str(x[0][0])+str(x[0][1]))

    for key, value in items:
        if value == max_weight:
            print(f"{key[0]} {key[1]}")
            del graph_mod[key]

    return graph_mod


def main():
    DEBUG = True

    graph_input, graph_features = read_input()

    non_similarity = calculate_non_similarity(graph_features)

    graph_weights = add_starting_weights_to_graph(graph_input, non_similarity)

    communities_over_iterations = []

    graph_centralises = graph_weights.copy()

    while True:
        graph_centralises = calculate_centralises(graph_centralises, graph_input, graph_weights)

        modularity = calculate_modularity(graph_input, graph_weights, graph_centralises)

        if DEBUG:
            print("MODULARITY %.4f" % modularity)

        communities_over_iterations.append(
            (get_current_graph_string(graph_input, graph_centralises, graph_weights), modularity))

        graph_centralises = remove_highest_edges_from_graph_and_print(graph_centralises)

        if len(graph_centralises.keys()) == 0:
            break

    communities_over_iterations.sort(key=(lambda x: x[1]), reverse=True)

    print(communities_over_iterations[0][0])


if __name__ == '__main__':
    main()
