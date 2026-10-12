---
name: follow-event-type-playbooks
description: "Follow the Ticket Fairy order of work for festivals, club nights, tours, conferences and other event types. Use when an organiser plans a whole event of one type."
---

# Follow event-type playbooks

This skill covers the order of work for festivals, club nights, tours, conferences and more on Ticket Fairy. It lists the 17 published guides for this area and what an agent can do for each one.

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

- [Run a conference on Ticket Fairy](#run-a-conference-on-ticket-fairy)
- [Run ticketing as an agency or promoter group](#run-ticketing-as-an-agency-or-promoter-group)
- [Run ticketing for a charity gala](#run-ticketing-for-a-charity-gala)
- [Run ticketing for a club night](#run-ticketing-for-a-club-night)
- [Run ticketing for a comedy or performing arts show](#run-ticketing-for-a-comedy-or-performing-arts-show)
- [Run ticketing for a concert](#run-ticketing-for-a-concert)
- [Run ticketing for a county, state or renaissance fair](#run-ticketing-for-a-county-state-or-renaissance-fair)
- [Run ticketing for a fan convention](#run-ticketing-for-a-fan-convention)
- [Run ticketing for a food or drink festival](#run-ticketing-for-a-food-or-drink-festival)
- [Run ticketing for a music festival](#run-ticketing-for-a-music-festival)
- [Run ticketing for a nightclub](#run-ticketing-for-a-nightclub)
- [Run ticketing for a university or campus event](#run-ticketing-for-a-university-or-campus-event)
- [Run ticketing for a venue and the promoters who hire it](#run-ticketing-for-a-venue-and-the-promoters-who-hire-it)
- [Run ticketing for an attraction](#run-ticketing-for-an-attraction)
- [Run ticketing for an esports tournament](#run-ticketing-for-an-esports-tournament)
- [Run ticketing for events at your bar or small venue](#run-ticketing-for-events-at-your-bar-or-small-venue)
- [Sell exhibitor stands for a trade show or exhibition](#sell-exhibitor-stands-for-a-trade-show-or-exhibition)

### Run a conference on Ticket Fairy

Slug `run-a-conference`. Guide: https://www.ticketfairy.com/guides/run-a-conference

Set up delegate passes, workshops and a dinner, limit the places in each room, collect every attendee name, and get speakers, press and crew through the door.

For: Running a conference, summit or professional programme.

What an agent can do: Fai, the assistant inside your dashboard, can build the event from the conference template and answer the questions it asks. She shows you the passes and add-ons she means to create before she creates them.

Prompt for Fai: "Set up a two day conference called <EVENT NAME> on <DATES> at <VENUE>, with a student rate and a networking dinner, and show me the passes before you create them"

### Run ticketing as an agency or promoter group

Slug `sell-as-an-agency-or-promoter-group`. Guide: https://www.ticketfairy.com/guides/sell-as-an-agency-or-promoter-group

Run each of your brands with its own team and payouts from one login, build one promoter roster that sells tickets for all of them, give partners their own ticket allocations, and set the commission each promoter earns.

For: Agencies, promoter groups and collectives selling tickets for several brands with one core team and one promoter roster.

What an agent can do: Fai, the assistant inside your dashboard, can list your brands, invite each brand's team, create your collective, invite your promoters, deploy the collective to an event or brand with its commission, give you your invite code, accept a venue's invitation, change what a host can see of your promoters' sales, create a partner's delegation and report each promoter's sales and commission. She shows you each change and asks you to approve it before she makes it. Create each brand in the dashboard, from Brands.

Prompt for Fai: "Set up my promoter collective <COLLECTIVE NAME>, invite <EMAIL ADDRESSES> as members and deploy it to <EVENT NAME> with <COMMISSION> commission; show me each change before you make it"

### Run ticketing for a charity gala

Slug `run-a-charity-gala`. Guide: https://www.ticketfairy.com/guides/run-a-charity-gala

Sell gala seats and whole tables, invoice a company for a block of seats, ask every guest for their meal choice, send sponsors their tickets, let supporters bring friends, email your guests and welcome them at the door.

For: Charity and fundraising teams selling a gala dinner, benefit or awards night by the seat and by the table.

What an agent can do: Fai, the assistant inside your dashboard, can create the gala's seats and tables, add the meal-choice question, draft a company's group booking, send sponsors their guest tickets, set the referral rewards before the first sale, send your guests an email and find a guest at the door. She shows you each change and asks you to approve it first, and asks again before anything is emailed.

Command line:

- Create the individual seat: `ticketfairy ticket create <EVENT_ID> --name "Gala seat" --price 150 --max-inventory 300`
- Create a table of ten paid in full online: `ticketfairy table create <EVENT_ID> --body '{"displayName": "Table of ten", "price": 150000, "maxInventory": 30, "minGuests": 10, "maxGuests": 10, "guestPrice": 0, "depositPercent": 100}'`
- Publish the gala: `ticketfairy event publish <EVENT_ID>`

Prompt for Fai: "For our gala <EVENT NAME>, create individual seats at <SEAT PRICE> and tables of <GUESTS> at <TABLE PRICE>, add a meal choice question each guest answers, and show me everything before you save it"

### Run ticketing for a club night

Slug `run-a-club-night`. Guide: https://www.ticketfairy.com/guides/run-a-club-night

Set up ticket releases, guest lists and VIP tables, track promoter sales, and prepare the venue team for the door.

For: Promoters running a club night with a host venue.

What an agent can do: Fai can start from the Club show template, create or change ticket types and VIP booths, invite promoters, issue guest tickets, send promoter links and publish the event after you approve each change. Follow check-ins and create named tracking links in the dashboard.

Command line:

- Create an early bird ticket release: `ticketfairy ticket create <EVENT_ID> --name "Early Bird" --price 18 --max-inventory 150`
- Publish the event and send each promoter their link: `ticketfairy event publish <EVENT_ID> --send-promoter-links`
- Check entry figures while doors are open: `ticketfairy checkin status <EVENT_ID> --output json`

Prompt for Fai: "Set up my next club night from the Club show template with early bird, advance and on the door tickets, a guest list ticket and VIP booths; ask me for the date, capacity, prices, allocations, booth guest limits and deposit before changing anything; keep the event in draft and show me the finished setup before I publish it"

### Run ticketing for a comedy or performing arts show

Slug `run-a-comedy-or-performing-arts-show`. Guide: https://www.ticketfairy.com/guides/run-a-comedy-or-performing-arts-show

Build the show from the theatre template, price the house by area and release, sell the programme and interval drinks, duplicate the show for every performance, put the run on one page, issue comps for press and cast, and follow arrivals at the door.

For: Selling a run of comedy or theatre performances from announcement to curtain up.

What an agent can do: Fai can build the show from the theatre template, create the house categories and price releases, add the programme and drinks, duplicate the show to every performance, issue guest tickets and passes, publish on a schedule and report arrivals. She shows you the setup before she creates anything and asks you to approve each change.

Command line:

- Create the stalls release: `ticketfairy ticket create <EVENT_ID> --name "Stalls" --price 32 --max-inventory 180`
- Create the programme add-on: `ticketfairy addon create <EVENT_ID> --name "Programme" --price 5 --quantity 500`
- Publish a performance: `ticketfairy event publish <EVENT_ID>`
- Read arrivals during the show: `ticketfairy checkin status <EVENT_ID> --output json`

Prompt for Fai: "Help me set up ticketing for our run of <SHOW NAME>; ask about our performance dates and times, the areas of the house and their prices, concessions, programme and drinks, comps and press, cast and crew passes and our on-sale date, then show me the proposed setup before changing anything"

### Run ticketing for a concert

Slug `run-a-concert`. Guide: https://www.ticketfairy.com/guides/run-a-concert

Build the show from the Concert template, sell general admission and VIP in releases, hold tickets back for partners, sell merchandise with the ticket, schedule the on-sale, and get comps, crew passes and the door ready for show day.

For: Selling a single concert or gig from announcement to show day.

What an agent can do: Fai can build the show from the Concert template, create the categories and releases with their holds and door times, add the merchandise, switch on names, resale and the waiting list, publish on a schedule, create tracking links, send guest tickets and crew passes, and report arrivals. She shows you the setup before she creates anything and asks you to approve each change.

Command line:

- Create the general admission release with 40 tickets held for the label: `ticketfairy ticket create <EVENT_ID> --name "General admission" --price 35 --max-inventory 1200 --holds-enabled --hold "40:Label allocation"`
- Create the VIP ticket: `ticketfairy ticket create <EVENT_ID> --name "VIP package" --price 85 --max-inventory 120`
- Create the merchandise add-on: `ticketfairy addon create <EVENT_ID> --name "Tour T-shirt" --price 25 --quantity 300`
- Publish the show: `ticketfairy event publish <EVENT_ID>`
- Read arrivals while the doors are open: `ticketfairy checkin status <EVENT_ID> --output json`

Prompt for Fai: "Help me set up ticketing for our concert <SHOW NAME> on <DATE>; start from the Concert template, ask me about the capacity, general admission and VIP prices, releases, holds for the label and partners, merch, comps for the artist's guests, crew passes and our on-sale time, then show me the proposed setup before changing anything"

### Run ticketing for a county, state or renaissance fair

Slug `run-a-fair`. Guide: https://www.ticketfairy.com/guides/run-a-fair

Sell adult, concession and family admission to a county, state or renaissance fair, let a season pass in once a day, sell rides, parking and grandstand seats with the ticket, and get exhibitors, vendors and crew in on every day of the fair.

For: Selling admission to a county, state, agricultural or renaissance fair.

What an agent can do: Fai can build the fair from the Exhibition template, set the season pass to one entry a day, add rides, parking and grandstand seats, issue and send exhibitor passes, create the hidden Exhibitor ticket type and a delegation for a club or school, schedule the on-sale and report arrivals. She shows you each change and asks you to approve it before she makes it. Time slots and exhibitor applications are set up in the dashboard.

Command line:

- Create a season pass that admits its holder once in each 24 hours: `ticketfairy ticket create <EVENT_ID> --name "Season pass" --price 45 --max-inventory 2000 --scan-rule "day:1"`
- Create a free Exhibitor ticket type that never shows on your public event page and admits its holder once in each 24 hours: `ticketfairy ticket create <EVENT_ID> --name "Exhibitor" --price 0 --max-inventory 1000 --hidden --hiding-option always_hidden --scan-rule "day:1"`
- Create the ride wristband add-on: `ticketfairy addon create <EVENT_ID> --name "Unlimited ride wristband" --price 30 --quantity 5000`
- Publish the fair: `ticketfairy event publish <EVENT_ID>`
- Read arrivals for each day of the fair: `ticketfairy checkin status <EVENT_ID> --breakdown dates --output json`

Prompt for Fai: "Help me set up ticketing for our fair <EVENT NAME>; ask about our opening days, adult, concession and family prices, a season pass, rides, parking and grandstand shows, exhibitors and vendors, and our on-sale date, then show me the proposed setup before changing anything"

### Run ticketing for a fan convention

Slug `run-a-fan-convention`. Guide: https://www.ticketfairy.com/guides/run-a-fan-convention

Build a comic, anime or gaming convention from the Convention template, group weekend and day passes, let a weekend pass in once a day, sell extras and exhibitor booths, take artist alley applications, and get guests, press and crew through the door.

For: Selling a comic, anime, gaming or fan convention from announcement to the doors.

What an agent can do: Fai can build the convention from the Convention template, group the passes, set the once-a-day entry rule, add the extras and the exhibitor booth, send guest tickets, issue and send crew passes, schedule the on-sale and report arrivals. She shows you each change and asks you to approve it before she makes it. Artist alley applications are set up on the Forms page in the dashboard.

Command line:

- Create a weekend pass that admits its holder once in each 24 hours: `ticketfairy ticket create <EVENT_ID> --name "Weekend pass" --price 90 --max-inventory 3000 --scan-rule "day:1"`
- Create an extra sold with the pass: `ticketfairy addon create <EVENT_ID> --name "Convention tote" --price 15 --quantity 500`
- Create the exhibitor booth for up to 4 traders, paid in full online. Prices are in the smallest unit of your event currency, so 40000 is 400.00: `ticketfairy table create <EVENT_ID> --body '{"displayName": "Exhibitor booth", "price": 40000, "maxInventory": 60, "minGuests": 1, "maxGuests": 4, "guestPrice": 0, "depositPercent": 100}'`
- Publish the convention: `ticketfairy event publish <EVENT_ID>`
- Read arrivals while the doors are open: `ticketfairy checkin status <EVENT_ID> --output json`

Prompt for Fai: "Help me set up ticketing for our fan convention <EVENT NAME>; ask about our days, weekend, day and VIP prices, child tickets, extras, exhibitor booths, guests, press and crew, and our on-sale date, then show me the proposed setup before changing anything"

### Run ticketing for a food or drink festival

Slug `run-a-food-or-drink-festival`. Guide: https://www.ticketfairy.com/guides/run-a-food-or-drink-festival

Build the festival from a template, give each tasting session its own entry time, sell glasses, tokens and parking with the ticket, take trader applications, issue trader passes, hand sponsors their allocations and follow arrivals at the gate.

For: Food, wine, beer and street food festivals selling entry by session with traders on site.

What an agent can do: Fai, the assistant inside your dashboard, can build the festival from the one-day festival template, add the glass, token and parking add-ons, create a trader pass type and issue the passes, and read arrivals by session. She shows you each change and asks you to approve it first. Time slots and trader application forms are set up in the dashboard.

Command line:

- Create the tasting glass add-on: `ticketfairy addon create <EVENT_ID> --name "Tasting glass" --price 5 --quantity 3000`
- Publish the festival: `ticketfairy event publish <EVENT_ID>`
- Read arrivals by session while the gates are open: `ticketfairy checkin status <EVENT_ID> --breakdown slots --output json`

Prompt for Fai: "Help me set up our one-day food festival <EVENT NAME> on <DATE> at <VENUE>; ask about our ticket tiers, the tasting glass, token card and parking add-ons and our trader passes, then show me the setup before you create anything"

### Run ticketing for a music festival

Slug `run-a-music-festival`. Guide: https://www.ticketfairy.com/guides/run-a-music-festival

Build the event from the festival template, group day and weekend tickets, offer instalments, sell camping with the ticket, keep resale at face value, open each release on time, and accredit your crew, artists, press and partners for the gate.

For: Selling a multi-day music festival from announcement to the gate.

What an agent can do: Fai can build the festival from the template, create the ticket categories and releases, turn on a payment plan, add the camping and travel add-ons, switch on names, ID and resale, publish on a schedule, issue crew passes and report arrivals. She shows you the setup before she creates anything and asks you to approve each change.

Command line:

- Create the first weekend release: `ticketfairy ticket create <EVENT_ID> --name "Weekend - First Release" --price 149 --max-inventory 2000`
- Create the camping add-on: `ticketfairy addon create <EVENT_ID> --name "Weekend Camping" --price 45 --quantity 800`
- Publish the event: `ticketfairy event publish <EVENT_ID>`
- Read arrivals during the festival: `ticketfairy checkin status <EVENT_ID> --output json`

Prompt for Fai: "Help me set up ticketing for our festival; ask about our days, ticket classes and price releases, instalments, camping and travel, resale, crew and press passes and our on-sale date, then show me the proposed setup before changing anything"

### Run ticketing for a nightclub

Slug `run-a-nightclub`. Guide: https://www.ticketfairy.com/guides/run-a-nightclub

Set up one night in full, duplicate it for every date, give your venue team the right access, and see who comes back.

For: Nightclub owners and venue teams running a regular programme of ticketed nights.

What an agent can do: Fai can invite your permanent team, build the reference night, copy it for each new date, publish it and show you who buys across your nights.

Command line:

- Copy the reference night as a draft with its ticket and table types, team, promotions, emails, contacts and FAQs. Enter the start and end as local date and time, such as 2026-10-10T22:00:00; sale windows and door times move by the same number of whole days: `ticketfairy event clone <EVENT_ID> --body '{"data": {"displayName": "<NEW EVENT NAME>", "slug": "", "shortName": "", "startDate": "<NEW START>", "endDate": "<NEW END>", "ticketTypes": true, "team": true, "credentials": false, "preRegistration": false, "promotions": true, "delegations": false, "emailTemplates": true, "contacts": true, "faqs": true}}'`
- Publish the new night: `ticketfairy event publish <EVENT_ID>`
- Check how a night sold: `ticketfairy event stats <EVENT_ID> --metric sales`

Prompt for Fai: "Copy <REFERENCE NIGHT NAME> for our night on <DATE>, keep the ticket types, table packages and door times, and show me the new event before I publish it"

### Run ticketing for a university or campus event

Slug `run-a-university-or-campus-event`. Guide: https://www.ticketfairy.com/guides/run-a-university-or-campus-event

Sell a student ticket that only students can unlock, ask each student for their student number, approve their orders before tickets go out, ask for photo ID at the door, take applications from societies and stallholders, and credit each society rep with the tickets they sell.

For: Students' unions, societies and university events teams selling tickets to campus events.

What an agent can do: Fai can build the event from a template with a student ticket, hide that ticket behind a no-discount access code, add the student number question, turn on order approval and ID at the door, approve or decline a waiting order, invite your society reps and door team, and read the applications on your forms. She shows you each change and asks you to approve it before she makes it, and asks again before she approves or declines an order.

Command line:

- Create a Student ticket that never shows on your public event page until a buyer enters its access code: `ticketfairy ticket create <EVENT_ID> --name "Student" --price 8 --max-inventory 400 --hidden --hiding-option always_hidden`
- Create the full-price ticket: `ticketfairy ticket create <EVENT_ID> --name "Standard" --price 20 --max-inventory 200`
- Publish the event: `ticketfairy event publish <EVENT_ID>`
- Read arrivals for each ticket type on the night: `ticketfairy checkin status <EVENT_ID> --breakdown ticket-types --output json`

Prompt for Fai: "Help me set up <EVENT NAME> on <DATE> for our students' union; ask me about the student and standard prices, how many student tickets there are, the access code for students, the student number question and whether I approve each student order, then show me the proposed setup before changing anything"

### Run ticketing for a venue and the promoters who hire it

Slug `run-a-venue`. Guide: https://www.ticketfairy.com/guides/run-a-venue

Put your venue's page under your brand, give your own team and each hiring promoter the access their job needs, hand partners their ticket allocations, get your door team scanning and compare the ticket sales each promoter brings to your venue.

For: Venue owners and venue teams who put on their own nights and hire the room to outside promoters.

What an agent can do: Fai, the assistant inside your dashboard, can add a section to your venue's page, invite your permanent team to the brand, invite a hiring promoter to one night's team, and read the brand Promoters report and the door figures for you. She shows you each invitation and change and asks you to confirm it first. Proving an address at the venue's own domain stays with you, because that code is what gives the venue's page to your brand.

Command line:

- Publish the night and email everyone on its team their own promoter link: `ticketfairy event publish <EVENT_ID> --send-promoter-links`
- Read the check-in figures while the doors are open: `ticketfairy checkin status <EVENT_ID> --output json`

Prompt for Fai: "Invite <PROMOTER EMAIL> to the team for <EVENT NAME> as an administrator so they can build their night, and show me the invitation before you send it"

### Run ticketing for an attraction

Slug `run-an-attraction`. Guide: https://www.ticketfairy.com/guides/run-an-attraction

Sell attraction tickets by date and time slot with a capacity on every slot, add a season pass for visitors who come back, sell extras with the entry, give your staff a pass and follow arrivals slot by slot.

For: Selling timed entry to an attraction that opens for a season.

What an agent can do: Fai can build the event from the Exhibition template, set the season pass so it admits once a day, add the extras, publish on a schedule, create tracking links, issue staff passes and read arrivals slot by slot. Time slots are set up in the dashboard, and Fai tells you so when you ask. She shows you each change and waits for your approval before she makes it.

Command line:

- Create a season pass that admits its holder once in any 24 hours: `ticketfairy ticket create <EVENT_ID> --name "Season pass" --price 60 --max-inventory 300 --scan-rule "day:1"`
- Create an extra sold with the entry: `ticketfairy addon create <EVENT_ID> --name "Photo package" --price 12 --quantity 500`
- Publish the event: `ticketfairy event publish <EVENT_ID>`
- Read arrivals broken down by time slot: `ticketfairy checkin status <EVENT_ID> --breakdown slots --output json`

Prompt for Fai: "Help me set up ticketing for <ATTRACTION NAME>, open from <FIRST DAY> to <LAST DAY>; start from the Exhibition template with a season pass that lets holders in once a day, ask me about prices, extras, staff passes and our on-sale time, and show me the setup before changing anything"

### Run ticketing for an esports tournament

Slug `run-an-esports-tournament`. Guide: https://www.ticketfairy.com/guides/run-an-esports-tournament

Sell spectator passes for an esports or gaming tournament, take player sign-ups with a form, issue player tickets from a place spectators cannot buy, give teams and crew passes, measure the tickets your stream sells, and check everybody in on the day.

For: Running an esports or gaming tournament with players and a paying crowd.

What an agent can do: Fai can build the tournament from the Convention template, create the hidden player ticket type, add merchandise, send player and press tickets, issue and send team and crew passes, create the tracking link for your stream, schedule the on-sale and report arrivals. She shows you each change and asks you to approve it before she makes it. The player sign-up form is set up and read on the Forms page in the dashboard.

Command line:

- Create a player ticket type that never shows on your public event page: `ticketfairy ticket create <EVENT_ID> --name "Player" --price 0 --max-inventory 64 --hidden --hiding-option always_hidden`
- Create the merchandise add-on: `ticketfairy addon create <EVENT_ID> --name "Tournament jersey" --price 35 --quantity 300`
- Publish the tournament: `ticketfairy event publish <EVENT_ID>`
- Read arrivals for players and spectators separately: `ticketfairy checkin status <EVENT_ID> --breakdown ticket-types --output json`

Prompt for Fai: "Help me set up ticketing for our esports tournament <EVENT NAME>; ask about our player places, spectator prices, merchandise, team and crew passes, press, our stream and our on-sale date, then show me the proposed setup before changing anything"

### Run ticketing for events at your bar or small venue

Slug `run-a-bar-or-small-venue`. Guide: https://www.ticketfairy.com/guides/run-a-bar-or-small-venue

Start each event from a template, keep free RSVPs honest with a refundable deposit, take table bookings, sell tickets on your own website, give your bar staff a door login and turn the people who come into a list you can invite back.

For: Bars, lounges, rooftops, restaurants and small rooms that put on events beside their everyday trade.

What an agent can do: Fai, the assistant inside your dashboard, can start a night from a template, turn on the refundable deposit for free RSVPs, create your table types, copy a night to a new date, invite your door staff and find the people who keep coming back. She shows you each change and asks you to approve it first.

Command line:

- Copy last week's night as a draft with its ticket and table types, team, promotions, emails, contacts and FAQs. Enter the start and end as local date and time, such as 2026-10-10T22:00:00; sale windows and door times move by the same number of whole days: `ticketfairy event clone <EVENT_ID> --body '{"data": {"displayName": "<NEW EVENT NAME>", "slug": "", "shortName": "", "startDate": "<NEW START>", "endDate": "<NEW END>", "ticketTypes": true, "team": true, "credentials": false, "preRegistration": false, "promotions": true, "delegations": false, "emailTemplates": true, "contacts": true, "faqs": true}}'`
- Add a booth that takes a 25% deposit online: `ticketfairy table create <EVENT_ID> --body '{"displayName": "Booth", "price": 20000, "maxInventory": 4, "minGuests": 4, "maxGuests": 6, "guestPrice": 4000, "depositPercent": 25}'`
- Publish the night: `ticketfairy event publish <EVENT_ID>`
- List the people who have bought tickets from your brand: `ticketfairy customer list`

Prompt for Fai: "Set up a free quiz night at <VENUE> on <DATE> for <CAPACITY> people with a <DEPOSIT> refundable deposit on each rsvp, and show me the setup before you create it"

### Sell exhibitor stands for a trade show or exhibition

Slug `sell-exhibitor-stands-for-a-trade-show`. Guide: https://www.ticketfairy.com/guides/sell-exhibitor-stands-for-a-trade-show

Sell each stand package at your trade show, expo or consumer exhibition as its own booking with a deposit, take exhibitor applications, and let every exhibitor name their own stand staff up to the number their package includes.

For: Selling stands and exhibitor passes for a trade show, expo or consumer exhibition.

What an agent can do: Fai can build the show from the Convention template with an exhibitor booth, create each stand package, create the hidden stand staff ticket type, set up a delegation for each exhibitor and report arrivals. She shows you each change and asks you to approve it before she makes it. Exhibitor applications are set up and read on the Forms page in the dashboard.

Command line:

- Create a stand package for a team of up to 4 with a 50% deposit online. Prices are in the smallest unit of your event currency, so 120000 is 1,200.00: `ticketfairy table create <EVENT_ID> --body '{"displayName": "Shell scheme stand", "price": 120000, "maxInventory": 40, "minGuests": 1, "maxGuests": 4, "guestPrice": 0, "depositPercent": 50}'`
- Create a free stand staff ticket type that never shows on your public event page and admits its holder once in each 24 hours: `ticketfairy ticket create <EVENT_ID> --name "Stand staff" --price 0 --max-inventory 400 --hidden --hiding-option always_hidden --scan-rule "day:1"`
- Read arrivals for visitors and stand staff separately: `ticketfairy checkin status <EVENT_ID> --breakdown ticket-types --output json`

Prompt for Fai: "Help me set up exhibitor stands for our trade show <EVENT NAME>; ask about our stand packages, prices, deposits and how many staff each includes, then show me the stand packages and the exhibitor allocations before changing anything"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
