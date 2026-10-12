---
name: sell-add-ons-and-tables
description: "Sell Ticket Fairy add-ons beside tickets: merchandise, parking, donations, tables and accommodation. Use when an organiser wants to sell extras with their event."
---

# Sell add-ons and tables

This skill covers merchandise, parking, donations, tables and accommodation on Ticket Fairy. It lists the 1 published guides for this area and what an agent can do for each one.

## How to work

1. **Find the guide.** Pick the guide below that matches the task. If none fits, search all guides:
   connect an MCP client to `https://www.ticketfairy.com/docs/mcp` (Streamable HTTP, no account or
   key) and call `search_guides` with the task in plain words.
2. **Read it before you act.** Call `get_guide` with the guide's slug. It returns who the guide is
   for, what to have ready, every step and the common questions. Follow those steps; do not guess
   the dashboard from memory.
3. **Do the work, or hand it over.** Each guide below says what an agent can do:
   - **Command line.** With the organiser's permission, install the official CLI
     (`npm install -g ticketfairy`) and sign in with `ticketfairy login`, or use a Personal Access
     Token in `TICKET_FAIRY_API_KEY`. Pass `--output json --non-interactive` in scripts.
   - **MCP.** `ticketfairy mcp --read-only` starts the CLI's MCP server with read tools. Drop
     `--read-only` only when the organiser wants you to make changes.
   - **Fai.** Fai is the assistant inside the organiser's dashboard. When a task is not on the
     command line, give the organiser the suggested prompt to paste into Fai.
   - **Dashboard.** Otherwise, send the organiser the guide link and walk them through it.
4. **Confirm before you change anything.** Show the organiser what you will create, change, send,
   refund or cancel, and wait for their yes. You can do only what their team role allows.
5. **Never take payment.** Buyers pay in the browser checkout. Bank, tax and payout details stay
   in the organiser's own browser.

## Guides

- [Sell one pass that covers several of your events](#sell-one-pass-that-covers-several-of-your-events)

### Sell one pass that covers several of your events

Slug `sell-a-pass-that-covers-several-events`. Guide: https://www.ticketfairy.com/guides/sell-a-pass-that-covers-several-events

Sell a season pass or a multi-night bundle once, then let the buyer book the nights they want as you announce them.

For: Selling a season ticket or a multi-night bundle across your programme.

What an agent can do: Fai can build the pass, choose the events it covers and read what it has sold. She asks before each change, because a pass is something buyers pay for.

Command line:

- Show the brand's events: `ticketfairy event list`

CLI MCP tools (reads): `select_brand`.

Prompt for Fai: "Create a season pass for <BRAND NAME> covering four events, priced at 96, usable until the end of March, and show me the events it would cover before saving"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
