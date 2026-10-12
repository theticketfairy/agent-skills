---
name: email-and-market-to-buyers
description: "Send Ticket Fairy emails and SMS to buyers, design emails, and build event websites and landing pages. Use when an organiser wants to reach their buyers or promote an event."
---

# Email and market to buyers

This skill covers messages to buyers, email design, event websites and landing pages on Ticket Fairy. It lists the 13 published guides for this area and what an agent can do for each one.

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
     Token in `TICKET_FAIRY_API_KEY`. Pass `--output json --non-interactive` in scripts.
   - **MCP.** `ticketfairy mcp --read-only` starts the CLI's MCP server with read tools. Drop
     `--read-only` only when the organiser wants you to make changes.
   - **Fai.** Fai is the assistant inside the organiser's dashboard. When a task is not on the
     command line, give the organiser the suggested prompt to paste into Fai.
   - **Dashboard.** Otherwise, send the organiser the guide link and walk them through it.
4. **Confirm before you change anything.** Show the organiser what you will create, change, send,
   refund or cancel, and wait for their yes. You can do only what their team role allows.
5. **Never take payment.** Buyers pay in the browser checkout. Bank, tax and payout details stay
   in the organiser's own browser.

## Guides

- [Add your own words to the ticket confirmation email](#add-your-own-words-to-the-ticket-confirmation-email)
- [Build a website for your events](#build-a-website-for-your-events)
- [Connect your own web address to your event website](#connect-your-own-web-address-to-your-event-website)
- [Create extra landing pages for your event](#create-extra-landing-pages-for-your-event)
- [Email the people who bought tickets to your event](#email-the-people-who-bought-tickets-to-your-event)
- [Give your promoters artwork to post about your event](#give-your-promoters-artwork-to-post-about-your-event)
- [Let Fai improve your event website](#let-fai-improve-your-event-website)
- [List your events on your website](#list-your-events-on-your-website)
- [Protect, hide and redirect pages on your event website](#protect-hide-and-redirect-pages-on-your-event-website)
- [Save the emails you send buyers, guests and applicants](#save-the-emails-you-send-buyers-guests-and-applicants)
- [Take enquiries and RSVPs on your event website](#take-enquiries-and-rsvps-on-your-event-website)
- [Tell ticket holders where your event is](#tell-ticket-holders-where-your-event-is)
- [Translate your event website](#translate-your-event-website)

### Add your own words to the ticket confirmation email

Slug `add-your-own-words-to-the-confirmation-email`. Guide: https://www.ticketfairy.com/guides/add-your-own-words-to-the-confirmation-email

Add your door time, travel advice and event rules to the confirmation email buyers get with their tickets, and send their replies to an address your team reads.

For: Telling buyers what they need to know when they buy.

What an agent can do: Fai can draft the message from what she knows about the event and show it to you before it is saved. Reading it back afterwards is the check worth doing.

Command line:

- Show the event and its saved settings: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Draft the extra text for the confirmation email for <EVENT NAME>. Cover the door time, the age limit and how to get home, and show it to me before saving"

### Build a website for your events

Slug `build-a-website-for-your-events`. Guide: https://www.ticketfairy.com/guides/build-a-website-for-your-events

Give your festival, venue or club night its own website: Fai drafts it from your events and brand, or you start from a template, then you change the pages, sections and look and publish it for ticket buyers.

For: Building a website for your events.

What an agent can do: Fai, the assistant inside your dashboard, can start a website from your events, your current website or a description, add and change pages and sections, change the design, publish the website and put an earlier version back. She shows you each change and waits for your yes first. To start from a flyer or PDF, upload it in the dashboard.

Prompt for Fai: "Build a website for <BRAND NAME> from our upcoming events, then show me what you made before you publish it"

### Connect your own web address to your event website

Slug `connect-your-own-web-address-to-your-event-website`. Guide: https://www.ticketfairy.com/guides/connect-your-own-web-address-to-your-event-website

Put your event website on a web address you already own, such as www.yourfestival.com, so ticket buyers find you under your own name. You add the records the dashboard shows at your domain provider, and you choose which address is the main one.

For: Putting your event website on your own domain.

What an agent can do: Fai can connect your domain, tell you the records to add, check them again, make an address your main one and disconnect a domain. She asks before each change. You add the records yourself at your domain provider.

Prompt for Fai: "Connect www.<YOUR DOMAIN> to my <WEBSITE NAME> website and tell me the records to add at my domain provider"

### Create extra landing pages for your event

Slug `create-extra-landing-pages-for-your-event`. Guide: https://www.ticketfairy.com/guides/create-extra-landing-pages-for-your-event

Give one event extra pages at their own addresses, each with its own name, dates, venue, images, description or ticket types, so every ad campaign, sponsor or audience lands on a page made for them while every ticket sold is a ticket for the same event.

For: Giving different audiences their own page for one event.

What an agent can do: Fai, the assistant inside your dashboard, can list an event's extra pages and create one with its own address, name, dates, description and ticket types, including whether each ticket type stays on the main event page. She asks you to approve each page before she creates it. To upload a flyer or background image from your computer, use the dashboard.

Prompt for Fai: "Create an extra landing page for <EVENT NAME> at the address <PAGE ADDRESS>, named <PAGE NAME>, for <AUDIENCE OR CAMPAIGN>. Offer only the <TICKET TYPE> ticket type on it and keep that ticket type on the main event page too. Show me the details before you create it"

### Email the people who bought tickets to your event

Slug `email-your-buyers`. Guide: https://www.ticketfairy.com/guides/email-your-buyers

Send the doors time, the set times, a venue change or a thank-you to everyone attending, to one ticket type or to the waiting list, now or at a time you choose, and see who opened it.

For: Telling ticket holders what they need to know before, during and after the event.

What an agent can do: Fai, the assistant inside your dashboard, can draft the message with you, send it to the audience you name, now or at a time you set, and send a test copy to you first. She shows you the subject, the message and who will receive it, and asks you to approve before anything is sent.

Command line:

- Send a message described in a file: subject, message and audience: `ticketfairy messaging send --event-id <EVENT_ID> --from-file <FILE>`
- List the messages sent for the event: `ticketfairy messaging list --event-id <EVENT_ID>`

Prompt for Fai: "Draft an email to <AUDIENCE, SUCH AS EVERYONE ATTENDING OR VIP TICKET HOLDERS> of <EVENT NAME> about <WHAT THEY NEED TO KNOW>, send a test to me first, then show me the final message and who will get it before sending"

### Give your promoters artwork to post about your event

Slug `give-your-promoters-artwork-to-post`. Guide: https://www.ticketfairy.com/guides/give-your-promoters-artwork-to-post

Keep the flyers, videos and ready-to-paste captions for your event on its Marketing Assets page, where every promoter downloads them beside their own promoter link.

For: Getting your promoters posting the right artwork.

What an agent can do: Fai, the assistant inside your dashboard, can add an asset from a link to a file that is already online, set its name, channel, caption, folder and tags, hide it or schedule when your promoters see it, email your promoters about it and tell you how often each asset has been downloaded. She asks you to approve every change before she makes it. To add a file from your computer, use **Add asset**{marketingAssets.browser.addHere} in the dashboard.

Prompt for Fai: "Add the line-up poster at <FILE LINK> to the marketing assets for <EVENT NAME>, sized for instagram stories, with a caption our promoters can paste, and keep it hidden from promoters until <DATE AND TIME>"

### Let Fai improve your event website

Slug `let-fai-improve-your-event-website`. Guide: https://www.ticketfairy.com/guides/let-fai-improve-your-event-website

Fai checks your event website and suggests what to fix next, drafts missing text, rewords what you have, suggests a look from your logo and, if you switch it on, lists new events by herself. You decide what goes on the website, and every change can be undone.

For: Keeping your event website current with Fai.

What an agent can do: Fai can list her ideas for a website, apply, dismiss, undo or bring back each one, check the website again, draft the missing text, reword text and suggest a theme. She asks before each change to your website.

Prompt for Fai: "What are your ideas for my <WEBSITE NAME> website? apply the ones about events and show me the text ones first"

### List your events on your website

Slug `list-your-events-on-your-website`. Guide: https://www.ticketfairy.com/guides/list-your-events-on-your-website

Show your upcoming events on your event website with live dates, prices and sold-out labels: every public event automatically or only the ones you choose, events sold on other websites, a What's on calendar, and events from partner brands that say yes.

For: Showing your events on your website.

What an agent can do: Fai can switch your website between automatic and chosen events, add an event from its ticket link, change the order, add a What's on calendar, and ask another brand to let you list its events. She asks before each change.

Prompt for Fai: "Show only our summer festival events on my <WEBSITE NAME> website, with the opening night first"

### Protect, hide and redirect pages on your event website

Slug `protect-hide-and-redirect-pages-on-your-event-website`. Guide: https://www.ticketfairy.com/guides/protect-hide-and-redirect-pages-on-your-event-website

Give a crew, artist or guest page on your event website a password, keep a page out of search engines, choose what visitors see at an address you do not have, and send old addresses from last year's event to the right page.

For: Controlling who finds each page of your website.

What an agent can do: Fai can hide a page from search engines, set, change or remove its password, choose the page visitors see at an unknown address and add or remove redirects. She asks before each change.

Prompt for Fai: "Password-protect the Crew briefing page on my <WEBSITE NAME> website and hide it from search engines"

### Save the emails you send buyers, guests and applicants

Slug `save-the-emails-you-send`. Guide: https://www.ticketfairy.com/guides/save-the-emails-you-send

Draft an invitation, an application answer or a gift certificate message once, then pick it by name each time you send it, so every email you send buyers, guests and applicants sounds like you.

For: Sending invitations, application answers and gift certificate emails in your own wording.

What an agent can do: Keeping the templates is dashboard work. Fai, the assistant inside your dashboard, can draft the wording for one before you paste it in.

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Draft the email we send acts we have accepted for <EVENT NAME>, with the load-in time and the parking left as blanks for me to fill"

### Take enquiries and RSVPs on your event website

Slug `take-enquiries-and-rsvps-on-your-event-website`. Guide: https://www.ticketfairy.com/guides/take-enquiries-and-rsvps-on-your-event-website

Add a contact, private hire or RSVP form to your event website with the questions you need, get an email for each new reply, then read, sort and download the replies in one place.

For: Collecting enquiries and RSVPs from your website.

What an agent can do: Fai can add a contact or RSVP form with your own questions or the private hire questions, read the replies for the days you name and mark them read, archived or spam. She asks before each change. To download the replies as a file, use Download replies in the dashboard.

Prompt for Fai: "Add a private hire enquiry form to the Private hire page of my <WEBSITE NAME> website"

### Tell ticket holders where your event is

Slug `announce-your-venue-location`. Guide: https://www.ticketfairy.com/guides/announce-your-venue-location

Save the location details, choose when future buyers can see the venue, and email a confirmed venue update to ticket holders and RSVPs.

For: Announcing an event location or venue change to the people attending.

What an agent can do: Fai can save the location information and email it to your ticket holders and RSVPs. She shows you the event and the location text and asks for your approval before sending, and the email cannot be recalled after you approve it. Set whether the venue is hidden on the Details page first, because the announcement leaves that setting as it is.

Prompt for Fai: "Announce the venue location for <EVENT NAME> with this location information: <LOCATION INFORMATION>. Show me the event and the text, and ask for my approval before sending"

### Translate your event website

Slug `translate-your-event-website`. Guide: https://www.ticketfairy.com/guides/translate-your-event-website

Fai translates your event website into the languages your ticket buyers read, you check her texts, and you put each language live when it is ready, with a language menu for visitors.

For: Offering your website in more languages.

What an agent can do: Fai can translate your website into the languages you name, show how far she has got, accept, edit or translate a text again, and publish or take off a language. She asks before each change.

Prompt for Fai: "Translate my <WEBSITE NAME> website into French and German and tell me when the texts are ready to check"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
