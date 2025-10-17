from collections import deque

dq = deque([])


for x in range(5):
    dq.append(x+1)

dq.popleft()
dq.popleft()

print(dq)