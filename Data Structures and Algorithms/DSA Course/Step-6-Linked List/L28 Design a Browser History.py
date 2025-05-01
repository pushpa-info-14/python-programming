class ListNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Browser:
    def __init__(self, url):
        self.current = ListNode(url)

    def visit(self, url):
        new_node = ListNode(url)
        new_node.prev = self.current
        self.current.next = new_node
        self.current = new_node

    def back(self, steps: int):
        while steps:
            if self.current.prev:
                self.current = self.current.prev
            else:
                break
            steps -= 1
        return self.current.data

    def forward(self, steps):
        while steps:
            if self.current.next:
                self.current = self.current.next
            else:
                break
            steps -= 1
        return self.current.data


browser = Browser("takeyouforward.org")
browser.visit("google.com")
browser.visit("instagram.com")
browser.visit("facebook.com")
print(browser.back(1))
print(browser.back(1))
print(browser.forward(1))
browser.visit("takeyouforward.org")
print(browser.forward(2))
print(browser.back(2))
print(browser.back(7))
