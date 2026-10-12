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

#### Then: Set up payouts later

What an agent can do: Skip the payout step on the page itself. Fai can later list the payment accounts on your brand and start linking one, which the guide to taking ticket money with a payment processing account covers.

Prompt for Fai: "Show the payment accounts on <BRAND NAME> and help me connect one for payouts"

#### Then: Create your brand later

What an agent can do: Create the brand in the dashboard, from Brands. Fai reads your brands and switches between them.

### Find your way around the home page of your event dashboard

Slug `find-your-way-around-the-dashboard-home`. Guide: https://www.ticketfairy.com/guides/find-your-way-around-the-dashboard-home

Use Home in your event dashboard to follow first steps chosen for the events you run, start common jobs such as issuing guest tickets from Quick Actions, and replay the tour.

For: Getting started in the dashboard before your first event goes on sale.

What an agent can do: Fai, the assistant inside your dashboard, can take you to the page behind any first step or Quick Action when you say what you want to do. Hiding the welcome and correcting your organisation type are done on Home in the dashboard.

Prompt for Fai: "Take me to the page where I set up a weekly series of club nights"

#### Then: Accept or decline an invitation

What an agent can do: Fai lists the invitations waiting for you, emails you the code, and accepts or declines the one you choose once you give it the code.

Prompt for Fai: "Show me the invitations waiting for me"

#### Then: Hide the welcome

What an agent can do: Hide the welcome on Home in the dashboard.

### Install the Ticket Fairy Promoter desktop app to manage your events

Slug `install-the-promoter-desktop-app`. Guide: https://www.ticketfairy.com/guides/install-the-promoter-desktop-app

Download the Ticket Fairy Promoter app for Mac or Linux, install it and sign in, then keep several events open in tabs while the app updates itself.

For: Running your events from the Ticket Fairy Promoter app on your Mac or Linux computer.

What an agent can do: Installing the app happens on your computer, so it is yours to do. Once you are signed in, you type to Fai, the assistant inside your dashboard, in the app as you do in a browser, and in the app she can also move around the page you have open, reading it and using its controls with you.

Prompt for Fai: "Take me to the page where I change the ticket prices for <EVENT NAME>"

#### Then: Keep several events open in tabs

What an agent can do: Tabs and windows belong to the app on your computer, so you open them yourself.

#### Then: Install an update

What an agent can do: Updates install on your computer, so you answer the update question yourself.

#### Then: Open Fai from the keyboard

What an agent can do: Fai answers the same questions and makes the same changes in the app as in a browser, and in the app she can also work on the page with you.

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

#### Then: Send an invitation again

What an agent can do: Fai can send the brand's invitation email again. It reaches every address on the invitation list, people who already accepted included, so use Resend beside one person to reach that person. MCP and the CLI do not resend an invitation.

Prompt for Fai: "Show me who I invited to <BRAND NAME> and who has accepted, then send the invitation email again to the whole list"

#### Then: Cancel an invitation

What an agent can do: Cancelling a pending invitation is done in the dashboard. Fai, MCP and the CLI can list the invitations but not cancel one.

Prompt for Fai: "Show me the pending invitations on <BRAND NAME> with the address and role of each"

#### Then: Change someone's role

What an agent can do: Fai can change a member's role to anything except owner, after showing you the change. The CLI updates a role by the membership id from the team list.

Command line:

- Change a role: `ticketfairy team update <ID> --role <ROLE>`

Prompt for Fai: "On <BRAND NAME>, change <NAME OR EMAIL> from <CURRENT ROLE> to <NEW ROLE> and ask me to approve it first"

#### Then: Remove someone from the team

What an agent can do: Fai can remove a member after showing you who they are and what they lose. The CLI revokes access by the membership id.

Command line:

- Revoke access: `ticketfairy team revoke <ID> --force`

Prompt for Fai: "Remove <NAME OR EMAIL> from <BRAND NAME> and ask me to confirm before you do"

#### Then: Let promoters join with one link

What an agent can do: The promoter join link is managed in the dashboard. Fai invites promoters by address instead.

