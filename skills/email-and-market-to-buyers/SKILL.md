---
name: email-and-market-to-buyers
description: "Send Ticket Fairy emails and SMS to buyers, design emails, and build event websites and landing pages. Use when an organiser wants to reach their buyers or promote an event."
---

# Email and market to buyers

This skill covers messages to buyers, email design, event websites and landing pages on Ticket Fairy. It lists the 25 published guides for this area and what an agent can do for each one.

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

- [Add your own words to the ticket confirmation email](#add-your-own-words-to-the-ticket-confirmation-email)
- [Build a website at your event's link](#build-a-website-at-your-events-link)
- [Build a website for your events](#build-a-website-for-your-events)
- [Connect your own domain to the website for your events](#connect-your-own-domain-to-the-website-for-your-events)
- [Create extra landing pages for your event](#create-extra-landing-pages-for-your-event)
- [Design the look of the emails about your events](#design-the-look-of-the-emails-about-your-events)
- [Email or text your fans and ticket holders from your brand](#email-or-text-your-fans-and-ticket-holders-from-your-brand)
- [Email your ticket buyers about your event](#email-your-ticket-buyers-about-your-event)
- [Find your event emails and templates from the previous Messaging pages](#find-your-event-emails-and-templates-from-the-previous-messaging-pages)
- [Get your own text number to text fans about your events](#get-your-own-text-number-to-text-fans-about-your-events)
- [Give your promoters artwork to post about your event](#give-your-promoters-artwork-to-post-about-your-event)
- [Let Fai improve your event website](#let-fai-improve-your-event-website)
- [List your events on your website](#list-your-events-on-your-website)
- [Manage one event's emails and texts in Messaging](#manage-one-events-emails-and-texts-in-messaging)
- [Protect, hide and redirect pages on your event website](#protect-hide-and-redirect-pages-on-your-event-website)
- [Reuse email, text and gift certificate templates across your events](#reuse-email-text-and-gift-certificate-templates-across-your-events)
- [Review the messages Fai suggests for your events](#review-the-messages-fai-suggests-for-your-events)
- [Save the emails you send buyers, guests and applicants](#save-the-emails-you-send-buyers-guests-and-applicants)
- [Sell tickets on your own website](#sell-tickets-on-your-own-website)
- [Send automatic messages before and after every event](#send-automatic-messages-before-and-after-every-event)
- [Set quiet hours and a weekly marketing limit for your events](#set-quiet-hours-and-a-weekly-marketing-limit-for-your-events)
- [Show your sponsors on your tickets and event page](#show-your-sponsors-on-your-tickets-and-event-page)
- [Take enquiries and RSVPs on your event website](#take-enquiries-and-rsvps-on-your-event-website)
- [Tell ticket holders where your event is](#tell-ticket-holders-where-your-event-is)
- [Translate your event website](#translate-your-event-website)

### Add your own words to the ticket confirmation email

Slug `add-your-own-words-to-the-confirmation-email`. Guide: https://www.ticketfairy.com/guides/add-your-own-words-to-the-confirmation-email

Add your door time, travel advice and event rules to the confirmation email buyers get with their tickets, and send their replies to an address your team reads.

For: Telling buyers what they need to know when they buy.

What an agent can do: Fai can draft the message from what she knows about the event and show it to you before it is saved. Read it again afterwards to check it.

Command line:

- Show the event and its saved settings: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Draft the extra text for the confirmation email for <EVENT NAME>. Cover the door time, the age limit and how to get home, and show it to me before saving"

#### Then: Change the message as the event nears

What an agent can do: Fai can show you the current text and draft the replacement.

Command line:

- Show the event and its saved settings: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "What does the confirmation email for <EVENT NAME> currently say, and draft a version with the new door time in it"

#### Then: Take the message off again

What an agent can do: Fai can open the card so you can remove the text yourself.

Command line:

- Show the event and its saved settings: `ticketfairy event get <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open the confirmation email settings for <EVENT NAME>"

### Build a website at your event's link

Slug `build-a-website-at-your-event-link`. Guide: https://www.ticketfairy.com/guides/build-a-website-at-your-event-link

Give one event its own website with as many pages as it needs, such as the line-up, tickets, travel and practical information, and show it at the event link you already share in place of the standard event page.

For: Building a multi-page website for one event.

What an agent can do: Fai can start the event site, change its pages and sections, show it at your event's link and put the standard event page back. She shows you each change and waits for your yes first.

Prompt for Fai: "Build a website for <EVENT NAME> at its event link, and show me the draft before you publish it"

#### Then: Check what Fai drafted

What an agent can do: Fai lists what she drafted and marks a section as checked, or publishes an entry, only after you confirm it is right.

Prompt for Fai: "Show me what you drafted on the event site for <EVENT NAME> that I still need to check"

#### Then: Publish your later changes

What an agent can do: Fai publishes your latest changes to the event site after you confirm.

Prompt for Fai: "Publish the changes on the event site for <EVENT NAME>"

#### Then: Show the standard event page again

What an agent can do: Fai takes the site off your event's link and shows the standard event page again after you confirm.

Prompt for Fai: "Show the standard event page at the link for <EVENT NAME> again"

### Build a website for your events

Slug `build-a-website-for-your-events`. Guide: https://www.ticketfairy.com/guides/build-a-website-for-your-events

Give your festival, venue or club night its own website: Fai drafts it from your events and brand, or you start from a template, then you change the pages, sections and look and publish it for ticket buyers.

For: Building a website for your events.

What an agent can do: Fai can start a website from your events, your current website or a description, add and change pages and sections, change the design, publish the website and put an earlier version back. She shows you each change and waits for your yes first. To start from a flyer or PDF, upload it in the dashboard.

Prompt for Fai: "Build a website for <BRAND NAME> from our upcoming events, then show me what you made before you publish it"

#### Then: Publish your later changes

What an agent can do: Fai publishes your latest changes after you confirm.

Prompt for Fai: "Publish the changes on my <WEBSITE NAME> website"

#### Then: Go back to an earlier version

What an agent can do: Fai lists your published versions and puts one back on your live website after you confirm.

Prompt for Fai: "Put my <WEBSITE NAME> website back to the version published on <DATE>"

#### Then: Take your website offline

What an agent can do: Fai takes a website offline after you confirm.

Prompt for Fai: "Take my <WEBSITE NAME> website offline"

### Connect your own domain to the website for your events

Slug `connect-your-own-web-address-to-your-event-website`. Guide: https://www.ticketfairy.com/guides/connect-your-own-web-address-to-your-event-website

Put your event website on a web address you already own, such as www.yourfestival.com, so ticket buyers find you under your own name. You add the records the dashboard shows at your domain provider, and you choose which address is the main one.

For: Putting your event website on your own domain.

What an agent can do: Fai can connect your domain, tell you the records to add, check them again, make an address your main one and disconnect a domain. She asks before each change. You add the records yourself at your domain provider.

Prompt for Fai: "Connect www.<YOUR DOMAIN> to my <WEBSITE NAME> website and tell me the records to add at my domain provider"

#### Then: Make your address secure

What an agent can do: Fai checks your records again, tells you the step your address is at and the record to change, and makes it your main address after you confirm.

Prompt for Fai: "Is www.<YOUR DOMAIN> secure yet? If it is, make it the main address of my <WEBSITE NAME> website"

#### Then: Put your event site on your own address

What an agent can do: Fai connects your own address to your event site, tells you the records to add, checks them and makes the address primary after you confirm.

Prompt for Fai: "Connect www.<YOUR DOMAIN> to the event site of <EVENT NAME> and make it the main address when it is secure"

#### Then: Add another free address

What an agent can do: Fai adds a free web address after you confirm.

Prompt for Fai: "Add the free web address <NAME>.sites.ticketfairy.com to my <WEBSITE NAME> website"

#### Then: Disconnect your domain

What an agent can do: Fai disconnects a domain after you confirm.

Prompt for Fai: "Disconnect www.<YOUR DOMAIN> from my <WEBSITE NAME> website"

### Create extra landing pages for your event

Slug `create-extra-landing-pages-for-your-event`. Guide: https://www.ticketfairy.com/guides/create-extra-landing-pages-for-your-event

Give one event extra pages at their own addresses, each with its own name, dates, venue, images, description or ticket types, while every ticket sold is a ticket for the same event.

For: Giving different audiences their own page for one event.

What an agent can do: Fai can list an event's extra pages and create one with its own address, name, dates, description and ticket types, including whether each ticket type stays on the main event page. She asks you to approve each page before she creates it. To upload a flyer or background image from your computer, use the dashboard.

Prompt for Fai: "Create an extra landing page for <EVENT NAME> at the address <PAGE ADDRESS>, named <PAGE NAME>, for <AUDIENCE OR CAMPAIGN>. Offer only the <TICKET TYPE> ticket type on it and keep that ticket type on the main event page too. Show me the details before you create it"

#### Then: Change an extra page

What an agent can do: Fai can change an extra page after you approve the change. When she updates a page, she replaces its settings with the ones she sends, so the prompt asks her to keep everything else on the page as it is.

Prompt for Fai: "On <EVENT NAME>, change the <PAGE NAME> extra page so that <CHANGE>. Keep everything else on the page as it is and show me the change before you save it"

#### Then: Delete an extra page

What an agent can do: Fai can delete an extra page once you approve it.

Prompt for Fai: "Delete the <PAGE NAME> extra page from <EVENT NAME>. Show me which page it is before you delete it"

### Design the look of the emails about your events

Slug `design-the-look-of-your-brands-emails`. Guide: https://www.ticketfairy.com/guides/design-the-look-of-your-brands-emails

Set the header and logo, colours, fonts and footer that every email to your ticket holders and fans is built on, starting from a ready-made design that already uses your brand kit, and choose the one your emails use by default.

For: Brand teams who want every email to carry their own look.

What an agent can do: Fai can list your designs, make one from your brand kit, change it, make it your default or delete it. She shows you the design and asks you to approve before she saves, changes the default or deletes anything.

Prompt for Fai: "Make an email design from our brand kit with our logo at the top and our address in the footer, show it to me, then make it our default"

#### Then: Delete a design

What an agent can do: Fai can delete one of your designs after she names it and tells you which emails switch to your default.

Prompt for Fai: "Delete the <DESIGN NAME> email design and tell me which emails move to our default first"

### Email or text your fans and ticket holders from your brand

Slug `email-or-text-your-fans-and-ticket-holders`. Guide: https://www.ticketfairy.com/guides/email-or-text-your-fans-and-ticket-holders

Email or text your ticket holders and fans from Messaging: start from a template or a Fai design, choose who gets it in plain words, test it, then send now or later and follow the results.

For: Sending emails and texts to ticket holders and fans across your events.

What an agent can do: Fai can draft an email or a text with you, start it from one of your templates, save it as a draft, count who it reaches, run the checks, send a test to you or to up to 20 people on your team, and send or schedule it. She shows you the message, the group and the number of people, and asks you to approve before she saves, sends or schedules anything.

Prompt for Fai: "Draft an email to <GROUP, SUCH AS EVERYONE WITH A TICKET OR FANS WHO HAVEN'T BOUGHT YET> for <EVENT NAME> about <WHAT THEY NEED TO KNOW>, send a test to me and <TEAMMATE NAME>, then show me the checks and how many people it goes to before you schedule it for <DATE AND TIME>"

#### Then: Change or cancel a scheduled message

What an agent can do: Fai can cancel a scheduled message and put it back in your drafts, after she shows you which message it is and when it was due to go out.

Prompt for Fai: "Cancel the schedule on <MESSAGE NAME> and put it back in my drafts"

#### Then: Send a message again

What an agent can do: Fai can copy a message into a new draft and change the event or wording before you check and send it.

Prompt for Fai: "Copy <MESSAGE NAME> into a new draft for <EVENT NAME> and show it to me"

### Email your ticket buyers about your event

Slug `email-your-buyers`. Guide: https://www.ticketfairy.com/guides/email-your-buyers

Send the doors time, the set times, a venue change or a thank-you to everyone attending, to one ticket type or to the waiting list, now or at a time you choose, and see who opened it.

For: Telling ticket holders what they need to know before, during and after the event.

What an agent can do: Fai can draft the message with you, send it to the audience you name, now or at a time you set, and send a test copy to you first. She shows you the subject, the message and who will receive it, and asks you to approve before anything is sent.

Command line:

- Send a message described in a file: subject, message and audience: `ticketfairy messaging send --event-id <EVENT_ID> --from-file <FILE>`
- List the messages sent for the event: `ticketfairy messaging list --event-id <EVENT_ID>`

Prompt for Fai: "Draft an email to <AUDIENCE, SUCH AS EVERYONE ATTENDING OR VIP TICKET HOLDERS> of <EVENT NAME> about <WHAT THEY NEED TO KNOW>, send a test to me first, then show me the final message and who will get it before sending"

#### Then: Send it at a time you choose

What an agent can do: Fai can schedule the message for the time you name, after showing you the message and the audience. The CLI sends from a file that names the schedule time.

Prompt for Fai: "Schedule an email to <AUDIENCE> of <EVENT NAME> for <DATE AND TIME> about <WHAT THEY NEED TO KNOW>, and show me the message and who will get it before you schedule it"

#### Then: Cancel a scheduled email

What an agent can do: You cancel a scheduled message in the dashboard. Fai, MCP and the CLI do not cancel one.

#### Then: Save a message to send again

What an agent can do: You save and choose templates in the dashboard. Fai drafts each message fresh with you.

Prompt for Fai: "Draft a doors-and-timings email for <EVENT NAME> in the same style as the one I sent for <PREVIOUS EVENT NAME>"

### Find your event emails and templates from the previous Messaging pages

Slug `find-your-emails-and-templates-from-the-previous-messaging-pages`. Guide: https://www.ticketfairy.com/guides/find-your-emails-and-templates-from-the-previous-messaging-pages

See the emails and texts your team sent or scheduled to ticket holders from the previous Messaging pages in Messages, with their results, send one again, and find your email templates and Mailchimp list in their new places.

For: Teams moving to Messaging from the previous Messaging and Email Templates pages.

What an agent can do: Fai can list the messages sent from the previous Messaging pages with their results, and copy one into a new draft. She shows you the draft before you check and send it.

Prompt for Fai: "Find the emails we sent for <EVENT NAME> from the previous Messaging page, show me how each did, and copy the best one into a new draft for <NEW EVENT NAME>"

### Get your own text number to text fans about your events

Slug `get-your-own-text-number-for-marketing-texts`. Guide: https://www.ticketfairy.com/guides/get-your-own-text-number-for-marketing-texts

Request a phone number for your brand from Messaging settings, see the monthly charge and the price per text part before you agree, and send every text from it once it is ready. Event information texts carry no charge per text, and marketing texts are charged for each text part.

For: Promoters and venues who want to text their fans and ticket holders from their own number.

What an agent can do: Fai can show whether your brand has a text number and what it costs, request one with the country, business name and contact email you give her, and give a number up. She shows you the monthly charge and the price per text part and asks you to agree before she requests a number.

Prompt for Fai: "Get us a UK text number under the name <BUSINESS NAME>, updates to <EMAIL ADDRESS>, and show me the monthly charge and price per text before you request it"

#### Then: Give up your text number

What an agent can do: Fai can give up your brand's text number after she shows you which number it is and asks you to confirm.

Prompt for Fai: "Give up our text number and stop the monthly charge"

### Give your promoters artwork to post about your event

Slug `give-your-promoters-artwork-to-post`. Guide: https://www.ticketfairy.com/guides/give-your-promoters-artwork-to-post

Keep the flyers, videos and ready-to-paste captions for your event on its Marketing Assets page, where every promoter downloads them beside their own promoter link.

For: Getting your promoters posting the right artwork.

What an agent can do: Fai can add an asset from a link to a file that is already online, set its name, channel, caption, folder and tags, hide it or schedule when your promoters see it, email your promoters about it and tell you how often each asset has been downloaded. She asks you to approve every change before she makes it. To add a file from your computer, use **Add asset** in the dashboard.

Prompt for Fai: "Add the line-up poster at <FILE LINK> to the marketing assets for <EVENT NAME>, sized for instagram stories, with a caption our promoters can paste, and keep it hidden from promoters until <DATE AND TIME>"

#### Then: Share one set across every event

What an agent can do: Fai adds and changes brand assets the same way when you name the brand instead of an event, and asks you to approve each change. She needs a link to a file that is already online.

Prompt for Fai: "Add our logo pack at <FILE LINK> to the brand marketing assets so every event gets it"

### Let Fai improve your event website

Slug `let-fai-improve-your-event-website`. Guide: https://www.ticketfairy.com/guides/let-fai-improve-your-event-website

Fai checks your event website and suggests what to fix next, drafts missing text, rewords what you have, suggests a look from your logo and, if you switch it on, lists new events by herself. You decide what goes on the website, and every change can be undone.

For: Keeping your event website current with Fai.

What an agent can do: Fai can list her ideas for a website, apply, dismiss, undo or bring back each one, check the website again, draft the missing text, reword text and suggest a theme. She asks before each change to your website.

Prompt for Fai: "What are your ideas for my <WEBSITE NAME> website? Apply the ones about events and show me the text ones first"

#### Then: Undo an idea you applied

What an agent can do: Fai undoes an applied idea, or brings back a dismissed one, after you confirm.

Prompt for Fai: "Undo the last idea applied on my <WEBSITE NAME> website"

### List your events on your website

Slug `list-your-events-on-your-website`. Guide: https://www.ticketfairy.com/guides/list-your-events-on-your-website

Show your upcoming events on your event website with live dates, prices and sold-out labels: every public event automatically or only the ones you choose, events sold on other websites, a What's on calendar, and events from partner brands that say yes.

For: Showing your events on your website.

What an agent can do: Fai can switch your website between automatic and chosen events, add an event from its ticket link, change the order, add a What's on calendar, and ask another brand to let you list its events. She asks before each change.

Prompt for Fai: "Show only our summer festival events on my <WEBSITE NAME> website, with the opening night first"

#### Then: List events from another brand

What an agent can do: Fai asks a brand for you from a link to one of its events, and lists its events once the brand approves. She asks before each change.

Prompt for Fai: "Ask the brand behind <EVENT LINK> if we can list their events on my <WEBSITE NAME> website"

#### Then: Answer a request to list your events

What an agent can do: Fai lists the requests to list your events and approves, declines or stops one after you confirm.

Prompt for Fai: "Which websites asked to list our events? Approve the one from <BRAND NAME>"

### Manage one event's emails and texts in Messaging

Slug `manage-one-events-emails-and-texts-in-messaging`. Guide: https://www.ticketfairy.com/guides/manage-one-events-emails-and-texts-in-messaging

Open Messaging from an event to see only that event's messages, Fai's suggestions, automatic messages, templates and Mailchimp list, and start new emails and texts that are already about it.

For: Promoters and venue teams working on the messages for one event.

What an agent can do: Fai can list one event's messages, automatic messages and templates, and draft, schedule or send a message about it. She shows you the message and who it goes to, and asks you to approve before she saves, sends or schedules anything.

Prompt for Fai: "Show me every email and text for <EVENT NAME>, what is scheduled next and which automatic messages will go out for it"

### Protect, hide and redirect pages on your event website

Slug `protect-hide-and-redirect-pages-on-your-event-website`. Guide: https://www.ticketfairy.com/guides/protect-hide-and-redirect-pages-on-your-event-website

Give a crew, artist or guest page on your event website a password, keep a page out of search engines, choose what visitors see at an address you do not have, and send old addresses from last year's event to the right page.

For: Controlling who finds each page of your website.

What an agent can do: Fai can hide a page from search engines, set, change or remove its password, choose the page visitors see at an unknown address and add or remove redirects. She asks before each change.

Prompt for Fai: "Password-protect the Crew briefing page on my <WEBSITE NAME> website and hide it from search engines"

#### Then: Change or remove a page password

What an agent can do: Fai changes or removes a page password after you confirm.

Prompt for Fai: "Remove the password from the <PAGE NAME> page on my <WEBSITE NAME> website"

### Reuse email, text and gift certificate templates across your events

Slug `reuse-email-text-and-gift-certificate-templates`. Guide: https://www.ticketfairy.com/guides/reuse-email-text-and-gift-certificate-templates

Keep the words you send for every event as templates for emails, texts and the gift certificate email, start any message from one, and switch off, copy or change them as your team needs.

For: Teams who send the same kinds of message for every event.

What an agent can do: Fai can list your templates, save a message as a template, change one, copy it, switch it off or on, and start a message from it. She shows you the template and asks you to approve before she saves, copies or switches anything.

Prompt for Fai: "Save <MESSAGE NAME> as a template for every event called <TEMPLATE NAME>, then switch off our old <OLD TEMPLATE NAME> template"

#### Then: Copy a template

What an agent can do: Fai can copy one of your templates, and change the copy with you before she saves it.

Prompt for Fai: "Copy our <TEMPLATE NAME> template and change the copy for <EVENT NAME>"

#### Then: Switch a template off or on

What an agent can do: Fai can switch one of your email or gift certificate templates off or on after she names it.

Prompt for Fai: "Switch off our <TEMPLATE NAME> email template"

#### Then: Upload or change your own HTML design

What an agent can do: Fai can add an HTML design to an event's templates from a zip file already uploaded to your dashboard, after she confirms the event and the name with you. She can't upload the file for you, and you change an uploaded design on the previous Email templates page.

Prompt for Fai: "Add the email design in <ADDRESS OF THE UPLOADED ZIP FILE> to <EVENT NAME>'s templates as <TEMPLATE NAME>"

#### Then: Delete a text template

What an agent can do: Fai can delete one of your text templates after she names it.

Prompt for Fai: "Delete our <TEMPLATE NAME> text template"

### Review the messages Fai suggests for your events

Slug `review-the-messages-fai-suggests-for-your-events`. Guide: https://www.ticketfairy.com/guides/review-the-messages-fai-suggests-for-your-events

Preview the emails Fai prepares when an event reaches a good moment to message, then edit, schedule, send or dismiss each one, or switch on the automatic message she suggests.

For: Promoters and venue teams deciding which ready-made messages go to their fans.

What an agent can do: Fai can list the suggestions waiting for your team, open one as a draft, schedule it, send it, switch on the automatic message she suggests, or dismiss it with your reason. She shows you the message, the group and the number of people, and asks you to approve before she schedules or sends anything.

Prompt for Fai: "Show me the messages you suggest for my events this week, with who each one goes to and when, and wait for me to say which ones to schedule"

#### Then: Ask Fai for new ideas

What an agent can do: Fai can look at your events again and list what she suggests now.

Prompt for Fai: "Look at my upcoming events again and tell me what you would send this week"

#### Then: Switch Fai's suggestions off

What an agent can do: Fai can switch her suggestions off or on for your brand, after she shows you the change.

Prompt for Fai: "Stop suggesting messages for this brand"

### Save the emails you send buyers, guests and applicants

Slug `save-the-emails-you-send`. Guide: https://www.ticketfairy.com/guides/save-the-emails-you-send

Draft an invitation, an application answer or a gift certificate message once, then pick it by name each time you send it, so every email you send buyers, guests and applicants sounds like you.

For: Sending invitations, application answers and gift certificate emails in your own wording.

What an agent can do: You keep your templates in the dashboard, and Fai can draft the wording for one before you paste it in.

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Draft the email we send acts we have accepted for <EVENT NAME>, with the load-in time and the parking left as blanks for me to fill"

#### Then: Work from one you already have

What an agent can do: Copying and previewing are dashboard work. Fai can rewrite the wording of a message you paste to her, in your brand's voice.

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Rewrite this email so it is shorter and sounds like our other messages to buyers"

### Sell tickets on your own website

Slug `sell-tickets-on-your-own-website`. Guide: https://www.ticketfairy.com/guides/sell-tickets-on-your-own-website

Create a website embed and paste its snippet into your own page, so buyers choose tickets, pay by card and receive their confirmation without leaving your website.

For: Selling tickets from your own website.

What an agent can do: Fai can create, view, edit and turn off Event Embeds for a brand, then give you the ready-to-copy snippet. She asks before she creates or changes an embed.

Prompt for Fai: "Create a website checkout for this event on my website, ask me for its address first, and give me the snippet to paste before you make any later changes."

#### Then: Test the checkout after changing your website

What an agent can do: Fai can review the saved embed setup and its allowed-site settings. You still complete the buyer test on your own website. MCP and the CLI do not test a browser checkout.

Prompt for Fai: "Review the checkout embed for <EVENT NAME>, including its allowed websites and current setup, so I can test the checkout on phone and desktop"

#### Then: Install the WordPress plugin

What an agent can do: Install the plugin and edit your ticket pages in WordPress.

### Send automatic messages before and after every event

Slug `send-automatic-messages-before-and-after-every-event`. Guide: https://www.ticketfairy.com/guides/send-automatic-messages-before-and-after-every-event

Switch on ready-made messages once, such as know before you go, a thank-you or a last chance, and each goes out for every event, one event series or one event at the moment you set.

For: Promoters and venues who run many events and send the same messages for each.

What an agent can do: Fai can list the automatic messages and your event series, set one up for every event, for one event series or for one event, change its timing, group or wording, and pause, resume or delete it. She shows you the message and when it goes out, and asks you to approve before she switches one on.

Prompt for Fai: "Switch on the thank you for coming email for every event, rewritten in our voice, and show me the message and when it goes out before you switch it on"

#### Then: Pause or resume an automatic message

What an agent can do: Fai can pause or resume an automatic message, after she shows you which one and what changes.

Prompt for Fai: "Pause the event-day reminder text until I say so"

#### Then: Change an automatic message

What an agent can do: Fai can change the timing, group or wording of an automatic message and shows you the change before she saves it.

Prompt for Fai: "Send the know before you go email three days before each event instead of two"

### Set quiet hours and a weekly marketing limit for your events

Slug `set-quiet-hours-and-a-weekly-marketing-limit`. Guide: https://www.ticketfairy.com/guides/set-quiet-hours-and-a-weekly-marketing-limit

Choose the hours when marketing texts wait instead of waking your fans, how many marketing messages a week your team can send before the checks warn you, and whether Fai suggests messages for your events.

For: Brand teams deciding when and how often fans hear from them.

What an agent can do: Fai can show your quiet hours, weekly marketing limit and whether her suggestions are on, and change any of them. She shows you the change and asks you to approve it before she saves.

Prompt for Fai: "Hold marketing texts between 9pm and 10am and warn me after 2 marketing messages a week"

### Show your sponsors on your tickets and event page

Slug `show-your-sponsors-on-your-tickets-and-event-page`. Guide: https://www.ticketfairy.com/guides/show-your-sponsors-on-your-tickets-and-event-page

Add your event's sponsors with their logos and websites, choose whether each one shows on your PDF tickets, on your event page or both, put them in order, and give a VIP ticket type sponsors of its own.

For: Promoters, festivals and venues with sponsors to show on tickets and the event page.

What an agent can do: Fai can list your event's sponsors, add, change, remove and reorder them, choose where each one shows, and give a ticket type its own sponsors. She shows you each change and asks you to approve it before saving. Upload logo files in the dashboard, or give Fai their web addresses, because Fai cannot upload files.

Prompt for Fai: "On <EVENT NAME>, add <SPONSOR NAME> as a sponsor with the logo at <LOGO ADDRESS> and the website <WEBSITE>, and show it on tickets and on the event page. Show me the change before you save it"

#### Then: Show your sponsors on your event website

What an agent can do: Fai can set a Sponsors section on your website to show an event's sponsors once you approve the change.

Prompt for Fai: "On my <WEBSITE NAME> website, make the Sponsors section on the <PAGE NAME> page show the sponsors of <EVENT NAME>"

#### Then: Change where a sponsor shows

What an agent can do: Fai can turn a sponsor on or off for tickets or the event page once you approve the change.

Prompt for Fai: "On <EVENT NAME>, stop showing <SPONSOR NAME> on the event page and keep it on the tickets"

#### Then: Change a sponsor's details

What an agent can do: Fai can change a sponsor's name, logo address, website and tier once you approve the change.

Prompt for Fai: "On <EVENT NAME>, change the website of <SPONSOR NAME> to <WEBSITE>"

#### Then: Remove a sponsor

What an agent can do: Fai can remove a sponsor once you approve it.

Prompt for Fai: "Remove <SPONSOR NAME> from the sponsors of <EVENT NAME>"

### Take enquiries and RSVPs on your event website

Slug `take-enquiries-and-rsvps-on-your-event-website`. Guide: https://www.ticketfairy.com/guides/take-enquiries-and-rsvps-on-your-event-website

Add a contact, private hire or RSVP form to your event website with the questions you need, get an email for each new reply, then read, sort and download the replies in one place.

For: Collecting enquiries and RSVPs from your website.

What an agent can do: Fai can add a contact or RSVP form with your own questions or the private hire questions, read the replies for the days you name and mark them read, archived or spam. She asks before each change. To download the replies as a file, use Download replies in the dashboard.

Prompt for Fai: "Add a private hire enquiry form to the Private hire page of my <WEBSITE NAME> website"

#### Then: Download the replies

What an agent can do: Fai can read the replies for the days you name, but she cannot give you the file. Use Download in the dashboard for the spreadsheet.

#### Then: Mark a reply as spam

What an agent can do: Fai marks a reply as spam after you confirm.

Prompt for Fai: "Mark the reply from <NAME> on my <WEBSITE NAME> website as spam"

### Tell ticket holders where your event is

Slug `announce-your-venue-location`. Guide: https://www.ticketfairy.com/guides/announce-your-venue-location

Save the location details, choose when future buyers can see the venue, and email a confirmed venue update to ticket holders and RSVPs.

For: Announcing an event location or venue change to the people attending.

What an agent can do: Fai can save the location information and email it to your ticket holders and RSVPs. She shows you the event and the location text and asks for your approval before sending, and you can't recall the email once you approve it. Set whether the venue is hidden on the Details page first, because announcing doesn't change that setting.

Prompt for Fai: "Announce the venue location for <EVENT NAME> with this location information: <LOCATION INFORMATION>. Show me the event and the text, and ask for my approval before sending"

### Translate your event website

Slug `translate-your-event-website`. Guide: https://www.ticketfairy.com/guides/translate-your-event-website

Fai translates your event website into the languages your ticket buyers read, you check her texts, and you put each language live when it is ready, with a language menu for visitors.

For: Offering your website in more languages.

What an agent can do: Fai can translate your website into the languages you name, show how far she has got, accept, edit or translate a text again, and publish or take off a language. She asks before each change.

Prompt for Fai: "Translate my <WEBSITE NAME> website into French and German and tell me when the texts are ready to check"

#### Then: Take a language off your website

What an agent can do: Fai takes a language off your website after you confirm.

Prompt for Fai: "Take German off my <WEBSITE NAME> website"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
