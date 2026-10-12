---
name: set-up-event-tickets
description: "Set up a Ticket Fairy event: ticket types, release tiers, sessions, seating, add-ons, resale and transfer rules. Use when an organiser wants to create or change what their event sells."
---

# Set up event tickets

This skill covers ticket types, release tiers, multi-day and timed entry, seating, resale and transfer rules on Ticket Fairy. It lists the 29 published guides for this area and what an agent can do for each one.

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

- [Add your flyer and description to your event page](#add-your-flyer-and-description-to-your-event-page)
- [Answer your buyers' questions on the event page](#answer-your-buyers-questions-on-the-event-page)
- [Approve orders before buyers receive tickets](#approve-orders-before-buyers-receive-tickets)
- [Cancel an event](#cancel-an-event)
- [Choose who Ticket Fairy support contacts about your event](#choose-who-ticket-fairy-support-contacts-about-your-event)
- [Create a reusable event template](#create-a-reusable-event-template)
- [Create an event](#create-an-event)
- [Duplicate an event](#duplicate-an-event)
- [Group your tickets into categories](#group-your-tickets-into-categories)
- [Hold back tickets for later](#hold-back-tickets-for-later)
- [Issue reusable event passes to crew and artists](#issue-reusable-event-passes-to-crew-and-artists)
- [Limit who can buy a ticket type](#limit-who-can-buy-a-ticket-type)
- [Make your event invitation-only](#make-your-event-invitation-only)
- [Password-protect your event](#password-protect-your-event)
- [Postpone or reschedule an event](#postpone-or-reschedule-an-event)
- [Run a recurring event series](#run-a-recurring-event-series)
- [Run an A/B test for your event](#run-an-ab-test-for-your-event)
- [Schedule ticket releases](#schedule-ticket-releases)
- [Schedule when your event goes live](#schedule-when-your-event-goes-live)
- [Sell parking, camping and merchandise with your tickets](#sell-parking-camping-and-merchandise-with-your-tickets)
- [Sell tickets by personal invitation](#sell-tickets-by-personal-invitation)
- [Sell tickets only to your NFT holders](#sell-tickets-only-to-your-nft-holders)
- [Sell timed-entry tickets for an attraction, exhibition or food event](#sell-timed-entry-tickets-for-an-attraction-exhibition-or-food-event)
- [Sell VIP tables and bottle service through your promoters](#sell-vip-tables-and-bottle-service-through-your-promoters)
- [Set up ticket types](#set-up-ticket-types)
- [Set up ticketing for a multi-day festival](#set-up-ticketing-for-a-multi-day-festival)
- [Take pre-registrations before your ticket on-sale](#take-pre-registrations-before-your-ticket-on-sale)
- [Unlock hidden tickets with an access code](#unlock-hidden-tickets-with-an-access-code)
- [Use Freefund to reduce no-shows at free and RSVP events](#use-freefund-to-reduce-no-shows-at-free-and-rsvp-events)

### Add your flyer and description to your event page

Slug `design-your-event-page`. Guide: https://www.ticketfairy.com/guides/design-your-event-page

Add the flyer, the background image and the description a buyer reads before they choose a ticket, keep the short description brief enough to read in a shared link, and give each language its own wording and artwork.

For: Turning visitors into ticket buyers on your event page.

What an agent can do: Fai, the assistant inside your dashboard, drafts the wording for you and sets the one-line version herself, asking you to approve it first. The full description goes into the card on the page, and so does the artwork, because she can neither save the long text nor hold your flyer for you.

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "For <EVENT NAME>, draft an event description covering the line-up, the door times, the age rule and how to get there, then set the one-line version"

#### Then: Sell the same event in another language

What an agent can do: Fai can draft the description in another language from the English one, and asks you to approve it before it is saved.

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "For <EVENT NAME>, draft the event description in <LANGUAGE> from the English one"

### Answer your buyers' questions on the event page

Slug `add-faqs-to-your-event-page`. Guide: https://www.ticketfairy.com/guides/add-faqs-to-your-event-page

Group the questions buyers keep asking into sections on your event page, keep a question private until you have decided the answer, and import a set of questions from a know-before-you-go sheet you already have.

For: Answering common buyer questions on your event page.

What an agent can do: Fai, the assistant inside your dashboard, can read your FAQ sections, draft new ones, add and reword questions, reorder them and import a set from a document. She asks you to approve anything she drafts. The same workflow is on the FAQs page.

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "On <EVENT NAME>, add an FAQ section called Getting Here with questions about parking, the shuttle bus and which gate coaches use"

#### Then: Import the questions from a document you already have

What an agent can do: Fai can read a photo of your sheet, or text you paste to her, and draft the sections and questions from it for you to approve. A Word file or a PDF goes through Import from document on the page instead, which reads them for you.

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "On <EVENT NAME>, turn this photo of our info sheet into FAQ sections"

#### Then: Rename or delete a section

What an agent can do: Fai can rename, reorder and delete sections and questions, and asks you to approve each change first.

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "On <EVENT NAME>, rename the Getting Here FAQ section to Travel and Parking"

### Approve orders before buyers receive tickets

Slug `approve-orders-before-buyers-receive-tickets`. Guide: https://www.ticketfairy.com/guides/approve-orders-before-buyers-receive-tickets

Review every order, or only orders containing selected ticket types. Choose when to take payment, then approve or decline each request before its payment hold expires.

For: Reviewing ticket requests before confirming admission.

What an agent can do: Fai, the assistant inside your dashboard, can turn order approval on for the event or selected ticket types, show you a pending order, and approve or decline it. She asks you to approve settings changes and asks again before the order decision. You can also complete the whole workflow in the dashboard. Your own AI assistant over the MCP server can show you a specified pending order and approve it only after you confirm.

CLI MCP tools that read: `select_event`, `get_order`.

CLI MCP tools that make changes (not available with `--read-only`): `mark_order_paid`.

Prompt for Fai: "Find my event by name. Require approval for <EVERY ORDER OR TICKET TYPE NAMES> and <HOLD SUPPORTED PAYMENTS OR COLLECT AT CHECKOUT>. Show me the setting and ask me to approve it. Then open pending order <ORDER NUMBER>, show me the buyer, ticket types, total and payment state, and ask whether I want to approve or decline it. Do not make the order decision until I choose and approve it"

#### Then: Decline a pending order

What an agent can do: Fai can decline the pending order after showing you the buyer, tickets, total and payment-hold deadline. MCP can open the order but cannot decline it, and the CLI does not expose this decision.

CLI MCP tools that read: `select_event`, `get_order`.

Prompt for Fai: "Open pending order <ORDER NUMBER> for <EVENT NAME>. Show me the buyer, tickets, total, payment status and hold deadline, then ask before declining it"

### Cancel an event

Slug `cancel-an-event`. Guide: https://www.ticketfairy.com/guides/cancel-an-event

Mark the event cancelled, start refunds for every order and tell ticket holders yourself before the refund emails reach them.

For: Ending an event after you have already sold tickets.

What an agent can do: Fai can open Event Details for you, read the event back, and draft the announcement to ticket holders. Cancelling is yours to confirm in the dashboard or with the CLI, which asks you to confirm before it sends anything.

Command line:

- Cancel an event and confirm at the prompt: `ticketfairy event cancel <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open Event Details for <EVENT NAME>, tell me how many orders it has, and draft an email telling ticket holders it is cancelled and their refund is on the way"

#### Then: Check the refunds have gone out

What an agent can do: Fai can open the event so you can check the orders. What each order has been refunded is read on the Orders page today.

Command line:

- Show the event and its current status: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open <EVENT NAME> so I can check its refunds"

#### Then: Cancel an event whose funds have been paid out

What an agent can do: Fai can open the support request for you with the event ID already in it.

Command line:

- Show the event before you contact support: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open a support request to cancel <EVENT NAME>. Its funds have already been paid out. Include the event ID"

#### Then: Reinstate a cancelled event

What an agent can do: Ask Fai to open the support request. MCP can show whether the event is still cancelled. The CLI command works only for an authorised Ticket Fairy staff account.

Command line:

- Reinstate and stop existing resale invitations: `ticketfairy event reinstate <EVENT_ID> --invalidate-resale-invitations`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open a support request to reinstate <EVENT NAME>. Include its event ID and ask me whether existing resale invitations should remain valid"

### Choose who Ticket Fairy support contacts about your event

Slug `choose-who-ticket-fairy-support-contacts-about-your-event`. Guide: https://www.ticketfairy.com/guides/choose-who-ticket-fairy-support-contacts-about-your-event

Give Ticket Fairy support two email addresses for one event, the one buyer escalations go to and your team's point of contact, in place of your brand's, or send the event back to your brand's addresses.

For: Pointing Ticket Fairy support at the team that runs one event.

What an agent can do: Fai, the assistant inside your dashboard, can set both addresses on one event. She shows you the change and asks you to approve it before she saves it. The command line sets the same two addresses through an event update.

Command line:

- Sets the event's escalation address and its point of contact for Ticket Fairy support, in place of the brand's: `ticketfairy event update <EVENT_ID> --body '{"externalSupportEmail":"<ESCALATION_EMAIL>","internalSupportEmail":"<TEAM_EMAIL>"}'`

Prompt for Fai: "For <EVENT NAME>, set the contact email for escalations to <ESCALATION EMAIL> and the point of contact email for Ticket Fairy support to <TEAM EMAIL>, then show me the change before you save it"

#### Then: Go back to your brand's addresses

What an agent can do: Fai can remove the event's own addresses, so the event uses your brand's again. She shows you the change and asks you to approve it first. The command line does the same with an event update that clears both addresses.

Command line:

- Removes the event's own addresses so the event uses the brand's again: `ticketfairy event update <EVENT_ID> --body '{"externalSupportEmail":null,"internalSupportEmail":null}'`

Prompt for Fai: "For <EVENT NAME>, remove the event's own support contact addresses so it uses the brand contacts again, and show me the change before you save it"

### Create a reusable event template

Slug `create-a-reusable-event-template`. Guide: https://www.ticketfairy.com/guides/create-a-reusable-event-template

Share your ticket tiers and allocations as a template without publishing your prices. Your brand name appears on every template you publish.

For: Sharing an event setup as a reusable template.

What an agent can do: Fai can copy the ticket tiers and allocations from your event, choose an anchor tier and draft the template details. She shows you the wording and asks before submitting it. You can also create the template from your event in the dashboard.

Prompt for Fai: "Share my Summer Weekender as a template called "Two stage weekender", use the weekend ticket as the anchor, draft a one-line summary for a two-day outdoor event with camping, and show me the draft before submitting"

#### Then: Withdraw a template

What an agent can do: Fai can find the template and withdraw it after showing you its current status. MCP and the CLI do not manage organiser-shared event templates.

Prompt for Fai: "Find my event template called <TEMPLATE NAME>, show me its current status and public details, then ask before withdrawing it to draft"

### Create an event

Slug `create-an-event`. Guide: https://www.ticketfairy.com/guides/create-an-event

Start from a template or a blank event, add the details buyers need, set up your ticket types before anything is saved, and choose how you want to sell.

For: Creating a new event and preparing it for ticket sales.

What an agent can do: Fai can recommend built-in and organiser-shared templates, lead with the one suggested for your brand, ask for the details and prices that belong to your event, and prepare the event with its ticket types and add-ons. She shows you the complete setup and asks before creating it. MCP and the CLI can create an event directly from the details you provide.

Command line:

- A guided event setup in your terminal: `ticketfairy event create --interactive`
- A draft from the main event details: `ticketfairy event create --name "<EVENT NAME>" --start <START> --end <END> --venue-search "<VENUE AND CITY>" --currency <CURRENCY> --draft`
- A complete event from a JSON or YAML file: `ticketfairy event create --from-file event.json`

CLI MCP tools that read: `set_context`.

CLI MCP tools that make changes (not available with `--read-only`): `create_event`.

Prompt for Fai: "Create an event for <EVENT DESCRIPTION>. Compare the built-in and organiser-shared templates, recommend the closest setup, ask me for every missing detail and price, then show me the event, ticket types, add-ons and sales settings before creating it"

#### Then: Return to a saved draft

What an agent can do: Fai can find the draft, show you what still needs attention and continue the setup after you approve each change. MCP and the CLI can inspect the saved event. The dashboard is the clearest place to review the whole setup.

Command line:

- Your events and their statuses: `ticketfairy event list`
- The current details for the draft: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `list_events`, `get_event`.

Prompt for Fai: "Find my draft event called <EVENT NAME>, show me its event details, ticket types, add-ons and sales settings, then ask what I want to finish before making any changes"

#### Then: Start an event before you sign up

What an agent can do: Fai can list the events you started before signing in and, after you approve, attach one to a brand as a draft event. Starting or editing the draft happens only on the page itself, before you have an account.

Prompt for Fai: "Show me the events I started before signing in, then attach <EVENT NAME> to my brand <BRAND> as a draft"

#### Then: Use the classic event form

What an agent can do: Open the classic editor in the dashboard. Fai, MCP and the CLI can edit event data, but they cannot open this editor.

### Duplicate an event

Slug `duplicate-an-event`. Guide: https://www.ticketfairy.com/guides/duplicate-an-event

Start your next date with the ticket types, event settings and optional features you already use, then enter the new name, web address and dates before it goes on sale.

For: Preparing another date from an existing event.

What an agent can do: Fai can duplicate an event as a new draft, copy the parts you choose, and set its new name, URL and dates after you approve the change.

Prompt for Fai: "Duplicate <EVENT_NAME> for <NEW_DATE>. Show me the new name, dates and everything you will copy before you create the draft"

#### Then: Prepare the copied event before it goes on sale

What an agent can do: Fai can inspect the copied draft, compare its tickets and settings with the new date, and update the fields you approve. MCP and the CLI can inspect and update individual parts, but neither provides one complete copied-event review.

CLI MCP tools that read: `select_event`, `get_event`, `list_tickets`.

Prompt for Fai: "Review the copied draft <EVENT NAME> before it goes on sale. Show me its dates, venue, tickets, allocations, sale windows, entry times, promotions, messages, team and buyer questions, and flag anything that still names the source event or its date"

#### Then: Publish the new event

What an agent can do: Fai, MCP and the CLI can publish the copied draft after showing you the event you selected. Scheduling a future publish time is available in the dashboard and through Fai.

Command line:

- Publish the copied event: `ticketfairy event publish <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

CLI MCP tools that make changes (not available with `--read-only`): `publish_event`.

Prompt for Fai: "Show me the copied draft <EVENT NAME>, its public event page and ticket sale windows. Ask whether to send promoter links and whether to publish now or at a scheduled time, then wait for my approval"

#### Then: Delete a duplicate you made by mistake

What an agent can do: Fai, MCP and the CLI can delete the mistaken draft after confirming its identity. The action is refused when the event already has orders.

Command line:

- Delete the mistaken draft: `ticketfairy event delete <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

CLI MCP tools that make changes (not available with `--read-only`): `delete_event`.

Prompt for Fai: "Find the draft <EVENT NAME>, show me its dates, venue and whether it has any orders, then ask before deleting it"

### Group your tickets into categories

Slug `group-your-tickets-into-categories`. Guide: https://www.ticketfairy.com/guides/group-your-tickets-into-categories

Group day passes, weekend passes and price releases into categories so buyers can find the right ticket quickly.

For: Making a long ticket list easier to browse.

What an agent can do: Fai, the assistant inside your dashboard, can create the categories, put each ticket type into one, and tell you which ticket types are still uncategorised. She asks you to approve every change before she makes it. You can also create and organise the categories in the dashboard.

Prompt for Fai: "Make ticket categories called Friday, Saturday, Sunday and Full Weekend on this event, then list my ticket types, put each one in the category that best matches its name, and tell me which are still uncategorised"

#### Then: Rename a ticket category

What an agent can do: Fai can rename the category without changing its tickets or resale type. MCP and the CLI do not manage ticket categories.

Prompt for Fai: "Find the ticket category <OLD NAME> on <EVENT NAME>, show me its ticket types and resale type, then rename it to <NEW NAME> without changing anything else"

#### Then: Change which ticket types are in a category

What an agent can do: Fai can set the ticket types in a category in one step. MCP and the CLI do not manage ticket categories.

Prompt for Fai: "Put <TICKET TYPE NAMES> in the ticket category <CATEGORY NAME> on <EVENT NAME> and take every other ticket type out of it"

#### Then: Delete a ticket category

What an agent can do: Fai can show the tickets that will return to the main list, then delete the category after you approve it. MCP and the CLI do not manage ticket categories.

Prompt for Fai: "Find the ticket category <CATEGORY NAME> on <EVENT NAME> and list every ticket type in it. Confirm that the tickets will stay on sale, then ask before deleting only the category"

### Hold back tickets for later

Slug `hold-back-ticket-stock`. Guide: https://www.ticketfairy.com/guides/hold-back-ticket-stock

Set aside part of a ticket type for a guest list, a competition or a partner, so those tickets stay out of the public on-sale until you hand them out.

For: Keeping part of a release for guests, competitions and partners.

What an agent can do: Fai, the assistant inside your dashboard, reads your ticket types and can tell you what each one has left. Setting a hold is yours to do on the page.

Prompt for Fai: "For <EVENT NAME>, how many tickets are left on <TICKET TYPE NAME> and how many have sold"

#### Then: Keep a second reserve on the same ticket

What an agent can do: Fai reads what each ticket type has left, which is the number a second reserve has to fit inside. Adding it is yours to do on the page.

Prompt for Fai: "For <EVENT NAME>, list my ticket types with how many of each are left"

#### Then: Give the held tickets out

What an agent can do: Choosing the reserve an invitation draws on is yours to do on the Invitations page. Fai cannot list the invitations sent from it.

#### Then: Put a reserve back on sale

What an agent can do: Fai reads the ticket type afterwards and can confirm what buyers can now reach. Removing the reserve is yours to do on the page.

Prompt for Fai: "For <EVENT NAME>, how many of <TICKET TYPE NAME> are available to buyers now"

### Issue reusable event passes to crew and artists

Slug `issue-entry-passes-to-your-crew`. Guide: https://www.ticketfairy.com/guides/issue-entry-passes-to-your-crew

Give crew and artists named multi-entry passes. Your door team can scan them in the same app they use for tickets.

For: Letting your team in and out of an event all day.

What an agent can do: Fai, the assistant inside your dashboard, can create the pass types, issue the passes and send them out. She asks you to approve each action first. You can also manage the passes in the dashboard. Review every recipient before sending, because an email that has gone cannot be recalled.

Prompt for Fai: "Create a Crew Member pass type for this brand with twelve entries per event, issue one to every person in the list I paste next, and show me the names before sending anything"

#### Then: Update a pass

What an agent can do: Fai can find the pass and update its holder, type, uses or notes after showing you the current details. MCP and the CLI do not manage entry passes.

Prompt for Fai: "Find the entry pass for <PERSON> on <EVENT OR BRAND>, show me its type, email address, uses and notes, then ask what I want to change"

#### Then: Remove a pass

What an agent can do: Fai can show the pass holder, type and remaining uses, then remove it after you approve the change. MCP and the CLI do not manage entry passes.

Prompt for Fai: "Find the entry pass for <PERSON> on <EVENT OR BRAND>, show me its type and remaining uses, then ask before removing the pass"

### Limit who can buy a ticket type

Slug `limit-who-can-buy-tickets`. Guide: https://www.ticketfairy.com/guides/limit-who-can-buy-tickets

Limit how many tickets one order or customer account can buy, or send one ticket type to another ticketing page instead of selling it through Ticket Fairy.

For: Controlling ticket quantities and where buyers complete a purchase.

What an agent can do: Fai can set the per-order limit, the per-account limit and the external sales address on a ticket type. She shows you the ticket type and the change and asks for your approval before saving it. MCP and the CLI can set the two limits after approval.

Command line:

- Find every ticket type and its ID: `ticketfairy ticket list <EVENT_ID> --all`
- Limit one order to 6 tickets and one customer account to 8: `ticketfairy ticket update <EVENT_ID> <TICKET_ID> --max-per-order 6 --max-per-account 8`

CLI MCP tools that read: `set_context`, `list_tickets`.

CLI MCP tools that make changes (not available with `--read-only`): `update_ticket`.

Prompt for Fai: "On <EVENT NAME>, limit <TICKET TYPE> to <NUMBER> per order and <NUMBER> per customer account. Show me the ticket type and the change, and ask before saving it"

### Make your event invitation-only

Slug `make-an-event-invitation-only`. Guide: https://www.ticketfairy.com/guides/make-an-event-invitation-only

Compare a shared password, personal invitations and a ticket access code, or approve each order after checkout before the buyer gets their tickets.

For: Controlling who can buy tickets before or after checkout.

What an agent can do: Fai, the assistant inside your dashboard, can compare the four approaches, check how your event is currently configured and set up the option you choose. She explains who gets access and when, then asks you to approve each change separately. You can also make every change in the dashboard.

Prompt for Fai: "Find my event by name. Ask me whether access should use shared passwords, personal invitations, a shared access code, or a decision after checkout. Recommend the best fit from my answer, explain who can get through and when access is decided, then show me every setting, ticket, promotion or invitation message you would change and ask me to approve each change separately"

### Password-protect your event

Slug `password-protect-your-event`. Guide: https://www.ticketfairy.com/guides/password-protect-your-event

Put your event page behind one or more shared passwords, test them and change a password without locking out the groups that still need access.

For: Sharing a private event through one or more trusted groups.

What an agent can do: Fai, the assistant inside your dashboard, can add or remove event passwords and turn password protection on or off. She shows you the event and asks you to approve each change before she makes it. You can also complete the whole workflow in the dashboard.

Prompt for Fai: "Find my event by name, add these event passwords: <PASSWORDS>, and turn on Password required to view event only after at least one password is saved. Show me the event and every password that will remain, then ask me to approve each change"

#### Then: Replace a shared password

What an agent can do: Fai can create the replacement and remove the old password after you have tested the new one. MCP and the CLI do not manage event passwords.

Prompt for Fai: "For <EVENT NAME>, create a replacement for the password <OLD PASSWORD>. Show me the new password before saving it, and do not remove the old one until I confirm that I have tested the replacement"

#### Then: Review sales made with each password

What an agent can do: Fai can show Sales by Password and explain the rows. MCP and the CLI do not provide this password report.

Prompt for Fai: "Show me Sales by Password for <EVENT NAME>. Compare sales and revenue for each password and explain what the report can and cannot identify"

#### Then: Turn password protection off

What an agent can do: Fai can turn password protection off after showing you the event and the effect of the change. MCP and the CLI do not expose this setting.

Prompt for Fai: "Turn password protection off for <EVENT NAME>. Show me the event and confirm that its page will open without a password before changing it"

### Postpone or reschedule an event

Slug `postpone-or-reschedule-an-event`. Guide: https://www.ticketfairy.com/guides/postpone-or-reschedule-an-event

Tell ticket holders that the date has changed, publish the new date once you have it, and choose who can ask for a refund.

For: Changing the date of an event that has already been announced.

What an agent can do: Fai can open Event Details for you and guide you through the Event Status controls. The CLI can postpone an event from a reviewed JSON or YAML file. MCP can show your assistant the event's current dates and status before and after the change.

Command line:

- Postpone or reschedule an event from a reviewed file: `ticketfairy event postpone <EVENT_ID> --from-file postponement.yaml`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open Event Details for <EVENT NAME> and help me postpone it. I want to check the new dates, what ticket holders will see and who can request a refund before I confirm"

#### Then: Update the date or refund choice

What an agent can do: Fai can open Event Details for the event. The CLI uses the same reviewed-file command as the first postponement. MCP can check the dates and status afterward.

Command line:

- Replace the current postponement values: `ticketfairy event postpone <EVENT_ID> --from-file postponement.yaml`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open Event Details for <EVENT NAME> so I can update its postponement"

#### Then: Reveal a date that was hidden

What an agent can do: Fai can open Event Details so you can reveal the date. The CLI asks you to confirm the change. MCP can check the event date afterward.

Command line:

- Reveal the new event date: `ticketfairy event disclose-date <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open Event Details for <EVENT NAME> so I can reveal its postponed date"

#### Then: Remove the postponed status

What an agent can do: Fai can open Event Details so you can review refunds and remove the postponed status. The CLI can update the refund choice before removing the status. MCP can check the event status afterward.

Command line:

- Turn off self-service refunds while keeping the current postponement details: `ticketfairy event postpone <EVENT_ID> --from-file postponement.yaml`
- Remove the postponed status: `ticketfairy event postpone <EVENT_ID> --body '{"flagPostponed":false}'`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open Event Details for <EVENT NAME> so I can review its refund choice and remove the postponed status"

### Run a recurring event series

Slug `run-a-recurring-event-series`. Guide: https://www.ticketfairy.com/guides/run-a-recurring-event-series

Keep every edition together, add future dates automatically, and give buyers one public page for the series.

For: Running a festival, tour, club night or show across several dates or editions.

What an agent can do: Fai can find suggested series, create one with an automatic name rule, add known editions, make its buyer page public, or attach one event directly.

Prompt for Fai: "Set up a recurring series for <EVENT_NAME>. Find any earlier editions, suggest a rule that will include future dates, and show me the series name, events and public URL before creating it"

#### Then: Create a suggested series from your event history

What an agent can do: Fai can list the same suggestions and create the one you approve. MCP and the CLI do not manage event series.

Prompt for Fai: "Show me the suggested event series for <BRAND NAME>, including the editions in each suggestion. Recommend the best match and ask before creating it"

#### Then: Add an edition that does not match the name rule

What an agent can do: Fai can attach the chosen edition directly. MCP and the CLI do not manage event series.

Prompt for Fai: "Add <EVENT NAME> to the series <SERIES NAME> as a directly attached edition. Show me the event date and venue, then ask before attaching it"

#### Then: Add several existing editions through Fai

What an agent can do: Fai can attach several named editions after showing you every date and venue. MCP and the CLI do not manage event series.

Prompt for Fai: "Add <EVENT NAMES> to the series <SERIES NAME>. Show me every event with its date and venue, then ask once before attaching them"

#### Then: Add future events at particular venues

What an agent can do: Fai can add a venue rule alone or together with the series name rule. MCP and the CLI do not manage event series.

Prompt for Fai: "For the series <SERIES NAME>, add a rule for <VENUE OR VENUES>. Show me whether the existing name rule will also be required and which current events match before saving"

#### Then: Change the series name, rule or public page

What an agent can do: Fai can show the current series and update only the name, description, rules or public-page setting you choose. MCP and the CLI do not manage event series.

Prompt for Fai: "Show me the series <SERIES NAME>, its editions, automatic rules and public-page setting, then ask what I want to change and show the result before saving"

#### Then: Delete a series you no longer need

What an agent can do: Fai can show the series, its editions, any connected social account and any automatic messages switched on for it before deleting only the series. She asks before pausing those messages. MCP and the CLI do not manage event series.

Prompt for Fai: "Show me the series <SERIES NAME>, every edition and any connected social account. Confirm that its events will remain, then ask before deleting the series"

### Run an A/B test for your event

Slug `run-an-ab-test-for-your-event`. Guide: https://www.ticketfairy.com/guides/run-an-ab-test-for-your-event

Compare event pages or checkout questions and answers, split visitors between versions and find which one brings in more ticket sales or revenue.

For: Testing which event page or checkout questions and answers sell more tickets.

What an agent can do: Fai can create and edit a draft, start or pause a test, conclude it and compare the results. She reads the latest version first and asks you to approve every change. You can do the same work in the Experiments section of the dashboard.

Prompt for Fai: "Find my event and help me create an A/B test. Ask what I want to test, whether it should run on the event page or checkout, and whether conversion rate or revenue per visitor matters most. Show me the complete draft and visitor split before asking me to approve it. Do not start it until I approve that separately"

### Schedule ticket releases

Slug `schedule-ticket-sale-windows-and-release-tiers`. Guide: https://www.ticketfairy.com/guides/schedule-ticket-sale-windows-and-release-tiers

Plan a clear sequence of ticket releases with the right price, sales dates and hidden reveal rules so buyers see the right choice at the right time.

For: Planning when each ticket release becomes available.

What an agent can do: Fai can list your releases in their current order with each one's category and sales dates, and she can save a new order after you approve it. Set the availability option, the dates and the Hidden rule for each release on the dashboard: Fai cannot see which availability option a release uses, and a sales window she sets opens at whichever comes first, the date or the previous release selling out. MCP can list the releases but cannot reorder them.

Command line:

- Create a release that sells between two dates: `ticketfairy ticket create <EVENT_ID> --name "Early Bird" --price 39 --max-inventory 200 --sales-start 2026-11-01T10:00:00Z --sales-end 2026-11-15T23:59:59Z`
- Create a release that goes on sale when the one before it sells out: `ticketfairy ticket create <EVENT_ID> --name "First Release" --price 49 --max-inventory 500 --available-after-previous`
- List the event's ticket types with the id each one has: `ticketfairy ticket list <EVENT_ID>`
- Move an existing release's sales window: `ticketfairy ticket update <EVENT_ID> <TICKET_ID> --sales-start 2026-11-08T10:00:00Z --sales-end 2026-11-22T23:59:59Z`

CLI MCP tools that read: `set_context`, `list_tickets`.

Prompt for Fai: "Open the Tickets page for <EVENT NAME> and list the ticket types in their current order with their category and sales dates. If I give you a new order, show me the complete order and ask before saving it. Tell me to set the dates and reveal settings for <TICKET TYPE> on the dashboard"

#### Then: Change a release after it is scheduled

What an agent can do: Fai can show the release with its category and sales dates. Change its dates or reveal settings on the dashboard, because Fai cannot see which availability option or reveal rule the release uses.

CLI MCP tools that read: `set_context`, `list_tickets`.

Prompt for Fai: "Open the Tickets page for <EVENT NAME> and list the basic details for <TICKET TYPE>. Tell me to select it in the dashboard and change its dates or reveal settings. Do not change anything"

### Schedule when your event goes live

Slug `schedule-when-your-event-goes-live`. Guide: https://www.ticketfairy.com/guides/schedule-when-your-event-goes-live

Choose a date and time in your event's timezone so Ticket Fairy makes the event page public at that time.

For: Running an on-sale at a set time.

What an agent can do: Fai, the assistant inside your dashboard, can set the schedule for you, and asks you to approve the schedule before saving it. You can also set the date in the dashboard. Your own AI assistant over our MCP server can tell you whether the event is live.

Command line:

- Your event page, live now: `ticketfairy event publish <EVENT_ID>`
- Live now, with promoter links emailed: `ticketfairy event publish <EVENT_ID> --send-promoter-links`
- Your event page, unpublished now: `ticketfairy event unpublish <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Schedule my event to go live at 10am on 12 September, and tell me which timezone you are using for that"

### Sell parking, camping and merchandise with your tickets

Slug `sell-add-ons-with-your-tickets`. Guide: https://www.ticketfairy.com/guides/sell-add-ons-with-your-tickets

Add parking, camping, meals, merchandise and upgrades to the ticket checkout, with stock, options and limits for each.

For: Selling extras with event admission.

What an agent can do: Fai and MCP can list or create add-ons. Fai asks before creating one. MCP creates it after you provide the event, price in that event's currency, stock and ticket limit. For a multi-currency event, provide a price in every currency. You can also use the command line.

Command line:

- Everything already on sale beside the tickets: `ticketfairy addon list <EVENT_ID>`
- A new one, priced and limited: `ticketfairy addon create <EVENT_ID> --name "Return shuttle" --price 12.50 --quantity 250`
- A whole add-on from a file you created, picture and all: `ticketfairy addon create <EVENT_ID> --from-file <ADDON_FILE> --upload imageUrl=<PICTURE_FILE>`
- A change to one that already exists: `ticketfairy addon update <ADD_ON_ID> --body '{"price":1500}'`
- The same change, on an event taking payments in more than one currency: `ticketfairy addon update <ADD_ON_ID> --body '{"price":1500,"currencies":[{"currency":"EUR","faceValue":1400}]}'`

CLI MCP tools that read: `select_brand`, `select_event`, `list_addons`.

CLI MCP tools that make changes (not available with `--read-only`): `create_addon`.

Prompt for Fai: "Add a return shuttle at 12.50 to this event, limited to 250, one per ticket"

#### Then: Take an add-on off sale

What an agent can do: Fai can turn the add-on off after showing you its current price, stock and restrictions. MCP creates add-ons but does not update them. Use the dashboard or Fai for the Enabled setting; the CLI update command accepts event data fields but has no dedicated on-sale flag.

Prompt for Fai: "Find the add-on <ADD-ON NAME> on <EVENT NAME>. Show me its current price, stock and ticket restrictions, then ask before turning it off"

#### Then: Change an add-on that is on sale

What an agent can do: Fai can show the existing add-on and update the fields you choose. MCP creates add-ons but does not update them. The CLI can apply exact field changes by ID.

Command line:

- Change an add-on price and stock: `ticketfairy addon update <ADDON_ID> --body '{"price": <PRICE>, "stock": <REMAINING_STOCK>}'`

Prompt for Fai: "Find the add-on <ADD-ON NAME> on <EVENT NAME>, show me its price, remaining stock, description and ticket restrictions, then ask what I want to change"

### Sell tickets by personal invitation

Slug `sell-tickets-by-personal-invitation`. Guide: https://www.ticketfairy.com/guides/sell-tickets-by-personal-invitation

Send each approved guest a personal ticket link, set how many tickets they can buy and how many orders they can place, and track or cancel an invitation after you send it.

For: Selling tickets through an approved invitation list.

What an agent can do: Fai, the assistant inside your dashboard, can turn on the invitation requirement and prepare and send the approved list. She asks you to approve each change before she makes it. To check, resend or cancel an invitation you have sent, use the Invitations page, or your own AI assistant over the MCP server.

CLI MCP tools that read: `select_event`, `list_invitations`.

CLI MCP tools that make changes (not available with `--read-only`): `resend_invitation`, `cancel_invitation`.

Prompt for Fai: "Find my event by name, turn on Invitation required to attend, and prepare an invitation email for these approved guests: <names, email addresses, maximum tickets and maximum orders>. Unlock these ticket types with the same invitation: <ticket type names>. Show me the event setting, subject, message, ticket access and each recipient limit, then ask me to approve the event change and the send"

#### Then: Cancel a scheduled invitation

What an agent can do: Cancel a scheduled invitation in the dashboard. Fai, MCP and the CLI cannot cancel it before it is sent.

#### Then: Check what happened after you sent an invitation

What an agent can do: Your own AI assistant over the MCP server can list the invitations and their current statuses. Fai cannot list them, and the CLI does not have an invitation status command.

CLI MCP tools that read: `select_event`, `list_invitations`.

#### Then: Resend one invitation

What an agent can do: Your own AI assistant over the MCP server can resend one active invitation after you confirm the recipient. Fai cannot find the invitation, and the CLI does not expose invitation resends.

CLI MCP tools that read: `select_event`, `list_invitations`.

CLI MCP tools that make changes (not available with `--read-only`): `resend_invitation`.

#### Then: Cancel one invitation

What an agent can do: Your own AI assistant over the MCP server can cancel one active invitation after showing you the recipient and ticket choice. Fai cannot find the invitation, and the CLI does not expose invitation cancellation.

CLI MCP tools that read: `select_event`, `list_invitations`.

CLI MCP tools that make changes (not available with `--read-only`): `cancel_invitation`.

#### Then: Send an invitation reminder

What an agent can do: Send an invitation reminder in the dashboard. Fai, MCP and the CLI cannot send this reminder.

### Sell tickets only to your NFT holders

Slug `sell-tickets-only-to-your-nft-holders`. Guide: https://www.ticketfairy.com/guides/sell-tickets-only-to-your-nft-holders

Require ticket buyers to connect a wallet that holds one of your NFTs before they can buy tickets to your event, for every ticket or for one ticket type, and have the door check the NFT again at entry.

For: Selling event tickets to the holders of an NFT collection.

What an agent can do: Fai, the assistant inside your dashboard, can take you to the event's Settings page, and you turn the NFT requirement on there. The command line can set the requirement for the whole event through an event update.

Command line:

- Requires buyers of any ticket to the event to hold an NFT from one Ethereum collection: `ticketfairy event update <EVENT_ID> --body '{"flagNftOwnershipRequired":true,"nftContracts":{"ethereum":["<CONTRACT_ADDRESS>"],"polygon":[]},"nftLists":{"solana-mainnet":[]}}'`

Prompt for Fai: "Open the settings page for <EVENT NAME> so I can require NFT ownership to buy tickets"

#### Then: Require an NFT for one ticket type only

What an agent can do: Fai can take you to the event's Tickets page, and you set the requirement on the ticket type there. The command line sets it through a ticket type update.

Command line:

- Find every ticket type and its ID: `ticketfairy ticket list <EVENT_ID> --all`
- Requires buyers of one ticket type to hold an NFT from one Polygon collection: `ticketfairy ticket update <EVENT_ID> <TICKET_ID> --body '{"flagNftOwnershipRequired":true,"nftContracts":{"ethereum":[],"polygon":["<CONTRACT_ADDRESS>"]},"nftLists":{"solana-mainnet":[]}}'`

Prompt for Fai: "Open the tickets page for <EVENT NAME> so I can make <TICKET TYPE> available to NFT holders only"

#### Then: Stop requiring an NFT

What an agent can do: Fai can take you to the Settings page to turn the requirement off. The command line turns off the event's requirement through an event update.

Command line:

- Stops requiring an NFT for the whole event: `ticketfairy event update <EVENT_ID> --body '{"flagNftOwnershipRequired":false}'`

Prompt for Fai: "Open the settings page for <EVENT NAME> so I can stop requiring NFT ownership"

### Sell timed-entry tickets for an attraction, exhibition or food event

Slug `sell-timed-entry-tickets`. Guide: https://www.ticketfairy.com/guides/sell-timed-entry-tickets

Give a ticket type its own entry times so buyers pick a date and a slot, cap each slot separately, see sales and arrivals by slot, and know what a sold-out slot looks like to a buyer.

For: Selling entry by date and time slot for a venue that runs all day.

What an agent can do: Fai, the assistant inside your dashboard, can read arrivals by time slot for a date and report on the event. Creating and changing time slots is done in the dashboard for now, and Fai tells you so when you ask.

Command line:

- Read arrivals for the event broken down by time slot: `ticketfairy checkin status <EVENT_ID> --breakdown slots --output json`

Prompt for Fai: "Show me the check-ins by time slot for <EVENT NAME> on <DATE>, with how many people have arrived in each"

#### Then: Move a buyer to another slot

What an agent can do: Moving a ticket between slots is done in the dashboard. Fai can find the order and report how busy each slot is.

Prompt for Fai: "Find the order for <BUYER EMAIL> on <EVENT NAME> and tell me how many people have arrived in each time slot on <DATE>"

#### Then: Add a new date after the slots exist

What an agent can do: Generating slots is done in the dashboard. Fai reads the slots on a day you name, one day at a time.

Prompt for Fai: "Tell me which time slots <EVENT NAME> already has on <DATE>"

#### Then: Give staff and guests a slot

What an agent can do: A guest ticket for a slot is issued on this page: the form takes the ticket type, the date and the time, and Fai addresses a ticket type by its own number, which no reading of the event gives her for one slot. She can create a pass type and issue passes after showing you the list. The CLI does neither.

Prompt for Fai: "Create an all-day crew pass for <EVENT NAME> and issue it to <NAME> <EMAIL>, and show me the list before sending"

### Sell VIP tables and bottle service through your promoters

Slug `sell-vip-tables-and-bottle-service`. Guide: https://www.ticketfairy.com/guides/sell-vip-tables-and-bottle-service

Create a table type for each booth or bottle-service package, give every promoter their own link to sell it, and see the table bookings each promoter brings to your event under Sales by Promoter.

For: Venue teams and promoters selling VIP tables, booths and bottle service alongside entry tickets.

What an agent can do: Fai can create or change your table types, invite promoters to the event, publish the event, resend promoter links once your promoters have accepted their invitations, and show you Sales by Promoter. She shows you each table type and each invitation before saving and asks you to approve the send. Set up tables and promoters in the dashboard or with Fai; your own assistant over the MCP server covers events, tickets and orders only.

Command line:

- Create a table type. Prices are in the smallest unit of your event currency, so 40000 is 400.00, and the deposit is a percentage: `ticketfairy table create <EVENT_ID> --body '{"displayName": "VIP booth", "price": 40000, "maxInventory": 6, "minGuests": 4, "maxGuests": 8, "guestPrice": 7500, "depositPercent": 25}'`
- List the table types on the event with their ids: `ticketfairy table list <EVENT_ID>`
- Publish the event and email every promoter their link: `ticketfairy event publish <EVENT_ID> --send-promoter-links`

Prompt for Fai: "Find my event by name and create a table type called VIP booth, <NUMBER OF BOOTHS> available, for 4 to 8 guests at <TABLE PRICE> with <EXTRA GUEST PRICE> per extra guest and a <DEPOSIT PERCENT> deposit paid online; invite <PROMOTER EMAILS> as promoters; show me the table type and the invitations before saving. Once they have accepted, resend the promoter links when I ask and show me Sales by Promoter"

#### Then: Take a table off sale

What an agent can do: Fai can deactivate, reactivate or mark a table type sold out after you confirm. When she marks one sold out she asks whether buyers who already have it in their basket may finish paying or lose it. Delete a table type in the dashboard. The command line can deactivate a table type.

Command line:

- Hide a table type from buyers and keep its bookings: `ticketfairy table update <TABLE_ID> --body '{"active": false}'`

Prompt for Fai: "Find my event by name, show me its table types, and mark the VIP booth sold out; let anyone who already has one in their basket finish paying, and ask me to confirm first"

### Set up ticket types

Slug `set-up-ticket-types`. Guide: https://www.ticketfairy.com/guides/set-up-ticket-types

Create clear ticket choices with the right price, allocation, purchase limits, availability and entry rules before your event goes on sale.

For: Preparing the tickets buyers will choose for an event.

What an agent can do: Fai can list your existing ticket types, ask for every setting that matters and show the proposed ticket before creating it. MCP and the CLI can also create a ticket type from the details you provide. Every surface asks for approval before making the change.

Command line:

- A standard General Admission ticket type: `ticketfairy ticket create <EVENT_ID> --name "General Admission" --price 35 --max-inventory 500 --max-per-order 6`
- A ticket type using every field in a reviewed file: `ticketfairy ticket create <EVENT_ID> --from-file ticket-type.yaml`

CLI MCP tools that read: `set_context`, `list_tickets`.

CLI MCP tools that make changes (not available with `--read-only`): `create_ticket`.

Prompt for Fai: "Set up a ticket type for <EVENT NAME>. Before creating it, ask whether booking fees should be added to the price, absorbed into it or, where available, added at checkout. Ask me what admission it includes, its name, price, allocation, purchase limits, sale window, visibility, entry rules and resale policy. Show me the booking-fee choice and every ticket setting before making either change"

#### Then: Edit a ticket type

What an agent can do: Fai, MCP and the CLI can show the current ticket and update the fields you name after approval.

Command line:

- Find every ticket type and its ID: `ticketfairy ticket list <EVENT_ID> --all`
- Change a ticket price and allocation: `ticketfairy ticket update <EVENT_ID> <TICKET_ID> --price 42 --max-inventory 650`

CLI MCP tools that read: `set_context`, `list_tickets`.

CLI MCP tools that make changes (not available with `--read-only`): `update_ticket`.

Prompt for Fai: "Show me <TICKET TYPE> on <EVENT NAME>, including its price, allocation, limits, availability and entry rules. Ask what I want to change, then show the complete update before saving it"

#### Then: Duplicate a ticket type

What an agent can do: Fai can duplicate a standard ticket type, then rename or reprice the copy after you approve each change. MCP and the CLI do not duplicate ticket types; create a new ticket from reviewed values instead.

Prompt for Fai: "Duplicate <TICKET TYPE> on <EVENT NAME>. Show me the source ticket and what the copy will keep, then ask before creating it. Afterward ask for the new name, price, allocation and sale window"

#### Then: Change the order buyers see

What an agent can do: Fai can list the current order and save the complete new order after approval. MCP and the CLI do not reorder ticket types.

Prompt for Fai: "Show me the ticket order for <EVENT NAME>, then arrange it as <ORDER>. Show the complete final order and ask before saving it"

#### Then: Take a ticket type off sale without deleting it

What an agent can do: Fai, MCP and the CLI can change the ticket type between active and inactive after approval.

Command line:

- Take the ticket off sale: `ticketfairy ticket update <EVENT_ID> <TICKET_ID> --deactivate`
- Restore the ticket: `ticketfairy ticket update <EVENT_ID> <TICKET_ID> --activate`

CLI MCP tools that read: `set_context`, `list_tickets`.

CLI MCP tools that make changes (not available with `--read-only`): `update_ticket`.

Prompt for Fai: "Show me <TICKET TYPE> on <EVENT NAME> and ask before turning it off. Keep all its other settings unchanged"

#### Then: Mark a ticket type as sold out

What an agent can do: Fai can mark the ticket sold out after showing it and asking whether buyers with live baskets may finish. MCP and the CLI do not expose this action.

Prompt for Fai: "Mark <TICKET TYPE> on <EVENT NAME> as sold out. Show me the ticket, then ask whether buyers who already have it in a live basket may finish checkout before making the change"

#### Then: Delete an unused ticket type

What an agent can do: Fai, MCP and the CLI can delete an unused ticket type after showing its identity and asking for approval. Ticket Fairy refuses the deletion when it has orders or live basket reservations.

Command line:

- Delete the unused ticket type after confirmation: `ticketfairy ticket delete <EVENT_ID> <TICKET_ID>`

CLI MCP tools that read: `set_context`, `list_tickets`.

CLI MCP tools that make changes (not available with `--read-only`): `delete_ticket`.

Prompt for Fai: "Show me <TICKET TYPE> on <EVENT NAME>, including its current status and sales, then ask before deleting it"

### Set up ticketing for a multi-day festival

Slug `sell-a-multi-day-festival`. Guide: https://www.ticketfairy.com/guides/sell-a-multi-day-festival

Group day and weekend tickets so buyers find the right one, open each price release on its own date, sell camping and travel in the same checkout, and keep resale at face value.

For: Selling day and weekend tickets for a festival.

What an agent can do: Fai can create the ticket categories, release tiers, per-day door times, add-ons and resale settings after you provide prices, stock and sale dates. She shows you the complete setup and asks before making changes. MCP and the CLI can create ticket types and add-ons, but you must finish ticket categories, per-day door times, attendee-name checks, ID requirements and resale settings in the dashboard. Name which releases start hidden and what reveals each one. A new tier starts on sale and public unless you say otherwise, so leaving this out puts every release on sale together.

Command line:

- One release tier, priced, stocked and dated: `ticketfairy ticket create <EVENT_ID> --name "Early Bird" --price 39 --max-inventory 200 --max-per-order 4 --sales-start <SALE_OPENS> --sales-end <SALE_CLOSES>`
- A tier that appears when the one before it sells out: `ticketfairy ticket create <EVENT_ID> --name "Tier 2" --price 59 --max-inventory 500 --hidden --hiding-option previous_ticket_sold`
- A camping, parking or travel add-on: `ticketfairy addon create <EVENT_ID> --name "Weekend Camping" --price 45 --quantity 800`
- Everything you have built so far, to check it: `ticketfairy ticket list <EVENT_ID>`

CLI MCP tools that read: `select_brand`, `select_event`.

CLI MCP tools that make changes (not available with `--read-only`): `create_ticket`, `create_addon`.

Prompt for Fai: "Set up general admission and VIP categories for this festival; inside each, create early bird, first release, second release and final release ticket types; keep only early bird visible, then reveal each later tier on its date or when the previous tier sells out, whichever comes first; set the door opening and last entry on each day ticket to that day; add camping and parking; require names, name checks and ID; allow resale; ask for prices, stock and dates before changing anything"

### Take pre-registrations before your ticket on-sale

Slug `take-pre-registrations-before-your-on-sale`. Guide: https://www.ticketfairy.com/guides/take-pre-registrations-before-your-on-sale

Take the names of the people who want tickets before you have any to sell, reward them for bringing friends, and open a pre-sale to them ahead of everyone else.

For: Building demand before tickets go on sale.

What an agent can do: Fai can set both ends of the registration window and both ends of the pre-sale window, and report how many people have registered and how many tickets they asked for. She shows you the dates before she saves them. Set the points, the prizes and the pre-sale release yourself.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "For <EVENT NAME>, open pre-registration at 9am on 1 September and close it at 5pm on 7 September, then open the pre-sale at 10am on 8 September and close it at 10pm on 9 September. Show me the dates before you save."

#### Then: Email the people who registered

What an agent can do: Fai can draft the message and send it to the pre-registered audience after you approve it.

Command line:

- Show the event before you message its audience: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Draft an email to everyone pre-registered for <EVENT NAME> telling them the pre-sale is open, and show it to me before sending"

#### Then: Close the pre-sale release

What an agent can do: Close the release in the dashboard when the window ends. Fai, MCP and the command line cannot mark a release sold out.

#### Then: Message registered fans who did not buy

What an agent can do: Build this audience and send the message in the dashboard. Fai, MCP and the CLI cannot create this follow-up audience.

#### Then: Read how the registration went

What an agent can do: Fai can read the pre-registration totals back to you.

Command line:

- Show the event statistics: `ticketfairy event stats <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "For <EVENT NAME>, how many people pre-registered and how many tickets did they ask for"

### Unlock hidden tickets with an access code

Slug `unlock-hidden-tickets-with-an-access-code`. Guide: https://www.ticketfairy.com/guides/unlock-hidden-tickets-with-an-access-code

Keep your event page public with the ticket types hidden, and let buyers see them by entering an access code that carries no discount.

For: Sharing a private ticket sale through one reusable access code.

What an agent can do: Fai, the assistant inside your dashboard, can hide the tickets, create a no-discount access code and close the promotion later. She shows you each change and asks you to approve it before she makes it. You can also complete the whole workflow in the dashboard.

Prompt for Fai: "Find my event by name. Keep <TICKET NAMES> active, hide them from the public with Always hidden, then create a promotion called <NAME> with access code <CODE>, No Discount, no automatic application, and only those tickets attached. Use <START AND END TIMES OR NO SCHEDULE> and <SHARED LIMIT OR NO LIMIT>. Show me the exact tickets, normal prices, schedule and limit, then ask me to approve the ticket changes and promotion separately"

#### Then: Replace an access code

What an agent can do: Fai can add the replacement code and remove the old one after you confirm the new code works. MCP and the CLI do not manage the hidden-ticket access-code workflow.

Prompt for Fai: "For the access-code promotion <PROMOTION NAME> on <EVENT NAME>, add <NEW CODE>. Keep <OLD CODE> active until I confirm the replacement works, then ask before removing the old code"

#### Then: Close every access code on the promotion

What an agent can do: Fai can delete the promotion after showing you its codes and hidden tickets. MCP and the CLI do not close this access-code workflow.

Prompt for Fai: "Show me the access-code promotion <PROMOTION NAME> on <EVENT NAME>, including its codes and hidden tickets, then ask before deleting the promotion"

### Use Freefund to reduce no-shows at free and RSVP events

Slug `reduce-no-shows-at-free-rsvp-events`. Guide: https://www.ticketfairy.com/guides/reduce-no-shows-at-free-rsvp-events

Keep entry free for people who show up while refundable deposits give attendees a reason to attend.

For: Planning attendance, staffing, stock and sponsor expectations for a free event.

What an agent can do: Fai can turn Freefund on for all admission tickets or one admission ticket type, set a relative or specific cutoff and show exactly what is charged before asking you to approve it. The approval records your confirmation.

Prompt for Fai: "Set up Freefund for my event. Ask if it should cover all admission tickets or one admission ticket type, what deposit to use and when check-in stops earning it back"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
