def canFinish(numCourses, prerequisites):
    
    # STEP 1: Build the graph
    # create empty list for each course
    # example: {0: [], 1: [], 2: [], 3: []}
    graph = {i: [] for i in range(numCourses)}
    
    # fill the graph with prerequisites
    # [1,0] means 0 → 1 (take 0 f   irst, then 1)
    for a, b in prerequisites:
        graph[b].append(a)
    
    # STEP 2: Create visited list
    # 0 = WHITE (not visited)
    # 1 = GRAY  (currently visiting)
    # 2 = BLACK (fully done)
    visited = [0] * numCourses  # [0, 0, 0, 0] for 4 courses
    
    # STEP 3: DFS function
    def dfs(node):
        
        if visited[node] == 1:   # node is GRAY → cycle!
            return False
        
        if visited[node] == 2:   # node is BLACK → already safe!
            return True
        
        visited[node] = 1        # mark as GRAY (currently visiting)
        
        # visit all neighbors of current node
        for neighbor in graph[node]:
            if not dfs(neighbor):    # if cycle found
                return False
        
        visited[node] = 2        # mark as BLACK (fully done)
        return True
    
    # STEP 4: Run DFS for every course
    # (some courses may not be connected to others)
    for i in range(numCourses):
        if not dfs(i):           # if cycle found
            return False
    
    return True                  # no cycle found, can finish!


