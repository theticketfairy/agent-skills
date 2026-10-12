---
name: manage-invitations-and-guest-lists
description: "Send Ticket Fairy invitations and guest tickets, and manage partner allocations and group bookings. Use when an organiser wants to give people tickets without a normal purchase."
---

# Manage invitations and guest lists

This skill covers invitations, guest tickets, partner allocations and group bookings on Ticket Fairy. It lists the 4 published guides for this area and what an agent can do for each one.

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

- [Let a partner hand out their own tickets for your event](#let-a-partner-hand-out-their-own-tickets-for-your-event)
- [Send free tickets to your guest list](#send-free-tickets-to-your-guest-list)
- [Share one invitation link to your event](#share-one-invitation-link-to-your-event)
- [Take act and trader applications for your event](#take-act-and-trader-applications-for-your-event)

### Let a partner hand out their own tickets for your event

Slug `let-a-partner-hand-out-their-own-tickets`. Guide: https://www.ticketfairy.com/guides/let-a-partner-hand-out-their-own-tickets

Give an act's management, a radio station or a sponsor a fixed allocation they can hand out themselves, without a login to your event and without asking you each time.

For: Handing a counted allocation to a partner who issues their own tickets.

What an agent can do: Fai, the assistant inside your dashboard, can create the delegation with the ticket types and limits you name, add the people who hold it and read you its access link. She shows you the delegation and the people before saving and asks you to approve each change, and adding a person emails them their invitation once your event is published. Choose the email template for an Invitation row in the dashboard.

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Create a delegation called <PARTNER NAME> on <EVENT NAME> that can hand out <NUMBER> guest tickets on <TICKET TYPE NAME>, give <NAME> <EMAIL> access to it, and show me the delegation before you save it"

#### Then: Change an allocation later

What an agent can do: Fai can read how many tickets a partner has issued against each limit, change a limit, and add or remove the people who hold the delegation. She shows you the change and asks you to approve it before saving.

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "On <EVENT NAME>, show me how many tickets the <PARTNER NAME> delegation has issued, raise its limit on <TICKET TYPE NAME> to <NUMBER> and add <NAME> <EMAIL> to it, and show me the changes before saving"

### Send free tickets to your guest list

Slug `issue-guest-tickets`. Guide: https://www.ticketfairy.com/guides/issue-guest-tickets

Send a guest, a reviewer or a crew member a ticket at no charge from the Guest Tickets page, one person at a time or from a spreadsheet, and see who you have sent tickets to.

For: Giving press, guests and crew a ticket at no charge.

What an agent can do: Fai, the assistant inside your dashboard, can send guest tickets for you from a list you give her. She shows you the recipients, the ticket type and the count and asks you to approve before anything is emailed, because a sent ticket cannot be unsent. The whole workflow is also in the dashboard.

Prompt for Fai: "Send a Guest list ticket for <EVENT NAME> to <NAME> at <EMAIL ADDRESS>, show me the ticket type and the count before you send it"

#### Then: Send a whole list at once

What an agent can do: Fai takes the same list in the conversation and reads it back to you before she sends anything.

Prompt for Fai: "Here is my press list for <EVENT NAME>. Send each of them one Guest list ticket, and show me the whole list and the total before you send"

#### Then: Issue more tickets than the type has left

What an agent can do: Fai reads what the type has left, names the shortfall and waits for you to say yes before she goes past it.

Prompt for Fai: "Send 12 Guest list tickets for <EVENT NAME> to <EMAIL ADDRESS> and tell me first whether that type has 12 left"

#### Then: Take a guest ticket back

What an agent can do: Fai finds the order and shows you the guest and the tickets on it. Cancelling is yours to do on the page, because she is not given that one unless you ask us for it.

Prompt for Fai: "Find the guest ticket order for <EMAIL ADDRESS> on <EVENT NAME> and show me what it holds"

### Share one invitation link to your event

Slug `share-one-invitation-link-to-your-event`. Guide: https://www.ticketfairy.com/guides/share-one-invitation-link-to-your-event

Create one invitation link for a group, such as a sponsor's staff or a members' chat, choose the hidden tickets it unlocks and cap the tickets and orders the whole group can buy through it, then copy it and share it yourself.

For: Sharing ticket access with a group through one link.

What an agent can do: Fai, the assistant inside your dashboard, can create an invitation link with the hidden ticket types it unlocks and its ticket and transaction limits. She asks you to approve it before she creates it. Then copy the new link with **Copy Link** on the Links tab. To give the link a held allocation, create it in the dashboard.

Prompt for Fai: "Create an invitation link for <EVENT NAME> for <GROUP NAME>. It should unlock the <HIDDEN TICKET TYPE> ticket type and allow up to <TICKETS> tickets across <ORDERS> orders in total. Show me the details before you create it"

### Take act and trader applications for your event

Slug `take-applications-with-a-form`. Guide: https://www.ticketfairy.com/guides/take-applications-with-a-form

Build a form for your event from a ready-made form, a description Fai turns into questions, or an empty one, ask only what each applicant needs to answer, read every application in one list, accept or decline each one, and send the people you accept a ticket.

For: Choosing acts, traders or guests from the people who apply.

What an agent can do: Fai, the assistant inside your dashboard, can draft a form from your description or from a ready-made form, save it once you say yes, read every application, open the files applicants sent, and accept, decline or add an applicant to your event lists, asking you first each time.

Prompt for Fai: "Draft a trader application form for <EVENT NAME> with a pitch fee of 150 and an insurance certificate upload, and add each applicant to our trader applications"

#### Then: Send an accepted applicant a free ticket

What an agent can do: Fai can send guest tickets to the applicants you accepted. She reads their names and email addresses from the form, and shows you the recipients, the ticket type and the count to approve before anything is sent.

Prompt for Fai: "Send one Artist ticket each to the applicants I accepted on the artist applications form for <EVENT NAME>, and show me who gets what before you send"

#### Then: Invite an accepted applicant to buy tickets

What an agent can do: Send this invitation from the application in the dashboard, which fills in the applicant's email address and name for you.

#### Then: Work through a long list of applications

What an agent can do: Fai can read the applications on your form and list the ones that match what you describe, such as every act who picked Saturday. Tag and export the applications in the dashboard.

Prompt for Fai: "Go through the artist applications form for <EVENT NAME> and list the acts who picked Saturday, with their email addresses"

#### Then: Get the form in front of applicants

What an agent can do: Fai can draft social captions that ask acts or traders to apply, in your brand's voice, and shows you every version to choose from. Nothing is posted, so add the form's address to the caption you pick, and download the QR code from the form in the dashboard.

Prompt for Fai: "Draft three social captions for <EVENT NAME> asking acts to apply for a slot, and leave space for the application link"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
