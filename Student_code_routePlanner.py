import math
from queue import PriorityQueue


def shortest_path(graph, start, goal):

    pQueue = PriorityQueue()
    pQueue.put(start, 0)

    prev = {start: None}
    score = {start: 0}

    while not pQueue.empty():
        current = pQueue.get()

        if current == goal:
            generatePath(prev, start, goal)

        for node in graph.roads[current]:
            updateScore = score[current] + heuristicMeasure(
                graph.intersections[current], graph.intersections[node])

            if node not in score or updateScore < score[node]:
                score[node] = updateScore
                totalScore = updateScore + \
                    heuristicMeasure(
                        graph.intersections[current], graph.intersections[node])
                pQueue.put(node, totalScore)
                prev[node] = current

    return generatePath(prev, start, goal)


def heuristicMeasure(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))


def generatePath(prev, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = prev[current]
        path.append(current)
    path.reverse()
    return path
