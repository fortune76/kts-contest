class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.childrens = []
        self.visited = False

    def add_node(self, node):
        self.childrens.append(node)


def get_node(nodes, val):
    node = None
    for i in nodes:
        if i.value == val:
            node = i
            break
    if not node:
        node = Node(val)
        nodes.append(node)
    return node

def main():
    MAX_NODES = int(input())
    nodes = []
    while True:
        try:
            line = input()
            val1, val2 = line.split()
            val1, val2 = int(val1), int(val2)
            node1 = get_node(nodes, val1)
            node2 = get_node(nodes, val2)
            node1.add_node(node2)
            node2.add_node(node1)
        except EOFError:
            break
    result = 0
    for i in nodes:
        if not i.visited:
            result += dfs(i)
    result += MAX_NODES - len(nodes) 
    print(result)

def dfs(node):
    if len(node.childrens) == 0:
        node.visited = True
        return 1
    elif (len(node.childrens) == 1 and len(node.childrens[0].childrens) == 1 and node.childrens[0].childrens[0] == node):
        node.visited = True
        node.childrens[0].visited = True
        node.childrens[0] = True
        return 1
    else:
        summary = len(node.childrens)
        for i in node.childrens:
            i.visited = True
            if (len(i.childrens) != summary):
                return 0
        return 1
main()
    