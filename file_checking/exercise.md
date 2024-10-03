---
Level (intermediate):
Tags (2-5): file
Dependencies (list any required libraries or leave as "None"):
GitHub user to credit: xettrisomeman
---

# File Handling

---
The python function `check_file` takes a string (`filename`) and returns `True` if there exists file with similar name in the system else returns `False`. The function should use built in `os` method to loop over files and find exact file.

The function takes in `filename`.`extension`

Example Usage:
```python

check_file("script.py") ## True
check_file("something.py") ## False
```