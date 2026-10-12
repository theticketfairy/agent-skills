---
name: read-event-reports
description: "Read Ticket Fairy event reports: sales, page views, buyers and what each figure counts. Use when an organiser asks how an event is selling or what a report means."
---

# Read event reports

This skill covers the dashboard reports, what each one counts and how to use the figures on Ticket Fairy. It lists the 11 published guides for this area and what an agent can do for each one.

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

- [Check the weather for your event](#check-the-weather-for-your-event)
- [See how visitors find your event page](#see-how-visitors-find-your-event-page)
- [See how your ticket sales are going](#see-how-your-ticket-sales-are-going)
- [See where your event audiences are strongest](#see-where-your-event-audiences-are-strongest)
- [See which team members sell your tickets](#see-which-team-members-sell-your-tickets)
- [See who visits your event website](#see-who-visits-your-event-website)
- [Share a live ticket sales report with a partner](#share-a-live-ticket-sales-report-with-a-partner)
- [Track which promotion sells your tickets](#track-which-promotion-sells-your-tickets)
- [Understand who buys tickets across your events](#understand-who-buys-tickets-across-your-events)
- [Understand who buys tickets to your event](#understand-who-buys-tickets-to-your-event)
- [Understand your event's referral results](#understand-your-events-referral-results)

### Check the weather for your event

Slug `check-your-event-weather`. Guide: https://www.ticketfairy.com/guides/check-your-event-weather

See the weather forecast for your event's venue on the Performance page, with your event days marked and any severe-weather warning for the area, and see what the date is usually like while the event is still weeks away.

For: Planning an outdoor event around the weather at your venue.

What an agent can do: Fai, the assistant inside your dashboard, reads the same forecast for your event's venue, including any severe-weather warning, and what the date is usually like when the event is further out. You read the weather on your event's Performance page or through Fai.

Prompt for Fai: "What's the weather looking like for <EVENT NAME> on the day, is there any warning out for the venue, and what is that date usually like there"

### See how visitors find your event page

Slug `see-how-visitors-find-your-event-page`. Guide: https://www.ticketfairy.com/guides/see-how-visitors-find-your-event-page

See how many visits your event page receives, where they came from and how many of them reached order confirmation.

For: Choosing where to promote your event next.

What an agent can do: Ask Fai for a date range. She applies it to every traffic result except the referrer list, which always covers the event's full run.

Command line:

- Visits, unique visits and conversions: `ticketfairy event stats <EVENT_ID> --metric traffic`
- The sites that sent you visits, a day at a time: `ticketfairy event stats <EVENT_ID> --metric referrer-by-day`

CLI MCP tools that read: `select_event`, `get_event_performance`.

Prompt for Fai: "Where did the traffic for this event come from, and how many times was the order confirmation page reached"

### See how your ticket sales are going

Slug `check-your-sales`. Guide: https://www.ticketfairy.com/guides/check-your-sales

See how many tickets you have sold and what your event has earned, from the figures across the top of the Performance page to the day-by-day table and the breakdown for every ticket type.

For: Following an on-sale and reporting on it afterwards.

What an agent can do: Fai, the assistant inside your dashboard, reads the same figures and can explain what each one counts. She reads them; the page is where you change anything.

Command line:

- The figures across the top of the page: `ticketfairy event stats <EVENT_ID> --metric summary`
- Sales over time, the same run the Ticket Sales chart plots: `ticketfairy event stats <EVENT_ID> --metric sales --output json`
- The same totals per ticket type: `ticketfairy event stats <EVENT_ID> --metric performance --output json`

CLI MCP tools that read: `select_event`, `get_event_performance`.

Prompt for Fai: "For <EVENT NAME>, tell me how many tickets have sold and what the event has earned after referral rebates, then which ticket type is selling fastest"

### See where your event audiences are strongest

Slug `see-where-your-event-audiences-are-strongest`. Guide: https://www.ticketfairy.com/guides/see-where-your-event-audiences-are-strongest

Compare where ticket buyers are based across all your events, or focus on a series, venue, city, country or any events you choose.

For: Planning where to advertise, tour or grow next.

What an agent can do: Ask Fai to compare where buyers are based across the brand or for any group of events the Geographics page supports. She can find the matching series, venue, host city or host country before reading the report.

Prompt for Fai: "Where are the buyers for our Manchester events based, compare orders and tickets in the leading cities, and tell me which places are strong enough for a local campaign"

### See which team members sell your tickets

Slug `see-which-team-members-sell-your-tickets`. Guide: https://www.ticketfairy.com/guides/see-which-team-members-sell-your-tickets

Use the brand Promoters report to compare every team member's referred visits and credited sales across all your events, and see who is selling the most, who has slowed down and who never shared a link.

For: Deciding who to back and who to bring onto your brand team.

What an agent can do: Ask Fai to read the brand Promoters report for you. She can name the people behind each insight, compare two team members, narrow the report to a period or a group of events, and, with your confirmation, invite the person she recommends to the brand team.

Prompt for Fai: "Look at our brand's Promoters report for the last 90 days, tell me which event-level promoters should join the brand team and why, and who has stopped selling"

### See who visits your event website

Slug `see-who-visits-your-event-website`. Guide: https://www.ticketfairy.com/guides/see-who-visits-your-event-website

See how many page views your event website gets, how many visitors select a ticket button and how many open the ticket checkout, day by day, with the pages and events that draw the most interest.

For: Checking how your website sells tickets.

What an agent can do: Ask Fai for the days you want. She reads the same page views, ticket clicks, checkouts opened and top pages and events for your website.

Prompt for Fai: "How many people visited my <WEBSITE NAME> website in the last 30 days, and which pages and events did they click on most"

### Share a live ticket sales report with a partner

Slug `share-a-live-sales-report`. Guide: https://www.ticketfairy.com/guides/share-a-live-sales-report

Give a venue, co-promoter or sponsor a sales report link that shows the live ticket sales and revenue of the ticket types and add-ons you choose, without giving them a role on your event.

For: Showing a partner the live ticket sales of the part of your event they share in.

What an agent can do: Fai, the assistant inside your dashboard, can make a sales report link for the ticket types and add-ons you name, and she shows it to you and asks you to approve it first. Copy the finished link from the External/3rd-Party Sales Reporting section on the event's Settings page. Sales report links are made in the dashboard or through Fai.

Prompt for Fai: "On <EVENT NAME>, make a sales report link called <NAME> for the <TICKET TYPES> ticket types and the <ADD-ONS> add-ons, <WITH OR WITHOUT> the day-by-day breakdown, and show it to me before you create it"

### Track which promotion sells your tickets

Slug `track-which-promotion-sold-your-tickets`. Guide: https://www.ticketfairy.com/guides/track-which-promotion-sold-your-tickets

Give each advert, post, email or partner a separate tracking link so your event report shows the clicks, orders and ticket revenue each link brings in.

For: Promoting an event in more than one place at once.

What an agent can do: Fai, the assistant inside your dashboard, can read this table for you and say which link brought in the most: she reports the same clicks, orders and revenue, and the same caution that an order counts from the moment it is placed while a refund lowers the revenue. She cannot make a link or delete one, so those stay with you on this page.

Prompt for Fai: "Show me the tracking links on this event and tell me which one brought in the most orders"

### Understand who buys tickets across your events

Slug `understand-who-buys-tickets-across-your-events`. Guide: https://www.ticketfairy.com/guides/understand-who-buys-tickets-across-your-events

Use **Customers** to see everybody who has bought from your brand, which events and tickets they ordered, what they spent and which sales their referrals brought in.

For: Finding repeat customers for your next event.

What an agent can do: In the dashboard, Fai can rank repeat customers and the customers whose referral links drove the most ticket purchases.

Command line:

- Your customers, fifty at a time: `ticketfairy customer list`

Prompt for Fai: "Show me the customers who have ordered tickets for more than one of my events, then separately show the customers whose referral links drove the most ticket purchases"

### Understand who buys tickets to your event

Slug `read-your-audience-demographics`. Guide: https://www.ticketfairy.com/guides/read-your-audience-demographics

Use the Demographics and Devices reports for your event to compare age bands, gender, jobs and employers, see which devices buyers ordered on, and understand what each figure counts.

For: Deciding who to market your next event to.

What an agent can do: Ask Fai for the age figures and for what buyers bought on. Your own AI assistant reads the age figures through our MCP server. Review the Gender and Professions sections in the dashboard.

Command line:

- The age bands shown in the dashboard: `ticketfairy event stats <EVENT_ID> --metric demographics`
- The same figures, ready for a script: `ticketfairy event stats <EVENT_ID> --metric demographics --output json`
- What buyers bought on, from the Devices report: `ticketfairy event stats <EVENT_ID> --metric devices`

CLI MCP tools that read: `select_event`, `get_event_performance`.

Prompt for Fai: "Look at the ages of the people who bought for this event and tell me which band bought the most, then tell me what they bought on, counting refunded and cancelled orders too"

### Understand your event's referral results

Slug `read-your-referral-results`. Guide: https://www.ticketfairy.com/guides/read-your-referral-results

Use the Influencers report to see how much buyers shared your event, how many clicks those shares brought, which referral links led to sales and what you owe in rewards.

For: Running a referral push for an event.

What an agent can do: Fai and your own AI assistant through our MCP server can both get your referral figures and explain what they show.

Command line:

- Your referrers and what each of them brought in: `ticketfairy event stats <EVENT_ID> --metric referrals`
- The same figures, ready for a spreadsheet: `ticketfairy event stats <EVENT_ID> --metric referrals --output csv`

CLI MCP tools that read: `select_event`, `get_event_performance`.

Prompt for Fai: "Look at the referral results for this event and tell me who brought in the most sales and whether the reward is paying for itself"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
