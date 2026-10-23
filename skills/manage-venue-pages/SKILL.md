---
name: manage-venue-pages
description: "Claim a Ticket Fairy venue page and keep its details current. Use when a venue team wants to control what people read about their venue."
---

# Manage venue pages

This skill covers venue pages: claiming one and keeping its details current on Ticket Fairy. It lists the 4 published guides for this area and what an agent can do for each one.

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

- [Add a venue page to the brand you already run](#add-a-venue-page-to-the-brand-you-already-run)
- [Ask the venue to help with their page](#ask-the-venue-to-help-with-their-page)
- [Change what your venue's page says](#change-what-your-venues-page-says)
- [Claim your venue's page on Ticket Fairy](#claim-your-venues-page-on-ticket-fairy)

### Add a venue page to the brand you already run

Slug `add-a-venue-to-your-brand`. Guide: https://www.ticketfairy.com/guides/add-a-venue-to-your-brand

Choose a venue your brand has run events at, or search for any venue by name, prove an email address at the venue's own website, and its public page appears in your brand beside your events.

For: Running a brand on Ticket Fairy and taking over a venue page from inside it.

What an agent can do: Fai can list the venues your brand has played whose pages it could still claim, and search every venue on the platform by name. She tells you which ones can be claimed and why the others cannot. You prove the address yourself in the dialog, because confirming a code gives a venue page to a brand. MCP and the command line can't claim a venue.

Prompt for Fai: "Which venues has this brand run events at that we could still claim the page for? Then look up <VENUE NAME> and tell me whether we can claim it and which email domain it needs"

### Ask the venue to help with their page

Slug `ask-the-venue-to-help-with-their-page`. Guide: https://www.ticketfairy.com/guides/ask-the-venue-to-help-with-their-page

Invite the venue's booker or marketing manager by email so they can manage the content on the venue page with you, and send the invitation again or call it off if it does not land.

For: Getting the venue's own people to fill in the parts of the page only they know.

What an agent can do: Fai can tell you who looks after a venue page and who has been invited but not joined, invite a person by email, send an invitation again and call one off. She asks you to confirm before she invites, resends or cancels, and she doesn't need your confirmation to show you either list. She can't remove someone who has already joined. MCP and the CLI can't work on a venue page.

Prompt for Fai: "For the venue page for <VENUE NAME>, show me who looks after it and who has been asked and not joined. Then invite <EMAIL ADDRESS> onto the venue team, and tell me what they will and will not be able to see"

#### Then: Send the invitation again

What an agent can do: Fai can tell you who is waiting and when each invitation last went out, and send one again. She asks you to confirm before she sends. MCP and the CLI can't work on a venue page.

Prompt for Fai: "On the venue page for <VENUE NAME>, show me who has been asked and not joined, with when each invitation last went out. Then send <EMAIL ADDRESS> theirs again"

#### Then: Call an invitation off

What an agent can do: Fai can call an invitation off, and she asks you to confirm first. She can't remove someone who has already joined. MCP and the CLI can't work on a venue page.

Prompt for Fai: "On the venue page for <VENUE NAME>, call off the invitation to <EMAIL ADDRESS>. Tell me what it does to the link they already have"

### Change what your venue's page says

Slug `change-what-your-venue-page-says`. Guide: https://www.ticketfairy.com/guides/change-what-your-venue-page-says

Add a section for getting to the venue, the rooms and the door, order them with Move up and Move down, and keep one as a draft until it is ready for the public page.

For: Keeping a venue's public page current for the people coming to it.

What an agent can do: Fai can list the venues your brand looks after, show you every section and whether it's a draft, add one, change a heading or the words under it, set the order, take a section off the page and put it back. She never overwrites a teammate's save, and she asks you to confirm before each change. MCP and the CLI can't work on a venue page.

Prompt for Fai: "Open the venue page for <VENUE NAME> and read me every section it has. Then add a section headed "Getting here" saying <WHAT PEOPLE NEED TO KNOW>, keep it as a draft, and show me the wording before you save it"

#### Then: Take a section off the page, and put it back

What an agent can do: Fai can take a section off a venue page and put it back, and she asks you to confirm each one. MCP and the CLI can't work on a venue page.

Prompt for Fai: "On the venue page for <VENUE NAME>, take the section headed "<HEADING>" off the page. Show me what it says first and wait for me to confirm, and tell me how to put it back"

#### Then: Answer what visitors ask before they come

What an agent can do: Fai can show you the questions on a venue page, add one, change a question or its answer, set their order, take one off the page and put it back. She asks you to confirm before each change. MCP and the CLI can't work on a venue page.

Prompt for Fai: "On the venue page for <VENUE NAME>, add the question "<THE QUESTION>" with the answer <YOUR ANSWER>, and show me the wording before you save it"

#### Then: See what changed on the page

What an agent can do: Fai can check the same history and tell you what changed on a venue page and when. MCP and the CLI can't work on a venue page.

Prompt for Fai: "Tell me what changed on the venue page for <VENUE NAME> over the last month, and when each change was made"

### Claim your venue's page on Ticket Fairy

Slug `claim-your-venue-page`. Guide: https://www.ticketfairy.com/guides/claim-your-venue-page

Get a code sent to an email address at your venue's own domain, enter it, and you can keep the venue's public page up to date, with a brand of your own to manage it.

For: Taking over the public page of a venue you run.

What an agent can do: no agent route is recorded for this guide. Send the organiser the guide link and walk them through the steps in the dashboard.

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
