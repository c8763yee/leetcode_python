class Solution:
    def isPathCrossing(self, path: str) -> bool:
        previous = {0,}
        path_point = { # (x, y) = 100000x + y
            'N': 1,
            "E": 100000,
            "S": -1,
            "W": -100000
        }
        start_point = 0
        for c in path:
            start_point += path_point[c]
            if start_point in previous:
                return True
            
            previous.add(start_point)
        return False