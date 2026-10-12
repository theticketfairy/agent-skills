---
name: run-event-production
description: "Run event production in Ticket Fairy Event Management: budgets, schedules, artists, crew, sponsors, traders, volunteers and compliance. Use when an organiser plans or runs the show itself."
---

# Run event production

This skill covers budgets, schedules, artists, crew, sponsors, traders, volunteers and compliance on Ticket Fairy. It lists the 97 published guides for this area and what an agent can do for each one.

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

- [Add everyone who sends your event form to your volunteers, traders or crew](#add-everyone-who-sends-your-event-form-to-your-volunteers-traders-or-crew)
- [Add shifts to your event rota from a spreadsheet](#add-shifts-to-your-event-rota-from-a-spreadsheet)
- [Add your run of show to your team's calendars](#add-your-run-of-show-to-your-teams-calendars)
- [Advance your performers before the show](#advance-your-performers-before-the-show)
- [Approve or decline accreditation requests for your event](#approve-or-decline-accreditation-requests-for-your-event)
- [Approve the hours your event crew and volunteers worked](#approve-the-hours-your-event-crew-and-volunteers-worked)
- [Ask attendees for feedback after your event](#ask-attendees-for-feedback-after-your-event)
- [Balance your event team's workload](#balance-your-event-teams-workload)
- [Book delivery times for your event and check vehicles in at the gate](#book-delivery-times-for-your-event-and-check-vehicles-in-at-the-gate)
- [Book dressing rooms and plan build and break days for your event](#book-dressing-rooms-and-plan-build-and-break-days-for-your-event)
- [Build a dressing-room shopping list from your event's artist riders](#build-a-dressing-room-shopping-list-from-your-events-artist-riders)
- [Build the running order for your event day](#build-the-running-order-for-your-event-day)
- [Build your event rota and check staff in](#build-your-event-rota-and-check-staff-in)
- [Call your show live on show day](#call-your-show-live-on-show-day)
- [Charge outside teams for the crew meals they eat at your event](#charge-outside-teams-for-the-crew-meals-they-eat-at-your-event)
- [Check accreditation passes in and out at your event staff gates](#check-accreditation-passes-in-and-out-at-your-event-staff-gates)
- [Check in attendees and print name badges at your event registration desk](#check-in-attendees-and-print-name-badges-at-your-event-registration-desk)
- [Check your running order for clashes before show day](#check-your-running-order-for-clashes-before-show-day)
- [Check your traders' takings after your event and invoice their share of sales](#check-your-traders-takings-after-your-event-and-invoice-their-share-of-sales)
- [Choose how your event emails look](#choose-how-your-event-emails-look)
- [Choose what Fai does on your event](#choose-what-fai-does-on-your-event)
- [Choose who approves accreditation requests for your event](#choose-who-approves-accreditation-requests-for-your-event)
- [Collect crew certificates and licences before they work an event shift](#collect-crew-certificates-and-licences-before-they-work-an-event-shift)
- [Collect insurance and certificates from your event's outside teams](#collect-insurance-and-certificates-from-your-events-outside-teams)
- [Compare your ticket sales with your last event](#compare-your-ticket-sales-with-your-last-event)
- [Copy the setup of your last event into your next one](#copy-the-setup-of-your-last-event-into-your-next-one)
- [Draw your event site map and share it](#draw-your-event-site-map-and-share-it)
- [Fill in each performer's advance for your event from tour books, riders and emails](#fill-in-each-performers-advance-for-your-event-from-tour-books-riders-and-emails)
- [Find any performer, stage or day on your event](#find-any-performer-stage-or-day-on-your-event)
- [Find the crew and volunteers who work your events](#find-the-crew-and-volunteers-who-work-your-events)
- [Get hire suppliers to confirm orders and count deliveries for your event](#get-hire-suppliers-to-confirm-orders-and-count-deliveries-for-your-event)
- [Get your traders ready for show day](#get-your-traders-ready-for-show-day)
- [Give crew meals at your event meal desk](#give-crew-meals-at-your-event-meal-desk)
- [Give exhibitors a lead scanner for their booth at your event](#give-exhibitors-a-lead-scanner-for-their-booth-at-your-event)
- [Give your event crew one page for all their shifts](#give-your-event-crew-one-page-for-all-their-shifts)
- [Give your event volunteers their own page and track their hours](#give-your-event-volunteers-their-own-page-and-track-their-hours)
- [Give your event's unused hotel rooms back before the release date](#give-your-events-unused-hotel-rooms-back-before-the-release-date)
- [Hand out accreditation passes at your event desk](#hand-out-accreditation-passes-at-your-event-desk)
- [Hand out radios and kit to your event crew](#hand-out-radios-and-kit-to-your-event-crew)
- [Handle lost property at your event](#handle-lost-property-at-your-event)
- [Handle the contract, invoice and riders an artist's agent sends for your event](#handle-the-contract-invoice-and-riders-an-artists-agent-sends-for-your-event)
- [Handle trader requests to move pitch at your event](#handle-trader-requests-to-move-pitch-at-your-event)
- [Hold dates for shows at your venue](#hold-dates-for-shows-at-your-venue)
- [Hold hotel rooms for your event's artists and crew](#hold-hotel-rooms-for-your-events-artists-and-crew)
- [Issue accreditation passes for your event](#issue-accreditation-passes-for-your-event)
- [Keep a risk register for your event](#keep-a-risk-register-for-your-event)
- [Keep rider lists and notes for your event's artists](#keep-rider-lists-and-notes-for-your-events-artists)
- [Keep the jobs behind your event moving](#keep-the-jobs-behind-your-event-moving)
- [Keep track of where your event's artists and crew are staying](#keep-track-of-where-your-events-artists-and-crew-are-staying)
- [Let department leads approve their team's hours at your event](#let-department-leads-approve-their-teams-hours-at-your-event)
- [Let event staff work a desk from their phone with a desk link](#let-event-staff-work-a-desk-from-their-phone-with-a-desk-link)
- [Let exhibitors follow up their event leads and see their results](#let-exhibitors-follow-up-their-event-leads-and-see-their-results)
- [Let outside teams name their own people for event passes](#let-outside-teams-name-their-own-people-for-event-passes)
- [Let outside teams order kit and equipment for your event](#let-outside-teams-order-kit-and-equipment-for-your-event)
- [Let ticket holders pick the conference sessions they attend](#let-ticket-holders-pick-the-conference-sessions-they-attend)
- [Make an offer to an artist's agent for your show](#make-an-offer-to-an-artists-agent-for-your-show)
- [Message the crew, volunteers and traders working on your event](#message-the-crew-volunteers-and-traders-working-on-your-event)
- [Offer open shifts on your event rota to crew and volunteers](#offer-open-shifts-on-your-event-rota-to-crew-and-volunteers)
- [Place your traders on pitches on your event site map](#place-your-traders-on-pitches-on-your-event-site-map)
- [Plan crew meal times and food needs for your event](#plan-crew-meal-times-and-food-needs-for-your-event)
- [Plan next year's event from your attendee feedback](#plan-next-years-event-from-your-attendee-feedback)
- [Plan your artists' pickups with drivers and vehicles for your event](#plan-your-artists-pickups-with-drivers-and-vehicles-for-your-event)
- [Plan your run of show and who calls it](#plan-your-run-of-show-and-who-calls-it)
- [Publish your event line-up and set times](#publish-your-event-line-up-and-set-times)
- [Raise purchase orders and track what your event owes](#raise-purchase-orders-and-track-what-your-event-owes)
- [Read your event's email in one inbox](#read-your-events-email-in-one-inbox)
- [Recruit volunteers for your event](#recruit-volunteers-for-your-event)
- [Report and handle incidents at your event](#report-and-handle-incidents-at-your-event)
- [Review act and talk applications for your event with your team](#review-act-and-talk-applications-for-your-event-with-your-team)
- [Run a safety induction for everyone who works your event](#run-a-safety-induction-for-everyone-who-works-your-event)
- [Run your event from its Today page](#run-your-event-from-its-today-page)
- [Scan delegates into event sessions at the door and see who came](#scan-delegates-into-event-sessions-at-the-door-and-see-who-came)
- [See the all-in cost of each act on your event](#see-the-all-in-cost-of-each-act-on-your-event)
- [See what your brand spends across its events](#see-what-your-brand-spends-across-its-events)
- [See which event pass holders have arrived and send a pass again](#see-which-event-pass-holders-have-arrived-and-send-a-pass-again)
- [See why tickets and passes were refused at the door](#see-why-tickets-and-passes-were-refused-at-the-door)
- [Sell hotel rooms to your ticket buyers from a hotel block](#sell-hotel-rooms-to-your-ticket-buyers-from-a-hotel-block)
- [Send contracts to many performers, traders or suppliers for your event at once](#send-contracts-to-many-performers-traders-or-suppliers-for-your-event-at-once)
- [Send event document packs to your performers, traders and crew](#send-event-document-packs-to-your-performers-traders-and-crew)
- [Send your event contracts and get them signed online](#send-your-event-contracts-and-get-them-signed-online)
- [Send your event hire lists to suppliers](#send-your-event-hire-lists-to-suppliers)
- [Send your event lists to your team on a schedule](#send-your-event-lists-to-your-team-on-a-schedule)
- [Set each performer's guest list, hotel and meal allowances for your event](#set-each-performers-guest-list-hotel-and-meal-allowances-for-your-event)
- [Set pitch rules and let Fai plan your trader pitches at your event](#set-pitch-rules-and-let-fai-plan-your-trader-pitches-at-your-event)
- [Set up a self-service check-in kiosk for your event](#set-up-a-self-service-check-in-kiosk-for-your-event)
- [Settle a show with an artist after your event](#settle-a-show-with-an-artist-after-your-event)
- [Share a power sheet with your event electrician](#share-a-power-sheet-with-your-event-electrician)
- [Share a private event site map with emergency services and suppliers](#share-a-private-event-site-map-with-emergency-services-and-suppliers)
- [Share day sheets with your event's on-site teams](#share-day-sheets-with-your-events-on-site-teams)
- [Share your event's rooming lists with hotels and pickups with drivers](#share-your-events-rooming-lists-with-hotels-and-pickups-with-drivers)
- [Show each act their whole stay and what changed](#show-each-act-their-whole-stay-and-what-changed)
- [Show now and next on screens backstage and at the side of the stage](#show-now-and-next-on-screens-backstage-and-at-the-side-of-the-stage)
- [Show your traders in a directory on your website](#show-your-traders-in-a-directory-on-your-website)
- [Take food, drink and market trader applications for your event](#take-food-drink-and-market-trader-applications-for-your-event)
- [Take notes on your event calls with Fai](#take-notes-on-your-event-calls-with-fai)
- [Track every artist booking for your event](#track-every-artist-booking-for-your-event)
- [Work out the backline and production to hire for your event](#work-out-the-backline-and-production-to-hire-for-your-event)

### Add everyone who sends your event form to your volunteers, traders or crew

Slug `add-form-applicants-to-your-event-teams`. Guide: https://www.ticketfairy.com/guides/add-form-applicants-to-your-event-teams

Connect a form on your event to your volunteers, traders, press, crew or an act's contacts, match each detail to a question, and every person who sends the form is added to that list in the Event Operating System, with their answers kept on the form.

For: Getting form applicants into the lists your event team works from.

What an agent can do: Fai sets where a form's answers go when she creates or updates the form, and adds one applicant to your Event Operating System list when you ask. She shows you the change and waits for your yes.

Prompt for Fai: "Make the trader form on <EVENT NAME> add every applicant to our traders, and add the applicants who already sent it"

#### Then: Add people who applied before you connected the form

What an agent can do: Fai adds the applicants who sent the form before it was connected, after you confirm.

Prompt for Fai: "Add everyone who already sent the trader form on <EVENT NAME> to our traders"

### Add shifts to your event rota from a spreadsheet

Slug `add-shifts-to-your-event-rota-from-a-spreadsheet`. Guide: https://www.ticketfairy.com/guides/add-shifts-to-your-event-rota-from-a-spreadsheet

Drop the event rota spreadsheet your team already keeps, in CSV or Excel, and Fai reads which column holds the day, the times, the department and the role. You check every row and fix any column before up to 500 shifts are added to your rota in one go.

For: Bringing a rota you planned in a spreadsheet into your event.

What an agent can do: Fai reads rows you paste into the chat as a spreadsheet, shows you each shift and its problems, and adds the ready rows after you confirm. For an Excel file, use the dialog in Shifts.

Prompt for Fai: "Add these shifts to the rota at <EVENT NAME>: <PASTED ROWS WITH A HEADING ROW>"

### Add your run of show to your team's calendars

Slug `add-your-run-of-show-to-your-teams-calendars`. Guide: https://www.ticketfairy.com/guides/add-your-run-of-show-to-your-teams-calendars

Give your production team a calendar link that puts every cue of the run of show in Google Calendar, Apple Calendar or Outlook, for every stage or one. Their calendar app checks it again by itself, so a moved cue moves in their calendar too.

For: Getting the run of show into your production team's own calendars.

What an agent can do: Fai makes a calendar link for every stage or one stage, after you confirm. She never shows a link's address, so copy it from the dashboard.

Prompt for Fai: "Make a calendar link of the whole run of show at <EVENT NAME> for the production team"

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

### Approve or decline accreditation requests for your event

Slug `approve-or-decline-accreditation-requests-for-your-event`. Guide: https://www.ticketfairy.com/guides/approve-or-decline-accreditation-requests-for-your-event

Decide the pass requests your event's approval rules send you, with facts beside each one such as how many passes the group has left, from Approvals in the dashboard or from the link in your email with no sign-in. A declined request carries your reason back to the person who asked, and an approved one goes to the next person or can be issued.

For: Deciding the pass requests that wait for you.

What an agent can do: Fai lists what is waiting for you with the facts beside each request, approves or declines one or up to 100 at once, and emails an approver a fresh decision link. She reads you each request and waits for your yes before she decides. Declining needs a reason, which the person who asked sees.

Prompt for Fai: "What is waiting for my approval at <EVENT NAME>? Approve Jane Smith's press pass and decline Tom Price, the Harbour FM allowance is used up"

#### Then: Decide many requests at once

What an agent can do: Fai approves or declines up to 100 requests at once when you ask, after you confirm.

Prompt for Fai: "Approve every press pass waiting for me at <EVENT NAME>"

#### Then: Decide in someone's place

What an agent can do: Fai decides a step in the named approver's place when an owner or admin asks, with the reason you give, after you confirm.

Prompt for Fai: "Sam is away, approve Jane Smith's press pass at <EVENT NAME> for him"

#### Then: Send an approver a new decision link

What an agent can do: Fai emails an approver a fresh decision link when you ask, after you confirm. She never shows the link itself.

Prompt for Fai: "Send Sam Carter a new link to decide the passes waiting for him at <EVENT NAME>"

### Approve the hours your event crew and volunteers worked

Slug `approve-the-hours-your-crew-and-volunteers-worked`. Guide: https://www.ticketfairy.com/guides/approve-the-hours-your-crew-and-volunteers-worked

Approve each person's hours at your event from the times they were checked in and out of their shifts. Fai checks every line first, so you approve the lines with nothing odd in one go, fix the rest with a reason, and check an agency's invoice against the hours its people worked.

For: Approving worked hours for your crew, agency staff and volunteers.

What an agent can do: Fai reads the hours lines of a day with what she noticed on each, and approves the lines you choose or every line with nothing odd. She tells you how many lines she will approve and waits for your yes first.

Prompt for Fai: "Approve the hours at <EVENT NAME> on Saturday that have nothing odd in them"

#### Then: Check an agency's invoice

What an agent can do: Fai reads the hours by outside team, and sets a shift's outside team and cost per hour after you confirm.

Prompt for Fai: "How many hours did SecureCo's stewards work at <EVENT NAME>, and how many are approved?"

#### Then: Download the hours

What an agent can do: Fai starts the same file of the hours lines you choose after you confirm. You download it from the Hours view, where it waits for 7 days and each download is recorded.

Prompt for Fai: "Give me the approved hours at <EVENT NAME> for SecureCo as a file"

#### Then: Change hours that are already approved

What an agent can do: Fai changes a line's hours with the reason you give, after you confirm, and the line goes back for approval.

Prompt for Fai: "Take 30 minutes off Ana Lima's bar shift on Saturday at <EVENT NAME> for an unpaid break"

### Ask attendees for feedback after your event

Slug `ask-attendees-for-feedback-after-your-event`. Guide: https://www.ticketfairy.com/guides/ask-attendees-for-feedback-after-your-event

Email everyone who checked in at your event a short survey the morning after it ends, in their own language and with their own link, and optionally ask ticket holders who did not come what stopped them. The standard survey already rates your stages, acts, sessions and traders, and you can change the questions and the send time before anything goes out.

For: Asking the people who came to your event what they thought.

What an agent can do: Fai sets up the standard survey, changes its questions and wording, schedules it, stops it before it sends, and closes or reopens it. She shows you each change and waits for your yes first, and she always asks before scheduling, because the survey emails your attendees.

Prompt for Fai: "Set up the feedback survey for <EVENT NAME> and schedule it for the morning after, and also ask the people who did not come"

#### Then: Close or reopen the survey

What an agent can do: Fai closes or reopens a survey when you ask, after you confirm.

Prompt for Fai: "Close the feedback survey for <EVENT NAME>"

### Balance your event team's workload

Slug `balance-your-event-teams-workload`. Guide: https://www.ticketfairy.com/guides/balance-your-event-teams-workload

See how many hours each person on your event team has day by day, from their tasks and their rota shifts, spot anyone over the limit before the week of the event, and move a task to the teammate with the most room in one step when Fai suggests it.

For: Spreading the work across your event team.

What an agent can do: Fai reads each person's task time and rota hours for the next 7 or 14 days, says who is over the daily limit and suggests which tasks to move. Move the task in the dashboard when you agree with her.

Prompt for Fai: "Who on the <EVENT NAME> team is over 8 hours a day in the next two weeks, and which tasks should move?"

### Book delivery times for your event and check vehicles in at the gate

Slug `book-delivery-times-and-check-vehicles-in-at-the-gate`. Guide: https://www.ticketfairy.com/guides/book-delivery-times-and-check-vehicles-in-at-the-gate

Set the times vehicles can arrive at each gate of your event and how many can come each time. Suppliers, contractors and other outside teams book a delivery on their own page and get a code for the gate, and on the day your gate team finds each vehicle by its code or number plate and checks it in and out.

For: Planning deliveries and running the gate for your event.

What an agent can do: Fai reads your arrival times, the deliveries booked and the day at the gate, adds or changes an arrival time, books, moves or cancels a delivery for a team, and checks a vehicle in or out or marks it as not arrived. She shows you each change first and waits for your yes, and the team is emailed only when you say so.

Prompt for Fai: "Add an arrival time at Gate B on Friday 2 October from 8 to 11 for 6 vehicles from outside teams at <EVENT NAME>, then tell me who has booked so far"

#### Then: Book a delivery for a team

What an agent can do: Fai books a delivery for a team with the time and vehicle you give, after you confirm, and emails the team only if you ask.

Prompt for Fai: "Book Northern Staging a delivery at Gate B on Friday morning for their 7.5 tonne truck, plate AB12 CDE, and email them"

#### Then: Move or cancel a delivery

What an agent can do: Fai moves or cancels a delivery that has not arrived, after you confirm.

Prompt for Fai: "Move Northern Staging's delivery K7QX at <EVENT NAME> to the afternoon time at Gate B"

#### Then: Mark a vehicle as not arrived

What an agent can do: Fai marks a vehicle as not arrived once its arrival time has ended, after you confirm.

Prompt for Fai: "Mark delivery K7QX at <EVENT NAME> as not arrived"

### Book dressing rooms and plan build and break days for your event

Slug `book-dressing-rooms-and-plan-build-and-break-days`. Guide: https://www.ticketfairy.com/guides/book-dressing-rooms-and-plan-build-and-break-days

Give every performer at your event a dressing room around their set, with Fai suggesting the whole day's rooms and flagging any overlap, and add the build days before the show and the break days after it to your run of show with the usual load-in, rig, sound check, de-rig and load-out cues.

For: Planning dressing rooms and the days around your show.

What an agent can do: Fai reads your dressing rooms and a day's bookings with any overlaps, suggests a room for every performer, adds, changes or removes rooms, books or cancels a room, saves her plan, and adds a build or break day with the usual cues. She shows you each change and waits for your yes first, and asks before she books a room that overlaps another booking.

Prompt for Fai: "Give every performer on Saturday at <EVENT NAME> a dressing room around their set"

#### Then: Cancel a dressing room booking

What an agent can do: Fai cancels a dressing room booking when you ask, after you confirm.

Prompt for Fai: "Cancel The Harbour's dressing room booking on Saturday at <EVENT NAME>"

### Build a dressing-room shopping list from your event's artist riders

Slug `build-a-dressing-room-shopping-list-from-artist-riders`. Guide: https://www.ticketfairy.com/guides/build-a-dressing-room-shopping-list-from-artist-riders

Turn every act's hospitality rider and your standard dressing-room packages into one shopping list for your event, with how much to buy for each day and which dressing room it goes to. Set up what every dressing room gets once, add it to acts in one step, and print a shopping sheet for each day.

For: Buying hospitality for the acts on your event.

What an agent can do: Fai reads the shopping list by item or by day, and adds, changes or takes off an item when you ask. She shows you each change and waits for your yes first. Packages and copying another act's items are set up in the dashboard.

Prompt for Fai: "What do we need to buy for the dressing rooms at <EVENT NAME> on Saturday?"

### Build the running order for your event day

Slug `plan-your-event-production`. Guide: https://www.ticketfairy.com/guides/plan-your-event-production

Lay out every stage and every set of your event day on one timeline, so you can see every set time and every changeover in one running order.

For: Running the stages and set times on your event day.

What an agent can do: Fai can open the event so you can read the timeline. The running order itself is built and changed in the dashboard today.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open <EVENT NAME> so I can build its running order"

#### Then: Keep the day current as it changes

What an agent can do: Fai can open the event so you can move the set yourself. Set times are changed on the timeline in the dashboard today.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open <EVENT NAME> so I can move a set on its running order"

### Build your event rota and check staff in

Slug `build-your-event-rota-and-check-staff-in`. Guide: https://www.ticketfairy.com/guides/build-your-event-rota-and-check-staff-in

Plan the shifts each team needs across your event, let Fai suggest shifts and the people to fill them, send everyone their own shift times, and check your crew and volunteers in and out at the door on the day.

For: Staffing every team and hour of your event.

What an agent can do: Fai reads the rota, its coverage and clashes, suggests shifts from your expected crowd and people for open places, adds and changes shifts, adds people, sets the rota rules, emails people their own shifts and checks people in or out. She shows you each change and waits for your yes first; only sending shifts emails anyone.

Prompt for Fai: "Which shifts on Saturday at <EVENT NAME> still need people? Suggest volunteers to fill them"

#### Then: Cancel a shift

What an agent can do: Fai cancels a shift or brings one back when you ask, after you confirm.

Prompt for Fai: "Cancel the Sunday pit barrier shift at <EVENT NAME>"

#### Then: Take someone off a shift

What an agent can do: Fai takes someone off a shift when you ask, after you confirm.

Prompt for Fai: "Take Cai Jones off the Saturday bar shift at <EVENT NAME>"

### Call your show live on show day

Slug `call-your-show-live-on-show-day`. Guide: https://www.ticketfairy.com/guides/call-your-show-live-on-show-day

Follow what is on now and next on every stage of your event against the event's own clock, call each cue as it happens, see how late each stage is really running from the times you call, catch a stage up, and report an incident without leaving the page.

For: Running each stage on the day of the show.

What an agent can do: Fai reads what is on now and next on each stage and how late each stage is running, calls a cue standby, live, done or skipped, undoes a call, records or corrects when a cue started or finished, or moves the rest of a stage's day when you ask. She waits for your yes before each call or change.

Prompt for Fai: "Neon Tide is live on the Main Stage at <EVENT NAME>, and move the rest of the Main Stage 10 minutes later"

### Charge outside teams for the crew meals they eat at your event

Slug `charge-outside-teams-for-their-crew-meals`. Guide: https://www.ticketfairy.com/guides/charge-outside-teams-for-their-crew-meals

Charge suppliers, contractors and other outside teams for the meals their people ate at your event's crew catering. The meals are counted from the meal desk, you choose the days, the price per meal and the currency, and the team gets an invoice with a payment page.

For: Recovering the cost of meals your event gives to outside teams.

What an agent can do: Fai lists the meals each outside team ate and what is charged, charges a team for chosen days at your price, tries a failed invoice again and emails an invoice to the team. She waits for your yes before each charge or email, and only an owner or admin can approve them.

Prompt for Fai: "Charge Northern PA Hire for the crew meals they ate at <EVENT NAME> on Friday and Saturday, at 8.50 GBP a meal"

### Check accreditation passes in and out at your event staff gates

Slug `check-passes-in-and-out-at-your-staff-gates`. Guide: https://www.ticketfairy.com/guides/check-passes-in-and-out-at-your-staff-gates

Scan crew, performer and supplier passes at the staff gates of your event so only people whose pass opens that zone, on that day and at that hour, get in. A supervisor can let a refused person through with a reason, and every scan in and out keeps a live count of who is on site and inside each zone.

For: Controlling who goes backstage and into each zone of your event.

What an agent can do: Fai tells you how many people are on site and in each zone, who is inside one zone, a pass's movements and a gate's latest scans. Fai also records a scan in or out for you after you confirm, and lets a refused person through only with your reason.

Prompt for Fai: "How many people are backstage at <EVENT NAME> right now, and who are they?"

### Check in attendees and print name badges at your event registration desk

Slug `check-in-attendees-and-print-badges-at-registration`. Guide: https://www.ticketfairy.com/guides/check-in-attendees-and-print-badges-at-registration

Run the registration desk at your conference, trade show or festival from any browser: scan a ticket or find the attendee by name, email or order number, check them in and print their name badge on an A6 or card printer. A second badge needs a reason, walk-ups buy a ticket from a QR code, and you can share a desk link so volunteers work the desk from their own laptop.

For: Checking attendees in and printing their name badges at registration.

What an agent can do: Fai finds a ticket holder, reads the desk's counts and a badge's print history, checks a ticket in and changes the badge setup, after you confirm. Printing a badge happens in the browser at the desk, so Fai tells you where to print it.

Prompt for Fai: "How many people have checked in at registration for <EVENT NAME> so far, and how many badges were printed again?"

#### Then: Print a second badge

What an agent can do: Print a second badge at the registration desk, where you enter the reason. Fai can read you a person's badge history first.

#### Then: Let volunteers work the desk from a link

What an agent can do: Fai makes a registration desk link after you confirm. Open Desks and links and select **Get a new link** to see its address.

Prompt for Fai: "Make a registration desk link called Registration desk 2 for <EVENT NAME>"

#### Then: Help walk-ups without a ticket

What an agent can do: Show walk-ups the QR code in the Registration view of Desks, then check them in with their new ticket.

### Check your running order for clashes before show day

Slug `check-your-running-order-for-clashes-before-show-day`. Guide: https://www.ticketfairy.com/guides/check-your-running-order-for-clashes-before-show-day

Have Fai check each day of your event's run of show for overlapping sets, short changeovers, an act booked on two stages, flights that land after soundcheck, sets outside a stage's hours or past curfew, and riders a stage cannot meet. Each problem comes with up to two fixes Fai has tried against the rest of the day, which you apply in one tap and can undo.

For: Catching clashes in your running order before show day.

What an agent can do: Fai reads the problems on any day with their fixes, applies a fix after you confirm, changes the timing rules, and drafts each act's and each department's call times for you to approve on Today. She never moves a cue on a locked stage or one already called on the day.

Prompt for Fai: "Check the running order for Saturday at <EVENT NAME> and fix the short changeover on the Main Stage"

#### Then: Set a stage's hours from Stages

What an agent can do: Fai changes a stage's changeover, opening and closing times and closed days when you ask, after you confirm.

Prompt for Fai: "The Big Top at <EVENT NAME> closes at 23:00 and needs 20 minutes between acts"

### Check your traders' takings after your event and invoice their share of sales

Slug `check-trader-takings-and-invoice-a-share-of-sales`. Guide: https://www.ticketfairy.com/guides/check-trader-takings-and-invoice-a-share-of-sales

Collect each trader's takings with their till and card reports after your event, let Fai read the reports and say whether they match, accept the figure or ask the trader about it, and raise the share-of-sales invoice with your minimum and maximum applied.

For: Taking a share of your traders' sales as their pitch fee.

What an agent can do: Fai lists your traders' takings with her reading of their reports and every trader invoice, enters takings for a trader, accepts takings, asks a trader for a corrected figure, reads the reports again and raises the share-of-sales invoice. She shows you each change and waits for your yes first.

Prompt for Fai: "Which traders at <EVENT NAME> sent takings whose reports do not match, and what did Fai read in each"

#### Then: Enter takings a trader gave you on paper

What an agent can do: Fai enters a trader's takings for you after you confirm.

Prompt for Fai: "Enter takings of 4,520 pounds for <BUSINESS NAME> at <EVENT NAME>, from their paper sheet"

#### Then: Ask Fai to read the reports again

What an agent can do: Fai reads a trader's reports again when you ask.

Prompt for Fai: "Read the takings reports from <BUSINESS NAME> at <EVENT NAME> again"

### Choose how your event emails look

Slug `choose-how-your-event-emails-look`. Guide: https://www.ticketfairy.com/guides/choose-how-your-event-emails-look

See a real email from your event exactly as agents, suppliers, crew, approvers and attendees receive it: sent in your brand's name, with your logo, colour and font from your brand kit. Give one event its own logo or colour when it needs a different look, and change it back in one step.

For: Making the emails your event sends look like your brand.

What an agent can do: Fai tells you how your event's emails look and where each part comes from, and gives an event its own logo or main colour, or sets it back to your brand kit. She shows you the change and waits for your yes first.

Prompt for Fai: "Use our festival logo and the colour #1a73e8 for the emails <EVENT NAME> sends"

#### Then: Go back to the brand kit

What an agent can do: Fai sets an event's emails back to your brand kit when you ask, after you confirm.

Prompt for Fai: "Put the emails for <EVENT NAME> back on our brand kit"

### Choose what Fai does on your event

Slug `choose-what-fai-does-on-your-event`. Guide: https://www.ticketfairy.com/guides/choose-what-fai-does-on-your-event

See the work Fai does on her own for one event and the actions she can take when you ask, and turn off any of her work you do not want on that event.

For: Deciding how much of an event's work Fai does on her own.

What an agent can do: Fai opens the event's Management page for you, where you turn her work on or off for the event in Fai config.

Prompt for Fai: "Open the Management page for <EVENT NAME>"

### Choose who approves accreditation requests for your event

Slug `choose-who-approves-accreditation-requests`. Guide: https://www.ticketfairy.com/guides/choose-who-approves-accreditation-requests

Send the passes your event's rules pick out, such as press passes or a contractor's crew, to named people who approve them in order before the pass can go out. Each rule reads as a sentence, the first rule that matches decides who is asked, and a pass that matches no rule goes ahead as it always did.

For: Getting the right people to approve passes before they go out.

What an agent can do: Fai reads your approval rules and adds, changes, turns off, reorders or deletes a rule when you say it as a sentence. She shows you the rule and waits for your yes first. The people she names must be on the event's team.

Prompt for Fai: "At <EVENT NAME>, when passes from press organisations come in, ask Sam Carter, then Jo Patel from security"

#### Then: Change or delete a rule

What an agent can do: Fai changes, turns off or deletes a rule when you ask, after you confirm.

Prompt for Fai: "Turn off the lighting crew approval rule at <EVENT NAME>"

### Collect crew certificates and licences before they work an event shift

Slug `collect-crew-certificates-before-they-work-a-shift`. Guide: https://www.ticketfairy.com/guides/collect-crew-certificates-before-they-work-a-shift

Ask the crew and volunteers on your event's shifts for the certificates and licences the work needs, such as a first aid certificate for medics or a food hygiene certificate for the bar. Each person adds a document once from their My shifts page, it counts at every event of your brand until it expires, and nobody goes on a shift without it unless you give a reason.

For: Making sure everyone on your event's shifts holds the certificates the work needs.

What an agent can do: Fai asks for a document, tells you who on the shifts lacks one or has one to check, marks a document as checked, sends one back with your reason and records a document someone showed you. She waits for your yes before each change. Opening a file is in the dashboard.

Prompt for Fai: "Ask everyone on the medic shifts at <EVENT NAME> for a first aid certificate, and tell me who still needs one"

#### Then: Add a document a person gave you

What an agent can do: Fai records a document you saw, with its expiry date, after you confirm. Add a file in the dashboard.

Prompt for Fai: "I have seen Priya Shah's first aid certificate for <EVENT NAME>, it expires in March 2028, record it"

#### Then: Put someone on a shift without the document

What an agent can do: Fai tells you who lacks a document when she adds people to a shift, and adds them anyway only with the reason you give, after you confirm.

Prompt for Fai: "Put Priya Shah on the Saturday medic shift at <EVENT NAME> anyway, her new certificate is on its way"

#### Then: Stop asking for a document

What an agent can do: Fai stops asking for a document when you ask, after you confirm.

Prompt for Fai: "Stop asking for the food hygiene certificate at <EVENT NAME>"

### Collect insurance and certificates from your event's outside teams

Slug `collect-insurance-and-certificates-from-your-outside-teams`. Guide: https://www.ticketfairy.com/guides/collect-insurance-and-certificates-from-your-outside-teams

Ask your event's suppliers, contractors, caterers and other outside teams for public liability insurance, risk assessments, method statements and safety certificates. Each team adds the file on its own page with no sign-in, Fai reads the expiry date and cover, and you accept the file or ask for changes, with reminders before it is due and before it expires.

For: Getting every outside team's paperwork in before your event.

What an agent can do: Fai lists what you asked outside teams for and where each team stands, asks teams for a new document, changes, closes or removes a request, accepts a file with its expiry date, asks a team for changes, gives a team more time and sends reminders. She shows you each change or email first and waits for your yes. She cannot add a file for a team; select Add their file in the dashboard for that.

Prompt for Fai: "Ask every supplier at <EVENT NAME> for public liability insurance by 1 October, and tell me which teams still owe their risk assessment"

#### Then: Send a reminder now

What an agent can do: Fai emails a reminder to the teams that still owe a document, after you confirm.

Prompt for Fai: "Remind the suppliers who have not sent their insurance for <EVENT NAME>"

#### Then: Give a team more time

What an agent can do: Fai gives one team a later due date, after you confirm.

Prompt for Fai: "Give Northern Staging until Friday to send their insurance for <EVENT NAME>"

#### Then: Add a file a team emailed you

What an agent can do: Fai cannot upload a file. Add it with Add their file, then ask Fai what she read in it.

Prompt for Fai: "What did you read in the insurance Northern Staging sent for <EVENT NAME>"

#### Then: Close or remove a request

What an agent can do: Fai closes, opens again or removes a request, after you confirm.

Prompt for Fai: "Close the gas safety certificate request for <EVENT NAME>, we have everything we need"

### Compare your ticket sales with your last event

Slug `compare-your-ticket-sales-with-your-last-event`. Guide: https://www.ticketfairy.com/guides/compare-your-ticket-sales-with-your-last-event

See how your event is selling against your last edition at the same number of days before the start: tickets sold, share of capacity, last time's total and, after the event, no-shows and how fast people arrived. Ticket Fairy suggests which earlier event to compare with, and you can choose another or turn the comparison off.

For: Checking an on-sale against your last edition.

What an agent can do: Fai reads the comparison with your last edition: tickets sold against last time at the same point, share of capacity, last time's total, and no-shows and arrivals after the event. She also lists the earlier events you can compare with and changes the choice, or turns the comparison off, after you confirm.

Prompt for Fai: "How is <EVENT NAME> selling compared with last year at this point?"

#### Then: Compare with a different event

What an agent can do: Fai lists the earlier events you can compare with and changes the choice after you confirm.

Prompt for Fai: "Compare <EVENT NAME> with <EARLIER EVENT NAME> instead"

#### Then: Turn the comparison off

What an agent can do: Fai turns the comparison off for an event after you confirm.

Prompt for Fai: "Stop comparing <EVENT NAME> with an earlier event"

### Copy the setup of your last event into your next one

Slug `copy-the-setup-of-your-last-event-into-your-next-one`. Guide: https://www.ticketfairy.com/guides/copy-the-setup-of-your-last-event-into-your-next-one

Bring the stages, teams, shifts, passes, site map, kit list, hotel blocks, budget plan, forms and the rest of an earlier event's setup into a new event of the same brand. You see what each part adds before anything is copied, the dates move to the new event, and nothing the new event already has changes.

For: Starting a new edition from the setup of your last one.

What an agent can do: Fai lists the brand's events you can copy from, shows what each part would add, what the new event already has and what is left out, starts the copy of the parts you choose and tells you how it went. She shows you the parts first and waits for your yes before she copies anything.

Prompt for Fai: "Copy the stages, shifts, passes and budget plan from <LAST EVENT NAME> into <EVENT NAME>, and show me what each part adds first"

### Draw your event site map and share it

Slug `draw-your-event-site-map-and-share-it`. Guide: https://www.ticketfairy.com/guides/draw-your-event-site-map-and-share-it

Upload your event's site plan as an image, mark the arena, campsites, stages, bars, toilets, first aid, entrances and routes on it, and let Fai check it for the safety essentials your crowd needs. Your whole team can open the map on any device, and you can publish a map with only the places attendees need on your event page.

For: Planning and sharing where everything is on your event site.

What an agent can do: Fai reads your site map, adds, changes, moves, removes or puts back a place, links it to a stage or a team, places a trader on a pitch, sets the scale and expected attendance, puts a street or satellite map under the plan from the venue address, checks the map for first aid, ways out, water, toilets and accessible viewing, and publishes or takes down the attendee map. She shows you each change and waits for your yes first. Upload the plan itself in the dashboard.

Prompt for Fai: "Check the site map for <EVENT NAME> and tell me what safety essentials are missing for 12,000 people"

#### Then: Remove a place

What an agent can do: Fai removes a place or puts one back when you ask, after you confirm.

Prompt for Fai: "Remove the old car park from the site map for <EVENT NAME>"

#### Then: Take the attendee map down

What an agent can do: Fai takes the attendee map down when you ask, after you confirm.

Prompt for Fai: "Take the attendee site map for <EVENT NAME> off the event page"

### Fill in each performer's advance for your event from tour books, riders and emails

Slug `fill-in-advances-from-tour-books-riders-and-emails`. Guide: https://www.ticketfairy.com/guides/fill-in-advances-from-tour-books-riders-and-emails

Let Fai read an act's tour book, rider, their team's email replies and last year's advance, and suggest each answer for their advance for your event, with the words she found it in. You accept, replace or reject each answer, and nothing a person entered is overwritten without you saying so.

For: Filling in performer advances from what their team sends you.

What an agent can do: Fai lists the answers waiting on an act's advance with where each came from, and accepts, replaces or rejects them when you tell her which, after you confirm. She never replaces a person's answer unless you ask for that answer by name. She cannot add a file for you; select Add a tour book or rider in the dashboard for that.

Prompt for Fai: "Which answers did you find for Bicep's advance at <EVENT NAME>, and accept the ones that fill empty questions"

### Find any performer, stage or day on your event

Slug `find-any-performer-stage-or-day-on-your-event`. Guide: https://www.ticketfairy.com/guides/find-any-performer-stage-or-day-on-your-event

Search your whole event from any part of its Management page, and open one page for a performer, a stage or a show day with their set times, advance, travel, hotel, crew and tasks together.

For: Finding everything about one act, one stage or one show day.

What an agent can do: Fai finds anything on the event by name and reads you the same performer, stage and day pages, so you can ask about an act, a stage or a show day without opening them. She only reads here and changes nothing.

Prompt for Fai: "What is happening on the Main Stage at <EVENT NAME> on Saturday, and what is still missing?"

### Find the crew and volunteers who work your events

Slug `find-the-crew-and-volunteers-who-work-your-events`. Guide: https://www.ticketfairy.com/guides/find-the-crew-and-volunteers-who-work-your-events

Search everyone who has worked or volunteered at any of your events in one People list, see how many shifts each person worked and whether they turned up, add their skills and confirm their age for shifts that need one. Fai suggests skills from the shifts they worked, and nobody is rated.

For: Rebooking the people who have worked your events before.

What an agent can do: Fai searches your brand's People, reads you a person's events, record, skills and age, and adds skills or confirms an age after you confirm.

Prompt for Fai: "Who has worked the bar at our events and always turned up?"

### Get hire suppliers to confirm orders and count deliveries for your event

Slug `get-hire-suppliers-to-confirm-orders-and-count-deliveries`. Guide: https://www.ticketfairy.com/guides/get-hire-suppliers-to-confirm-orders-and-count-deliveries

Give each hire supplier for your event its own page, with no sign-in, where it confirms what you ordered, asks for a change and sends its quote. Fai reads the quote against your list, your crew counts what arrives and goes back, and the purchase order shows any shortfall or damage before you pay the invoice.

For: Working with the suppliers who hire kit to your event.

What an agent can do: Fai reads goods in and out, what your suppliers asked on their page and where each quote stands. She counts goods in or out, undoes a count, accepts or declines a supplier's request, sets which outside team's page shows a supplier, and reads or puts aside a quote, showing you each change first and waiting for your yes. She cannot upload a quote for you; select Add their quote in the dashboard for that.

Prompt for Fai: "What have my hire suppliers asked for on their page at <EVENT NAME>, and what came up short when the staging arrived"

#### Then: Add a quote the supplier emailed you

What an agent can do: Fai cannot upload a file. Upload the quote with Add their quote, then ask Fai what she read in it.

Prompt for Fai: "What did you read in Northern Sound Hire's quote for <EVENT NAME>, and which lines are short"

#### Then: Undo a count

What an agent can do: Fai undoes a count when you ask, after you confirm.

Prompt for Fai: "Undo the last count of stage decks at <EVENT NAME>, it should have been 24"

#### Then: Put a quote aside

What an agent can do: Fai puts a quote aside when you ask, after you confirm.

Prompt for Fai: "Ignore the old Northern Sound Hire quote for <EVENT NAME>, they sent a new one"

### Get your traders ready for show day

Slug `get-your-traders-ready-for-show-day`. Guide: https://www.ticketfairy.com/guides/get-your-traders-ready-for-show-day

Give each approved trader their own page to accept your trading terms, pay their invoice, book a load-in time and upload certificates, chase what is missing, and check every pitch, power and water need before your event.

For: Getting approved traders' paperwork, payments and load-in sorted.

What an agent can do: Fai sets up your trading terms and load-in times, sends a trader their page or a reminder of what is missing, sets a pitch and reads the certificates traders upload. She asks you before anything is sent or changed.

Prompt for Fai: "Which traders at <EVENT NAME> are still missing certificates or have not paid, and send each of them a reminder"

#### Then: Stop a trader page link

What an agent can do: Fai stops a trader's page link after you confirm.

Prompt for Fai: "Stop the trader page link for <BUSINESS NAME> on <EVENT NAME>"

### Give crew meals at your event meal desk

Slug `give-crew-meals-at-your-meal-desk`. Guide: https://www.ticketfairy.com/guides/give-crew-meals-at-your-meal-desk

Run the crew catering counter at your event from each person's pass: scan it, see the meals left today and their dietary needs, and give a meal against their allowance. An extra meal needs the reason and your name, and the kitchen sees how many meals to expect each day with the dietary needs counted.

For: Serving crew and volunteer meals against each person's allowance.

What an agent can do: Fai finds a pass at the meal desk, records a meal or an extra meal with its reason, undoes the last meal, and reads you the kitchen forecast and who ate. She shows you the pass and waits for your yes before she records a meal.

Prompt for Fai: "How many meals should the kitchen expect at <EVENT NAME> tomorrow, and how many are vegetarian or gluten-free?"

#### Then: Give a whole team's meals to one collector

What an agent can do: Fai gives a team's meals to a named collector when you ask, after you confirm, and tells you who was skipped.

Prompt for Fai: "Jo from Northern PA Hire is collecting lunch for their crew at <EVENT NAME>"

#### Then: Give an act's drinks

What an agent can do: Fai gives or undoes a drink for a pass from an act's travel party, after you confirm, and gives one beyond the allowance only with your reason.

Prompt for Fai: "Give one of Nova Lights' crew a drink at <EVENT NAME>, pass code TF-7702-1188"

#### Then: Undo a meal

What an agent can do: Fai undoes a person's last meal today when you ask, after you confirm.

Prompt for Fai: "Undo the meal we gave Ana Ruiz a minute ago at <EVENT NAME>, it was scanned twice"

#### Then: See who ate

What an agent can do: Fai reads you the meals given on a day, the extra meals and who gave them.

Prompt for Fai: "Who was given an extra meal at <EVENT NAME> today, and by whom?"

### Give exhibitors a lead scanner for their booth at your event

Slug `give-exhibitors-a-lead-scanner-for-their-booth`. Guide: https://www.ticketfairy.com/guides/give-exhibitors-a-lead-scanner-for-their-booth

Give each exhibitor's booth staff a lead scanner link that works on their own phone or tablet with no sign-in. Staff scan a visitor's ticket or badge with a USB or Bluetooth scanner, or enter its code, rate the visitor and add notes, and the exhibitor gets the visitor's name, email address and phone number under your event's terms. You see every exhibitor's leads and results, record when a visitor no longer wants contact, and download the leads.

For: Capturing leads at the exhibitor booths at your conference or expo.

What an agent can do: Fai reads every exhibitor's leads and results, adds or removes booth staff, sets an exhibitor's rating words and tracking link, records that a visitor no longer wants contact and removes a lead. She makes a scanner link for you, and its address shows in the dashboard. She waits for your yes before every change.

Prompt for Fai: "How many leads has each exhibitor at <EVENT NAME> captured so far, and which booths have no scanner link yet"

#### Then: Record that a visitor no longer wants contact

What an agent can do: Fai records that a visitor no longer wants contact after you confirm.

Prompt for Fai: "<VISITOR NAME> asked Northwind Audio at <EVENT NAME> not to contact them, record it"

#### Then: Download an exhibitor's leads

What an agent can do: Download the leads from the exhibitor's panel in the dashboard, where the download is recorded with your name.

#### Then: Stop a scanner link

What an agent can do: Fai stops a scanner link after you confirm.

Prompt for Fai: "Stop Lena Brandt's lead scanner link for Northwind Audio at <EVENT NAME>"

### Give your event crew one page for all their shifts

Slug `give-your-crew-one-page-for-all-their-shifts`. Guide: https://www.ticketfairy.com/guides/give-your-crew-one-page-for-all-their-shifts

Email each crew member or volunteer a private My shifts link where they see their shifts at every one of your events, accept the shifts you offer them, say they are still coming, tell you the days they can work and add their shifts to their calendar. Their documents, safety induction and food needs are on the same page, and nobody needs an account.

For: Keeping crew and volunteers up to date on their shifts.

What an agent can do: Fai emails a person their My shifts link or turns their links off when you ask, after you confirm.

Prompt for Fai: "Email Ama Owusu her My shifts link"

#### Then: Turn off their links

What an agent can do: Fai turns off a person's My shifts links when you ask, after you confirm.

Prompt for Fai: "Turn off Leah Grant's My shifts links, she has left the team"

### Give your event volunteers their own page and track their hours

Slug `give-volunteers-their-own-page-and-track-hours`. Guide: https://www.ticketfairy.com/guides/give-volunteers-their-own-page-and-track-hours

Send each volunteer you accepted for your event a private page where they pick shifts, ask to swap or drop one, read their day sheet and the induction and add documents, then see hours given against hours worked, give the rewards people earned and download the list with every download recorded.

For: Looking after accepted volunteers from their first shift to their reward.

What an agent can do: Fai sends volunteers their page links, answers shift requests, reads hours given and worked and gives the rewards people earned. She asks you before anything is sent, and only an owner or admin can approve rewards.

Command line:

- List each volunteer's hours given and worked: `ticketfairy event-os volunteers list <EVENT_ID> --hours`

Prompt for Fai: "Send every accepted volunteer on <EVENT NAME> their page link, and tell me who has earned the free weekend ticket"

#### Then: Download the volunteer list

What an agent can do: Download the list from the Volunteers section in the dashboard, where the download is recorded with your name.

#### Then: Turn off a volunteer's link

What an agent can do: Turn a volunteer's link off or make a new one from their application in the dashboard.

### Give your event's unused hotel rooms back before the release date

Slug `give-unused-hotel-rooms-back-before-the-release-date`. Guide: https://www.ticketfairy.com/guides/give-unused-hotel-rooms-back-before-the-release-date

Give the empty rooms in your event's hotel block back to the hotel before its release date, keep enough rooms for the acts still without one, record why for your team and email the hotel which rooms go back. In the two weeks before the date, Fai suggests giving the empty rooms back, or asking the hotel for more rooms when your acts need them.

For: Giving empty hotel block rooms back before the hotel takes them back.

What an agent can do: Fai gives the empty rooms in a block back to the hotel, keeping the number of rooms a night you ask for, with your reason, and emails the hotel when the block has the contact's email. She shows you the rooms that go back and waits for your yes first.

Prompt for Fai: "Give the empty rooms at Hotel Lumen back for <EVENT NAME>, keep 2 a night for acts still without a room, and email the hotel"

### Hand out accreditation passes at your event desk

Slug `hand-out-accreditation-passes-at-your-desk`. Guide: https://www.ticketfairy.com/guides/hand-out-accreditation-passes-at-your-desk

Run your accreditation desk from the pass list: scan a ticket or badge, or enter a name, check the card with the photo, zones and days, and hand the pass to the holder or to a team lead collecting for their crew. The desk says in plain words what to sort out first, such as a missing badge photo, and records who took each pass and which teammate gave it out.

For: Handing out passes to crew, performers and guests at your accreditation desk.

What an agent can do: Fai finds a pass by its code or by a name, organisation or role, says whether it is ready to collect and what to sort out first, and records a collection, a whole group's collection or an undo. She shows you the pass and waits for your yes before she records anything.

Prompt for Fai: "Is Ana Ruiz's pass ready to collect at <EVENT NAME>? She is here now to collect it"

#### Then: Give out a whole group's passes

What an agent can do: Fai records a group's issued passes as taken by a named collector when you ask, after you confirm, and tells you which passes it left out and why.

Prompt for Fai: "Jo Lead is collecting all the bar crew's passes at <EVENT NAME>"

#### Then: Undo a collection

What an agent can do: Fai undoes a collection when you ask and give a reason, after you confirm.

Prompt for Fai: "Dev Patel's pass at <EVENT NAME> went to the wrong collector, undo it"

### Hand out radios and kit to your event crew

Slug `hand-out-radios-and-kit-to-your-event-crew`. Guide: https://www.ticketfairy.com/guides/hand-out-radios-and-kit-to-your-event-crew

Keep a list of the radios, hi-vis vests, tablets, torches, keys and buggies for your event, hand them out at the kit desk with a scan or a search, and take them back with their condition. See who has what at any moment, keep a radio plan of channels and call signs, and let Fai chase anyone who has not returned their kit after the event.

For: Handing out and getting back your event's radios and kit.

What an agent can do: Fai reads your kit list, who has what, the kit history, the not-returned list and the radio plan, hands kit out or takes it back, adds or changes kit, marks kit as lost and changes channels and call signs. She shows you each change and waits for your yes first. Any member of your event's team can ask Fai to hand out or take back kit; only owners, admins and producers can change the kit list or the radio plan.

Prompt for Fai: "Hand radio R-12 to Ana Silva from security at <EVENT NAME>, due back at midnight"

#### Then: Take lost kit off the list

What an agent can do: Fai takes lost units of a batch off the kit list when you ask, after you confirm.

Prompt for Fai: "Take the 4 hi-vis vests Sam from the bar lost off the kit list at <EVENT NAME>"

### Handle lost property at your event

Slug `handle-lost-property-at-your-event`. Guide: https://www.ticketfairy.com/guides/handle-lost-property-at-your-event

Log every phone, wallet and bag handed in at your event with a photo and a reference, take lost reports from your team or from attendees on a public page, and let Fai spot the found items that may match. Hand each item back with a record of who collected it and how you checked it was theirs.

For: Reuniting attendees with what they lost at your event.

What an agent can do: Fai reads what has been handed in, the lost reports and her possible matches, logs a found item or a lost report, hands an item back with a note of how you checked it was theirs, records an item as gone or undoes it, confirms or dismisses a match, and changes the settings. She shows you each change and waits for your yes first. Any member of your event's team can ask Fai to log an item, take a report or hand an item back.

Prompt for Fai: "Log a found item at <EVENT NAME>: black backpack with a red keyring, found by the main stage bar, kept in box 3 at the info tent"

#### Then: Record items as gone

What an agent can do: Fai records items as gone, or keeps one again, when you ask, after you confirm.

Prompt for Fai: "Record the unclaimed items at <EVENT NAME> as donated to charity"

### Handle the contract, invoice and riders an artist's agent sends for your event

Slug `handle-the-contract-invoice-and-riders-an-agent-sends-back`. Guide: https://www.ticketfairy.com/guides/handle-the-contract-invoice-and-riders-an-agent-sends-back

Once an agent answers your offer, Fai finds their contract, invoice and riders in your email or in files you add, and says what each one is. Compare their contract with your offer and upload the countersigned copy, put their invoice into payments due, and send their riders to the act's advance, with one next step shown for every act on your event.

For: Getting every act's paperwork from their agent sorted.

What an agent can do: Fai lists each act's files from their agent and the next step, checks your email for new ones, confirms what a file is or sets it aside, reads one again, puts an invoice into payments due, sends a rider to the advance and puts the offer's or a file's terms on the booking. She shows you each change first and waits for your yes. She cannot upload a file; select Add a file or Upload the signed copy in the dashboard for those.

Prompt for Fai: "What is still missing from the agents for <EVENT NAME>, and add Nova Lights' deposit invoice to payments due"

#### Then: Bring back a file you set aside

What an agent can do: Fai brings back a file you set aside when you ask, after you confirm.

Prompt for Fai: "Bring back the Nova Lights invoice I set aside for <EVENT NAME>"

### Handle trader requests to move pitch at your event

Slug `handle-trader-requests-to-move-pitch`. Guide: https://www.ticketfairy.com/guides/handle-trader-requests-to-move-pitch

Let traders at your event ask to move pitch from their own trader page, with their reason and where they would like to be. You move them to a free pitch that keeps your pitch rules, or decline with a note, and they see your answer on their page and by email.

For: Answering traders who ask for a different pitch.

What an agent can do: Fai lists the move requests waiting, checks a pitch against your rules, and moves a trader or declines their request with your note, after you confirm.

Prompt for Fai: "Rocket Coffee Van at <EVENT NAME> wants to move, what free pitch would keep our rules?"

#### Then: Decline a request

What an agent can do: Fai declines a move request with the note you give, after you confirm.

Prompt for Fai: "Decline Rocket Coffee Van's move request at <EVENT NAME>, every hard-standing pitch is taken"

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

### Issue accreditation passes for your event

Slug `issue-accreditation-passes-for-your-event`. Guide: https://www.ticketfairy.com/guides/issue-accreditation-passes-for-your-event

Give your crew, performers and their guests, traders' staff, volunteers and press a named pass for your event, with the zones it opens, the days and hours it works, meals and parking. Your door team scans each pass in the same app as your tickets and sees what it allows, and you print photo badges from the same list.

For: Accrediting everyone who works on or visits your event.

What an agent can do: Fai reads your passes, groups, zones and pass types, brings in everyone confirmed elsewhere in the event, sets up zones, pass types and group allowances, adds or changes a pass, issues passes, cancels a pass or issues it again, and makes a photo link for a pass holder. She shows you each change and waits for your yes first. Issuing emails each person their pass, so Fai always asks before she issues anything. Badges are printed in the dashboard.

Prompt for Fai: "Bring in everyone for passes at <EVENT NAME>"

#### Then: Cancel a pass

What an agent can do: Fai cancels a pass and its ticket, or issues a cancelled pass again, when you ask, after you confirm.

Prompt for Fai: "Cancel the pass for Sam Lee at <EVENT NAME>, he is not coming"

#### Then: Decline a request

What an agent can do: Fai declines a pass request or brings one back when you ask, after you confirm.

Prompt for Fai: "Decline the late guest list name for Bicep at <EVENT NAME>"

### Keep a risk register for your event

Slug `keep-a-risk-register-for-your-event`. Guide: https://www.ticketfairy.com/guides/keep-a-risk-register-for-your-event

List what could go wrong at your event, how likely and how bad each risk is and what you are doing about it, start from a draft Fai builds from your event and past incidents, and keep every risk's owner, review date and status current.

For: Keeping your event's risk assessment current.

What an agent can do: Fai reads the register, builds a draft from your event without saving it, adds risks one at a time or many at once, edits them and marks them controlled, accepted, closed or open again. She shows you each change and waits for your yes first; risks are never deleted.

Prompt for Fai: "Draft a risk register for <EVENT NAME>, an outdoor festival for 8,000 people, and show me before you add anything"

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

### Keep the jobs behind your event moving

Slug `keep-your-event-tasks-on-track`. Guide: https://www.ticketfairy.com/guides/keep-your-event-tasks-on-track

Put every job your team has to finish before the event on one board, give each one an owner and a date, and see what is blocked before it becomes a problem.

For: Running the jobs your team has to finish before the doors open.

What an agent can do: Fai can open the event so you can read the board. The tasks themselves are read and moved in the dashboard today.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open <EVENT NAME> so I can go through its tasks"

#### Then: See the same work as a list, a calendar or a timeline

What an agent can do: Fai can open the event. The task views are read in the dashboard today.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open <EVENT NAME> so I can see what is due this week"

### Keep track of where your event's artists and crew are staying

Slug `book-travel-and-accommodation-for-your-artists`. Guide: https://www.ticketfairy.com/guides/book-travel-and-accommodation-for-your-artists

Record each hotel, apartment or house you have booked for your event, assign every artist and crew member to one, and see who still has no room.

For: Housing the artists and crew who work your event.

What an agent can do: Fai can open the event so you can read the list. Where your artists and crew are staying is recorded in the dashboard today.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open <EVENT NAME> so I can check where the crew are staying"

#### Then: Handle the changes that always come

What an agent can do: Fai can open the event. Stays and travel are recorded in the dashboard today.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open <EVENT NAME> so I can move a crew member to another hotel"

### Let department leads approve their team's hours at your event

Slug `let-department-leads-approve-their-teams-hours`. Guide: https://www.ticketfairy.com/guides/let-department-leads-approve-their-teams-hours

Give the lead of each on-site department at your event the job of approving their own team's hours. Leads approve and correct the hours of their department's shifts from their My shifts page, with Fai's checks and no sign-in, and never see costs or their own hours.

For: Sharing hours approval with the leads of your on-site teams.

What an agent can do: Fai adds a person to a department and makes them its lead, after you confirm. The lead approves their team's hours on their own My shifts page.

Prompt for Fai: "Make Dan Price the lead of the Security department at <EVENT NAME>, his email is dan@secureco.example"

### Let event staff work a desk from their phone with a desk link

Slug `let-event-staff-work-a-desk-from-their-phone`. Guide: https://www.ticketfairy.com/guides/let-event-staff-work-a-desk-from-their-phone

Share a desk link so volunteers, caterers and gate staff without a dashboard login can hand out passes, give crew meals, check passes at a staff gate or run registration at your event from their own phone or tablet. Each link opens one desk of one event, everything done through it is recorded under its name, and you can stop it at any time.

For: Giving the staff at your event desks their own desk on their phone.

What an agent can do: Fai lists your event's desk links, and makes, changes or stops one after you confirm. Fai never gives out a link's address: to see it, open Desks and links and select **Get a new link**.

Prompt for Fai: "Make a staff gate desk link called Backstage gate phone for the backstage zone at <EVENT NAME>"

#### Then: Change a link

What an agent can do: Fai changes a link's name, zone, supervisor switch or end date after you confirm.

Prompt for Fai: "Let the Main desk tablet link at <EVENT NAME> work until Monday night"

#### Then: Get a new address for a link

What an agent can do: Fai replaces a link's address after you confirm, so the old address stops working, for example when it was shared by mistake. Fai never gives out the new address: select **Get a new link** in Desks and links when you need to see one.

Prompt for Fai: "The Main desk tablet link at <EVENT NAME> was shared by mistake, replace it so the old one stops working"

#### Then: Stop a link

What an agent can do: Fai stops a desk link after you confirm, for example when a phone goes missing.

Prompt for Fai: "Stop the Crew catering tent desk link at <EVENT NAME>, the phone went missing"

### Let exhibitors follow up their event leads and see their results

Slug `let-exhibitors-follow-up-their-leads-and-see-results`. Guide: https://www.ticketfairy.com/guides/let-exhibitors-follow-up-their-leads-and-see-results

Give each exhibitor a page of its own, with no sign-in, where its team sees the leads from its booth at your event, approves follow-up emails that Fai drafts, gives booth staff scanner links, downloads its leads and sees its results. You make the page from the exhibitor's leads and send the link from Outside teams.

For: Handing exhibitors their leads, follow-up emails and booth results.

What an agent can do: Fai gives an exhibitor its own page, reads its leads, follow-ups and results, and sets a sponsor's page and tracking link. She waits for your yes before every change. Only the exhibitor approves its follow-up emails, on its own page.

Prompt for Fai: "Give Northwind Audio its own page at <EVENT NAME> and tell me how many of its leads can be contacted"

#### Then: Show a sponsor its results

What an agent can do: Fai links a sponsor to its outside team and chooses its tracking link after you confirm.

Prompt for Fai: "Give the sponsor <SPONSOR NAME> at <EVENT NAME> its own page with the <TRACKING LINK NAME> tracking link"

### Let outside teams name their own people for event passes

Slug `let-outside-teams-name-their-own-people-for-passes`. Guide: https://www.ticketfairy.com/guides/let-outside-teams-name-their-own-people-for-passes

Give each security firm, caterer, supplier, press outlet or sponsor working on your event an allowance of passes and a page of their own, with no sign-in, where their contact enters the names, badge photos and email addresses of their people. You see who still owes names, and each person's pass goes through your usual accreditation.

For: Collecting names for passes from the companies working on your event.

What an agent can do: Fai lists your outside teams and who still owes names, adds or changes a team, gives, changes or takes away its passes, and emails its contact the page link. She shows you each change or email and waits for your yes first, and she never shows the link itself in the conversation. A week before names close, Fai also drafts a reminder to each team that still has places left, for you to approve on Today.

Prompt for Fai: "Add Brightline Security as a contractor at <EVENT NAME>, contact Tom Okafor at tom@brightline.example, give them 40 crew passes with names by Friday 6pm, then email Tom the link"

#### Then: Stop a team's page link

What an agent can do: Fai stops a team's page link when you ask, after you confirm.

Prompt for Fai: "Stop the page link for Brightline Security at <EVENT NAME>"

#### Then: Take away a team's passes

What an agent can do: Fai takes an allowance away from a team when you ask, after you confirm. The pass group and its people stay.

Prompt for Fai: "Take the guest passes away from Harbour Catering at <EVENT NAME>"

#### Then: Archive an organisation

What an agent can do: Fai archives an organisation or restores one when you ask, after you confirm.

Prompt for Fai: "Archive the Daily Echo at <EVENT NAME>, they are not covering it this year"

### Let outside teams order kit and equipment for your event

Slug `let-outside-teams-order-kit-and-equipment-for-your-event`. Guide: https://www.ticketfairy.com/guides/let-outside-teams-order-kit-and-equipment-for-your-event

Offer radios, hi-vis vests, buggies and other kit from your event's kit list to contractors, suppliers, press and other outside teams at a price you set. Each team orders from its own page, you approve the order and the kit is held for them, an invoice goes with it, and you hand the kit out and take it back at your event.

For: Renting your event's kit to the outside teams working on it.

What an agent can do: Fai reads your price list, the teams' orders and the pick list, offers a piece of kit or changes its price, limit or last day to order, approves or declines an order, orders for a team, hands an order out, takes it back and makes or emails its invoice. She shows you each change and waits for your yes first. Only owners, admins and producers can change the price list or decide an order.

Prompt for Fai: "Which kit orders from outside teams are waiting for a yes at <EVENT NAME>, and approve Harbour Radio's order and email them the invoice"

#### Then: Decline an order

What an agent can do: Fai declines an order with the reason you give, after you confirm.

Prompt for Fai: "Decline Coastline Catering's buggy order at <EVENT NAME>, all the buggies are with the stage crew that weekend"

#### Then: Cancel an order

What an agent can do: Fai cancels an order that is not handed out yet, after you confirm.

Prompt for Fai: "Cancel order 3 for Harbour Radio at <EVENT NAME>, they are bringing their own radios"

#### Then: Order kit for a team yourself

What an agent can do: Fai places an order for a team with the kit, amounts and dates you give, after you confirm. It then waits for a yes like any other order.

Prompt for Fai: "Order 6 radios and 6 hi-vis vests for Northern Sound Hire at <EVENT NAME> from Friday to Sunday, for the production office"

#### Then: Email an invoice you held back

What an agent can do: Fai makes or emails an approved order's invoice, after you confirm. She also suggests on Today emailing an invoice still waiting to go, and a reminder when one is due in 3 days or overdue.

Prompt for Fai: "Email Harbour Radio the invoice for their kit order at <EVENT NAME>"

### Let ticket holders pick the conference sessions they attend

Slug `let-ticket-holders-pick-the-sessions-they-attend`. Guide: https://www.ticketfairy.com/guides/let-ticket-holders-pick-the-sessions-they-attend

Turn the talks and workshops on your agenda into sessions ticket holders pick on their order page, with a place for each person, a waiting list when a room is full and a warning before two picks clash. Your team can add anyone to a session or give a place back.

For: Letting delegates choose their talks and workshops.

What an agent can do: Fai lists the sessions and the agenda items people cannot pick yet, makes a session from an agenda item or from scratch, and opens it for picking. She shows you each change and waits for your yes first.

Prompt for Fai: "Let ticket holders at <EVENT NAME> pick the sponsor deck workshop, with 40 places and a waiting list"

#### Then: Add a session that is not on your agenda

What an agent can do: Fai adds a session with the details you give and can open it for picking, after you confirm.

Prompt for Fai: "Add a 45 minute pricing clinic at 2pm on day two of <EVENT NAME> in Room B for 25 people"

#### Then: Add a ticket holder to a session or give their place back

What an agent can do: Fai looks up a ticket holder's picks by ticket code or email, adds them to a session and gives a place back, after you confirm each change.

Prompt for Fai: "Add the delegate with ticket code TF8841QX to the sponsor deck workshop at <EVENT NAME>"

#### Then: Change a session

What an agent can do: Fai changes a session's title, track, room, description or waiting list, and its time and places while nobody has picked it, after you confirm.

Prompt for Fai: "Move the design panel at <EVENT NAME> to the Design track"

#### Then: Finish or cancel a session

What an agent can do: Fai marks a session as finished or cancels it, after you confirm.

Prompt for Fai: "Cancel the Friday morning yoga session at <EVENT NAME>"

### Make an offer to an artist's agent for your show

Slug `make-an-offer-to-an-artists-agent`. Guide: https://www.ticketfairy.com/guides/make-an-offer-to-an-artists-agent

Build an offer for a performer from a template or your last deal, see what you paid them before and the fee Fai suggests, email it to their agent, record their counter-offers and book the artist on your event once they accept.

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

### Message the crew, volunteers and traders working on your event

Slug `message-the-people-working-on-your-event`. Guide: https://www.ticketfairy.com/guides/message-the-people-working-on-your-event

Email or text the people working on your event: a department, one day's rota, your volunteers, performers' teams, traders, press or sponsors in one go, start from a show-day template or let Fai draft it, check exactly who gets it before it goes, and see who it reached.

For: Telling the people working on your event what they need to know.

What an agent can do: Fai drafts a message in your brand's voice, counts who it will reach and sends it after you confirm the count and the channels. She never sends without your yes.

Command line:

- List the groups, statuses and channels this event can message: `ticketfairy event-os messages options <EVENT_ID>`
- Count who a message to every volunteer would reach by email: `ticketfairy event-os messages audience <EVENT_ID> --audience '{"groups":[{"source":"volunteers"}]}'`
- Have Fai draft the message from your words. Nothing is sent: `ticketfairy event-os messages draft <EVENT_ID> --request "Gates open 30 minutes early on Saturday"`
- Email every volunteer. This sends and asks you first; the count must match the one you checked: `ticketfairy event-os messages send <EVENT_ID> --audience '{"groups":[{"source":"volunteers"}]}' --subject "<SUBJECT>" --message "<MESSAGE>" --expected-count <COUNT>`
- List the messages sent and scheduled on the event: `ticketfairy event-os messages list <EVENT_ID>`

CLI MCP tools that read: `get_event_messages`, `count_event_message_audience`.

CLI MCP tools that make changes (not available with `--read-only`): `draft_event_message`, `send_event_message`.

Prompt for Fai: "Email Saturday's stewards and bar volunteers on <EVENT NAME> that the gates open 30 minutes early, and show me who gets it before you send"

#### Then: Send a message again to the people it missed

What an agent can do: Send a message again from its panel in the dashboard.

#### Then: Cancel a scheduled message

What an agent can do: Cancel a scheduled message from its panel in the dashboard.

#### Then: See every message one person was sent

What an agent can do: Fai lists the messages sent on the event and who each one reached.

Prompt for Fai: "Which messages did we send about <EVENT NAME> today, and who did they not reach?"

### Offer open shifts on your event rota to crew and volunteers

Slug `offer-open-shifts-to-your-crew-and-volunteers`. Guide: https://www.ticketfairy.com/guides/offer-open-shifts-to-your-crew-and-volunteers

Fill the gaps in your event rota by offering a shift to the crew and volunteers who fit it. Fai picks people who are free, rested, old enough and have the skill across all your events, each person gets an email with their own link, and the first to accept gets the place.

For: Filling the open places on your event rota.

What an agent can do: Fai lists the shifts that need people, finds who fits each one across your events, offers a shift to the people you choose and takes an offer back. She shows you who she will email and waits for your yes before anything is sent.

Prompt for Fai: "The Saturday bar shift at <EVENT NAME> still needs 2 people, offer it to whoever fits"

#### Then: Take back an offer

What an agent can do: Fai takes back an offer that is still waiting when you ask, after you confirm.

Prompt for Fai: "Take back the gate shift offer to Tomás Reyes at <EVENT NAME>"

#### Then: Ask who is still coming

What an agent can do: Fai asks everyone on the next day's shifts whether they are still coming, after you confirm, and reads you the answers.

Prompt for Fai: "Ask everyone on tomorrow's shifts at <EVENT NAME> if they are still coming"

#### Then: Find cover for someone who has not arrived

What an agent can do: Fai marks someone as not arrived and offers their place to people who fit, after you confirm each change.

Prompt for Fai: "Cai Jones hasn't turned up for his steward shift at <EVENT NAME>, mark him as not arrived and find cover"

#### Then: Let Fai send offers and ask by itself

What an agent can do: Fai turns either switch on or off in the rota rules when you ask, after you confirm.

Prompt for Fai: "At <EVENT NAME>, send the first shift offers yourself and ask people the day before if they are still coming"

### Place your traders on pitches on your event site map

Slug `place-your-traders-on-pitches-on-your-site-map`. Guide: https://www.ticketfairy.com/guides/place-your-traders-on-pitches-on-your-site-map

Drag each approved trader onto a pitch you drew on your event site map, move a trader when a pitch changes hands, and check every pitch with its power and water. Each trader then sees their own pitch on a map on their trader page.

For: Giving each approved trader a pitch on your site plan.

What an agent can do: Fai places a trader on a pitch of your site map, moves them to another pitch or takes them off the map. She shows you the change and waits for your yes first.

Prompt for Fai: "Put Smoke & Salt BBQ on pitch F2 on the site map for <EVENT NAME>"

#### Then: Take a trader off the map

What an agent can do: Fai takes a trader off the site map after you confirm.

Prompt for Fai: "Take <BUSINESS NAME> off the site map for <EVENT NAME>"

### Plan crew meal times and food needs for your event

Slug `plan-crew-meal-times-and-food-needs-for-your-event`. Guide: https://www.ticketfairy.com/guides/plan-crew-meal-times-and-food-needs-for-your-event

Set when your event's crew catering serves each day, with meal times suggested from the shifts, and see how many people are on shift at each meal and what food needs they have. Crew give their food needs once, and the kitchen follows the day's counts on its own link, with no names on it.

For: Telling your crew kitchen what to cook and when.

What an agent can do: Fai reads the meal times and the kitchen count, suggests meal times from the shifts, adds, changes or removes a meal time, and records a person's food needs. She waits for your yes before each change.

Prompt for Fai: "Add the meal times the shifts suggest for every day of <EVENT NAME>, and tell me how many vegan meals the kitchen needs for Saturday lunch"

#### Then: Change or remove a meal time

What an agent can do: Fai changes or removes a meal time when you ask, after you confirm.

Prompt for Fai: "Move Sunday lunch at <EVENT NAME> to 12:30 to 14:30"

#### Then: Record someone's food needs at the desk

What an agent can do: Fai records a person's food needs when you tell her them, after you confirm.

Prompt for Fai: "Ben Ode at <EVENT NAME> is vegan with a nut allergy, record his food needs"

### Plan next year's event from your attendee feedback

Slug `plan-next-year-from-your-attendee-feedback`. Guide: https://www.ticketfairy.com/guides/plan-next-year-from-your-attendee-feedback

Read your event's feedback as the answers come in: how many people answered, your Net Promoter Score beside the last edition's, each stage, act and trader's rating, and the themes Fai finds in their comments, with real quotes. Add the top things to improve as tasks on next year's event in one step.

For: Turning what your attendees said into next year's plan.

What an agent can do: Fai reads you the response rate, Net Promoter Score, each question's results and the themes in the comments, and reads the comments again when you ask. The tasks for next time are added from the dashboard or from Today, after you approve them.

Prompt for Fai: "What did people think of <EVENT NAME>, and what should we fix next year?"

#### Then: Download the answers

What an agent can do: Downloading the answers is done in the dashboard. Fai reads you the results and themes instead.

Prompt for Fai: "Summarise the feedback answers for <EVENT NAME> from people who would not recommend us"

### Plan your artists' pickups with drivers and vehicles for your event

Slug `plan-artist-pickups-with-drivers-and-vehicles`. Guide: https://www.ticketfairy.com/guides/plan-artist-pickups-with-drivers-and-vehicles

Give each airport and hotel pickup for your event a driver, a vehicle, a drive time and room for the bags, with a warning before you save when a driver is double booked, on a shift, short of rest or the vehicle is too small. When a flight is late, the pickup moves and Fai suggests a new plan, and each driver gets a day sheet on their phone.

For: Getting every artist from the airport to your event on time.

What an agent can do: Fai reads each day's pickups with their plans and warnings, adds, changes or removes a driver or vehicle, plans a pickup, checks a plan before it is saved, marks a flight as late and asks for a new plan. She shows you each change first and waits for your yes, and she texts drivers only when you approve a new plan.

Prompt for Fai: "Plan Kai Rivers' airport pickup at <EVENT NAME> with Sam in Van 2, a 55 minute drive and 3 bags, and tell me if anything clashes"

#### Then: Take a driver or vehicle off the list

What an agent can do: Fai removes a driver or vehicle when you ask, after you confirm.

Prompt for Fai: "Take the minibus off the vehicles list for <EVENT NAME>, it has broken down"

### Plan your run of show and who calls it

Slug `plan-your-run-of-show-and-who-calls-it`. Guide: https://www.ticketfairy.com/guides/plan-your-run-of-show-and-who-calls-it

Build the minute-by-minute run of show for each stage and day of your event, let Fai draft it from your schedule, fix clashes and late finishes before show day, lock it, and name the show callers who run it on the day.

For: Planning the running order for each stage and show day.

What an agent can do: Fai reads the run of show with everything that needs a check, drafts it from your schedule, adds, changes, moves or removes cues, locks or unlocks a day and names or removes show callers. She shows you each change and waits for your yes first, and nothing changes on a locked day.

Prompt for Fai: "Draft the run of show for Saturday at <EVENT NAME> with 30 minute changeovers and show me what clashes"

#### Then: Remove a cue

What an agent can do: Fai removes a cue when you ask, after you confirm.

Prompt for Fai: "Remove the confetti cannons cue from Saturday at <EVENT NAME>"

#### Then: Remove a show caller

What an agent can do: Fai removes a show caller when you ask, after you confirm.

Prompt for Fai: "Stop Tom Reyes calling the Harbour Tent at <EVENT NAME>"

### Publish your event line-up and set times

Slug `publish-your-line-up-and-set-times`. Guide: https://www.ticketfairy.com/guides/publish-your-line-up-and-set-times

Choose which acts appear on your public line-up with a photo, bio and links, let Fai draft the bios, announce acts in waves, review every change before it goes public, and put the timetable on your event page, your website and any other site, where fans star sets for their own schedule.

For: Announcing your line-up and keeping set times current everywhere fans look.

What an agent can do: Fai reads your public line-up, updates an act's public profile, drafts a bio from their links for you to accept, and publishes the line-up after you have seen what will change.

Command line:

- Show what publishing would change: acts and set times added, moved or taken off: `ticketfairy event-os lineup show <EVENT_ID> --review`
- Publish the line-up. This changes the public pages and asks you first unless you add --force: `ticketfairy event-os lineup publish <EVENT_ID>`

CLI MCP tools that read: `get_public_lineup`.

CLI MCP tools that make changes (not available with `--read-only`): `publish_lineup`.

Prompt for Fai: "Draft bios for the acts on <EVENT NAME> that have none, then show me what publishing the line-up would change"

#### Then: Take the line-up down

What an agent can do: Fai takes the public line-up down after you confirm.

Command line:

- Take the public line-up down. This asks you first unless you add --force: `ticketfairy event-os lineup publish <EVENT_ID> --withdraw`

CLI MCP tools that make changes (not available with `--read-only`): `publish_lineup`.

Prompt for Fai: "Take the public line-up for <EVENT NAME> down"

### Raise purchase orders and track what your event owes

Slug `raise-purchase-orders-and-track-what-your-event-owes`. Guide: https://www.ticketfairy.com/guides/raise-purchase-orders-and-track-what-your-event-owes

Send suppliers a purchase order for your event, check their invoice against it, and see every deposit, balance, per diem and supplier payment that is overdue, due this week or coming up. Approved orders count as committed costs in your event budget, and you record each payment as you make it.

For: Ordering from suppliers and paying performers and suppliers on time.

What an agent can do: Fai reads your purchase orders, committed costs and payments due, drafts an order by hand or from a confirmed supplier quote, changes, approves, sends or cancels it, enters an invoice total to check it against the order, marks a payment as paid, reverses a payment and adds or removes a per diem or cost. She shows you each change and waits for your yes first. Fai records payments and never moves money; to pay from Vault she uses a Vault transfer you approve, then records it.

Prompt for Fai: "What does <EVENT NAME> still owe, and what is overdue?"

#### Then: Add a per diem or cost

What an agent can do: Fai adds or removes a per diem, backline or other cost on a booking when you ask, after you confirm.

Prompt for Fai: "Add a 40 pound per diem for Nova Twins on Saturday at <EVENT NAME>"

#### Then: Reverse a payment recorded by mistake

What an agent can do: Fai reverses a payment with your reason when you ask, after you confirm.

Prompt for Fai: "Reverse the cash payment I recorded for Nova Twins' per diem at <EVENT NAME>, it was a mistake"

#### Then: Cancel a purchase order

What an agent can do: Fai cancels a purchase order with your reason when you ask, after you confirm.

Prompt for Fai: "Cancel PO-0013 at <EVENT NAME>, we are using a different barrier supplier"

### Read your event's email in one inbox

Slug `read-your-event-email-in-one-inbox`. Guide: https://www.ticketfairy.com/guides/read-your-event-email-in-one-inbox

See every email conversation about one event together, with Fai's summary of each, turn the follow-ups she finds into tasks, reply from your own email app and keep spam out.

For: Keeping up with the email about one event.

What an agent can do: Fai searches the conversations in your connected mailboxes, reads one in full and lists the follow-ups she found, so you can ask about the event's email without opening it.

Prompt for Fai: "What has come in by email about <EVENT NAME> this week, and what do we still need to do about it?"

#### Then: Connect your first mailbox

What an agent can do: Fai tells you which mailboxes your brand has connected and whether each one is working.

Prompt for Fai: "Which mailboxes does Fai read for <EVENT NAME>?"

### Recruit volunteers for your event

Slug `recruit-volunteers-for-your-event`. Guide: https://www.ticketfairy.com/guides/recruit-volunteers-for-your-event

Open a volunteer application form for your event that people fill in on their phone, let Fai read each application against the roles you need, accept, waitlist or decline people in batches with one email each, and invite back last year's volunteers with their answers already filled in.

For: Recruiting and choosing the volunteers who work your event.

What an agent can do: Fai sets up the volunteer form, lists applications with her reading of each, accepts, waitlists, declines or shortlists people, and invites back last year's volunteers. She shows you who gets which email and waits for your yes.

Command line:

- List the applications still to decide that Fai rates a strong fit, with each person's id and version: `ticketfairy event-os volunteers list <EVENT_ID> --status undecided --strong-fit`
- Accept people and email them the decision. Use id:version pairs from the list. This asks you first unless you add --force: `ticketfairy event-os volunteers decide <EVENT_ID> --decision accept --volunteers <VOLUNTEER_ID>:<VERSION>`

CLI MCP tools that read: `get_volunteer_applications`.

CLI MCP tools that make changes (not available with `--read-only`): `decide_volunteer_applications`.

Prompt for Fai: "Show me the volunteer applications for <EVENT NAME> that are a strong fit for the bar, and accept them with the usual email"

#### Then: Invite last year's volunteers back

What an agent can do: Fai suggests who to invite back from an earlier event, from the shifts they worked, and sends the invitations after you confirm.

Prompt for Fai: "Invite back the volunteers from last year's <EVENT NAME> who worked every shift"

### Report and handle incidents at your event

Slug `report-and-handle-incidents-at-your-event`. Guide: https://www.ticketfairy.com/guides/report-and-handle-incidents-at-your-event

Log anything that goes wrong on site at your event in seconds, alert your safety lead about serious incidents at once, keep medical and safeguarding details to your safety team, and follow each incident through to closed with a complete record.

For: Logging and following up what happens on site.

What an agent can do: Fai reads the incident log, logs an incident or adds an update to one, suggests its type and seriousness, changes its details, moves it on, reopens it or removes its personal details. She shows you each change and waits for your yes first. Any member of your event's team can report an incident or add an update through Fai.

Prompt for Fai: "Log an incident at <EVENT NAME>: someone fainted near the main bar, medium, first aid is with them"

#### Then: Remove personal details from an incident

What an agent can do: Fai removes an incident's personal details when you ask, after you confirm. It cannot be undone.

Prompt for Fai: "Remove the personal details from incident 31 at <EVENT NAME>"

### Review act and talk applications for your event with your team

Slug `review-act-and-talk-applications-with-your-team`. Guide: https://www.ticketfairy.com/guides/review-act-and-talk-applications-with-your-team

Collect applications to play and proposals for talks for your event in one list, with Fai's notes on each and a score from every reviewer on your panel, who score from their own link with no sign-in and, if you choose, without seeing names. Accepting an act or a talk adds it to your event with a draft offer or an agenda session, and starts their advance.

For: Choosing the acts and speakers for your event with a review panel.

What an agent can do: Fai lists the applications with her notes, the reviewers' scores and possible repeats, scores one for you, moves or declines one, accepts one, and adds, emails, stops or removes a reviewer's link. She shows you each change first and waits for your yes, and she never shows a reviewer's link in the conversation.

Prompt for Fai: "Which talk proposals for <EVENT NAME> have the best reviewer scores, and accept Designing for door staff for Saturday at 11 in the Main Hall"

#### Then: Decline or move an application

What an agent can do: Fai declines or moves an application with your reason, after you confirm. Nobody is emailed.

Prompt for Fai: "Decline the lightning talk about ticket scanning for <EVENT NAME>, we already have one on that"

#### Then: Stop a reviewer's link

What an agent can do: Fai stops, sends again or removes a reviewer's link, after you confirm.

Prompt for Fai: "Stop Sam Lee's review link for <EVENT NAME>"

### Run a safety induction for everyone who works your event

Slug `run-a-safety-induction-for-everyone-who-works-your-event`. Guide: https://www.ticketfairy.com/guides/run-a-safety-induction-for-everyone-who-works-your-event

Put the safety briefing your crew, volunteers and suppliers must read before they work your event in one place, let Fai draft a short test from it, and have the hand-out desk check that each person has done it before they collect their pass. You see who has done it and mark it done for anyone you briefed in person.

For: Briefing everyone who works on your event site on safety.

What an agent can do: Fai sets up or changes the induction, drafts the short test from your briefing, makes it live or takes it down, tells you who has not done it and marks it done for someone you briefed. She waits for your yes before each change.

Prompt for Fai: "Draft a short safety test from the induction at <EVENT NAME> and show me the questions"

#### Then: Take the test down

What an agent can do: Fai takes the test down or removes it when you ask, after you confirm.

Prompt for Fai: "Take the safety test down at <EVENT NAME>, I need to change a question"

### Run your event from its Today page

Slug `run-your-event-from-its-today-page`. Guide: https://www.ticketfairy.com/guides/run-your-event-from-its-today-page

Set your event up with Fai on your first visit, then see what needs you each day, approve, change or turn down what Fai suggests, and open any part of your event from one page.

For: Running an event day to day with Fai drafting the routine work.

What an agent can do: Fai reads the same Today page for you, lists what she suggests, and approves, changes, reminds you later or turns down a suggestion when you ask. She can also change what she helps with on the event, add or remove a section for your team and pin one for you. She shows you what she is about to send, add or change and waits for your yes first.

Prompt for Fai: "What does <EVENT NAME> need from me today? Show me your suggestions before you approve any of them"

#### Then: Add a section for your team or pin one for yourself

What an agent can do: Fai adds or removes a section for your team, pins one for you and changes what she helps with on the event, after you confirm.

Prompt for Fai: "Add the rota and incidents to the section list for <EVENT NAME> and pin Show day for me"

#### Then: Change the event type

What an agent can do: Fai reads the event type and changes it when you ask, after you confirm.

Prompt for Fai: "Make <EVENT NAME> a festival and a conference"

### Scan delegates into event sessions at the door and see who came

Slug `scan-ticket-holders-into-sessions-and-see-who-came`. Guide: https://www.ticketfairy.com/guides/scan-ticket-holders-into-sessions-and-see-who-came

Scan tickets at the door of each conference session so only the people who picked it go in, from the dashboard or a door link on a volunteer's phone. The attendance report then shows who came, who did not, who was turned away and your most popular sessions.

For: Running the doors of your conference sessions.

What an agent can do: Fai scans a ticket into a session for you, after you confirm, and tells you whether to let the person in and why not. She also makes a door link for volunteers, without showing its address.

Prompt for Fai: "Scan ticket TF8841QX into the Hiring your first designer talk at <EVENT NAME>"

#### Then: Give door staff a door link

What an agent can do: Fai makes a session door link with the name you give, after you confirm. She never shows the link's address, so copy it from the dashboard.

Prompt for Fai: "Make a door link for Room 2 phone for the sponsor deck workshop at <EVENT NAME>"

### See the all-in cost of each act on your event

Slug `see-the-all-in-cost-of-each-act-on-your-event`. Guide: https://www.ticketfairy.com/guides/see-the-all-in-cost-of-each-act-on-your-event

See what one act really costs on its performer page: the fee, the agency fee, travel, the hotel stay, per diems, backline and their share of hire, with one total for each currency. Enter what a trip cost or the room rate of a stay where they are missing, and the same figures reach your budget and the show's settlement.

For: Knowing what each act on your event costs in total.

What an agent can do: Fai reads an act's all-in cost with every part and where it comes from, and enters the cost of a trip or the room rate of a stay when you ask. She shows you the change and waits for your yes first.

Prompt for Fai: "What does <ARTIST NAME> cost us all in at <EVENT NAME>? Their outbound flight cost 320 euros"

### See what your brand spends across its events

Slug `see-what-your-brand-spends-across-its-events`. Guide: https://www.ticketfairy.com/guides/see-what-your-brand-spends-across-its-events

See the planned and recorded costs of every event your brand ran or has coming up in a period, the cost per person scanned in at the doors, your budget sections, your biggest suppliers and each event's figures, with every amount in its own currency.

For: Reviewing costs across all of your brand's events.

What an agent can do: Fai reads the same figures for a period: planned and recorded costs, income recorded, people scanned in, cost per checked-in attendee, budget sections, biggest suppliers and each event. She only reads here and changes nothing.

Prompt for Fai: "What did our events cost over the last 12 months, and what was the cost per person scanned in?"

### See which event pass holders have arrived and send a pass again

Slug `see-which-pass-holders-have-arrived-and-send-a-pass-again`. Guide: https://www.ticketfairy.com/guides/see-which-pass-holders-have-arrived-and-send-a-pass-again

See when and how each accreditation pass holder arrived, from the desk hand-over, a staff gate or the door scanner, and how many of each group have arrived. Send a pass email again to anyone who cannot find theirs.

For: Tracking who has arrived with an accreditation pass.

What an agent can do: Fai lists who has arrived and who has not, counts the arrivals of each group, and sends a pass email again after you confirm.

Prompt for Fai: "How many of the Northern Bars crew have arrived at <EVENT NAME>?"

#### Then: Send a pass again

What an agent can do: Fai sends a pass email again to the address it was issued to, after you confirm.

Prompt for Fai: "Send Jane Doe's crew pass for <EVENT NAME> again, she cannot find the email"

### See why tickets and passes were refused at the door

Slug `see-why-tickets-and-passes-were-refused-at-the-door`. Guide: https://www.ticketfairy.com/guides/see-why-tickets-and-passes-were-refused-at-the-door

Count every scan your door scanners and staff gates refused, by reason, entrance, hour and ticket or pass type, on the Check-in page. Spot shared screenshots of tickets and doors turning people away, then open each refused scan to see who it was.

For: Understanding the scans your door and staff gates turned away.

What an agent can do: Fai reads the refused scans by reason, entrance, hour and type for the whole event or one day, and lists the refused scans for one reason.

Prompt for Fai: "Why were people refused at the doors of <EVENT NAME> on Saturday, and at which entrance?"

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

### Send contracts to many performers, traders or suppliers for your event at once

Slug `send-contracts-to-many-performers-traders-or-suppliers-at-once`. Guide: https://www.ticketfairy.com/guides/send-contracts-to-many-performers-traders-or-suppliers-at-once

Make a contract for every booked performer or speaker, approved trader or supplier on your event from one template, each filled in from their own booking or record. You check every contract before anything is made, then send them all for signature in one approval or keep them as drafts, and see each person's result.

For: Sending the same agreement to all your performers, traders or suppliers.

What an agent can do: Fai shows who a batch can go to and a preview of every contract, then makes and sends the contracts from one template or keeps them as drafts, reads each batch's results and starts a batch that did not start. She shows you every contract first and waits for your yes.

Prompt for Fai: "Send the performance agreement to every booked performer at <EVENT NAME> who has no contract yet, and show me each contract first"

#### Then: Open a batch you made earlier

What an agent can do: Fai reads your latest batches and each contract's result and current status.

Prompt for Fai: "Which contracts from the batch I sent at <EVENT NAME> are still waiting for a signature"

#### Then: Try again for the people a batch missed

What an agent can do: Fai starts a batch that did not start after you confirm.

Prompt for Fai: "The contracts batch at <EVENT NAME> did not start, start it again"

### Send event document packs to your performers, traders and crew

Slug `send-document-packs-to-your-performers-traders-and-crew`. Guide: https://www.ticketfairy.com/guides/send-document-packs-to-your-performers-traders-and-crew

Put together what one kind of contact needs for your event, such as the site rules, the map, their own day sheet, their contract and their rider, and send it to all of them in one step. Each person gets an email with their own link, opens their pack with no sign-in, and sees their own day sheet and contract. You see who got it and who opened it, share one person's link with a QR code, and stop a link at any time.

For: Sending performers, traders, suppliers and crew everything they need for your event.

What an agent can do: Fai reads your packs and who got them, makes or changes a pack, emails it to the people you choose, starts a send that did not start and stops one person's link. She waits for your yes first. Share one person's link or QR code from the dashboard, because the link shows there once.

Prompt for Fai: "Make a performer welcome pack for <EVENT NAME> with the site rules, each performer's own day sheet and their contract, and send it to every booked performer"

#### Then: Share one person's link or QR code

What an agent can do: Get one person's link or QR code in the pack in the dashboard, where it shows once. Fai can email the pack to that person instead.

Prompt for Fai: "Send the performer welcome pack at <EVENT NAME> to <PERFORMER NAME> only"

#### Then: Stop one person's link

What an agent can do: Fai stops one person's link to a pack after you confirm.

Prompt for Fai: "Stop The Tidewater Band's link to the performer welcome pack at <EVENT NAME>"

#### Then: Remove a pack

What an agent can do: Fai removes a pack after you confirm, which stops every link to it.

Prompt for Fai: "Remove the crew pack from <EVENT NAME>"

### Send your event contracts and get them signed online

Slug `send-contracts-and-get-them-signed-online`. Guide: https://www.ticketfairy.com/guides/send-contracts-and-get-them-signed-online

Turn an accepted offer, a booked performer or speaker, an approved trader or a supplier's quote into a contract for your event, send it for signature by email, and sign it yourself once they have. The other party reads the agreement and signs by entering their name, with no account, and you both get the signed copy.

For: Getting performer, speaker, trader and supplier agreements signed.

What an agent can do: Fai reads your contracts, drafts one from an offer, a booking, a trader, a supplier quote or a template, changes a draft, sends it for signature or sends a reminder, signs it for you once the other party has, starts a new version or an amendment, cancels an unsigned one and manages your contract templates. She shows you each change and waits for your yes first, and nothing is emailed until you agree. When a contract has waited 5 days for a signature, Fai suggests a reminder on Today.

Prompt for Fai: "Draft the contract for Nova Twins at <EVENT NAME> from their accepted offer and tell me what is missing before I send it"

#### Then: Send a reminder

What an agent can do: Fai sends a reminder with a new link when you ask, after you confirm.

Prompt for Fai: "Remind Nova Twins to sign their contract for <EVENT NAME>"

#### Then: Change a contract that is already sent

What an agent can do: Fai starts a new version of a sent or declined contract when you ask, after you confirm.

Prompt for Fai: "Nova Twins asked for a later set time at <EVENT NAME>, start a new version of their contract"

#### Then: Amend a signed contract

What an agent can do: Fai starts an amendment or a termination agreement to a signed contract when you ask, after you confirm.

Prompt for Fai: "Start an amendment to the signed Nova Twins contract at <EVENT NAME> for an extra 15 minutes"

#### Then: Cancel a contract

What an agent can do: Fai cancels an unsigned contract with your reason when you ask, after you confirm.

Prompt for Fai: "Cancel the draft speaker contract for Dr Amara Lee at <EVENT NAME>, the session was dropped"

### Send your event hire lists to suppliers

Slug `send-your-hire-lists-to-suppliers`. Guide: https://www.ticketfairy.com/guides/send-your-hire-lists-to-suppliers

Send each supplier the items they are providing for your event, with the quantities, hire dates, delivery and collection, in an email Fai drafts for you to check. Each send keeps a copy of the list, so you see what changed since and send only the changes, and a supplier's priced items become a draft purchase order in one step.

For: Sending equipment and shopping lists to the suppliers of your event.

What an agent can do: Fai drafts the email to a supplier from their items and what changed since the last send, and sends it after you have read it and said yes. When a supplier's items change after a send, she also suggests sending the changes on Today.

Prompt for Fai: "Send Northern Backline the changes to our backline hire for <EVENT NAME>"

#### Then: Make a purchase order from a supplier's items

What an agent can do: Fai makes a draft purchase order from a supplier's priced items when you ask, after you confirm. You approve and send it in Contracts.

Prompt for Fai: "Make a purchase order for Northern Backline's items at <EVENT NAME>"

#### Then: Print a supplier's list

What an agent can do: Printing is done in the dashboard. Fai reads you a supplier's items, dates and delivery times instead.

Prompt for Fai: "What is on Northern Backline's list for <EVENT NAME>, and when do they deliver and collect?"

### Send your event lists to your team on a schedule

Slug `send-your-event-lists-to-your-team-on-a-schedule`. Guide: https://www.ticketfairy.com/guides/send-your-event-lists-to-your-team-on-a-schedule

Email your rota, run of show, advancing status, rooming list or pickups to the right people on your event team every day or every week, as a file they download after signing in. Every file and every download is recorded, and you can make a file now whenever you need one.

For: Keeping your team up to date with the latest lists.

What an agent can do: Fai reads your scheduled exports, their latest files and who can receive each list, schedules a list every day or week, changes, pauses, turns back on or stops a schedule, and makes a file now. She shows you each change and waits for your yes first.

Prompt for Fai: "Email the rota for <EVENT NAME> to me and Sam every Monday at 9am"

#### Then: Pause or stop a schedule

What an agent can do: Fai pauses, turns back on or stops a scheduled export when you ask, after you confirm.

Prompt for Fai: "Stop sending the rota for <EVENT NAME> every week"

#### Then: Make a file now

What an agent can do: Fai makes a file of the list now when you ask, after you confirm, and you download it in the dashboard.

Prompt for Fai: "Make a file of the run of show for <EVENT NAME> now"

### Set each performer's guest list, hotel and meal allowances for your event

Slug `set-each-performers-allowances-and-travel-party`. Guide: https://www.ticketfairy.com/guides/set-each-performers-allowances-and-travel-party

Give every act on your event's line-up its guest list places, hotel rooms and nights, and meals and drinks a day, taken from the accepted offer in one click. Keep one travel party list that passes, the rooming list, pickups and the kitchen all use, and let the tour manager fill it in, ask for more and invite a teammate from their advance link.

For: Agreeing what each act gets at your event.

What an agent can do: Fai reads an act's allowances, what is used and left, their asks for more and the travel party. She sets an allowance or uses the numbers from the accepted offer, approves an ask or says no with your reason, and adds, changes or removes people in the travel party, showing you each change and waiting for your yes.

Prompt for Fai: "Use the numbers from Bicep's accepted offer for their allowances at <EVENT NAME>, and add their tour manager Sam Lee to the travel party with a room"

#### Then: Change or remove a person

What an agent can do: Fai changes or removes a person in the travel party, after you confirm.

Prompt for Fai: "Bicep's drummer is not coming to <EVENT NAME> any more, take them off the travel party"

### Set pitch rules and let Fai plan your trader pitches at your event

Slug `set-pitch-rules-and-let-fai-plan-your-trader-pitches`. Guide: https://www.ticketfairy.com/guides/set-pitch-rules-and-let-fai-plan-your-trader-pitches

Enter your event's pitch rules the way you would say them, such as keeping the two coffee vans apart or the fire lane clear. The pitch check shows every pitch that breaks a rule, and Fai places the traders still without a pitch on free pitches that keep every rule, for you to approve.

For: Placing traders on your site plan by your own rules.

What an agent can do: Fai adds a pitch rule from your words, reads you the pitch check, and makes a pitch plan for the traders still without a pitch. She shows you each rule and plan, and nothing is placed until you approve it.

Prompt for Fai: "At <EVENT NAME>, keep the two coffee vans at least 30 metres apart, then plan pitches for the traders who still need one"

#### Then: Turn a rule off or remove it

What an agent can do: Fai turns a pitch rule off or on, or removes it, after you confirm.

Prompt for Fai: "Turn off the power rule for the food court at <EVENT NAME>"

### Set up a self-service check-in kiosk for your event

Slug `set-up-a-self-service-check-in-kiosk-for-your-event`. Guide: https://www.ticketfairy.com/guides/set-up-a-self-service-check-in-kiosk-for-your-event

Put a tablet and a badge printer by your event entrance so attendees check themselves in and print their own name badge. They scan the ticket from their email, or confirm their email address with a six-digit code, and each ticket gets one badge from the kiosk.

For: Letting attendees check in and print their own badges at your event.

What an agent can do: Fai makes, changes or stops a kiosk link after you confirm, and turns finding a ticket by email on or off in the badge setup. Open Desks and links and select **Get a new link** to see a kiosk link's address.

Prompt for Fai: "Make a self-service kiosk link called Kiosk by the main entrance for <EVENT NAME>"

#### Then: Accept scanned tickets only

What an agent can do: Fai turns finding a ticket by email on or off after you confirm.

Prompt for Fai: "At <EVENT NAME>, stop the kiosks finding tickets by email"

#### Then: Close the kiosk

What an agent can do: Fai stops a kiosk link after you confirm.

Prompt for Fai: "Close the Kiosk by the main entrance at <EVENT NAME>"

### Settle a show with an artist after your event

Slug `settle-a-show-with-an-artist`. Guide: https://www.ticketfairy.com/guides/settle-a-show-with-an-artist

Let Fai draft the settlement for a show from its ticket sales, budget costs, the artist's deal and the act's own travel, hotel and agency fee, check where every figure came from, add or reverse lines, and share it, mark it agreed and mark it paid.

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

### Share a power sheet with your event electrician

Slug `share-a-power-sheet-with-your-electrician`. Guide: https://www.ticketfairy.com/guides/share-a-power-sheet-with-your-electrician

Send your electrician a link to a sheet of every trader's pitch, the power they need in amps and whether they need water, for one zone of your event site map or the whole site. The sheet needs no sign-in, always shows the latest pitches, and you can stop the link at any time.

For: Giving your electrician and site crew the traders' power and water needs.

What an agent can do: Fai makes a power sheet link for one zone or the whole site, lists the links you have made and stops one. She waits for your yes before she makes or stops a link. The address of a new link shows once, in the dashboard.

Prompt for Fai: "Make a power sheet link for the food court at <EVENT NAME> that works for 14 days"

#### Then: Stop a power sheet link

What an agent can do: Fai stops a power sheet link after you confirm.

Prompt for Fai: "Stop the power sheet link for the food court at <EVENT NAME>"

### Share a private event site map with emergency services and suppliers

Slug `share-a-private-site-map-with-emergency-services-and-suppliers`. Guide: https://www.ticketfairy.com/guides/share-a-private-site-map-with-emergency-services-and-suppliers

Send the fire service, an accessibility team or a supplier a private link to your event's live site map, showing the exits, routes, power or other places they need on top of the public map. Each link ends on a date, records every opening and can be stopped at any time.

For: Sharing your site plan with emergency services, accessibility teams and suppliers.

What an agent can do: Fai lists your map links and how often each was opened, makes a link for the audience you name, gives a link a new address or stops it, after you confirm. She never shows a link's address, so copy it from Share links.

Prompt for Fai: "Make a map link for the fire service at <EVENT NAME> that works for 30 days"

#### Then: Give a link a new address or stop it

What an agent can do: Fai gives a map link a new address or stops it, after you confirm.

Prompt for Fai: "Stop the Northern Power map link at <EVENT NAME>"

### Share day sheets with your event's on-site teams

Slug `share-day-sheets-with-your-on-site-teams`. Guide: https://www.ticketfairy.com/guides/share-day-sheets-with-your-on-site-teams

Set up the departments working your event and who leads each one, then print or share a day sheet for each team, performer or stage with only their part of the show day, on any phone and without a sign-in.

For: Giving each on-site team its own plan for the day.

What an agent can do: Fai reads any team's, performer's or stage's day sheet, adds or changes departments and the people in them, makes or turns off a share link, and emails every department lead the link to their own day sheet. She shows you each change or email and waits for your yes first.

Prompt for Fai: "Email every department lead at <EVENT NAME> their day sheet for Saturday"

#### Then: Turn off a shared link

What an agent can do: Fai turns off a day sheet link when you ask, after you confirm.

Prompt for Fai: "Turn off the security day sheet link for Saturday at <EVENT NAME>"

### Share your event's rooming lists with hotels and pickups with drivers

Slug `share-rooming-lists-with-hotels-and-pickups-with-drivers`. Guide: https://www.ticketfairy.com/guides/share-rooming-lists-with-hotels-and-pickups-with-drivers

Send each hotel a live rooming list of the performers and crew staying for your event, with their dates, room types and notes, and give each driver a link to their pickups and shuttle runs for the day. Hotels and drivers open the link without signing in, the hotel's list updates as you change it, and drivers mark each pickup as they go.

For: Keeping hotels and drivers up to date for your event.

What an agent can do: Fai reads each hotel's rooming list and one day's pickups and shuttle runs, sets a guest's room type, rooms and note for the hotel, makes or turns off a hotel or driver link, adds, changes or removes a shuttle, and marks a pickup or a shuttle run. She shows you each change and waits for your yes first. Only owners and admins can put phone numbers and emails on a link.

Prompt for Fai: "Make a rooming list link for Harbour Hotel for <EVENT NAME> without contact details"

#### Then: Turn a link off

What an agent can do: Fai turns a hotel or driver link off when you ask, after you confirm.

Prompt for Fai: "Turn off the driver link for Kev at <EVENT NAME>"

### Show each act their whole stay and what changed

Slug `show-each-act-their-whole-stay-and-what-changed`. Guide: https://www.ticketfairy.com/guides/show-each-act-their-whole-stay-and-what-changed

Give each performer at your event one list of their whole stay, from their flights and pickup to their hotel, load-in, soundcheck and set, on their day sheet. You see what changed since the act last opened their day sheet link, and they see what changed since they last looked.

For: Keeping each act's travel, hotel and times in one place.

What an agent can do: Fai reads an act's whole stay in order and tells you what changed since the act last opened their day sheet link.

Prompt for Fai: "What has changed in Nova Lights' stay at <EVENT NAME> since they last looked at their day sheet?"

### Show now and next on screens backstage and at the side of the stage

Slug `show-now-and-next-on-backstage-screens`. Guide: https://www.ticketfairy.com/guides/show-now-and-next-on-backstage-screens

Put the act on now, the act next, the time left and how late each stage runs on any TV backstage or at the side of a stage. The TV opens it from a private link with no sign-in, updates by itself from your run of show and shows no personal details.

For: Keeping backstage teams on time with the running order.

What an agent can do: Fai makes a backstage TV link for every stage or one stage, lists your TV links with when each was last shown, and stops a link, after you confirm. She never shows a link's address, so copy it in Now and next.

Prompt for Fai: "Make a backstage screen for the side of the Main Stage at <EVENT NAME>"

#### Then: Stop showing a TV

What an agent can do: Fai stops a TV link when you ask, after you confirm.

Prompt for Fai: "Stop the green room TV screen at <EVENT NAME>"

### Show your traders in a directory on your website

Slug `show-your-traders-in-a-directory-on-your-website`. Guide: https://www.ticketfairy.com/guides/show-your-traders-in-a-directory-on-your-website

Publish a public list of the food, drink and market traders at your event, check each trader's listing before it goes up, ask a trader to change it, choose how the list looks, and put it on your own website with the embed code.

For: Showing the traders at your event on your own website.

What an agent can do: Fai reads your trader directory and its embed code, changes a trader's listing, publishes it, asks the trader for changes or takes it out of the directory. She shows you each change and waits for your yes first.

Prompt for Fai: "Which trader listings for <EVENT NAME> are waiting for review, and publish the ones that say what they sell"

#### Then: Take a trader out of the directory

What an agent can do: Fai takes a trader's listing out of the directory after you confirm.

Prompt for Fai: "Take <BUSINESS NAME> out of the trader directory for <EVENT NAME>"

### Take food, drink and market trader applications for your event

Slug `take-trader-applications-for-your-event`. Guide: https://www.ticketfairy.com/guides/take-trader-applications-for-your-event

Open an application page for food, drink, merchandise and market traders, set your pitch fees and how they are taxed, let Fai rank the applications against the mix you want, then approve, waitlist or decline each trader for your event and invoice the ones you approve.

For: Choosing and invoicing the traders who sell at your event.

What an agent can do: Fai lists your traders and applications with her reading of each, sets up the application page, fees and tax, adds a trader you already know, and approves, waitlists or declines an application. She shows you the email and invoice first and waits for your yes.

Command line:

- List the traders and applications on the event: `ticketfairy event-os traders list <EVENT_ID> --view to_review --sort fai`
- Show one trader's application, fees, paperwork and history: `ticketfairy event-os traders show <EVENT_ID> <VENDOR_ID>`
- Approve a trader, email them and raise and send their pitch invoice. This asks you first unless you add --force: `ticketfairy event-os traders decide <EVENT_ID> <VENDOR_ID> --decision approve --raise-invoice --send-invoice`

CLI MCP tools that read: `get_traders`.

CLI MCP tools that make changes (not available with `--read-only`): `decide_trader_application`.

Prompt for Fai: "Show me the trader applications for <EVENT NAME> that best fit our food mix, and approve Smoke & Salt BBQ on the 6m pitch with the invoice"

#### Then: Add a trader you already know

What an agent can do: Fai adds a trader to the event from the details you give her, after you confirm.

Prompt for Fai: "Add <BUSINESS NAME> to the traders on <EVENT NAME> as already agreed, contact <NAME> at <EMAIL>"

#### Then: Raise or send an invoice later

What an agent can do: Fai raises a trader's invoice and sends it after you confirm.

Prompt for Fai: "Raise and send the pitch invoice for <BUSINESS NAME> on <EVENT NAME>"

#### Then: Cancel an approved trader

What an agent can do: Fai cancels an approved trader after you confirm.

CLI MCP tools that read: `get_traders`.

CLI MCP tools that make changes (not available with `--read-only`): `decide_trader_application`.

Prompt for Fai: "Cancel <BUSINESS NAME> as a trader at <EVENT NAME>"

### Take notes on your event calls with Fai

Slug `take-notes-on-your-event-calls-with-fai`. Guide: https://www.ticketfairy.com/guides/take-notes-on-your-event-calls-with-fai

Send Fai's notetaker to a Zoom, Google Meet or Microsoft Teams call about your event and get a summary, the follow-ups agreed and notes you can share, filed under the event.

For: Keeping a record of the calls about one event.

What an agent can do: Fai sends the notetaker to a call link you give her, tells you where it is up to, and finds and reads the notes from earlier calls. She asks before the notetaker joins a call.

Prompt for Fai: "Send the notetaker to this call for <EVENT NAME>: <CALL LINK>"

#### Then: Call off the notetaker

What an agent can do: Fai tells you where the notetaker is up to on a call. To call it off, use Meetings in the dashboard.

Prompt for Fai: "Is the notetaker on the security briefing for <EVENT NAME> yet?"

### Track every artist booking for your event

Slug `book-and-brief-your-artists`. Guide: https://www.ticketfairy.com/guides/book-and-brief-your-artists

Keep the contract, the fee, the rider, the hospitality and the travel for every artist on your event together, and see which parts are still missing.

For: Booking artists and getting them to your event ready to play.

What an agent can do: Fai can read a booking contract or invoice and pull the fee, the deposit, the payment schedule and the flight details out of it. She can also read what an artist draws on the streaming platforms.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Read the contract I uploaded for <ARTIST NAME> and tell me the fee, the deposit and when the balance is due"

#### Then: Let Fai read the contract for you

What an agent can do: Fai reads a booking contract or invoice and pulls out the terms. What she finds is a reading of the document, so check it before you pay.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Read the invoice for <ARTIST NAME> and tell me what is due, to whom and by when"

### Work out the backline and production to hire for your event

Slug `work-out-the-backline-and-production-to-hire-for-your-event`. Guide: https://www.ticketfairy.com/guides/work-out-the-backline-and-production-to-hire-for-your-event

Turn every act's technical rider into one backline hire list for your event, add the PA, lighting, staging and power you hire yourself, and see how many of each item to hire across every stage and day. Gear that can be reused on other days is hired once for the busiest day, and what a stage already has or you already own comes off the number.

For: Working out how much equipment to hire for a festival or multi-stage event.

What an agent can do: Fai reads the hire lists with how each number was worked out, adds an item or a need, changes an item's details, reuse or status, answers a rider change and puts one item under another. She shows you each change and waits for your yes first. She also reads riders as they change and suggests adding items she finds in production documents you upload.

Prompt for Fai: "How many CDJs do we need to hire for <EVENT NAME>, and which acts need them on which days?"

#### Then: Change the hire period

What an agent can do: Fai changes the hire period when you ask, after you confirm.

Prompt for Fai: "Give every hire at <EVENT NAME> two load-in days before the first day"

#### Then: Put one item under another

What an agent can do: Fai puts one item under another when you ask, after you confirm.

Prompt for Fai: "CDJ3000 and Pioneer CDJ-3000 are the same thing at <EVENT NAME>, put them together"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
