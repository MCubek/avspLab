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


def add_weights_to_graph(graph, non_similarity):
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


def calculate_centralises(total_weights):
    pass


def calculate_modularity():
    pass


def get_current_graph_string(graph):
    pass


def remove_highest_edges_from_graph_and_print(graph):
    pass


def main():
    graph_input, graph_features = read_input()

    non_similarity = calculate_non_similarity(graph_features)

    graph_weights = add_weights_to_graph(graph_input, non_similarity)

    total_weights = calculate_total_weights(graph_weights)

    communities_over_iterations = {}

    while True:
        graph = calculate_centralises(total_weights)

        modularity = calculate_modularity()

        communities_over_iterations[get_current_graph_string(graph)] = modularity

        graph = remove_highest_edges_from_graph_and_print(graph)

        if len(graph.keys()) == 0:
            break

    communities_over_iterations = dict(sorted(communities_over_iterations.items()))

    print("%s %s".format(communities_over_iterations.items()[0]))


if __name__ == '__main__':
    main()
