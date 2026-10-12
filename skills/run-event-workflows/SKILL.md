---
name: run-event-workflows
description: "Follow Ticket Fairy start-to-finish workflows: on-sale day, repeating last year's event, and changing plans. Use when an organiser faces one of these moments."
---

# Run event workflows

This skill covers on-sale day, repeating last year's event, and changing plans on Ticket Fairy. It lists the 4 published guides for this area and what an agent can do for each one.

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

- [Change the date or call off an event](#change-the-date-or-call-off-an-event)
- [Open your ticket on-sale](#open-your-ticket-on-sale)
- [Prepare your door team for event day](#prepare-your-door-team-for-event-day)
- [Run last year's event again](#run-last-years-event-again)

### Change the date or call off an event

Slug `change-or-call-off-an-event`. Guide: https://www.ticketfairy.com/guides/change-or-call-off-an-event

Choose between postponing, cancelling and refunding, tell ticket holders before they hear it anywhere else, and see what each choice means for their tickets and their money.

For: Choosing between a new date, calling an event off and refunding buyers.

What an agent can do: Fai can read the ticket sales back to you, open the page where you make the change, and draft the message to ticket holders. Take her figure as ticket sales rather than the whole bill: add-ons and instalment plans sit outside it.

Command line:

- Show the event, its dates and its status: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "For <EVENT NAME>, tell me what its tickets have sold and whether its funds have been paid out yet. Say what your figure leaves out"

### Open your ticket on-sale

Slug `open-your-ticket-on-sale`. Guide: https://www.ticketfairy.com/guides/open-your-ticket-on-sale

Check every ticket type and buy a test ticket yourself, put the event live at the time you announced, and follow tickets sold, revenue and orders through the first hour.

For: Putting an announced event on sale at a set time.

What an agent can do: Fai can read the event back to you before you open it, publish it once you approve, and report the sales as they come in. The CLI publishes and reads the same event without opening the dashboard.

Command line:

- Show the event and its ticket types before you open it: `ticketfairy event get <EVENT_ID>`
- Put the event on sale: `ticketfairy event publish <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Before I open <EVENT NAME> for sale, list its ticket types with prices, allocations and sale windows, and tell me anything that looks wrong"

### Prepare your door team for event day

Slug `prepare-your-door-team`. Guide: https://www.ticketfairy.com/guides/prepare-your-door-team

Give everyone on your event door their own scanning login, send the guest list its tickets, set what each ticket may do at the door, test a ticket on every phone, then follow arrivals and find a guest by name once the doors open.

For: Getting a door team ready for the day of an event.

What an agent can do: Fai can invite your door team as Door Staff, send the guest list their tickets, set a ticket's repeat-scan rules, report arrivals and find one guest's ticket. She shows you each invitation, ticket and change and asks you to approve it before anything is sent or saved. Wristbands, door times and undoing a test scan are set up in the dashboard.

Command line:

- Read how many have checked in against the tickets sold: `ticketfairy checkin status <EVENT_ID>`
- Read arrivals for each ticket type, such as the guest list against general admission: `ticketfairy checkin status <EVENT_ID> --breakdown ticket-types --output json`

Prompt for Fai: "Get the door ready for <EVENT NAME>: invite <EMAIL ADDRESSES> to the event as Door Staff, send guest list tickets to the names I paste below, and let <TICKET TYPE NAME> holders back in once a day, showing me each change before you make it"

### Run last year's event again

Slug `run-last-years-event-again`. Guide: https://www.ticketfairy.com/guides/run-last-years-event-again

Copy last year's event, change the dates and prices, and open the on-sale to last year's buyers before you announce it publicly.

For: Running an event you have run before.

What an agent can do: Fai can read what last year's event sold back to you, tier by tier, and copy it once you approve. The CLI copies the event in one command.

Command line:

- Copy last year's event as a draft with its ticket types, team, emails, contacts and FAQs. Enter the start and end as local date and time, such as 2026-10-10T22:00:00; sale windows and door times move by the same number of whole days: `ticketfairy event clone <EVENT_ID> --body '{"data": {"displayName": "<NEW EVENT NAME>", "slug": "", "shortName": "", "startDate": "<NEW START>", "endDate": "<NEW END>", "ticketTypes": true, "team": true, "credentials": false, "preRegistration": false, "promotions": false, "delegations": false, "emailTemplates": true, "contacts": true, "faqs": true}}'`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Copy <EVENT NAME> for next year, keep the ticket types and add-ons, and show me the new event in draft with the dates I give you before anything is published"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
