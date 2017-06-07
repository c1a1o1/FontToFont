from datetime import datetime

start = datetime.now()

sm = 0
for i in range(10000):
    sm += i

end = datetime.now()

during_time = end - start

print("during time:{}".format(during_time.total_seconds()))