# 937. Reorder Data in Log Files

## Problem

You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

- Letter-logs: All words (except the identifier) consist of lowercase English letters.
- Digit-logs: All words (except the identifier) consist of digits.

Reorder these logs so that:

1. The letter-logs come before all digit-logs.
2. The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them
   lexicographically by their identifiers.
3. The digit-logs maintain their relative ordering.

Return the final order of the logs.

## Example

### Example1

```text
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
Explanation:
The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".
```

### Example2

```text
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
```

## Constraint

- 1 <= logs.length <= 100
- 3 <= logs[i].length <= 100
- All the tokens of logs[i] are separated by a single space.
- logs[i] is guaranteed to have an identifier and at least one word after the identifier.

## 풀이 요약

- 배열의 요소를 split해서 letter-logs와 digit-logs를 구분한다.
- letter-logs를 정렬한다.
    1. 문자열을 사전순으로 정렬
    2. 문자열이 동일한 경우 식별자를 사용해 정렬
- 정렬한 배열과 digit-logs 배열을 합친다.

## 복잡도

### 시간 복잡도

- logs 배열을 순회하면서 각 문자열을 split한다.
    - logs 배열의 길이를 `l`, 문자열의 최대 길이를 `s` 라고 했을때 `O(l*s)` 이다.
- letter-logs 배열을 정렬한다.
    - 최악의 경우 logs 배열이 모두 letter-logs로 구성되어 있다고 했을 때 `O(l*log(l))`이다. (정렬이 `O(n*log(n))`이라는 가정)
    - 모든 letter-logs 내용이 동일해 식별자를 통해 추가로 정렬하는 경우도 있지만, 이 경우 정렬이 한번 더 이루어져 `O(2*l*log(l))` 이기 때문에 결국 `O(l*log(l))`이다.

### 공간 복잡도

- letter-logs 배열과 digit-logs 배열을 할당하지만 두 배열의 공간을 합쳐야 logs 배열의 크기이다.
- letter-logs 배열을 정렬하지만 추가적인 공간을 할당하지 않는다.
- 따라서 공간복잡도는 `O(n)` 이다.