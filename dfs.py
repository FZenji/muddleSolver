# Python program to print all paths from a source to destination.
import random
from collections import defaultdict

with open('WordDictionary.txt', 'rb', 0) as file:
    w_set = set(file.read().splitlines())

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# gridL = list(input().lower().split(" "))
# print(gridL)

grid = [[i + j for i in range(4)] for j in range(0, 13, 4)]


# This class represents a directed graph
# using adjacency list representation
class Graph:
    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.make_structure()

    # function to add an edge to graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    def make_structure(self):
        for row in range(len(grid)):
            for col in range(len(grid)):
                self.add_edge(grid[row][col], grid[row][col])
                if row >= 1:
                    self.add_edge(grid[row][col], grid[row - 1][col])
                if col >= 1:
                    self.add_edge(grid[row][col], grid[row][col - 1])
                if row >= 1 and col >= 1:
                    self.add_edge(grid[row][col], grid[row - 1][col - 1])
                if row <= 2:
                    self.add_edge(grid[row][col], grid[row + 1][col])
                if col <= 2:
                    self.add_edge(grid[row][col], grid[row][col + 1])
                if row <= 2 and col <= 2:
                    self.add_edge(grid[row][col], grid[row + 1][col + 1])
                if row >= 1 and col <= 2:
                    self.add_edge(grid[row][col], grid[row - 1][col + 1])
                if row <= 2 and col >= 1:
                    self.add_edge(grid[row][col], grid[row + 1][col - 1])

    '''A recursive function to print all paths from 'u' to 'd'.
    visited[] keeps track of vertices in current path.
    path[] stores actual vertices and path_index is current
    index in path[]'''

    def all_paths_util(self, u, d, visited, path):

        # Mark the current node as visited and store in path
        visited[u] = True
        path.append(u)

        # If current vertex is same as destination, then print
        # current path[]
        if u == d:
            word = "".join([gridL[i] for i in path])
            if str.encode(word) in w_set and word not in words:
                words.append(word)
                print(word)
        else:
            # If current vertex is not destination
            # Recur for all the vertices adjacent to this vertex
            for i in self.graph[u]:
                if not visited[i]:
                    self.all_paths_util(i, d, visited, path)

        # Remove current vertex from path[] and mark it as unvisited
        path.pop()
        visited[u] = False

    # Prints all paths from 's' to 'd'
    def all_paths(self, s, d):

        # Mark all the vertices as not visited
        visited = [False] * self.V

        # Create an array to store paths
        path = []

        # Call the recursive helper function to print all paths
        self.all_paths_util(s, d, visited, path)


def long_words():
    with open("LongWords.txt", "r+") as LW_file:
        contents = LW_file.readlines()
        LW_file.writelines(("".join(gridL) + "," + word + "\n"
                            for word in words if len(word) >= 7 and word not in contents))


def boards():
    with open("Boards.txt", "a") as B_file:
        B_file.write("".join(gridL) + "," + str(len(words)) + "," + str(max(words, key=len)) + "\n")


def fake_long_words():
    with open("FakeLongWords.txt", "r+") as LW_file:
        contents = LW_file.readlines()
        LW_file.writelines(("".join(gridL) + "," + word + "\n"
                            for word in words if len(word) >= 7 and word not in contents))


def fake_boards():
    with open("FakeBoards.txt", "a") as B_file:
        B_file.write("".join(gridL) + "," + str(len(words)) + "," + str(max(words, key=len)) + "\n")


g = Graph(16)
for _ in range(20):
    words = []
    print("All words:")
    gridL = [random.choice(letters) for _ in range(16)]
    print(gridL)
    for start in range(16):
        for dest in range(16):
            g.all_paths(start, dest)
    print(f"Count: {len(words)}")
    # long_words()
    # boards()
    fake_long_words()
    fake_boards()
