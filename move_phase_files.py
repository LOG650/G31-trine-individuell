from pathlib import Path

root = Path(r'c:/Users/trioe/OneDrive/Trine/Molde 3.år/V LOG650 Forskningsprosjekt log og KI/G31-trine-individuell')
commands = [
    ('Proposal.docx', root / '011 fase 1 - proposal' / 'Proposal.docx'),
    ('Prosjektplan.docx', root / '012 fase 2 - plan' / 'Prosjektplan.docx'),
    ('LOG650 Gantt.mpp', root / '012 fase 2 - plan' / 'LOG650 Gantt.mpp'),
]

for src_name, dst_path in commands:
    src_path = root / src_name
    if src_path.exists():
        print(f'Moving {src_path} -> {dst_path}')
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        src_path.replace(dst_path)
    else:
        print(f'Skipping missing file: {src_path}')
