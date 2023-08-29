graph = {
    "A": ["B", "D", "E"],
    "B": ["A", "C", "D"],
    "C": ["B"],
    "D": ["A", "B"],
    "E": ["A"],
}
visited = []


def dfs(cur_v):
    visited.append(cur_v)
    for v in graph[cur_v]:
        if v not in visited:
            dfs(v)


dfs(graph, "A")


def traversal(root):
    if root is None:
        return
    traversal(root.left)
    traversal(root.right)


import json

student_data = {}
with open("student_file.json", "w") as f:
    json.dump(student_data, f)

with open("student_file.json", "r") as f:
    st_python = json.load(f)

# python 메모리에 있는 json fotmat data를 python 객체로 읽기
# 언제쓰나?
st_json = json.dumps(student_data)
st_python2 = json.loads(st_json)
