from collections import deque


def hot_potato(names=None, circles=1):
    if names:
        players = deque(names)
    else:
        players = deque()
    while len(players) > 1:
        for i in range(circles):
            players.append(players.pop())
        players.pop()
    return players.pop()


if __name__ == '__main__':
    assert hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7) == 'Bill'
