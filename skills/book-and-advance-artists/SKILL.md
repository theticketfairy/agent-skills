---
name: book-and-advance-artists
description: "Hold dates, make offers, send contracts, collect riders, advance performers and settle shows in Ticket Fairy. Use when an organiser books artists or speakers for an event."
---

# Book and advance artists

This skill covers holds, offers, contracts, riders, advancing, applications and settlements on Ticket Fairy. It lists the 14 published guides for this area and what an agent can do for each one.

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

- [Advance your performers before the show](#advance-your-performers-before-the-show)
- [Build a dressing-room shopping list from your event's artist riders](#build-a-dressing-room-shopping-list-from-your-events-artist-riders)
- [Fill in each performer's advance for your event from tour books, riders and emails](#fill-in-each-performers-advance-for-your-event-from-tour-books-riders-and-emails)
- [Handle the contract, invoice and riders an artist's agent sends for your event](#handle-the-contract-invoice-and-riders-an-artists-agent-sends-for-your-event)
- [Hold dates for shows at your venue](#hold-dates-for-shows-at-your-venue)
- [Keep rider lists and notes for your event's artists](#keep-rider-lists-and-notes-for-your-events-artists)
- [Make an offer to an artist's agent for your show](#make-an-offer-to-an-artists-agent-for-your-show)
- [Review act and talk applications for your event with your team](#review-act-and-talk-applications-for-your-event-with-your-team)
- [See the all-in cost of each act on your event](#see-the-all-in-cost-of-each-act-on-your-event)
- [Send event document packs to your performers, traders and crew](#send-event-document-packs-to-your-performers-traders-and-crew)
- [Set each performer's guest list, hotel and meal allowances for your event](#set-each-performers-guest-list-hotel-and-meal-allowances-for-your-event)
- [Settle a show with an artist after your event](#settle-a-show-with-an-artist-after-your-event)
- [Show each act their whole stay and what changed](#show-each-act-their-whole-stay-and-what-changed)
- [Track every artist booking for your event](#track-every-artist-booking-for-your-event)

### Advance your performers before the show

Slug `advance-your-performers-before-the-show`. Guide: https://www.ticketfairy.com/guides/advance-your-performers-before-the-show

Collect each performer's travel, hotel, schedule, technical and hospitality needs for your event, let their agent or tour manager fill in their part from a link with no sign-in, and sign each advance off when everything is confirmed.

For: Getting every performer's details agreed before show day.

What an agent can do: Fai reads every advance, fills in empty answers from the booking and documents, changes a section's answers or status, leaves out a section the act does not need or sets its due date, adds contacts, emails a contact the link to their part and signs an advance off or reopens it. She shows you each change or email and waits for your yes first, and she never shows the link itself in the conversation.

Prompt for Fai: "Which performers at <EVENT NAME> still have their advance open, and send Bicep's tour manager a link to fill in their travel and technical sections"

#### Then: Reopen a signed-off advance

What an agent can do: Fai reopens a signed-off advance when you ask, after you confirm.

Prompt for Fai: "Reopen Bicep's advance for <EVENT NAME>, their flights have changed"

#### Then: Stop a link

What an agent can do: Fai stops a contact's link when you ask, after you confirm.

Prompt for Fai: "Stop the advancing link we sent Bicep's agent for <EVENT NAME>"

### Build a dressing-room shopping list from your event's artist riders

Slug `build-a-dressing-room-shopping-list-from-artist-riders`. Guide: https://www.ticketfairy.com/guides/build-a-dressing-room-shopping-list-from-artist-riders

Turn every act's hospitality rider and your standard dressing-room packages into one shopping list for your event, with how much to buy each day and which dressing room it goes to.

For: Buying hospitality for the acts on your event.

What an agent can do: Fai reads the shopping list by item or by day, and adds, changes or takes off an item when you ask. She shows you each change and waits for your yes first. You set up packages and copy another act's items in the dashboard.

Prompt for Fai: "What do we need to buy for the dressing rooms at <EVENT NAME> on Saturday?"

### Fill in each performer's advance for your event from tour books, riders and emails

Slug `fill-in-advances-from-tour-books-riders-and-emails`. Guide: https://www.ticketfairy.com/guides/fill-in-advances-from-tour-books-riders-and-emails

Let Fai read an act's tour book, rider, their team's email replies and last year's advance, and suggest each answer for their advance for your event, with the words she found it in. You accept, replace or reject each answer, and nothing a person entered is overwritten without you saying so.

For: Filling in performer advances from what their team sends you.

What an agent can do: Fai lists the answers waiting on an act's advance with where each came from, and accepts, replaces or rejects them when you tell her which, after you confirm. She never replaces a person's answer unless you ask for that answer by name. She cannot add a file for you; select Add a tour book or rider in the dashboard for that.

Prompt for Fai: "Which answers did you find for Bicep's advance at <EVENT NAME>, and accept the ones that fill empty questions"

### Handle the contract, invoice and riders an artist's agent sends for your event

Slug `handle-the-contract-invoice-and-riders-an-agent-sends-back`. Guide: https://www.ticketfairy.com/guides/handle-the-contract-invoice-and-riders-an-agent-sends-back

Once an agent answers your offer, Fai finds their contract, invoice and riders in your email or in files you add, and says what each one is. Compare their contract with your offer and upload the countersigned copy, put their invoice into payments due, and send their riders to the act's advance, and see one next step for every act on your event.

For: Getting every act's paperwork from their agent sorted.

What an agent can do: Fai lists each act's files from their agent and the next step, checks your email for new ones, confirms what a file is or sets it aside, reads one again, puts an invoice into payments due, sends a rider to the advance and puts the offer's or a file's terms on the booking. She shows you each change first and waits for your yes. She cannot upload a file; select Add a file or Upload the signed copy in the dashboard for those.

Prompt for Fai: "What is still missing from the agents for <EVENT NAME>, and add Nova Lights' deposit invoice to payments due"

#### Then: Bring back a file you set aside

What an agent can do: Fai brings back a file you set aside when you ask, after you confirm.

Prompt for Fai: "Bring back the Nova Lights invoice I set aside for <EVENT NAME>"

### Hold dates for shows at your venue

Slug `hold-dates-for-shows-at-your-venue`. Guide: https://www.ticketfairy.com/guides/hold-dates-for-shows-at-your-venue

Hold a date on your rooms and stages for an artist, promoter or client, see every hold in queue order on one calendar, challenge the first hold when you need the date, and confirm the date once the event is agreed.

For: Keeping first, second and third holds on your rooms in order.

What an agent can do: Fai reads your calendar and holds, places a hold, challenges or confirms the first hold and releases a hold when you ask. She shows you each change and waits for your yes before she makes it.

Command line:

- List the events, holds and offers in a date range, with each space id: `ticketfairy event-os venue calendar --brand <BRAND_ID> --from 2026-11-01 --to 2026-11-30`
- Place a hold on a space. The answer says which place in the queue it took: `ticketfairy event-os venue holds place --brand <BRAND_ID> --space <SPACE_ID> --starts-on 2026-11-14 --hold-for "<ARTIST NAME>"`
- List the holds that are still held: `ticketfairy event-os venue holds list --brand <BRAND_ID> --status hold`
- Confirm the first hold and keep the holds behind it as backups. This changes the booking and asks you first unless you add --force: `ticketfairy event-os venue holds confirm <HOLD_ID> --brand <BRAND_ID> --lower-holds keep`
- Release a hold, so the holds behind it move up. This asks you first unless you add --force: `ticketfairy event-os venue holds release <HOLD_ID> --brand <BRAND_ID> --reason "<REASON>"`

CLI MCP tools that read: `get_venue_operations`.

CLI MCP tools that make changes (not available with `--read-only`): `place_venue_hold`, `decide_venue_hold`.

Prompt for Fai: "Hold Saturday 14 November in the Main Room for <ARTIST NAME> and tell me which hold we are"

#### Then: Release a hold you no longer need

What an agent can do: Fai releases a hold when you ask, after she shows you which hold it is and you say yes.

Command line:

- Release a hold. This asks you first unless you add --force: `ticketfairy event-os venue holds release <HOLD_ID> --brand <BRAND_ID> --reason "<REASON>"`

CLI MCP tools that read: `get_venue_operations`.

CLI MCP tools that make changes (not available with `--read-only`): `decide_venue_hold`.

Prompt for Fai: "Release the hold for <NAME> on <DATE> in the <SPACE NAME>, the tour has moved"

#### Then: Change a hold's details

What an agent can do: Fai changes who a hold is for, its times, contact, lapse date, event or notes after you confirm.

Prompt for Fai: "Change the hold for <NAME> on <DATE> to lapse on <NEW DATE>"

### Keep rider lists and notes for your event's artists

Slug `keep-rider-lists-and-notes-for-your-artists`. Guide: https://www.ticketfairy.com/guides/keep-rider-lists-and-notes-for-your-artists

List what each artist's rider asks for, tick each item off as it is sorted, and keep your team's notes on the artist in the same place, so every rider is sorted before your event.

For: Getting every artist's rider sorted before show day.

What an agent can do: Fai reads an artist's rider items and notes, adds or ticks off items and adds notes when you ask. She shows you each change and waits for your yes first.

Prompt for Fai: "Add "Car from Heathrow on 7 Oct" to Bicep's hospitality rider for <EVENT NAME>, and tell me what on their rider is still to do"

#### Then: Add a day to the schedule

What an agent can do: Fai adds a day and its opening hours to the event when you ask, after you confirm.

Prompt for Fai: "Add Sunday 9 October to <EVENT NAME>, open from 14:00 to 23:00"

#### Then: File a document under an artist

What an agent can do: Fai files a document under the artist and part of the booking it belongs to, archives it or restores it, after you confirm.

Prompt for Fai: "File the rider I uploaded for Bicep under their hospitality on <EVENT NAME>"

### Make an offer to an artist's agent for your show

Slug `make-an-offer-to-an-artists-agent`. Guide: https://www.ticketfairy.com/guides/make-an-offer-to-an-artists-agent

Build an offer for a performer from a template or your last deal, and see what you paid them before and the fee Fai suggests. Email it to their agent, record their counter-offers and book the artist on your event once they accept.

For: Sending offers to agents and turning the accepted ones into bookings.

What an agent can do: Fai creates an offer from a template, a hold or your last deal, drafts the email to the agent, sends it once you have read it, and records their answer, counter-offer included. She asks you before each change and before anything is sent.

Command line:

- Create a draft offer. Nothing is sent: `ticketfairy event-os venue offers create --brand <BRAND_ID> --performer "<ARTIST NAME>" --show-date 2026-11-14 --space <SPACE_ID> --terms '{"currency":"GBP","guarantee_cents":900000}'`
- Get the email Fai drafts for the offer: recipient, subject and message. Nothing is sent: `ticketfairy event-os venue offers draft-email <OFFER_ID> --brand <BRAND_ID>`
- Email the offer to the agent. This sends an email and asks you first unless you add --force: `ticketfairy event-os venue offers send <OFFER_ID> --brand <BRAND_ID> --to <AGENT_EMAIL> --subject "<SUBJECT>" --message "<MESSAGE>"`
- Record that the agent asked for different terms, as a new version: `ticketfairy event-os venue offers record-reply <OFFER_ID> --brand <BRAND_ID> --reply countered --terms '{"guarantee_cents":1000000}'`
- Record that the agent accepted. On an offer linked to an event, this also books the artist on it: `ticketfairy event-os venue offers record-reply <OFFER_ID> --brand <BRAND_ID> --reply accepted`

CLI MCP tools that read: `get_venue_operations`.

CLI MCP tools that make changes (not available with `--read-only`): `manage_venue_offer`, `send_venue_offer`.

Prompt for Fai: "Make an offer to <ARTIST NAME> for Saturday 14 November in the Main Room, start from what we paid them last time, and show me the email to their agent before you send it"

#### Then: Save an offer as a template

What an agent can do: Fai saves an offer as a template, and adds, changes or removes templates, after you confirm.

Prompt for Fai: "Save the offer to <ARTIST NAME> as a template called <TEMPLATE NAME>"

#### Then: Withdraw an offer

What an agent can do: Fai withdraws an offer after she shows you which one and you say yes.

Prompt for Fai: "Withdraw our offer to <ARTIST NAME> for <DATE>"

### Review act and talk applications for your event with your team

Slug `review-act-and-talk-applications-with-your-team`. Guide: https://www.ticketfairy.com/guides/review-act-and-talk-applications-with-your-team

Collect act and talk applications in one list with Fai's notes and a score from each reviewer, who scores from their own link with no sign-in. When you accept one, we add it to your event with a draft offer or an agenda session.

For: Choosing the acts and speakers for your event with a review panel.

What an agent can do: Fai lists the applications with her notes, the reviewers' scores and possible repeats, scores one for you, moves or declines one, accepts one, and adds, emails, stops or removes a reviewer's link. She shows you each change first and waits for your yes, and she never shows a reviewer's link in the conversation.

Prompt for Fai: "Which talk proposals for <EVENT NAME> have the best reviewer scores, and accept Designing for door staff for Saturday at 11 in the Main Hall"

#### Then: Decline or move an application

What an agent can do: Fai declines or moves an application with your reason, after you confirm. Nobody is emailed.

Prompt for Fai: "Decline the lightning talk about ticket scanning for <EVENT NAME>, we already have one on that"

#### Then: Stop a reviewer's link

What an agent can do: Fai stops, sends again or removes a reviewer's link, after you confirm.

Prompt for Fai: "Stop Sam Lee's review link for <EVENT NAME>"

### See the all-in cost of each act on your event

Slug `see-the-all-in-cost-of-each-act-on-your-event`. Guide: https://www.ticketfairy.com/guides/see-the-all-in-cost-of-each-act-on-your-event

See what one act really costs on its performer page: the fee, the agency fee, travel, the hotel stay, per diems, backline and their share of hire, with one total for each currency. Enter what a trip cost or the room rate of a stay where they are missing, and the same figures reach your budget and the show's settlement.

For: Knowing what each act on your event costs in total.

What an agent can do: Fai reads an act's all-in cost with every part and where it comes from, and enters the cost of a trip or the room rate of a stay when you ask. She shows you the change and waits for your yes first.

Prompt for Fai: "What does <ARTIST NAME> cost us all in at <EVENT NAME>? Their outbound flight cost 320 euros"

### Send event document packs to your performers, traders and crew

Slug `send-document-packs-to-your-performers-traders-and-crew`. Guide: https://www.ticketfairy.com/guides/send-document-packs-to-your-performers-traders-and-crew

Put together what one kind of contact needs for your event, such as the site rules, the map, their own day sheet, their contract and their rider, and send it to all of them in one step. Each person gets an email with their own link, opens their pack with no sign-in, and sees their own day sheet and contract. You see who got it and who opened it, share one person's link with a QR code, and stop a link at any time.

For: Sending performers, traders, suppliers and crew everything they need for your event.

What an agent can do: Fai reads your packs and who got them, makes or changes a pack, emails it to the people you choose, starts a send that did not start and stops one person's link. She waits for your yes first. Share one person's link or QR code from the dashboard, because that's where you see the link, once.

Prompt for Fai: "Make a performer welcome pack for <EVENT NAME> with the site rules, each performer's own day sheet and their contract, and send it to every booked performer"

#### Then: Share one person's link or QR code

What an agent can do: Get one person's link or QR code in the pack in the dashboard, where you see it once. Fai can email the pack to that person instead.

Prompt for Fai: "Send the performer welcome pack at <EVENT NAME> to <PERFORMER NAME> only"

#### Then: Stop one person's link

What an agent can do: Fai stops one person's link to a pack after you confirm.

Prompt for Fai: "Stop The Tidewater Band's link to the performer welcome pack at <EVENT NAME>"

#### Then: Remove a pack

What an agent can do: Fai removes a pack after you confirm, which stops every link to it.

Prompt for Fai: "Remove the crew pack from <EVENT NAME>"

### Set each performer's guest list, hotel and meal allowances for your event

Slug `set-each-performers-allowances-and-travel-party`. Guide: https://www.ticketfairy.com/guides/set-each-performers-allowances-and-travel-party

Give every act on your event's line-up its guest list places, hotel rooms and nights, and meals and drinks a day, taken from the accepted offer, and keep one travel party list that passes, the hotel and the kitchen all use.

For: Agreeing what each act gets at your event.

What an agent can do: Fai reads an act's allowances, what is used and left, their asks for more and the travel party. She sets an allowance or uses the numbers from the accepted offer, approves an ask or says no with your reason, and adds, changes or removes people in the travel party, showing you each change and waiting for your yes.

Prompt for Fai: "Use the numbers from Bicep's accepted offer for their allowances at <EVENT NAME>, and add their tour manager Sam Lee to the travel party with a room"

#### Then: Change or remove a person

What an agent can do: Fai changes or removes a person in the travel party, after you confirm.

Prompt for Fai: "Bicep's drummer is not coming to <EVENT NAME> any more, take them off the travel party"

### Settle a show with an artist after your event

Slug `settle-a-show-with-an-artist`. Guide: https://www.ticketfairy.com/guides/settle-a-show-with-an-artist

Let Fai draft the settlement for a show from its ticket sales, budget costs, the artist's deal and the act's own travel, hotel and agency fee. Check where every figure came from, add or reverse lines, then share it, mark it agreed and mark it paid.

For: Settling a show with the artist's side after the event.

What an agent can do: Fai drafts a show's settlement, brings it up to date, adds or reverses lines, and shares it, marks it agreed or paid, or reopens it, asking you before each change.

Command line:

- List the settlements for one event, with their status and version: `ticketfairy event-os venue settlements list --brand <BRAND_ID> --event <EVENT_ID>`
- Show one settlement with its lines and totals: `ticketfairy event-os venue settlements show <SETTLEMENT_ID> --brand <BRAND_ID>`

CLI MCP tools that read: `get_venue_operations`.

Prompt for Fai: "Draft the settlement for <EVENT NAME> with <ARTIST NAME>'s deal and tell me what is left for us"

#### Then: Correct a settlement after it is shared

What an agent can do: Fai reopens a shared, agreed or paid settlement as a new version after you confirm and give the reason.

Prompt for Fai: "Reopen the settlement for <EVENT NAME>, the bar share was left off"

### Show each act their whole stay and what changed

Slug `show-each-act-their-whole-stay-and-what-changed`. Guide: https://www.ticketfairy.com/guides/show-each-act-their-whole-stay-and-what-changed

Give each performer at your event one list of their whole stay, from their flights and pickup to their hotel, load-in, soundcheck and set, on their day sheet. You see what changed since the act last opened their day sheet link, and they see what changed since they last looked.

For: Keeping each act's travel, hotel and times in one place.

What an agent can do: Fai reads an act's whole stay in order and tells you what changed since the act last opened their day sheet link.

Prompt for Fai: "What has changed in Nova Lights' stay at <EVENT NAME> since they last looked at their day sheet?"

### Track every artist booking for your event

Slug `book-and-brief-your-artists`. Guide: https://www.ticketfairy.com/guides/book-and-brief-your-artists

Keep the contract, the fee, the rider, the hospitality and the travel for every artist on your event together, and see which parts are still missing.

For: Booking artists and getting them to your event ready to play.

What an agent can do: Fai can add an artist's booking, fill in the deal, payment dates, hotel and travel from their contract, and mark a part of the booking finished. She can also tell you how big an artist's audience is on the streaming platforms. She shows each change and waits for your yes.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Read the contract I uploaded for <ARTIST NAME>, add their booking to <EVENT NAME> with the fee, the deposit and when the balance is due, and show me before you save it"

#### Then: Let Fai read the contract for you

What an agent can do: Fai reads a booking contract or invoice and pulls out the terms. Check what she finds against the document before you pay.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Read the invoice for <ARTIST NAME> and tell me what is due, to whom and by when"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
