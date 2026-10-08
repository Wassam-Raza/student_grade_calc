import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from student_project import validate_name, validate_marks

def test_valid_name():
 assert validate_name("Ali") is True
def test_empty_name():
 assert validate_name("") is False
def test_valid_marks():
 assert validate_marks(85) is True
def test_negative_marks():
 assert validate_marks(-10) is False
def test_marks_above_limit():
 assert validate_marks(150) is False