Prompt for Fai: "Invite <EMAIL ADDRESSES> to <BRAND NAME> as promoters and show me the team afterwards"

### Let people apply to promote your event and choose who joins your team

Slug `let-people-apply-to-promote-your-event`. Guide: https://www.ticketfairy.com/guides/let-people-apply-to-promote-your-event

Add an Apply to promote section to your event page, choose the questions applicants answer, and read each application with Fai's suggestion beside it. The people you approve join your team as promoters with their own link to sell tickets to your event.

For: Recruiting promoters who sell tickets for your events.

What an agent can do: Fai, the assistant inside your dashboard, can turn applications on or off for your brand or one event, change the introduction, the questions and how you hear about new applications, read every application with her suggestion, approve or decline people for one event or all your events, with the commission you choose and a note in the email, and ask people for more information. She shows you each change and asks you to approve it first. The command line and MCP have no promoter application commands, so use the dashboard or Fai.

Prompt for Fai: "Turn on promoter applications for <EVENT NAME> with a yes or no question asking if they can hand out flyers, then show me who has applied and what you suggest for each one"

#### Then: Ask an applicant for more information

What an agent can do: Fai can ask one person, or up to 100 at once, for more information with your note and the questions they must answer, starting from her own draft when she suggested a closer look. She shows you who she will ask, the note and the questions, and asks you to approve it first.

Prompt for Fai: "Ask <APPLICANT NAME>, who applied to promote <EVENT NAME>, which events they promoted before and how many tickets they sold, and show me the request before you send it"

#### Then: Approve someone you declined

What an agent can do: Fai can find a declined application and approve it for one event or all your events, after showing you who it is and asking you to confirm.

Prompt for Fai: "Find <APPLICANT NAME> in the declined promoter applications for <EVENT NAME> and approve them for this event, and ask me before you do"

#### Then: Approve or decline several applications at once

What an agent can do: Fai can approve, decline or ask for more information on up to 100 applications in one go, such as every person she suggests approving, and shows you the list to confirm before anything changes.

Prompt for Fai: "Approve every promoter application for <EVENT NAME> that you suggest approving, and show me the list before you do"

#### Then: Stop taking applications

What an agent can do: Fai can turn applications off for your brand or one event, after showing you the change.

Prompt for Fai: "Stop taking promoter applications for <EVENT NAME>"

#### Then: Put an event back on your brand's settings

What an agent can do: Fai can put an event back on your brand's settings, after showing you the change.

Prompt for Fai: "Make <EVENT NAME> use our brand's promoter application settings again"

### Secure the account that runs your events

Slug `secure-your-account`. Guide: https://www.ticketfairy.com/guides/secure-your-account

Turn on sign-in protection so a stolen password alone can't open your events and ticket sales, and add a passkey to sign in with your face, fingerprint or device PIN.

For: Keeping the account behind your events safe from a stolen password.

What an agent can do: Fai, the assistant inside your dashboard, can open Account Settings for you. Turning the authenticator app on needs your password and your authenticator app, so you complete the setup yourself in the dashboard.

Prompt for Fai: "Open my account settings so I can turn on sign-in protection"

#### Then: Add a passkey

What an agent can do: Adding a passkey is yours to do in the dashboard, because your own device or password manager saves it. Fai can open Account Settings for you.

Prompt for Fai: "Open my account settings so I can add a passkey"

#### Then: Remove a passkey

What an agent can do: Remove a passkey in the dashboard, under Sign-in protection in Account Settings.

#### Then: Sign in on a shared or public computer

What an agent can do: You choose this on the sign-in page before you sign in, so it is yours to do.

#### Then: Turn the authenticator app off

What an agent can do: Turning the authenticator app off needs your password, so you do it in the dashboard, in Account Settings.

#### Then: Delete your account

What an agent can do: Fai can tell you whether you can delete your account and what to do if you cannot, and open the Delete account section for you. Only you can confirm it, with your password or the emailed code.

Prompt for Fai: "Can I delete my account?"

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
