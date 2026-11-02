class ListNode:
    def __init__(self, val: str, Next=None, prev=None):
        self.val = val
        self.next = Next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = homepage
        self.page = ListNode(self.homepage)
        self.x = 0
        self.idx = 0

    def visit(self, url: str) -> None:
        self.x += 1
        self.idx += 1
        newNode = ListNode(url, prev=self.page)
        self.page.next = newNode
        self.page = self.page.next
        


    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.idx == 0:
                break
            self.page = self.page.prev
            self.idx -= 1
        return self.page.val
    
    def forward(self, steps: int) -> str:
        while steps:
            steps -= 1
            if self.page.next is None:
                break
            self.page = self.page.next
            self.idx += 1

        return self.page.val



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)