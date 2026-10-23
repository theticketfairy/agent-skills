---
name: plan-the-running-order-and-show-day
description: "Build the running order and run of show, check clashes, share day sheets and call the show live in Ticket Fairy. Use when an organiser plans set times or runs show day."
---

# Plan the running order and show day

This skill covers line-ups, running orders, run of show, clash checks, day sheets and calling the show on Ticket Fairy. It lists the 9 published guides for this area and what an agent can do for each one.

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

- [Add your run of show to your team's calendars](#add-your-run-of-show-to-your-teams-calendars)
- [Book dressing rooms and plan build and break days for your event](#book-dressing-rooms-and-plan-build-and-break-days-for-your-event)
- [Build the running order for your event day](#build-the-running-order-for-your-event-day)
- [Call your show live on show day](#call-your-show-live-on-show-day)
- [Check your running order for clashes before show day](#check-your-running-order-for-clashes-before-show-day)
- [Plan your run of show and who calls it](#plan-your-run-of-show-and-who-calls-it)
- [Publish your event line-up and set times](#publish-your-event-line-up-and-set-times)
- [Share day sheets with your event's on-site teams](#share-day-sheets-with-your-events-on-site-teams)
- [Show now and next on screens backstage and at the side of the stage](#show-now-and-next-on-screens-backstage-and-at-the-side-of-the-stage)

### Add your run of show to your team's calendars

Slug `add-your-run-of-show-to-your-teams-calendars`. Guide: https://www.ticketfairy.com/guides/add-your-run-of-show-to-your-teams-calendars

Give your production team a calendar link that puts every cue of the run of show in Google Calendar, Apple Calendar or Outlook, for every stage or one. Their calendar app checks it again by itself, so a moved cue moves in their calendar too.

For: Getting the run of show into your production team's own calendars.

What an agent can do: Fai makes a calendar link for every stage or one stage, after you confirm. She never shows a link's address, so copy it from the dashboard.

Prompt for Fai: "Make a calendar link of the whole run of show at <EVENT NAME> for the production team"

### Book dressing rooms and plan build and break days for your event

Slug `book-dressing-rooms-and-plan-build-and-break-days`. Guide: https://www.ticketfairy.com/guides/book-dressing-rooms-and-plan-build-and-break-days

Give every performer at your event a dressing room around their set, with Fai suggesting the whole day's rooms and flagging any overlap. Add the build days before the show and the break days after it to your run of show with the usual load-in, rig, sound check, de-rig and load-out cues.

For: Planning dressing rooms and the days around your show.

What an agent can do: Fai reads your dressing rooms and a day's bookings with any overlaps, suggests a room for every performer, adds, changes or removes rooms, books or cancels a room, saves her plan, and adds a build or break day with the usual cues. She shows you each change and waits for your yes first, and asks before she books a room that overlaps another booking.

Prompt for Fai: "Give every performer on Saturday at <EVENT NAME> a dressing room around their set"

#### Then: Cancel a dressing room booking

What an agent can do: Fai cancels a dressing room booking when you ask, after you confirm.

Prompt for Fai: "Cancel The Harbour's dressing room booking on Saturday at <EVENT NAME>"

### Build the running order for your event day

Slug `plan-your-event-production`. Guide: https://www.ticketfairy.com/guides/plan-your-event-production

Lay out every stage and every set of your event day on one timeline, so you can see every set time and every changeover in one running order.

For: Running the stages and set times on your event day.

What an agent can do: Fai can add your stages and sets, move a set and read you the day's running order. She shows each change and waits for your yes.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Add a Main Stage to <EVENT NAME> and put <ACT NAME> on it at 21:00 for 75 minutes, then show me the day"

#### Then: Keep the day current as it changes

What an agent can do: Fai can move a set to a new time or stage and tell you what it now clashes with. She shows the change and waits for your yes.

Command line:

- Show the event and its dates: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Move <ACT NAME> on <EVENT NAME> to 22:15 on the same stage and show me what that changes"

### Call your show live on show day

Slug `call-your-show-live-on-show-day`. Guide: https://www.ticketfairy.com/guides/call-your-show-live-on-show-day

Follow what is on now and next on every stage of your event against the event's own clock, and call each cue as it happens. See how late each stage is really running from the times you call, catch a stage up, and report an incident without leaving the page.

For: Running each stage on the day of the show.

What an agent can do: Fai reads what is on now and next on each stage and how late each stage is running, calls a cue standby, live, done or skipped, undoes a call, records or corrects when a cue started or finished, or moves the rest of a stage's day when you ask. She waits for your yes before each call or change. Your own AI assistant can read now and next and move a cue, or the rest of a stage's day, over the MCP server, after your approval in your MCP client.

Command line:

- Show the run of show for the event: `ticketfairy event-os show-day run-of-show <EVENT_ID>`
- Move a cue later by a number of minutes: `ticketfairy event-os show-day move-cue <EVENT_ID> <CUE_ID> --minutes <MINUTES>`

CLI MCP tools that read: `select_event`, `get_run_of_show`.

CLI MCP tools that make changes (not available with `--read-only`): `manage_run_of_show_cue`.

Prompt for Fai: "Neon Tide is live on the Main Stage at <EVENT NAME>, and move the rest of the Main Stage 10 minutes later"

### Check your running order for clashes before show day

Slug `check-your-running-order-for-clashes-before-show-day`. Guide: https://www.ticketfairy.com/guides/check-your-running-order-for-clashes-before-show-day

Have Fai check each day of your event's run of show for overlapping sets, short changeovers, an act booked on two stages, flights that land after soundcheck, sets outside a stage's hours or past curfew, and riders a stage cannot meet. For each problem, Fai suggests up to two fixes she has tried against the rest of the day, and you can apply one in a tap and undo it.

For: Catching clashes in your running order before show day.

What an agent can do: Fai reads the problems on any day with their fixes, applies a fix after you confirm, changes the timing rules, and drafts each act's and each department's call times for you to approve on Today. She never moves a cue on a locked stage or one already called on the day.

Prompt for Fai: "Check the running order for Saturday at <EVENT NAME> and fix the short changeover on the Main Stage"

#### Then: Set a stage's hours from Stages

What an agent can do: Fai changes a stage's changeover, opening and closing times and closed days when you ask, after you confirm.

Prompt for Fai: "The Big Top at <EVENT NAME> closes at 23:00 and needs 20 minutes between acts"

### Plan your run of show and who calls it

Slug `plan-your-run-of-show-and-who-calls-it`. Guide: https://www.ticketfairy.com/guides/plan-your-run-of-show-and-who-calls-it

Build the minute-by-minute run of show for each stage and day of your event, let Fai draft it from your schedule, fix clashes and late finishes before show day, lock it, and name the show callers who run it on the day.

For: Planning the running order for each stage and show day.

What an agent can do: Fai reads the run of show with everything that needs a check, drafts it from your schedule, adds, changes, moves or removes cues, locks or unlocks a day and names or removes show callers. She shows you each change and waits for your yes first, and nothing changes on a locked day. Your own AI assistant can read the run of show, add or move a cue, and lock or unlock a day over the MCP server, where each change waits for your approval in your MCP client.

Command line:

- Show the run of show for the event: `ticketfairy event-os show-day run-of-show <EVENT_ID>`
- Move a cue later by a number of minutes: `ticketfairy event-os show-day move-cue <EVENT_ID> <CUE_ID> --minutes <MINUTES>`

CLI MCP tools that read: `select_event`, `get_run_of_show`.

CLI MCP tools that make changes (not available with `--read-only`): `manage_run_of_show_cue`.

Prompt for Fai: "Draft the run of show for Saturday at <EVENT NAME> with 30 minute changeovers and show me what clashes"

#### Then: Remove a cue

What an agent can do: Fai removes a cue when you ask, after you confirm.

Prompt for Fai: "Remove the confetti cannons cue from Saturday at <EVENT NAME>"

#### Then: Remove a show caller

What an agent can do: Fai removes a show caller when you ask, after you confirm.

Prompt for Fai: "Stop Tom Reyes calling the Harbour Tent at <EVENT NAME>"

### Publish your event line-up and set times

Slug `publish-your-line-up-and-set-times`. Guide: https://www.ticketfairy.com/guides/publish-your-line-up-and-set-times

Choose which acts appear on your public line-up with a photo, bio and links, and let Fai draft the bios. Announce acts in waves, review every change before it goes public, and put the timetable on your event page, your website and any other site, where fans star sets for their own schedule.

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

### Share day sheets with your event's on-site teams

Slug `share-day-sheets-with-your-on-site-teams`. Guide: https://www.ticketfairy.com/guides/share-day-sheets-with-your-on-site-teams

Set up the departments working your event and who leads each one, then print or share a day sheet for each team, performer or stage with only their part of the show day, on any phone and without a sign-in.

For: Giving each on-site team its own plan for the day.

What an agent can do: Fai reads any team's, performer's or stage's day sheet, adds or changes departments and the people in them, makes or turns off a share link, and emails every department lead the link to their own day sheet. She shows you each change or email and waits for your yes first.

Prompt for Fai: "Email every department lead at <EVENT NAME> their day sheet for Saturday"

#### Then: Turn off a shared link

What an agent can do: Fai turns off a day sheet link when you ask, after you confirm.

Prompt for Fai: "Turn off the security day sheet link for Saturday at <EVENT NAME>"

### Show now and next on screens backstage and at the side of the stage

Slug `show-now-and-next-on-backstage-screens`. Guide: https://www.ticketfairy.com/guides/show-now-and-next-on-backstage-screens

Put the act on now, the act next, the time left and how late each stage is running on any TV backstage or at the side of a stage. The TV opens a private link without signing in, and the page updates by itself from your run of show and shows no personal details.

For: Keeping backstage teams on time with the running order.

What an agent can do: Fai makes a backstage TV link for every stage or one stage, lists your TV links with when each was last shown, and stops a link, after you confirm. She never shows a link's address, so copy it in Now and next.

Prompt for Fai: "Make a backstage screen for the side of the Main Stage at <EVENT NAME>"

#### Then: Stop showing a TV

What an agent can do: Fai stops a TV link when you ask, after you confirm.

Prompt for Fai: "Stop the green room TV screen at <EVENT NAME>"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
