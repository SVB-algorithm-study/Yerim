Default dict 를 잘 사용할 수 있게 되었다.
a.sorted() 는 정렬한 값을 반환, a는 그대로.
a.sort() 는 a를 정렬, 반환 값 없음. + str에 사용 불가!!!



49. Group Anagrams
Medium
15.9K
450
Companies
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
Accepted
2M
Submissions
3.1M
Acceptance Rate
66.8%