import ast
import copy
import json
from pathlib import Path

import pytest

from hw6.function_xy import F
from hw6.test_function_xy import COMBINATIONS, EXPECTED

DIRECTORY = Path(__file__).parent
MANIFEST = json.loads((DIRECTORY / "mutants/manifest.json").read_text())


def load_mutant(ident):
    path = DIRECTORY / "mutants" / f"{ident}.py"
    namespace = {}
    exec(compile(path.read_text(), str(path), "exec"), namespace)
    return namespace["F"]


@pytest.mark.parametrize("record", MANIFEST, ids=[r["id"] for r in MANIFEST])
def test_kill_mutant(record):
    mutant = load_mutant(record["id"])
    x, y = record["case"]
    original_result = F(x, y)
    assert original_result == record["expected_original"] == EXPECTED[x][y]
    assert mutant(x, y) != original_result
    # The standard 15-case functional suite must also detect this mutant.
    assert any(mutant(a, b) != EXPECTED[a][b] for a, b in COMBINATIONS)


def statements(source):
    function = ast.parse(source).body[0]
    return {n.lineno: n for n in ast.walk(function)
            if isinstance(n, ast.stmt) and not isinstance(n, ast.FunctionDef)}


def local_signature(statement):
    node = copy.deepcopy(statement)
    # Compare each compound statement's own header separately from child statements.
    for field in ("body", "orelse", "finalbody"):
        if hasattr(node, field):
            setattr(node, field, [])
    return ast.dump(node, include_attributes=False)


def test_every_statement_mutated_once():
    source = (DIRECTORY / "function_xy.py").read_text()
    baseline = statements(source)
    assert len(baseline) == len(MANIFEST) == 12
    assert {r["line"] for r in MANIFEST} == set(baseline)
    assert len({r["id"] for r in MANIFEST}) == 12
    for record in MANIFEST:
        changed_source = (DIRECTORY / "mutants" / f'{record["id"]}.py').read_text()
        original_lines, changed_lines = source.splitlines(), changed_source.splitlines()
        assert len(original_lines) == len(changed_lines)
        assert [i for i, pair in enumerate(zip(original_lines, changed_lines), 1)
                if pair[0] != pair[1]] == [record["line"]]
        mutant = statements(changed_source)
        assert set(mutant) == set(baseline)
        assert [line for line in baseline
                if local_signature(baseline[line]) != local_signature(mutant[line])] == [record["line"]]
