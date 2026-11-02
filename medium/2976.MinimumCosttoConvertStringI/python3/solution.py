class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        distance = [
            [0 for _ in range(26)] for _ in range(26)
        ]  # distance[i][j] = cost to change original[i] to changed[j]
        for i in range(26):
            for j in range(26):
                distance[i][j] = float("inf") if i != j else 0

        # initialize distance
        for i, orig_char in enumerate(original):
            orig_val = ord(orig_char) - ord("a")
            changed_val = ord(changed[i]) - ord("a")
            distance[orig_val][changed_val] = min(
                cost[i], distance[orig_val][changed_val]
            )
        # floyd warshall
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    distance[i][j] = min(
                        distance[i][j], distance[i][k] + distance[k][j]
                    )

        distance_val = 0
        for i, src in enumerate(source):
            src_val = ord(src) - ord("a")
            tgt_val = ord(target[i]) - ord("a")
            if distance[src_val][tgt_val] == float("inf"):
                return -1

            distance_val += distance[src_val][tgt_val]
        return distance_val

