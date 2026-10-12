---
name: manage-orders-and-refunds
description: "Find and manage Ticket Fairy orders: checkout questions, order approval, refunds, transfers, waiting lists and buyer support. Use when an organiser asks about an order, a refund or the checkout."
---

# Manage orders and refunds

This skill covers checkout questions, order approval, refunds, transfers, waiting lists and buyer support on Ticket Fairy. It lists the 16 published guides for this area and what an agent can do for each one.

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

- [Add custom questions to your event checkout](#add-custom-questions-to-your-event-checkout)
- [Add custom terms to your event checkout](#add-custom-terms-to-your-event-checkout)
- [Choose which AI assistants sell your tickets](#choose-which-ai-assistants-sell-your-tickets)
- [Choose which details checkout asks your ticket buyers for](#choose-which-details-checkout-asks-your-ticket-buyers-for)
- [Clear the ticket orders waiting on an ID check](#clear-the-ticket-orders-waiting-on-an-id-check)
- [Download your ticket buyers](#download-your-ticket-buyers)
- [Find and manage the orders for your event](#find-and-manage-the-orders-for-your-event)
- [Let buyers refund their own tickets](#let-buyers-refund-their-own-tickets)
- [Let buyers resell their tickets at face value](#let-buyers-resell-their-tickets-at-face-value)
- [Move a buyer to a different ticket type or seat](#move-a-buyer-to-a-different-ticket-type-or-seat)
- [Print venue directions and entry details on your tickets](#print-venue-directions-and-entry-details-on-your-tickets)
- [Refund an order on your event](#refund-an-order-on-your-event)
- [Resend a buyer's tickets and fix their details](#resend-a-buyers-tickets-and-fix-their-details)
- [Run a waiting list for a sold-out event](#run-a-waiting-list-for-a-sold-out-event)
- [Sell a block of tickets to a company and invoice them](#sell-a-block-of-tickets-to-a-company-and-invoice-them)
- [Win back buyers who left checkout](#win-back-buyers-who-left-checkout)

### Add custom questions to your event checkout

Slug `add-custom-checkout-questions`. Guide: https://www.ticketfairy.com/guides/add-custom-checkout-questions

Collect extra information from buyers or ticket holders for your event checkout, such as a meal choice, accessibility request or company detail, and decide where each answer belongs.

For: Your event team collecting extra buyer, ticket-holder or add-on information at checkout.

What an agent can do: Fai can list an event's checkout fields and create basic order, ticket or add-on fields after showing you the proposed type, label and where the answer belongs. She can remove all custom fields only after an explicit full-wipe confirmation. Editing one existing field and setting conditional rules remain dashboard work. MCP and the CLI do not manage these fields.

Prompt for Fai: "Show me the custom checkout fields on <EVENT NAME>, then add a required ticket question called Meal preference with Vegetarian, Vegan and No preference as the choices. Show me the complete field and ask before saving it"

### Add custom terms to your event checkout

Slug `add-custom-terms-to-your-checkout`. Guide: https://www.ticketfairy.com/guides/add-custom-terms-to-your-checkout

Add labelled terms and conditions to your event checkout agreement, so buyers can open each section and accept the complete agreement before they pay.

For: Ticket Fairy staff adding approved terms to an event checkout.

What an agent can do: Custom event terms are a Ticket Fairy staff-only dashboard action. Fai can take you to the event Settings page, but she cannot create or edit the agreement and no MCP or CLI tool changes it.

Prompt for Fai: "Open the Settings page for <EVENT NAME> so a Ticket Fairy staff member can add the approved custom checkout terms"

### Choose which AI assistants sell your tickets

Slug `choose-which-ai-assistants-sell-your-tickets`. Guide: https://www.ticketfairy.com/guides/choose-which-ai-assistants-sell-your-tickets

AI shopping assistants can start a ticket order for buyers who ask them about events, at your prices and with your ticket rules, and send the buyer to the Ticket Fairy checkout page to pay. Turn an assistant off for your brand, or pause it for one event, to stop new ticket sales through it.

For: Brand owners and admins deciding which AI assistants sell their event tickets.

What an agent can do: Fai, the assistant inside your dashboard, can tell you which AI assistants sell your brand's tickets and turn one on or off for the brand. She shows you the change and asks you to approve it before she makes it.

Prompt for Fai: "Which AI assistants can sell tickets for <BRAND NAME>? Turn off <ASSISTANT NAME> so it stops selling our tickets"

### Choose which details checkout asks your ticket buyers for

Slug `choose-which-attendee-details-checkout-collects`. Guide: https://www.ticketfairy.com/guides/choose-which-attendee-details-checkout-collects

Make every ticket buyer at your event's checkout enter a phone number, nationality, Instagram handle or date of birth before they can pay, and turn away buyers under your event's minimum age.

For: Collecting a phone number, nationality, Instagram handle or date of birth from every ticket buyer.

What an agent can do: Fai, the assistant inside your dashboard, can turn each of these questions on or off for an event and set its minimum age, and she shows you the change and asks you to approve it first. These checkout settings are changed in the dashboard or through Fai.

Prompt for Fai: "On <EVENT NAME>, make checkout ask every buyer for their <PHONE NUMBER, NATIONALITY, INSTAGRAM HANDLE OR DATE OF BIRTH>, set the minimum age to <AGE>, and show me the change before you save it"

### Clear the ticket orders waiting on an ID check

Slug `verify-buyer-identity-at-checkout`. Guide: https://www.ticketfairy.com/guides/verify-buyer-identity-at-checkout

See which buyers have a card on hold in the Needs Verification tab, send the ID check again, take the payment without it, or release the hold and put the tickets back on sale.

For: Clearing the card holds waiting on an ID check so the tickets go back on sale.

What an agent can do: Fai, the assistant inside your dashboard, opens the event and takes you to its orders. The decisions on a hold are made on the page, because taking the money and releasing it both change what the buyer has and cannot be undone.

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Take me to the orders on <EVENT NAME>"

### Download your ticket buyers

Slug `download-your-ticket-buyers`. Guide: https://www.ticketfairy.com/guides/download-your-ticket-buyers

Get a CSV of every ticket for your event, with buyer details and optional add-ons as rows or columns.

For: Getting your event's ticket buyers into a spreadsheet.

What an agent can do: Ask Fai to prepare tickets only or tickets and add-ons for your event, with add-ons as rows or columns. If you do not choose, she prepares rows without add-ons. She shows you the request and waits for your approval, then gives you a dashboard link to your file. Owners and admins resume the file in Orders; marketing readers resume it in Marketing Assets. Open the link with the account that requested the file and select Download when it is ready. Fai checks progress without reading the buyers' details into the conversation.

Prompt for Fai: "Prepare a file of tickets and add-ons for <EVENT NAME>, then give me the page where I can download it"

### Find and manage the orders for your event

Slug `find-and-manage-your-event-orders`. Guide: https://www.ticketfairy.com/guides/find-and-manage-your-event-orders

Find any ticket order on your event by buyer, email address or order number, see which tab each order sits in, open it to read the tickets, the buyer and where the sale came from, and leave a note your team can see.

For: Looking after the orders on your event.

What an agent can do: Fai, the assistant inside your dashboard, finds an order by the buyer's email address or the order number, reads it back to you with its notes, and adds a note once you approve the wording. Over MCP your own assistant can list an event's orders by status and open one, and the command line does the same. Neither MCP nor the command line reads or changes order notes.

Command line:

- Lists the event's paid orders, newest first: `ticketfairy order list <EVENT_ID> --status paid`
- Opens one order with its tickets and buyer, using the number from the Order column: `ticketfairy order get <EVENT_ID> <ORDER_ID>`

CLI MCP tools that read: `select_brand`, `select_event`, `list_orders`, `get_order`.

Prompt for Fai: "Find the order for <BUYER EMAIL ADDRESS> on <EVENT NAME>, tell me its status, tickets and any notes on it, then add this note once I approve it: <NOTE>"

### Let buyers refund their own tickets

Slug `let-buyers-refund-themselves`. Guide: https://www.ticketfairy.com/guides/let-buyers-refund-themselves

Turn on self-refunds, see what a buyer is offered on their order page, and know what happens to the ticket and the stock afterwards.

For: Letting buyers refund their own tickets from their order page.

What an agent can do: Fai, the assistant inside your dashboard, can turn self-refunds on or off for an event and asks you to approve the change first. She refuses to turn them on once the event's money has been released, and says why. The terms a buyer is offered are not on anything she reads, so ask us for those.

Command line:

- Show the event, including whether buyers can refund themselves: `ticketfairy event get <EVENT_ID> --output json`

Prompt for Fai: "Turn on self-refunds for <EVENT NAME> and confirm the setting is on"

### Let buyers resell their tickets at face value

Slug `let-buyers-resell-their-tickets-at-face-value`. Guide: https://www.ticketfairy.com/guides/let-buyers-resell-their-tickets-at-face-value

Turn on ticket resale so a buyer who can't come to your event passes their ticket to the next fan on your waiting list, or to someone they name, at the ticket's own price, and follow every resale ticket on the Ticket Resale report.

For: Letting ticket buyers pass their tickets to fans who want them.

What an agent can do: Fai, the assistant inside your dashboard, can turn ticket resale, add-on resale and the waiting list on for you, tell you the resale fee on your event and list the tickets buyers have put up for resale. She shows you each change and asks you to approve it before she saves. Over MCP your own assistant can switch resale on and read the setting back.

Command line:

- Turn on ticket resale and add-on resale for an event: `ticketfairy event update <EVENT_ID> --body '{"flagResaleEnabled": true, "flagEnableAddOnResale": true}'`
- Check whether ticket and add-on resale are on, and the resale fee percentage the event carries: `ticketfairy event get <EVENT_ID> --fields flagResaleEnabled,flagEnableAddOnResale,resaleFeePercentage`
- List every ticket buyers have put up for resale, with its status, how it sold and the ticket it went to: `ticketfairy api /api/events/<EVENT_ID>/relationships/performance --query section=resale --output json`

CLI MCP tools that read: `select_brand`, `select_event`, `get_event`.

CLI MCP tools that make changes (not available with `--read-only`): `update_event`.

Prompt for Fai: "Turn on ticket resale, add-on resale and the waiting list for <EVENT NAME>, then tell me the resale fee on the event and list the tickets buyers have put up for resale"

### Move a buyer to a different ticket type or seat

Slug `move-a-buyer-to-a-different-ticket-type-or-seat`. Guide: https://www.ticketfairy.com/guides/move-a-buyer-to-a-different-ticket-type-or-seat

Change every ticket on a buyer's order to another ticket type in one go, move one ticket on its own, or give a ticket holder a different seat on your seat map, without the buyer placing a new order.

For: Moving a buyer to the right ticket or seat after they have bought.

What an agent can do: Fai, the assistant inside your dashboard, finds the order and reads out each ticket's type, holder and state, before and after you move it. Changing the ticket type and changing a seat are yours to do on the page, because she cannot do either. MCP and the command line have no command for either change.

Prompt for Fai: "For order <ORDER NUMBER> on <EVENT NAME>, list each ticket with its ticket type, holder and state, and tell me which of them are checked in or up for resale"

### Print venue directions and entry details on your tickets

Slug `print-venue-directions-and-entry-details-on-your-tickets`. Guide: https://www.ticketfairy.com/guides/print-venue-directions-and-entry-details-on-your-tickets

Add your own words to every ticket PDF for your event, such as how to get to the venue, which entrance to use and what to bring, and give one ticket type its own text or hide the date on its tickets.

For: Getting the door information onto every ticket your buyers carry.

What an agent can do: Fai, the assistant inside your dashboard, can set the words printed on every ticket for your event, or on one ticket type's tickets, and hide the date on a ticket type. She shows you the change and asks you to approve it before saving. MCP has no tool for ticket text.

Command line:

- Sets the text printed on every ticket PDF for the event, replacing any text already there: `ticketfairy event update <EVENT_ID> --body '{"ticketText":"<TICKET_TEXT>"}'`

Prompt for Fai: "On <EVENT NAME>, print this on every ticket PDF: <DIRECTIONS AND ENTRY DETAILS>. Show me the text before you save it"

### Refund an order on your event

Slug `refund-an-order`. Guide: https://www.ticketfairy.com/guides/refund-an-order

Return the face value of a paid order to the buyer's card from the Orders page, confirm it with the authorisation code Ticket Fairy emails you, and see what changes for the buyer, the tickets and your reports.

For: Returning a buyer's money for an order they no longer want.

What an agent can do: Fai, the assistant inside your dashboard, can request the authorisation code for an order and, once you give her the code from your email, refund it. She shows you the order and the amount and asks you to approve before any money moves. The whole workflow is also in the dashboard.

Command line:

- Email yourself the authorisation code for an order without refunding it: `ticketfairy order refund <ORDER_HASH> --request-code-only`
- Refund the order with the code from your email: `ticketfairy order refund <ORDER_HASH> --code <CODE>`

Prompt for Fai: "Find order <ORDER NUMBER> on <EVENT NAME>, show me the buyer, the tickets and the amount that would be refunded, then request the refund authorisation code and wait for me to give you the code before refunding"

### Resend a buyer's tickets and fix their details

Slug `resend-tickets-and-fix-a-buyers-details`. Guide: https://www.ticketfairy.com/guides/resend-tickets-and-fix-a-buyers-details

Send an order's tickets again to any email address the buyer gives you, and correct the name or email on a ticket so it matches the person arriving at the door.

For: Answering a buyer whose tickets went missing.

What an agent can do: Fai, the assistant inside your dashboard, finds the order and reads what was sent and to which address. Sending the tickets again and correcting a name are yours to do on the page, because neither is something she can carry out.

Prompt for Fai: "Find the order for <BUYER EMAIL ADDRESS> on <EVENT NAME> and tell me which tickets it holds and what state each one is in"

### Run a waiting list for a sold-out event

Slug `run-a-waiting-list`. Guide: https://www.ticketfairy.com/guides/run-a-waiting-list

Switch on the waiting list, decide how many tickets one person can ask for, see who is waiting, and find out how the next person in line is offered a returned ticket and how long they have to buy it.

For: Offering returned tickets to buyers who missed out.

What an agent can do: Fai, the assistant inside your dashboard, can switch the waiting list on or off, set the most tickets one signup may ask for, read who is waiting and email the list. She shows you each change before she makes it. The whole workflow is also in the dashboard.

Command line:

- Turn on the ticket and add-on waiting lists for an event: `ticketfairy event update <EVENT_ID> --body '{"flagEnableWaitingList": true, "flagEnableAddOnWaitingList": true}'`

Prompt for Fai: "Turn on the waiting list for <EVENT NAME> for tickets and add-ons, cap each signup at <NUMBER> tickets, then show me who is waiting and how many tickets they asked for"

### Sell a block of tickets to a company and invoice them

Slug `take-a-group-booking-and-invoice-it`. Guide: https://www.ticketfairy.com/guides/take-a-group-booking-and-invoice-it

Record a company's block of tickets with its purchase order and payment terms, get it signed off, and send the company one invoice with a due date that matches their terms.

For: Selling blocks of tickets to companies and teams.

What an agent can do: Fai can draft the booking, send it for sign-off and raise the invoice. She asks before each of those, because each one commits money or reaches a company.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Create a group booking for <EVENT NAME>: forty passes for <COMPANY NAME> against <PURCHASER NAME OR EMAIL>, on the general admission ticket at its current price, purchase order 8841, thirty day terms, and show it to me before saving"

### Win back buyers who left checkout

Slug `recover-abandoned-carts`. Guide: https://www.ticketfairy.com/guides/recover-abandoned-carts

Find the buyers who entered their details at checkout and never paid for their tickets, see why each one is on the list, and email them back to your event.

For: Turning lost checkouts into sales.

What an agent can do: Fai, the assistant inside your dashboard, can read the list and tell you how big it is and how recent. Sending the email is done in the dashboard, so she hands you back to the composer, and MCP has no reader for this list.

Prompt for Fai: "For <EVENT NAME>, how many people left checkout without paying in the last <NUMBER> days, and how many of them never got as far as an order"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
