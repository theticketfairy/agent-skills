---
name: run-door-check-in
description: "Run Ticket Fairy check-in at the door: scanning, entry rules, live check-in reports and wristbands. Use when an organiser prepares or runs entry to an event."
---

# Run door check-in

This skill covers scanning, entry rules, live check-in reports and wristbands on Ticket Fairy. It lists the 3 published guides for this area and what an agent can do for each one.

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
     Token that the organiser stores in `TICKET_FAIRY_API_KEY`. Then check the account and pick the
     brand: `ticketfairy auth status`, `ticketfairy brand list` and
     `ticketfairy brand use <BRAND_ID>`. Add `--output json --non-interactive` to every command
     you run that does not already choose its own mode, such as `--output csv` or `--interactive`;
     the commands below leave them out to stay short.
   - **MCP.** `ticketfairy mcp --read-only` starts the CLI's MCP server with read tools. Drop
     `--read-only` only when the organiser wants you to make changes.
   - **Fai.** Fai is the assistant inside the organiser's dashboard. When a task is not on the
     command line, give the organiser the suggested prompt to paste into Fai.
   - **Dashboard.** Otherwise, send the organiser the guide link and walk them through it.
4. **Keep secrets out of the chat.** Codes, passwords and tokens that the organiser receives go
   into the Ticket Fairy dashboard: the page that asks for them, or Fai there when the guide says
   so. They never go into your conversation with the organiser.
5. **Confirm before you change anything.** Show the organiser what you will create, change, send,
   refund or cancel, and wait for their yes. You can do only what their team role allows.
6. **Never take payment.** Buyers pay in the browser checkout. Bank, tax and payout details stay
   in the organiser's own browser.

## Guides

- [Assign wristbands to each ticket type](#assign-wristbands-to-each-ticket-type)
- [Scan tickets at the door](#scan-tickets-at-the-door)
- [Set ticket entry and repeat-scan rules](#set-ticket-entry-and-repeat-scan-rules)

### Assign wristbands to each ticket type

Slug `issue-wristbands-by-ticket-type`. Guide: https://www.ticketfairy.com/guides/issue-wristbands-by-ticket-type

Match each ticket type and add-on to the wristband or badge its holder gets, so the scanning app shows your door team the right band as each ticket is scanned.

For: Handing out the right wristband or badge for every ticket at the gate.

What an agent can do: no agent route is recorded for this guide. Send the organiser the guide link and walk them through the steps in the dashboard.

#### Then: Change which tickets get a band

What an agent can do: Fai, the MCP server and the command line have no credential tools, so change a credential on the Credentials page.

#### Then: Stop handing out a band for now

What an agent can do: Fai, the MCP server and the command line have no credential tools, so deactivate or activate a credential on the Credentials page.

#### Then: Remove a band

What an agent can do: Fai, the MCP server and the command line have no credential tools, so delete a credential on the Credentials page.

### Scan tickets at the door

Slug `scan-tickets-at-the-door`. Guide: https://www.ticketfairy.com/guides/scan-tickets-at-the-door

Get your door team on the scanning app with the right login, set the re-entry rules before the day, and watch arrivals and individual tickets while the doors are open.

For: Getting a crowd through the door on event night.

What an agent can do: Fai, the assistant inside your dashboard, reads how the doors are going and can find one person's ticket while you are standing at the entrance. Admitting people is the app's job.

Prompt for Fai: "For <EVENT NAME>, how many have checked in so far, and has <ATTENDEE NAME> arrived"

#### Then: Undo a scan

What an agent can do: Fai reads the ticket so you can see whether it went in and when. Undoing the scan is yours to do on the page.

Prompt for Fai: "For <EVENT NAME>, has <ATTENDEE NAME> checked in, and at what time"

#### Then: Admit an attendee when the app cannot

What an agent can do: Fai finds the order and the ticket. Changing its status is yours to do on the page.

Prompt for Fai: "Find the order for <BUYER EMAIL ADDRESS> on <EVENT NAME> and show me its tickets and their states"

### Set ticket entry and repeat-scan rules

Slug `set-ticket-entry-and-repeat-scan-rules`. Guide: https://www.ticketfairy.com/guides/set-ticket-entry-and-repeat-scan-rules

Control how often each ticket can admit its holder, from one visit per event to a set number of scans each hour or day.

For: Setting re-entry limits for multi-day events, passes and tickets with repeat access.

What an agent can do: Fai can set or clear a ticket type's repeat-scan rules, explain the hourly or daily limit and show the proposed change before asking you to approve it.

Prompt for Fai: "For <EVENT NAME>, set the repeat-scan rules for <TICKET TYPE NAME>. Allow one scan per day and two scans per hour, show me the change, and wait for my approval"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
