import re

"""
(?:pattern)
不匹配分组
"""

a = '<div>div text</div> <a href="#">click me</a>'
print(re.findall(r'(<.*?>)(.*?)(</.*?>)', a))
# [('<div>', 'div text', '</div>'), ('<a href="#">', 'click me', '</a>')]

a = '<div>div text</div> <a href="#">click me</a>'
print(re.findall(r'(?:<.*?>)(.*?)(?:</.*?>)', a))
# ['div text', 'click me']


"""
(?=pattern)
正向肯定预查
"""
a = 'Windows95'
print(re.findall(r'Windows(?=95|98|NT|2000)', a))
# ['Windows'] 
a = 'Windows10'
print(re.findall(r'Windows(?=95|98|NT|2000)', a))
# []


"""
(?!pattern)
正向否定预查
"""
a = 'Windows95'
print(re.findall(r'Windows(?!95|98|NT|2000)', a))
# []
a = 'Windows10'
print(re.findall(r'Windows(?!95|98|NT|2000)', a))
# ['Windows'] 


"""
(?<=pattern)
反向肯定预查
"""
a = 'aPhone bPhone xxxPhone'
print(re.findall(r'(?<=a|b|c)Phone', a))
# ['Phone', 'Phone']


"""
(?<!pattern)
反向否定预查
"""
a = 'aPhone bPhone xxxPhone'
print(re.findall(r'(?<!a|b|c)Phone', a))
# ['Phone']