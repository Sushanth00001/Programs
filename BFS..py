def BFS(graph,start):
    visited=set()
    q=[start]
    while q:
        n=q.pop(0)
        if n not in visited:
            print(n,end=" ")
            visited.add(n)
            q.extend(graph[n])
graph={
    'A':['B','C'],
    'B':['A','D','E'],
    'C':['A','F'],
    'D':['B'],
    'E':['B','F'],
    'F':['C','E']
}
BFS(graph, 'A')