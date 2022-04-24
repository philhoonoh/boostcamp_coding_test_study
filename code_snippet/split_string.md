# 문자열분리
- 알고리즘 문제를 풀다 보면 문자열을 일정크기로 잘라야하는 경우가 있다.

```python
def get_splits(s, split_len):
    return [s[i:i+split_len] for i in range(0, len(s), split_len)]

text = 'asdfhlkasdfjhlasdf'

print(get_splits(text, 2))
# ['as', 'df', 'hl', 'ka', 'sd', 'fj', 'hl', 'as', 'df']

print(get_splits(text, 4))
# ['asdf', 'hlka', 'sdfj', 'hlas', 'df']

print(get_splits(text, 3))
# ['asd', 'fhl', 'kas', 'dfj', 'hla', 'sdf']
```





