import time

# print(time.asctime())
# print(time.time())
# # 1622525174.31947
# # 1622525227.5755525
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))

# 获取两天前的时候
now_timestamp = time.time()
two_day_before = now_timestamp - 60*60*24*2
three_day_last = now_timestamp + 60*60*24*3
# print(time.localtime(two_day_before))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(two_day_before)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(three_day_last)))