---
name: manage-brand-and-team
description: "Manage a Ticket Fairy brand kit, team roles, several brands, collectives and account security. Use when an organiser wants to add people, change roles or organise brands."
---

# Manage the brand and team

This skill covers brand kit, team roles, several brands, collectives and account security on Ticket Fairy. It lists the 7 published guides for this area and what an agent can do for each one.

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

- [Create your Ticket Fairy account and brand to start selling tickets](#create-your-ticket-fairy-account-and-brand-to-start-selling-tickets)
- [Find your way around the home page of your event dashboard](#find-your-way-around-the-home-page-of-your-event-dashboard)
- [Install the Ticket Fairy Promoter desktop app to manage your events](#install-the-ticket-fairy-promoter-desktop-app-to-manage-your-events)
- [Invite your team to your events and choose what each person can do](#invite-your-team-to-your-events-and-choose-what-each-person-can-do)
- [Let people apply to promote your event and choose who joins your team](#let-people-apply-to-promote-your-event-and-choose-who-joins-your-team)
- [Secure the account that runs your events](#secure-the-account-that-runs-your-events)
- [Set up a brand kit for your events](#set-up-a-brand-kit-for-your-events)

### Create your Ticket Fairy account and brand to start selling tickets

Slug `create-your-account-and-first-brand`. Guide: https://www.ticketfairy.com/guides/create-your-account-and-first-brand

Sign up with your email address, Google account or Apple Account, create the brand your events sell under, and choose whether your ticket money is paid out after each event or as tickets sell.

For: Signing up to sell tickets for your events for the first time.

What an agent can do: The sign-up pages are yours to complete, because Fai, the assistant inside your dashboard, works once you have an account. After you sign up, she can tell you which payment accounts are linked to your brand and whether one still needs its setup finished, and open any page of the dashboard for you.

Prompt for Fai: "List the payment accounts linked to <BRAND NAME> and tell me if any of them still needs its setup finished before tickets go on sale"

### Find your way around the home page of your event dashboard

Slug `find-your-way-around-the-dashboard-home`. Guide: https://www.ticketfairy.com/guides/find-your-way-around-the-dashboard-home

Use Home in your event dashboard to follow first steps chosen for the events you run, start common jobs such as issuing guest tickets from Quick Actions, and replay the tour.

For: Getting started in the dashboard before your first event goes on sale.

What an agent can do: Fai, the assistant inside your dashboard, can take you to the page behind any first step or Quick Action when you say what you want to do. Hiding the welcome and correcting your organisation type are done on Home in the dashboard.

Prompt for Fai: "Take me to the page where I set up a weekly series of club nights"

### Install the Ticket Fairy Promoter desktop app to manage your events

Slug `install-the-promoter-desktop-app`. Guide: https://www.ticketfairy.com/guides/install-the-promoter-desktop-app

Download the Ticket Fairy Promoter app for Mac or Linux, install it and sign in, then keep several events open in tabs while the app updates itself.

For: Running your events from the Ticket Fairy Promoter app on your Mac or Linux computer.

What an agent can do: Installing the app happens on your computer, so it is yours to do. Once you are signed in, you type to Fai, the assistant inside your dashboard, in the app as you do in a browser, and in the app she can also move around the page you have open, reading it and using its controls with you.

Prompt for Fai: "Take me to the page where I change the ticket prices for <EVENT NAME>"

### Invite your team to your events and choose what each person can do

Slug `invite-your-team`. Guide: https://www.ticketfairy.com/guides/invite-your-team

Give each person on your team the access their job needs, across the brand or for one event, and see who has accepted.

For: Giving each person on your team the access their job needs on your events.

What an agent can do: Fai, the assistant inside your dashboard, can invite people to the brand or to one event with any role except owner, give an invited promoter the commission you name, send an invitation again, change a role and remove someone, after showing you the change and asking you to approve it. Making someone an owner is done in the dashboard.

Command line:

- List the team and the id of each membership: `ticketfairy team list`
- Change someone's role: `ticketfairy team update <ID> --role <ROLE>`
- Take someone's access away: `ticketfairy team revoke <ID> --force`

Prompt for Fai: "Invite <EMAIL ADDRESSES> to <BRAND OR EVENT NAME> as <ROLE>, then show me the team and who has not accepted yet"

### Let people apply to promote your event and choose who joins your team

Slug `let-people-apply-to-promote-your-event`. Guide: https://www.ticketfairy.com/guides/let-people-apply-to-promote-your-event

Add an Apply to promote section to your event page, choose the questions applicants answer, and read each application with Fai's suggestion beside it. The people you approve join your team as promoters with their own link to sell tickets to your event.

For: Recruiting promoters who sell tickets for your events.

What an agent can do: Fai, the assistant inside your dashboard, can turn applications on or off for your brand or one event, change the introduction, the questions and how you hear about new applications, read every application with her suggestion, approve or decline people for one event or all your events, with the commission you choose and a note in the email, and ask people for more information. She shows you each change and asks you to approve it first. The command line and MCP have no promoter application commands, so use the dashboard or Fai.

Prompt for Fai: "Turn on promoter applications for <EVENT NAME> with a yes or no question asking if they can hand out flyers, then show me who has applied and what you suggest for each one"

### Secure the account that runs your events

Slug `secure-your-account`. Guide: https://www.ticketfairy.com/guides/secure-your-account

Turn on sign-in protection so a stolen password alone can't open your events and ticket sales, and add a passkey to sign in with your face, fingerprint or device PIN.

For: Keeping the account behind your events safe from a stolen password.

What an agent can do: Fai, the assistant inside your dashboard, can open Account Settings for you. Turning the authenticator app on needs your password and your authenticator app, so you complete the setup yourself in the dashboard.

Prompt for Fai: "Open my account settings so I can turn on sign-in protection"

### Set up a brand kit for your events

Slug `set-up-your-brand-kit`. Guide: https://www.ticketfairy.com/guides/set-up-your-brand-kit

Set your brand's tone of voice, colours, fonts and logos once, so your Concierge widget and every new Website Builder site for your events use them.

For: Keeping one look and voice across every event you run.

What an agent can do: Fai, the assistant inside your dashboard, can read the current kit and save its text fields or a complete colours, typography, logos or assets list. She reads the current list first, keeps entries you did not ask to remove, and asks you to confirm before saving. Upload files in the dashboard first because Fai cannot upload binary files. She can preserve or update a typography entry with a font-file URL even when its font name is blank.

Prompt for Fai: "Read the current Brand Guidelines for my current brand. Set the tagline to "[tagline]", the about text to "[about]", the tone of voice to "[tone]" and the usage guidelines to "[guidelines]". Keep the existing colours, fonts, logos and assets, show me the exact changes, then ask me to confirm before saving anything"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
