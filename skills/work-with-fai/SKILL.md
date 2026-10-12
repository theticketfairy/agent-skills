---
name: work-with-fai
description: "Use Fai, the assistant inside the Ticket Fairy dashboard, for questions, the inbox and the buyer concierge. Use when an organiser wants Fai to do work for them."
---

# Work with Fai

This skill covers Fai in the dashboard, inbox handling and the buyer concierge on Ticket Fairy. It lists the 4 published guides for this area and what an agent can do for each one.

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

- [Add your ticket concierge to your website](#add-your-ticket-concierge-to-your-website)
- [Ask Fai about your event](#ask-fai-about-your-event)
- [Give ticket buyers an AI concierge](#give-ticket-buyers-an-ai-concierge)
- [Teach your concierge from your event FAQ pages and Google Docs](#teach-your-concierge-from-your-event-faq-pages-and-google-docs)

### Add your ticket concierge to your website

Slug `add-your-ticket-concierge-to-your-website`. Guide: https://www.ticketfairy.com/guides/add-your-ticket-concierge-to-your-website

Add your concierge to the website where buyers find your event, so it answers ticket questions and sells tickets in a chat on your own pages, and choose who takes the questions it passes on.

For: Getting your concierge onto the website your ticket buyers use.

What an agent can do: Fai can open your concierge widgets so you can copy the snippet. Choose the sites the chat loads on and where hand-offs go in the dashboard, then add the snippet to your own site.

Prompt for Fai: "Open the concierge widgets for <BRAND NAME> so I can copy the snippet for our website"

### Ask Fai about your event

Slug `ask-fai-about-your-event`. Guide: https://www.ticketfairy.com/guides/ask-fai-about-your-event

Ask Fai, the assistant in your dashboard, about your event by typing or out loud, have her chart the answer or make the change for you, and check her work before you rely on it.

For: Getting answers about your own events, orders and buyers.

What an agent can do: Fai is the agent path. She works on the brand and event you have open, reads what your role reaches, and asks before she changes anything.

Command line:

- Show an event and its current sales: `ticketfairy event stats <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "How many tickets has <EVENT NAME> sold so far, and how does that compare with the same point before my last event"

### Give ticket buyers an AI concierge

Slug `give-buyers-an-ai-concierge`. Guide: https://www.ticketfairy.com/guides/give-buyers-an-ai-concierge

Put an assistant on your own site that answers what buyers ask before they buy, from the answers you gave it.

For: Answering buyer questions on your own website.

What an agent can do: Fai can open the concierge builder for you. What the concierge knows is yours to enter and yours to keep current.

Command line:

- Show the brands you can act for: `ticketfairy brand list`

CLI MCP tools that read: `select_brand`.

Prompt for Fai: "Open the concierge widgets for <BRAND NAME>"

### Teach your concierge from your event FAQ pages and Google Docs

Slug `teach-your-concierge-from-your-event-faq-pages`. Guide: https://www.ticketfairy.com/guides/teach-your-concierge-from-your-event-faq-pages

Point your ticket concierge at the event FAQ, policy and venue pages you already keep, a Google Doc or your whole website, and it answers buyers from them and picks up your changes on a schedule you choose.

For: Giving your concierge the answers you already keep on your website and in documents.

What an agent can do: Fai can open your concierge's reference pages for you. Add a page, a Google Doc or a website, and choose which widgets answer from it, in the dashboard.

Prompt for Fai: "Open the concierge reference pages for <BRAND NAME>"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
