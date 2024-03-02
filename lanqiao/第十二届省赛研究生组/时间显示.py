DAY = 24 * 60 * 60
HOUR = 60 * 60
MINUTE = 60
time = int(input())
time = time // 1000 % DAY
hour = time // HOUR
time -= hour * HOUR
minute = time // MINUTE
time -= MINUTE * minute
# print(hour, minute, time)
ans = ""
if len(str(hour)) == 1:
    ans = ans + "0" + str(hour)
else:
    ans += str(hour)
ans += ":"
if len(str(minute)) == 1:
    ans = ans + "0" + str(minute)
else:
    ans += str(minute)
ans += ":"
if len(str(time)) == 1:
    ans = ans + "0" + str(time)
else:
    ans += str(time)
print(ans)
