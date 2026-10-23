#!/usr/bin/env python3
"""Copy canonical skills into the focused repositories in skill-repositories.json.

Run after refreshing and reviewing the canonical skills:
    python3 scripts/build_skill_repositories.py /path/to/release-packages

This writes release files locally. It does not create GitHub repositories, publish,
install skills, or submit indexing telemetry. Re-run from the committed hub before
publishing so SOURCE.json records that exact source revision.
"""

import hashlib
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

HUB = 'https://github.com/theticketfairy/agent-skills'


def description(skill):
    text = skill.read_text()
    name = re.search(r'^name: (.+)$', text, re.MULTILINE).group(1)
    if name != skill.parent.name:
        raise ValueError(f'Skill folder and name differ: {skill.parent.name}')
    value = re.search(r'^description: (.+)$', text, re.MULTILINE).group(1)
    return json.loads(value) if value.startswith('"') else value


def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: build_skill_repositories.py <release-packages-directory>')
    source = Path(__file__).resolve().parent.parent
    output = Path(sys.argv[1]).resolve()
    if output == source or source in output.parents:
        sys.exit('Use a release directory outside the canonical repository.')
    packages = json.loads((source / 'skill-repositories.json').read_text())
    selected = [skill for package in packages.values() for skill in package['skills']]
    canonical = {path.parent.name for path in (source / 'skills').glob('*/SKILL.md')}
    if len(selected) != len(set(selected)) or set(selected) != canonical:
        sys.exit('Collections must partition the canonical skills without aliases or omissions.')
    commit = subprocess.check_output(['git', '-C', str(source), 'rev-parse', 'HEAD'], text=True).strip()
    dirty = bool(subprocess.check_output(['git', '-C', str(source), 'status', '--porcelain'], text=True).strip())
    for repository, package in packages.items():
        target = output / repository
        target.mkdir(parents=True, exist_ok=True)
        inventory = []
        provenance = {'source_repository': HUB, 'source_commit': commit,
                      'uncommitted_source': dirty, 'skills': []}
        for name in package['skills']:
            skill = source / 'skills' / name / 'SKILL.md'
            summary = description(skill)
            directory = target / 'skills' / name
            directory.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(skill, directory / 'SKILL.md')
            inventory.append(f'| [`{name}`](skills/{name}/SKILL.md) | {summary} |')
            provenance['skills'].append({'name': name, 'source_path': f'skills/{name}/SKILL.md',
                                         'sha256': hashlib.sha256(skill.read_bytes()).hexdigest()})
        for filename in ['AGENTS.md', 'LICENSE']:
            shutil.copyfile(source / filename, target / filename)
        (target / 'SOURCE.json').write_text(json.dumps(provenance, indent=2) + '\n')
        first = package['skills'][0]
        readme = f'''# {package['title']}

{package['description']}

Official [Ticket Fairy](https://www.ticketfairy.com) agent skills, selected from the
[canonical collection]({HUB}). Install this collection or the individual skills you
need; their names and instructions are the same in both repositories.

## Install

```sh
npx skills add theticketfairy/{repository}
```

List the available skills without installing:

```sh
npx skills add theticketfairy/{repository} --list
```

Or select one skill:

```sh
npx skills add theticketfairy/{repository} --skill {first}
```

The current Skills CLI requires Node.js 22.20 or later. Skills install to your
current project by default. Choose the supported agent in the CLI. See the [Skills CLI documentation](https://skills.sh/docs/cli).

## Skills

| Skill | When to use it |
| --- | --- |
{chr(10).join(inventory)}

## Authority and recovery

A skill grants no account permission and does not authorise sending messages,
creating tickets, refunding orders or taking payment. Keep each action within the
person's approved scope and current role. Buyer discovery is public and read-only;
buyer purchases use a separately supported handler and explicit approval of the
final tickets, total and currency, or continue in the official browser checkout.
Organiser credentials do not grant purchase authority. Keep credentials out of chat
and logs. After an uncertain change, recover its original result before
retrying; never issue a new refund, send or ticket grant to resolve uncertainty.

## Documentation and maintenance

- [Official guides](https://www.ticketfairy.com/guides), read live with the public
  [guides MCP server](https://www.ticketfairy.com/docs/mcp).
- [Developer documentation](https://www.ticketfairy.com/developers).
- [Published skill index](https://www.ticketfairy.com/.well-known/agent-skills/index.json).
- [Agent rules](AGENTS.md) and [canonical source]({HUB}).

`SOURCE.json` records the canonical revision and skill hashes. Make instruction
changes in the canonical repository, then use its
`scripts/build_skill_repositories.py` to copy the reviewed release into this
repository. Do not maintain an independent fork of a skill here.

GitHub publication does not prove skills.sh indexing. Its
[FAQ](https://skills.sh/docs/faq) describes automatic listing through anonymous
Skills CLI installation telemetry. No installation count or indexing status is
claimed by this repository.

## Licence

MIT. See [LICENSE](LICENSE).
'''
        (target / 'README.md').write_text(readme)
        print(f'{repository}: {len(package["skills"])} skills')


if __name__ == '__main__':
    main()
