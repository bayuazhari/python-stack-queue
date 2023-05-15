from collections import deque

queue = deque([1,2,3,4,5])
print('antrian sekarang: ', queue)

# masuk antrian
queue.append(6)
print('antrian masuk: ', 6)
print('antrian sekarang: ', queue)

queue.append(7)
print('antrian masuk: ', 7)
print('antrian sekarang: ', queue)

# keluar antrian
out = queue.popleft()
print('antrian keluar: ', out)
print('antrian sekarang: ', queue)