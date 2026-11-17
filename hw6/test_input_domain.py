from itertools import product

import pytest

from hw6.course import summarize_course


LEVELS = (600, 700, 800)
MAJORS = ("swe", "cs", "isa", "infs")
COUNTS = (0, 1, 3)  # 3 is the representative of the >1 partition.
CATEGORIZATION = (
    (600, "swe", 3),
    (700, "cs", 0),
    (800, "isa", 1),
    (600, "infs", 3),
)
COMBINATORIAL = tuple(product(LEVELS, MAJORS, COUNTS))


def check_course(level, major, count):
    students = ["S001", "S002", "S003"][:count]
    original = students.copy()
    expected = {
        "course_code": f"{dict(swe='SWE', cs='CS', isa='ISA', infs='INFS')[major]}-{level}",
        "student_count": count,
        "category": {0: "empty", 1: "single", 3: "multiple"}[count],
        "students": original,
    }
    assert summarize_course(level, major, students) == expected
    assert students == original


@pytest.mark.parametrize(
    "level,major,count", CATEGORIZATION,
    ids=[f"CAT{i:02d}" for i in range(1, 5)],
)
def test_categorization(level, major, count):
    check_course(level, major, count)


@pytest.mark.parametrize(
    "level,major,count", COMBINATORIAL,
    ids=[f"COM{i:02d}-{level}-{major}-{count}"
         for i, (level, major, count) in enumerate(COMBINATORIAL, 1)],
)
def test_combinatorial(level, major, count):
    check_course(level, major, count)


def test_coverage_design():
    """Check domain coverage separately from line/branch coverage."""
    assert len(CATEGORIZATION) == 4
    for column, domain in enumerate((LEVELS, MAJORS, COUNTS)):
        assert {case[column] for case in CATEGORIZATION} == set(domain)
    assert len(COMBINATORIAL) == len(set(COMBINATORIAL)) == 36
    assert set(COMBINATORIAL) == {
        (level, major, count)
        for level in LEVELS for major in MAJORS for count in COUNTS
    }
