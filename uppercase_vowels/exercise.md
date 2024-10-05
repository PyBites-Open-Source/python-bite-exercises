---
Level (beginner, intermediate, advanced): beginner
Tags (2-5): string
Dependencies (list any required libraries or leave as "None"):
GitHub user to credit: xettrisomeman
---

# Uppercase Vowels

---
 The Python function `uppercase_vowels` takes in `string` or `filename` and returns `string` with vowels uppercased. The `string` can contain punctuation, uppercase consonants but in the final result vowels should be uppercased and consonants should be lowercased and punctuations should be removed while preserving spaces.

> Extension of `file` should not be uppercased.

Examples of `extensions`:
```
jpeg
jpg
mp3
mp4
pdf
png
txt
exe
```


Example Usage:
```python

uppercase_vowels("abcDeFGHIJ") # AbcdEfghIj
uppercase_vowels("..-") # "   "
uppercase_vowels("file monk.exe") # fIlE mOnk.exe
```
