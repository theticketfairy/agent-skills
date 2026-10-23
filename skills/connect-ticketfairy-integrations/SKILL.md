---
name: connect-ticketfairy-integrations
description: "Connect Ticket Fairy to Mailchimp, Zapier and other tools an organiser already uses. Use when an organiser wants their ticket data in another tool."
---

# Connect integrations

This skill covers Mailchimp, Zapier and the other tools an organiser already uses on Ticket Fairy. It lists the 3 published guides for this area and what an agent can do for each one.

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
5. **Keep actions within the organiser's approval.** Use their explicit approval for this exact
   action, or show what you will create, change, send, refund or cancel and wait for their yes.
   Installing a skill or asking for a draft does not authorise sending messages. Use only the
   approved brand, event and recipients, and only what the person's team role allows.
6. **Organiser access does not authorise ticket payments.** A buyer uses a separate supported
   checkout with their explicit approval, or pays in the browser. Bank, tax and payout details
   stay in the organiser's own browser.
7. **Recover the original result after an uncertain change.** Read the original order or operation
   before retrying. Reuse its idempotency key when the documented operation supports one. Never
   repeat an uncertain refund, transfer, message send or ticket grant as a fresh operation.

## Guides

- [Send your ticket buyers and orders to Hive](#send-your-ticket-buyers-and-orders-to-hive)
- [Send your ticket buyers to Laylo](#send-your-ticket-buyers-to-laylo)
- [Sync your ticket buyers to Mailchimp](#sync-your-ticket-buyers-to-mailchimp)

### Send your ticket buyers and orders to Hive

Slug `send-your-ticket-buyers-and-orders-to-hive`. Guide: https://www.ticketfairy.com/guides/send-your-ticket-buyers-and-orders-to-hive

Connect Hive to a brand with your Hive account ID, and each ticket buyer on that brand's events joins your Hive account with their order, in a Hive segment for one event when you choose one.

For: Adding your ticket buyers and their orders to Hive.

What an agent can do: Fai can save the Hive account ID on a brand, and she asks for your approval before she saves it. You email Hive yourself to ask them to whitelist Ticket Fairy.

Prompt for Fai: "Connect Hive on <BRAND NAME> with the account ID <HIVE ACCOUNT ID>, and ask me before you save it"

#### Then: Add one event's buyers to a Hive segment

What an agent can do: Fai can open the event's Settings page, where you enter the segment.

Prompt for Fai: "Open the settings page for <EVENT NAME>"

#### Then: Turn Hive off

What an agent can do: Fai can turn Hive off for a brand after you approve the change.

Prompt for Fai: "Turn off Hive on <BRAND NAME>, and ask me before you save it"

### Send your ticket buyers to Laylo

Slug `send-your-ticket-buyers-to-laylo`. Guide: https://www.ticketfairy.com/guides/send-your-ticket-buyers-to-laylo

Connect Laylo to a brand with the webhook link from your Laylo account, and Ticket Fairy sends the buyer, their order and their marketing choice to Laylo for each paid ticket order on that brand's events.

For: Adding the fans who buy your tickets to your Laylo audience.

What an agent can do: Fai can save or remove the Laylo link on a brand, and she asks for your approval before each change. The link contains your Laylo token, so paste it into the Laylo card yourself and ask Fai to open the page.

Prompt for Fai: "Open Integrations for <BRAND NAME> so I can connect Laylo"

#### Then: Turn Laylo off

What an agent can do: Fai can turn Laylo off for a brand after you approve the change.

Prompt for Fai: "Turn off Laylo on <BRAND NAME>, and ask me before you save it"

### Sync your ticket buyers to Mailchimp

Slug `sync-buyers-to-mailchimp`. Guide: https://www.ticketfairy.com/guides/sync-buyers-to-mailchimp

Connect Mailchimp to your brand, choose the audience buyers join, choose whether buyers, newsletter sign-ups and sales tracking are sent, and know what Mailchimp receives about each buyer and what happens when a buyer opts out.

For: Keeping a Mailchimp audience in step with ticket sales.

What an agent can do: Fai can list your connections and audiences, choose the audience, switch each sync on or off and disconnect, after showing you the change. The Mailchimp sign-in itself happens in your browser. Keep an API key in the dashboard form rather than in a message to Fai.

Prompt for Fai: "Show me the Mailchimp connection on <BRAND NAME>, list its audiences, then set the audience to <AUDIENCE NAME> with buyers and newsletter sign-ups syncing and campaign sending left to Ticket Fairy"

#### Then: Disconnect Mailchimp

What an agent can do: Fai can disconnect the account after confirming with you. There is no CLI command for integrations.

Prompt for Fai: "Disconnect Mailchimp from <BRAND NAME>, and confirm with me first"

#### Then: Send one event's buyers to a different list

What an agent can do: You choose the per-event list in the dashboard. Fai can tell you which audience the brand connection uses.

Prompt for Fai: "Which Mailchimp audience does <BRAND NAME> sync buyers into?"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
