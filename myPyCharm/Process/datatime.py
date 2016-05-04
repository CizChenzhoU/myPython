# 常用的内置模块
# datetime是Python处理日期和时间的标准库

# 获取当前日期和时间
# from datetime import datetime
#
# now = datetime.now()  # 获取当前datetime
# print(now)  # 输入当前日期
# print(type(now))  # 查看类型

# 注意datetime是模块，datetime模块还包含以恶搞datetime类，
# 通过from datetime import datetime导入的才是datetime这个
# 类。如果只导入import datetime,则必须引用全名datetime.datetime
# datetime.now()返回当前日期和时间，其类型是datetime

# 获得指定日期和时间
# from datetime import datetime
# dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
# print(dt)

# datetime转换为timestamp
# 在计算机中，时间实际上是用数字表示的。我们把1970年1月1日00：00：00 UTC+00：00时区的时刻称为epoch time
# 记为0（1970年以前的时间timestamp为负数）当前时间就是相对于epoch time的秒数，称为timestamp
# from datetime import datetime
# dt = datetime(2016,5,4,12,20) # 用指定日期时间创建datetime
# stamp =dt.timestamp() # 把timestamp转换为datetime
# print(stamp)
# 只要Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
# 某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000
# 就得到Python的浮点表示。

# timestamp转化为datetime
# 1462335600.0

# from datetime import datetime
# t = 1462335600.0
# print(datetime.fromtimestamp(t)) # 本地时间
# print(datetime.utcfromtimestamp(t)) # UTC时间

# str转换为datetime
# from datetime import datetime
# cday = datetime.strptime('2016-5-4 10:10:10','%Y-%m-%d %H:%M:%S')
# print(cday)

# datetime 转换为str
# from datetime import datetime
# now = datetime.now()
# print(now.strftime(S'%a,%b %d %H:%M'))

# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime.
# from datetime import datetime,timedelta
# now = datetime.now()
# print(now) # 当前时间
# print(now + timedelta(hours=10)) # 小时+10
# print(now - timedelta(days=1)) # 减一天
# print(now + timedelta(days=2,hours=12))

# 本地时间转化为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC + 8:00时区的时间
# 而UTC时间指UTC+0：00时区的时间。
# 一个datetime类型有一个时区属性tzinfo,但是默认为None,所以无法区分这个datetime到底是哪个时区
# 除非强行给datetime设置一个时区

# from datetime import datetime,timedelta,timezone
# tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC +8：00
# now = datetime.now()
# print(now)
# dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8：00
# print(dt)

# 时区转化
# 拿到UTC时间，并强制设置时区为UTC+0：00
# from datetime import datetime,timedelta,timezone
#
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
# # astimezone()将转换时区为北京时间
# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# print(bj_dt)
# 转换时区为东京时间
# tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt)
# # astimezone()将bj_dt转换时区为东京时间:
# tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt2)
# 时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
# 利用带时区的datetime,通过astimezone()方法，可以转换到任意时区。
# 注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt
# 到tokyo_dt的转换

# 小结
# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间
# 如果要存储datetime,最佳方法是将其转换为timestamp再存储，因为timestamp的值和时区完全无关。

# 练习
# 假设你要获取了用户输入的日期和时间如：2015-1-21 9：01：30 ，以及一个时区信息如UTC+5:00，均是str,
# 请编写一个函数将其转换为timestamp
import re
from datetime import datetime,timezone,timedelta


def to_timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')  # 字符串转为为时间格式
    tz = re.match(r'^(\w{3})([\+|\-]\d+):(\d+)', tz_str)  # 正则判断UTC格式
    dlt = int(tz.group(2)) - 8  # 获得需要减少的时间
    dt = dt - timedelta(hours=dlt)  # 减去时间
    return dt.timestamp()  # 转换时间戳，返回


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
print(t1)
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print(t2)
