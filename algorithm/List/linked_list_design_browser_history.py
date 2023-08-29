"""
link: https://leetcode.com/problems/design-browser-history/
"""


class Site:
    def __init__(self, url=0, next=None, previous=None):
        self.url = url
        self.next = next
        self.previous = previous


class BrowserHistory(object):
    def __init__(self, url):
        self.head = self.current = Site(url=url)
        # 아래 처럼 따로 선언하면 Site 가 각각 생성되는 것임. head & current가 같은 객체가 아니게 됨.
        # self.head = Site(url=url)
        # self.current = Site(url=url)

    def visit(self, url):
        new_site = Site(url=url, previous=self.current)
        self.current.next = new_site
        self.current = self.current.next
        # current = self.head
        # while current.next:
        #     current = current.next
        # current.next = new_site
        # self.now = new_site

    def back(self, steps):
        while steps > 0 and self.current.previous is not None:
            steps -= 1
            self.current = self.current.previous
        # current = self.now
        # for _ in range(steps):
        #     if current.previous:
        #         current = current.previous
        #     else:
        #         self.now = current
        #         return current
        # self.now = current
        return self.current.url

    def forward(self, steps):
        while steps > 0 and self.current.next is not None:
            steps -= 1
            self.current = self.current.next
        # current = self.now
        # for _ in range(steps):
        #     if current.next:
        #         current = current.next
        #     else:
        #         self.now = current
        #         return current
        # self.now = current
        return self.current.url


browserHistory = BrowserHistory("google1.com")
browserHistory.visit("google2.com")
browserHistory.visit("google3.com")
browserHistory.visit("google4.com")
browserHistory.visit("google5.com")
browserHistory.visit("google6.com")
browserHistory.visit("google7.com")
browserHistory.visit("google8.com")
browserHistory.visit("google9.com")
browserHistory.visit("google10.com")
print(browserHistory.back(8))
print(browserHistory.forward(4))
browserHistory.visit("google11.com")
browserHistory.visit("google12.com")
print(browserHistory.back(4))
print(browserHistory.forward(1))
print(browserHistory.forward(2))
print(browserHistory.forward(3))
print(browserHistory.forward(4))
