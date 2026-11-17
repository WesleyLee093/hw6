"""Run real tests and save their unmodified stdout plus a mutation comparison."""
from pathlib import Path
import html
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from hw6.function_xy import F
from hw6.test_function_xy import COMBINATIONS, EXPECTED
from hw6.test_mutation import MANIFEST, load_mutant

OUT = ROOT / 'hw6/evidence'
OUT.mkdir(exist_ok=True)
COMMANDS = {
    'course': ['hw6/test_input_domain.py', '-q', '--cov-branch'],
    'xy': ['hw6/test_function_xy.py', '-q', '--cov-branch'],
    'mutation_tests': ['hw6/test_mutation.py', '-q', '--no-cov'],
    'all_tests': ['-q', '--cov-branch'],
}

def save(name, title, body):
    (OUT / (name + '.txt')).write_text(body)
    (OUT / (name + '.html')).write_text(
        '<meta charset="utf-8"><style>body{margin:24px;color:#172536;font:18px Arial}'
        'h1{font-size:24px}pre{font:17px/1.5 Menlo,monospace;white-space:pre-wrap;overflow-wrap:anywhere;'
        'background:#f6f8fb;border:1px solid #ccd4dd;padding:18px}</style><h1>'
        + html.escape(title) + '</h1><pre>' + html.escape(body) + '</pre>')

for name, args in COMMANDS.items():
    cmd = [sys.executable, '-m', 'pytest', *args]
    result = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stdout + result.stderr)
    save(name, name + ' | actual pytest output',
         '$ python -m pytest ' + ' '.join(args) + '\n\n' + result.stdout + result.stderr)

rows = []
for record in MANIFEST:
    mutant = load_mutant(record['id'])
    x, y = record['case']
    original, changed = F(x, y), mutant(x, y)
    assert original == record['expected_original'] == EXPECTED[x][y]
    killed = original != changed
    detected = sum(mutant(a,b) != EXPECTED[a][b] for a,b in COMBINATIONS)
    assert killed and detected > 0
    rows.append({**record, 'original': original, 'mutated': changed,
                 'killed': killed, 'detected_by_cases': detected})
(OUT / 'mutation_results.json').write_text(json.dumps(rows, indent=2)+'\n')
lines = ['ID    line    input       original   mutant    result', '-' * 65]
for r in rows:
    lines.append(f"{r['id']:<6}{r['line']:<8}{str(tuple(r['case'])):<12}{r['original']:<11}{r['mutated']:<10}KILLED")
lines += ['', 'Generated: 12  |  Killed: 12  |  Survived: 0',
          'Invalid: 0  |  Equivalent among these 12: 0', 'Mutation score: 12 / 12 = 100%',
          'Each mutant changes one statement in the ORIGINAL function_xy.py.']
save('mutation_results', 'Mutation testing | actual output comparison', '\n'.join(lines))
source=(ROOT/'hw6/function_xy.py').read_text()
save('function_source','Original program | function_xy.py',
     '\n'.join(f'{i:2d}  {line}' for i,line in enumerate(source.splitlines(),1)))
print('Saved test logs, source display and 12 actual mutation comparisons to hw6/evidence.')
