"""Generate 12 first-order mutants, always from the original source."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "hw6/function_xy.py"
# id, original statement, replacement, distinguishing input, expected original output
SITES = [
    ("M01", "scaled = y // 10", "scaled = y + 10", [1, 10], 1),
    ("M02", "if x < 0:", "if x <= 0:", [0, 10], 0),
    ("M03", "weight = -1", "weight = -2", [-1, 10], -1),
    ("M04", "elif x == 0:", "elif x == 1:", [0, 10], 0),
    ("M05", "weight = 0", "weight = 1", [0, 10], 0),
    ("M06", "elif x == 1:", "elif x == 2:", [1, 10], 1),
    ("M07", "weight = 1", "weight = 4", [1, 10], 1),
    ("M08", "elif x == 2:", "elif x > 2:", [2, 10], 2),
    ("M09", "weight = 2", "weight = 5", [2, 10], 2),
    ("M10", "weight = 3", "weight = 6", [3, 10], 3),
    ("M11", "result = weight * scaled", "result = weight + scaled", [0, 10], 0),
    ("M12", "return result", "return result + 1", [1, 10], 1),
]


def main():
    original = SOURCE.read_text()
    records = []
    for ident, before, after, case, expected in SITES:
        lines = original.splitlines(keepends=True)
        indices = [i for i, line in enumerate(lines) if line.strip() == before]
        assert len(indices) == 1
        index = indices[0]
        lines[index] = lines[index].replace(before, after)
        mutated = "".join(lines)
        compile(mutated, ident, "exec")
        (ROOT / f"hw6/mutants/{ident}.py").write_text(mutated)
        records.append(dict(id=ident, line=index + 1, before=before, after=after,
                            case=case, expected_original=expected))
    (ROOT / "hw6/mutants/manifest.json").write_text(json.dumps(records, indent=2) + "\n")
    print(f"Generated {len(records)} mutants from {SOURCE.name}; one statement changed each.")


if __name__ == "__main__":
    main()
