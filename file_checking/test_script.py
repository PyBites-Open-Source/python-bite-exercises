from script import check_file



def test_check_file_script_py():
    assert check_file("script.py") is True

def test_check_file_something_else_py():
    assert check_file("something_else.py") is False

def test_check_file_exercise_md():
    assert check_file("exercise.md") is True