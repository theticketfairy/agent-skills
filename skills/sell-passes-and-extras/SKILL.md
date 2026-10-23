---
name: sell-passes-and-extras
description: "Sell Ticket Fairy extras beyond a single event ticket: add-ons sold with tickets, VIP tables and bottle service, hotel rooms and travel for your ticket buyers, and one pass that covers several of your events. Use when an event organiser wants to sell an add-on, a table, a stay or a pass."
---

# Sell passes and extras

This skill covers add-ons, VIP tables, hotel rooms and travel for ticket buyers, and passes that cover several events on Ticket Fairy. It lists the 5 published guides for this area and what an agent can do for each one.

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

- [Offer hotel and flight bookings on your event site](#offer-hotel-and-flight-bookings-on-your-event-site)
- [Sell hotel rooms to your ticket buyers from a hotel block](#sell-hotel-rooms-to-your-ticket-buyers-from-a-hotel-block)
- [Sell one pass that covers several of your events](#sell-one-pass-that-covers-several-of-your-events)
- [Sell parking, camping and merchandise with your tickets](#sell-parking-camping-and-merchandise-with-your-tickets)
- [Sell VIP tables and bottle service through your promoters](#sell-vip-tables-and-bottle-service-through-your-promoters)

### Offer hotel and flight bookings on your event site

Slug `offer-hotel-and-flight-bookings-on-your-event-site`. Guide: https://www.ticketfairy.com/guides/offer-hotel-and-flight-bookings-on-your-event-site

Let visitors book hotels and flights from your event site, suggest dates and arrival airports, and set your own markup when your plan includes it.

For: Offering travel bookings to visitors of your event site.

What an agent can do: Fai can read and change these travel preferences. She shows you the changes and waits for your approval before saving them.

Prompt for Fai: "Offer hotel bookings on <EVENT NAME> and search within 15 km. Show me the changes before saving."

### Sell hotel rooms to your ticket buyers from a hotel block

Slug `sell-hotel-rooms-to-your-ticket-buyers-from-a-hotel-block`. Guide: https://www.ticketfairy.com/guides/sell-hotel-rooms-to-your-ticket-buyers-from-a-hotel-block

Put the rooms a hotel holds for your event on sale at checkout from a hotel block: choose the room, the nights, the rooms each night, the rate buyers pay and the last day they can book. You see how many room nights are booked and still for sale, and the day after the last day to book, the rooms nobody booked go back to the hotel.

For: Selling a hotel's block of rooms to your ticket buyers at checkout.

What an agent can do: Fai reads the blocks for ticket buyers with each night's rooms booked and still for sale, adds a block for a room from the Accommodation page, changes its rooms, rate or last day to book, and gives back rooms nobody booked. She needs an owner or admin to approve these changes, shows you each one and waits for your yes first.

Prompt for Fai: "Hold 30 double rooms at Hotel Lumen for ticket buyers at <EVENT NAME> from 2 to 4 October at 120.50 pounds a night, with 26 September as the last day to book"

#### Then: Give back rooms nobody booked before the last day

What an agent can do: Fai gives back the rooms nobody booked, keeping the rooms on sale you ask for, after an owner or admin confirms.

Prompt for Fai: "Give back the double rooms nobody has booked at Hotel Lumen for <EVENT NAME>, keep 5 a night on sale"

#### Then: Change the rooms or the rate

What an agent can do: Fai changes a block's rooms, rate or last day to book after an owner or admin confirms.

Prompt for Fai: "Make the last day to book the Hotel Lumen double rooms for <EVENT NAME> 30 September"

#### Then: Remove a block added by mistake

What an agent can do: Fai removes a block for ticket buyers after an owner or admin confirms.

Prompt for Fai: "Remove the twin room hotel block for <EVENT NAME>, I added it by mistake"

### Sell one pass that covers several of your events

Slug `sell-a-pass-that-covers-several-events`. Guide: https://www.ticketfairy.com/guides/sell-a-pass-that-covers-several-events

Sell a season pass or a multi-night bundle once, then let the buyer book the nights they want as you announce them.

For: Selling a season ticket or a multi-night bundle across your programme.

What an agent can do: Fai can build the pass, choose the events it covers and read what it has sold. She asks before each change, because a pass is something buyers pay for.

Command line:

- Show the brand's events: `ticketfairy event list`

CLI MCP tools that read: `select_brand`.

Prompt for Fai: "Create a season pass for <BRAND NAME> covering four events, priced at 96, usable until the end of March, and show me the events it would cover before saving"

#### Then: See how many passes you have sold and how many events holders have booked

What an agent can do: Fai can read the roll-up for a pass: how many sold, how many events were booked and how much revenue is still waiting.

Command line:

- Show the brands you can act for: `ticketfairy brand list`

CLI MCP tools that read: `select_brand`.

Prompt for Fai: "For <BRAND NAME>, how many season passes have sold and how many events have been booked with them"

#### Then: Stop selling a pass while the ones already bought still work

What an agent can do: Fai can archive a pass once you confirm it. She asks first, because it takes a product off sale.

Command line:

- Show the brands you can act for: `ticketfairy brand list`

CLI MCP tools that read: `select_brand`.

Prompt for Fai: "Take the last season pass for <BRAND NAME> off sale"

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
- Shipping details turned on, so checkout asks the buyer for a delivery address: `ticketfairy addon update <ADD_ON_ID> --body '{"requireShippingInfo":true}'`

CLI MCP tools that read: `select_brand`, `select_event`, `list_addons`.

CLI MCP tools that make changes (not available with `--read-only`): `create_addon`.

Prompt for Fai: "Add a return shuttle at 12.50 to this event, limited to 250, one per ticket"

#### Then: Take an add-on off sale

What an agent can do: Fai can turn the add-on off after showing you its current price, stock and restrictions. Your own AI assistant can do the same over the MCP server, after your approval in your MCP client.

CLI MCP tools that read: `select_event`, `list_addons`.

CLI MCP tools that make changes (not available with `--read-only`): `update_addon`.

Prompt for Fai: "Find the add-on <ADD-ON NAME> on <EVENT NAME>. Show me its current price, stock and ticket restrictions, then ask before turning it off"

#### Then: Change an add-on that is on sale

What an agent can do: Fai can show the existing add-on and update the fields you choose. Your own AI assistant can update the fields you choose over the MCP server, after your approval in your MCP client, and the CLI can apply exact field changes by ID.

Command line:

- Change an add-on price and stock: `ticketfairy addon update <ADDON_ID> --body '{"price": <PRICE>, "stock": <REMAINING_STOCK>}'`

CLI MCP tools that read: `select_event`, `list_addons`.

CLI MCP tools that make changes (not available with `--read-only`): `update_addon`.

Prompt for Fai: "Find the add-on <ADD-ON NAME> on <EVENT NAME>, show me its price, remaining stock, description and ticket restrictions, then ask what I want to change"

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

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
