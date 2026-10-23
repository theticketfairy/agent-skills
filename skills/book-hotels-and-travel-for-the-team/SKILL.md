---
name: book-hotels-and-travel-for-the-team
description: "Hold hotel rooms, share rooming lists, plan pickups and book travel for artists and crew in Ticket Fairy. Use when an organiser looks after where the team stays and how it travels."
---

# Book hotels and travel for the team

This skill covers hotel blocks, rooming lists, pickups and travel bookings on Ticket Fairy. It lists the 6 published guides for this area and what an agent can do for each one.

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

- [Book hotels and flights for your event team](#book-hotels-and-flights-for-your-event-team)
- [Give your event's unused hotel rooms back before the release date](#give-your-events-unused-hotel-rooms-back-before-the-release-date)
- [Hold hotel rooms for your event's artists and crew](#hold-hotel-rooms-for-your-events-artists-and-crew)
- [Keep track of where your event's artists and crew are staying](#keep-track-of-where-your-events-artists-and-crew-are-staying)
- [Plan your artists' pickups with drivers and vehicles for your event](#plan-your-artists-pickups-with-drivers-and-vehicles-for-your-event)
- [Share your event's rooming lists with hotels and pickups with drivers](#share-your-events-rooming-lists-with-hotels-and-pickups-with-drivers)

### Book hotels and flights for your event team

Slug `book-hotels-and-flights-for-your-event-team`. Guide: https://www.ticketfairy.com/guides/book-hotels-and-flights-for-your-event-team

Search near your event venue, choose a hotel room or flight fare, enter who is travelling and hold the price. Then review the total, pay and share the trip. Your team can see every booking and its history afterwards.

For: Booking a hotel or flight for someone working at your event.

What an agent can do: Fai can search near your venue, compare every room of a hotel or every fare of a flight, enter traveller details and a bed preference, and hold a price. She explains what guests say, the hotel's important information and any security deposit. She shows you the exact booking or change for approval, then opens your booking so you can pay. Card details stay with you.

Prompt for Fai: "Find a hotel near <EVENT NAME> for two crew members arriving the day before. Show me the rooms, what guests say, the total and cancellation terms before holding a price."

#### Then: Find a booking and see what changed

What an agent can do: Fai reads your team bookings with the lead traveller and who booked each one, and explains who changed a booking and how the total changed.

Prompt for Fai: "Show the booking and seats and bags history for <BOOKING> on <EVENT NAME>."

#### Then: Remove a booking that never held a price

What an agent can do: Fai removes a booking that never held a price from the list after you approve it, and can put it back.

Prompt for Fai: "Remove the test hotel booking that never held a price from <EVENT NAME>."

#### Then: Correct the hotel booking contact

What an agent can do: Fai reads the current hotel contact, shows your exact correction for approval and checks the outcome of the same request.

Prompt for Fai: "Show the current hotel booking contact for <BOOKING> and help me correct its email address."

#### Then: Review and cancel a booking

What an agent can do: Fai reads the current cancellation estimate and asks you to approve that quote before requesting cancellation.

Prompt for Fai: "Review cancellation of <BOOKING> on <EVENT NAME>. Show charges and the possible refund before I decide."

#### Then: Report your event travel costs

What an agent can do: Fai prepares your event travel cost report after you approve the filters, checks its status and helps you download or cancel it.

Prompt for Fai: "Prepare an event travel costs report for <EVENT NAME> from <START DATE> through <END DATE>. Show me the filters before starting."

### Give your event's unused hotel rooms back before the release date

Slug `give-unused-hotel-rooms-back-before-the-release-date`. Guide: https://www.ticketfairy.com/guides/give-unused-hotel-rooms-back-before-the-release-date

Give the empty rooms in your event's hotel block back to the hotel before its release date, keep enough rooms for the acts still without one, record why for your team and email the hotel which rooms go back. In the two weeks before the date, Fai suggests giving the empty rooms back, or asking the hotel for more rooms when your acts need them.

For: Giving empty hotel block rooms back before the hotel takes them back.

What an agent can do: Fai gives the empty rooms in a block back to the hotel, keeping the number of rooms a night you ask for, with your reason, and emails the hotel when the block has the contact's email. She shows you the rooms that go back and waits for your yes first.

Prompt for Fai: "Give the empty rooms at Hotel Lumen back for <EVENT NAME>, keep 2 a night for acts still without a room, and email the hotel"

### Hold hotel rooms for your event's artists and crew

Slug `hold-hotel-rooms-for-your-artists-and-crew`. Guide: https://www.ticketfairy.com/guides/hold-hotel-rooms-for-your-artists-and-crew

Record the rooms a hotel holds for your event's acts and crew as a hotel block, with the nights, the rooms each night, the rate in its own currency and the release date. As you give people their stays, the block counts the filled rooms night by night, lists the acts still without a room and warns you as the release date gets close.

For: Holding hotel rooms for the acts and crew on your event.

What an agent can do: Fai reads each block's rooms held, filled and left night by night and the acts still without a room, adds a block, changes its rooms, rate, release date or hotel contact, counts a stay in a block, and closes, reopens or removes one. She shows you each change and waits for your yes first.

Prompt for Fai: "Add a hotel block at Hotel Lumen for <EVENT NAME>: 12 rooms a night from 2 to 4 October at 145 pounds a night, with a release date of 26 September"

#### Then: Change the rooms a block holds

What an agent can do: Fai changes a block's nights or rooms when you ask, with the reason when rooms go back, after you confirm.

Prompt for Fai: "Hold 2 more rooms on 3 October in the Hotel Lumen block for <EVENT NAME>"

#### Then: Change the rate, release date or contact

What an agent can do: Fai changes a block's rate, release date, contact or notes when you ask, after you confirm.

Prompt for Fai: "The Hotel Lumen block for <EVENT NAME> now releases on 30 September, change it"

#### Then: Close, reopen or remove a block

What an agent can do: Fai closes, reopens or removes a block when you ask, after you confirm.

Prompt for Fai: "Close the Harbour Inn crew block for <EVENT NAME>, we are done with it"

### Keep track of where your event's artists and crew are staying

Slug `book-travel-and-accommodation-for-your-artists`. Guide: https://www.ticketfairy.com/guides/book-travel-and-accommodation-for-your-artists

Record each hotel, apartment or house you have booked for your event, assign every artist and crew member to one, and see who still has no room.

For: Housing the artists and crew who work your event.

What an agent can do: Fai adds, changes and removes the hotels and apartments for your artists and crew, and puts a person into one, after you confirm.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Add the Hilton Garden Inn, 12 Dock Street, as a hotel for <EVENT NAME> and put <ARTIST NAME>'s tour manager in it for Friday and Saturday"

#### Then: Handle the changes that always come

What an agent can do: Fai can move a person to another hotel or apartment, and change the dates of their stay, after you confirm.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Move <CREW MEMBER> on <EVENT NAME> to the Hilton Garden Inn for Saturday night and show me before you save it"

### Plan your artists' pickups with drivers and vehicles for your event

Slug `plan-artist-pickups-with-drivers-and-vehicles`. Guide: https://www.ticketfairy.com/guides/plan-artist-pickups-with-drivers-and-vehicles

Give each airport and hotel pickup for your event a driver, a vehicle, a drive time and room for the bags, with a warning before you save when a driver is double booked, on a shift, short of rest or the vehicle is too small. When a flight is late, the pickup moves and Fai suggests a new plan. Each driver gets a day sheet on their phone.

For: Getting every artist from the airport to your event on time.

What an agent can do: Fai reads each day's pickups with their plans and warnings, adds, changes or removes a driver or vehicle, plans a pickup, checks a plan before it is saved, marks a flight as late and asks for a new plan. She shows you each change first and waits for your yes, and she texts drivers only when you approve a new plan.

Prompt for Fai: "Plan Kai Rivers' airport pickup at <EVENT NAME> with Sam in Van 2, a 55 minute drive and 3 bags, and tell me if anything clashes"

#### Then: Take a driver or vehicle off the list

What an agent can do: Fai removes a driver or vehicle when you ask, after you confirm.

Prompt for Fai: "Take the minibus off the vehicles list for <EVENT NAME>, it has broken down"

### Share your event's rooming lists with hotels and pickups with drivers

Slug `share-rooming-lists-with-hotels-and-pickups-with-drivers`. Guide: https://www.ticketfairy.com/guides/share-rooming-lists-with-hotels-and-pickups-with-drivers

Send each hotel a live rooming list of the performers and crew staying for your event, with their dates, room types and notes, and give each driver a link to their pickups and shuttle runs for the day. Hotels and drivers open the link without signing in, the hotel's list updates as you change it, and drivers mark each pickup as they go.

For: Keeping hotels and drivers up to date for your event.

What an agent can do: Fai reads each hotel's rooming list and one day's pickups and shuttle runs, sets a guest's room type, rooms and note for the hotel, makes or turns off a hotel or driver link, adds, changes or removes a shuttle, and marks a pickup or a shuttle run. She shows you each change and waits for your yes first. Only owners and admins can put phone numbers and emails on a link.

Prompt for Fai: "Make a rooming list link for Harbour Hotel for <EVENT NAME> without contact details"

#### Then: Turn a link off

What an agent can do: Fai turns a hotel or driver link off when you ask, after you confirm.

Prompt for Fai: "Turn off the driver link for Kev at <EVENT NAME>"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
