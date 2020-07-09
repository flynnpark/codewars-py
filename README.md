# Codewars 연습 프로젝트

각 문제의 답은 `solutions` 폴더 내에 정리되어 있으며, 테스트 코드는 `test` 폴더에 정리되어 있음.

<details>
<summary>004. Roman Numerals Encoder</summary>

#### [Codewars Link](https://www.codewars.com/kata/51b62bf6a9c58071c600001b)

Create a function taking a positive integer as its parameter and returning a string containing the Roman Numeral representation of that integer.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.

### Example:

```python
solution(1000) # should return 'M'
```

### Help:

```
Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
```

Remember that there can't be more than 3 identical symbols in a row.

More about roman numerals - http://en.wikipedia.org/wiki/Roman_numerals

</details>
<details>
<summary>003. Find The Parity Outlier</summary>

#### [Codewars Link](https://www.codewars.com/kata/5526fc09a1bbd946250002dc)

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer `N`. Write a method that takes the array as an argument and returns this "outlier" `N`.

### Examples

```
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
```

</details>
<details>
<summary>002. Find the odd int</summary>

#### [Codewars Link](https://www.codewars.com/kata/54da5a58ea159efa38000836)

Given an array, find the integer that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

</details>
<details>
<summary>001. Replace With Alphabet Position</summary>

#### [Codewars Link](https://www.codewars.com/kata/546f922b54af40e1e90001da)

Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

`"a" = 1`, `"b" = 2`, etc.

Example

```python
alphabet_position("The sunset sets at twelve o' clock.")
```

Should return `"20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"`(as a string)

</details>
