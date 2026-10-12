# Ticket Fairy agent skills

Official [Agent Skills](https://agentskills.io) and AI coding agent rules from
[Ticket Fairy](https://www.ticketfairy.com), the ticketing platform for festivals, club
nights, concerts, conferences and tours.

## Skills

### Start here

| Skill | What it does |
| --- | --- |
| [`find-event-tickets`](skills/find-event-tickets/SKILL.md) | Find Ticket Fairy events, read ticket details, and help a buyer continue to browser checkout. |
| [`start-organising-events`](skills/start-organising-events/SKILL.md) | Help an organiser prepare their first event, start a Ticket Fairy account and compare published feature plans. |
| [`connect-organiser-account`](skills/connect-organiser-account/SKILL.md) | Get a Ticket Fairy organiser credential for an AI agent, with the person's approval, and use it on the organiser API. |
| [`manage-events-with-the-cli`](skills/manage-events-with-the-cli/SKILL.md) | Manage Ticket Fairy events, tickets, orders, customers, invitations, promotions, check-in and webhooks with the official ticketfairy CLI or its MCP server. |
| [`answer-ticketfairy-questions`](skills/answer-ticketfairy-questions/SKILL.md) | Answer how-to questions about Ticket Fairy from the official guides, with the guides MCP server. |

### By area

Each of these skills lists every published guide for its area, what an agent can do for each
guide, and the exact command-line and MCP routes. The steps stay in the guides, which an agent
reads live from the guides MCP server at `https://www.ticketfairy.com/docs/mcp`.

| Skill | What it does |
| --- | --- |
| [`build-with-the-ticketfairy-api`](skills/build-with-the-ticketfairy-api/SKILL.md) | Use Ticket Fairy access tokens, API keys and webhooks, and sell from your own app. |
| [`connect-ticketfairy-integrations`](skills/connect-ticketfairy-integrations/SKILL.md) | Connect Ticket Fairy to Mailchimp, Zapier and other tools an organiser already uses. |
| [`email-and-market-to-buyers`](skills/email-and-market-to-buyers/SKILL.md) | Send Ticket Fairy emails and SMS to buyers, design emails, and build event websites and landing pages. |
| [`follow-event-type-playbooks`](skills/follow-event-type-playbooks/SKILL.md) | Follow the Ticket Fairy order of work for festivals, club nights, tours, conferences and other event types. |
| [`get-paid-for-ticket-sales`](skills/get-paid-for-ticket-sales/SKILL.md) | Set up Ticket Fairy payment accounts, choose who pays the fees, pick currencies and follow payouts. |
| [`grow-sales-with-referrals`](skills/grow-sales-with-referrals/SKILL.md) | Set up Ticket Fairy referral rewards and see who brought in each sale. |
| [`manage-brand-and-team`](skills/manage-brand-and-team/SKILL.md) | Manage a Ticket Fairy brand kit, team roles, several brands, collectives and account security. |
| [`manage-invitations-and-guest-lists`](skills/manage-invitations-and-guest-lists/SKILL.md) | Send Ticket Fairy invitations and guest tickets, and manage partner allocations and group bookings. |
| [`manage-orders-and-refunds`](skills/manage-orders-and-refunds/SKILL.md) | Find and manage Ticket Fairy orders: checkout questions, order approval, refunds, transfers, waiting lists and buyer support. |
| [`manage-venue-pages`](skills/manage-venue-pages/SKILL.md) | Claim a Ticket Fairy venue page and keep its details current. |
| [`read-event-reports`](skills/read-event-reports/SKILL.md) | Read Ticket Fairy event reports: sales, page views, buyers and what each figure counts. |
| [`run-door-check-in`](skills/run-door-check-in/SKILL.md) | Run Ticket Fairy check-in at the door: scanning, entry rules, live check-in reports and wristbands. |
| [`run-event-production`](skills/run-event-production/SKILL.md) | Run event production in Ticket Fairy Event Management: budgets, schedules, artists, crew, sponsors, traders, volunteers and compliance. |
| [`run-event-workflows`](skills/run-event-workflows/SKILL.md) | Follow Ticket Fairy start-to-finish workflows: on-sale day, repeating last year's event, and changing plans. |
| [`run-promotions-and-discounts`](skills/run-promotions-and-discounts/SKILL.md) | Create Ticket Fairy promo codes, group discounts and promoter links. |
| [`sell-add-ons-and-tables`](skills/sell-add-ons-and-tables/SKILL.md) | Sell Ticket Fairy add-ons beside tickets: merchandise, parking, donations, tables and accommodation. |
| [`set-up-event-tickets`](skills/set-up-event-tickets/SKILL.md) | Set up a Ticket Fairy event: ticket types, release tiers, sessions, seating, add-ons, resale and transfer rules. |
| [`solve-ticketing-problems`](skills/solve-ticketing-problems/SKILL.md) | Solve common event ticketing problems with Ticket Fairy: queues, no-shows, reports, marketing and access. |
| [`track-advertising-campaigns`](skills/track-advertising-campaigns/SKILL.md) | Connect advertising pixels and conversion tracking to Ticket Fairy and see which campaigns sold tickets. |
| [`use-vault-and-capital`](skills/use-vault-and-capital/SKILL.md) | Use the Ticket Fairy Vault account, cards, transfers and invoices, and Capital working capital. |
| [`work-with-fai`](skills/work-with-fai/SKILL.md) | Use Fai, the assistant inside the Ticket Fairy dashboard, for questions, the inbox and the buyer concierge. |

`scripts/build_guide_skills.py` builds the area skills from the guide catalogue; the script
explains how to export it and run it.

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
and `mcp.json` connects the public Ticket Fairy event search and guides MCP servers, which need no account.

`find-event-tickets` and `start-organising-events` are also published at
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
