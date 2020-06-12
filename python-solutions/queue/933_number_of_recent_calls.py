from collections import deque

'''
Keep a queue of the most recent calls in increasing order of t. When we see a new call with time t, remove all 
calls that occurred before t - 3000
'''


class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)

        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
def main():
    result = RecentCounter()
    print(result.ping(100))  # 1
    print(result.ping(1000))  # 2
    print(result.ping(2000))  # 3
    print(result.ping(3000))  # 4
    print(result.queue[0])  # 100
    print(result.queue)  # deque([100, 1000, 2000, 3000])
    print(result.ping(4000))  # 4
    print(result.queue[0])  # 1000 , popleft was called and 100 was removed
    print(result.queue)  # deque([1000, 2000, 3000, 4000])
    print(result.ping(5000))  # 4
    print(result.queue)  # deque([2000, 3000, 4000, 5000])


if __name__ == '__main__':
    main()
