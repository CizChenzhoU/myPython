# collections是Python内建的一个集合模块，提供了许多有用的集合类。

# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并规定了
# tuple元素的格式，并可以用属性而不是索引来引用tuple的某个元素。
#
# from collections import namedtuple
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(1, 2)
# print(p.x, p.y)

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
# from collections import deque
# q = deque(['a', 'b', 'c'])
# q.append('x')
# q.appendleft('y')
# print(q)

# defaultdict
# from collections import defaultdict
# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2']) # key2不存在，返回默认值

# OrderedDict
# from collections import OrderedDict
# d = dict([('a', 1),('b', 2),('c',3)])
# print(d)  # dict的Key是无序的
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# print(od)  # OrderedDict的Key是有序的。
# # 注意，OrderdDict的Key会按照插入顺序排列，不是Key本身排序
# od1 = OrderedDict()
# od1['z'] = 1
# od1['y'] = 2
# od1['x'] = 3
# print(list(od1.keys())) #按照插入的Key的顺序返回
# from collections import OrderedDict
#
# class LastUpdatedOrderedDict(OrderedDict):
#
#     def __init__(self,capacity):
#         super(LastUpdatedOrderedDict,self).__init__()
#         self._capacity = capacity
#
#     def __setitem__(self, key, value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove:', last)
#
#         if containsKey:
#             del self[key]
#             print('set:', (key, value))
#         else:
#             print('add:', (key, value))
#         OrderedDict.__setitem__(self, key, value)

# Counter是一个简单的计数器
from collections import Counter

c = Counter()
for ch in 'programmingzzzzz':
    c[ch] = c[ch] + 1

print(c)