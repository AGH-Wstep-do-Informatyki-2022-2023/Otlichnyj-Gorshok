import re

s = 'asdf=5;iwantthis123jasd'
result = re.search('asdf=5;(.*)123jasd', s)
print(result.group(0))