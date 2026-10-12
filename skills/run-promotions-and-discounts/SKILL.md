---
name: run-promotions-and-discounts
description: "Create Ticket Fairy promo codes, group discounts and promoter links. Use when an organiser wants to give some buyers a better price."
---

# Run promotions and discounts

This skill covers promo codes, group discounts and promoter links on Ticket Fairy. It lists the 3 published guides for this area and what an agent can do for each one.

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
     you run; the commands below leave them out to stay short.
   - **MCP.** `ticketfairy mcp --read-only` starts the CLI's MCP server with read tools. Drop
     `--read-only` only when the organiser wants you to make changes.
   - **Fai.** Fai is the assistant inside the organiser's dashboard. When a task is not on the
     command line, give the organiser the suggested prompt to paste into Fai.
   - **Dashboard.** Otherwise, send the organiser the guide link and walk them through it.
4. **Keep secrets out of the chat.** Codes, passwords and tokens that the organiser receives go
   into the dashboard page that asks for them, never into the conversation.
5. **Confirm before you change anything.** Show the organiser what you will create, change, send,
   refund or cancel, and wait for their yes. You can do only what their team role allows.
6. **Never take payment.** Buyers pay in the browser checkout. Bank, tax and payout details stay
   in the organiser's own browser.

## Guides

- [Create promo codes for your event](#create-promo-codes-for-your-event)
- [Offer group discounts on your event tickets](#offer-group-discounts-on-your-event-tickets)
- [Sell a gift certificate for your event](#sell-a-gift-certificate-for-your-event)

### Create promo codes for your event

Slug `create-promo-codes`. Guide: https://www.ticketfairy.com/guides/create-promo-codes

Give a partner, a mailing list or an early crowd a better price with a promotion that carries the discount, the ticket types it applies to, the codes people enter and the limits you set.

For: Offering a discount to a particular group of buyers.

What an agent can do: Fai, the assistant inside your dashboard, can create a promotion with its codes, discount, ticket types, limits and dates, add a code to one later, switch a promotion off and read how each code is doing. She shows you the promotion before she creates it and asks you to approve it. The whole workflow is also in the dashboard.

Command line:

- List the promotions on the event, with their codes: `ticketfairy promotion list <EVENT_ID>`

Prompt for Fai: "Find my event by name and create a promotion called <NAME> with code <CODE>: <PERCENTAGE OR AMOUNT> off <TICKET TYPES>, <LIMIT PER CODE OR NO LIMIT>, valid <DATES OR ALWAYS>. Show me the tickets, the discounted prices, the limit and the dates, then ask me to approve it before you create it"

### Offer group discounts on your event tickets

Slug `offer-group-discounts-on-event-tickets`. Guide: https://www.ticketfairy.com/guides/offer-group-discounts-on-event-tickets

Give buyers a lower ticket price automatically once their basket reaches a group size you choose, with a bigger discount for bigger groups if you want one, and no code for a buyer to type.

For: Rewarding buyers who book tickets as a group.

What an agent can do: Fai, the assistant inside your dashboard, can create a group discount with its code, discount, ticket types and group size, and a second one for bigger groups. She shows you the promotion before she creates it and asks you to approve it. Use the CLI to list the promotions on an event; create and change group discounts in the dashboard or through Fai.

Command line:

- List the promotions on the event, with their codes: `ticketfairy promotion list <EVENT_ID>`

Prompt for Fai: "Find my event by name and create a group discount called <NAME> with the code <CODE>: <PERCENTAGE OR AMOUNT> off <TICKET TYPES> once a basket holds <NUMBER> tickets. Show me the tickets, the discounted prices and the group size, then ask me to approve it before you create it"

### Sell a gift certificate for your event

Slug `sell-gift-certificates`. Guide: https://www.ticketfairy.com/guides/sell-gift-certificates

Sell a certificate worth a ticket type you choose or a fixed sum, set how many months it stays valid, and let the buyer decide who uses it and when.

For: Selling to buyers who want to give a ticket as a present.

What an agent can do: Fai can list the certificates on an event, create one, change one, take one off sale and remove one. She shows you the settings and waits for your approval before saving, because a certificate is something buyers pay for.

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Set up a gift certificate on <EVENT NAME> worth one Weekend Ticket, valid for 12 months; show me the settings before you save"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
