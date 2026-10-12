---
name: build-with-the-ticketfairy-api
description: "Use Ticket Fairy access tokens, API keys and webhooks, and sell from your own app. Use when a developer integrates with Ticket Fairy."
---

# Build with the Ticket Fairy API

This skill covers access tokens, API keys, webhooks and selling from your own app on Ticket Fairy. It lists the 2 published guides for this area and what an agent can do for each one.

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

- [Create an API key so your own tools can read your ticket sales](#create-an-api-key-so-your-own-tools-can-read-your-ticket-sales)
- [Get a webhook each time you take a ticket order](#get-a-webhook-each-time-you-take-a-ticket-order)

### Create an API key so your own tools can read your ticket sales

Slug `create-an-api-key-for-your-own-app`. Guide: https://www.ticketfairy.com/guides/create-an-api-key-for-your-own-app

Give the command line, a script or an agent its own key to your ticket sales, choose how long it lasts, and take it back the moment you need to.

For: Connecting your own tools, scripts or agents to your ticket sales.

What an agent can do: Fai can open the page where the tokens live. Minting one is yours to do, because the token is shown once and only to you.

Command line:

- Sign in with a token you have created: `ticketfairy auth login`
- Show the brands the token can act for: `ticketfairy brand list`

CLI MCP tools that read: `select_brand`.

Prompt for Fai: "Open my account settings so I can create an access token"

#### Then: Swap a token without any downtime

What an agent can do: Fai can open the page. Rotating and copying the new token stay with you, because the value is shown once and only to you.

Command line:

- Sign in with the token you copied: `ticketfairy auth login`

CLI MCP tools that read: `select_brand`.

Prompt for Fai: "Open my account settings so I can rotate an access token"

#### Then: Take access back

What an agent can do: Fai can open the page. Revoking is yours to confirm, because it stops a live integration the moment it happens.

Command line:

- Show the brands the current token can act for: `ticketfairy brand list`

CLI MCP tools that read: `select_brand`.

Prompt for Fai: "Open my account settings so I can revoke an access token"

### Get a webhook each time you take a ticket order

Slug `get-a-webhook-when-a-ticket-sells`. Guide: https://www.ticketfairy.com/guides/get-a-webhook-when-a-ticket-sells

Add a webhook on the Webhooks page of your brand, a tour or an event, and each order reaches an address you own seconds after the buyer pays, with its tickets, add-ons, totals and ticket holder details.

For: Sending each ticket sale to your own systems as it happens.

What an agent can do: Fai can list, add, change, test and delete the webhooks on a brand, a tour or an event, and she asks for your approval before each change. She shows each address without the part after the question mark, where a tool often keeps its access token. If your address has a question mark or a password in it, add it on the Webhooks page instead, so the access key stays out of the chat.

Command line:

- Call your address every time an order is placed: `ticketfairy webhook create --url https://example.com/hooks/tickets --on order`
- Show the webhooks on the active brand: `ticketfairy webhook list`

Prompt for Fai: "Add a webhook to <BRAND NAME> that sends every order to <YOUR ADDRESS> in the Full order format, then send it a test"

#### Then: Pause or change a webhook

What an agent can do: Fai can turn a webhook off or on, or change its address or format, after you approve the change.

Command line:

- Show the webhooks on the active brand: `ticketfairy webhook list`
- Stop a webhook receiving without deleting it: `ticketfairy webhook update <WEBHOOK_ID> --disable`

Prompt for Fai: "Turn off the webhook that sends <BRAND NAME> orders to <YOUR ADDRESS>, and ask me before you save it"

#### Then: Delete a webhook

What an agent can do: Fai can delete a webhook after you approve it. She names the address that stops receiving before you do.

Command line:

- Show the webhooks on the active brand: `ticketfairy webhook list`
- Delete a webhook: `ticketfairy webhook delete <WEBHOOK_ID>`

Prompt for Fai: "Delete the webhook that sends <BRAND NAME> orders to <YOUR ADDRESS>, and ask me before you delete it"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
