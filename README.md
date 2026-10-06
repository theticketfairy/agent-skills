# Ticket Fairy agent skills

Official [Agent Skills](https://agentskills.io) and AI coding agent rules from
[Ticket Fairy](https://www.ticketfairy.com), the ticketing platform for festivals, club
nights, concerts, conferences and tours.

## Skills

| Skill | What it does |
| --- | --- |
| [`find-event-tickets`](skills/find-event-tickets/SKILL.md) | Find Ticket Fairy events, read ticket details, and help a buyer continue to browser checkout. |
| [`start-organising-events`](skills/start-organising-events/SKILL.md) | Help an organiser prepare their first event, start a Ticket Fairy account and compare published feature plans. |

Install them with the [skills CLI](https://skills.sh):

```sh
npx skills add theticketfairy/agent-skills
```

In Claude Code, you can also add them as a plugin:

```text
/plugin marketplace add theticketfairy/agent-skills
/plugin install ticketfairy@ticketfairy
```

The repository is also an [Agent Plugin](https://agent-plugins.org/specification): `plugin.json` describes it,
and `mcp.json` connects the public Ticket Fairy event search MCP server, which needs no account.

The same skills are published at
https://www.ticketfairy.com/.well-known/agent-skills/index.json.

## Rules for AI coding agents

[AGENTS.md](AGENTS.md) tells Claude Code, Cursor, Windsurf, Codex and other coding agents how
to use the Ticket Fairy API, MCP server and CLI correctly. `CLAUDE.md`, `.cursorrules` and
`.cursor/rules/` point to it.

## More

- Developer documentation: https://www.ticketfairy.com/developers
- OpenAPI: https://www.ticketfairy.com/api/v1/openapi.json
- CLI: https://www.npmjs.com/package/ticketfairy
- Support: support@ticketfairy.com

## Licence

MIT. See [LICENSE](LICENSE).
