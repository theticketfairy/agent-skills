---
name: manage-brand-and-team
description: "Manage a Ticket Fairy brand kit, team roles, several brands, collectives and account security. Use when an organiser wants to add people, change roles or organise brands."
---

# Manage the brand and team

This skill covers brand kit, team roles, several brands, collectives and account security on Ticket Fairy. It lists the 12 published guides for this area and what an agent can do for each one.

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

- [Create your Ticket Fairy account and brand to start selling tickets](#create-your-ticket-fairy-account-and-brand-to-start-selling-tickets)
- [Find your way around the home page of your event dashboard](#find-your-way-around-the-home-page-of-your-event-dashboard)
- [Finish the event workspace your assistant prepared](#finish-the-event-workspace-your-assistant-prepared)
- [Install the Ticket Fairy Promoter desktop app to manage your events](#install-the-ticket-fairy-promoter-desktop-app-to-manage-your-events)
- [Invite promoters to your collective so they can sell tickets for your events](#invite-promoters-to-your-collective-so-they-can-sell-tickets-for-your-events)
- [Invite your team to your events and choose what each person can do](#invite-your-team-to-your-events-and-choose-what-each-person-can-do)
- [Let people apply to promote your event and choose who joins your team](#let-people-apply-to-promote-your-event-and-choose-who-joins-your-team)
- [Make statements of what you owe your promoters](#make-statements-of-what-you-owe-your-promoters)
- [Secure the account that runs your events](#secure-the-account-that-runs-your-events)
- [See the commission you earn as a promoter](#see-the-commission-you-earn-as-a-promoter)
- [Set commission for your promoters](#set-commission-for-your-promoters)
- [Set up a brand kit for your events](#set-up-a-brand-kit-for-your-events)

### Create your Ticket Fairy account and brand to start selling tickets

Slug `create-your-account-and-first-brand`. Guide: https://www.ticketfairy.com/guides/create-your-account-and-first-brand

Sign up with your email address, Google account or Apple Account, create the brand your events sell under, and choose whether your ticket money is paid out after each event or as tickets sell.

For: Signing up to sell tickets for your events for the first time.

What an agent can do: You complete the sign-up pages yourself, because Fai works only once you have an account. After you sign up, she can tell you which payment accounts are linked to your brand and whether one still needs its setup finished, and open any page of the dashboard for you.

Prompt for Fai: "List the payment accounts linked to <BRAND NAME> and tell me if any of them still needs its setup finished before tickets go on sale"

#### Then: Set up payouts later

What an agent can do: Skip the payout step on the page itself. Fai can later list the payment accounts on your brand and start linking one, which the guide to taking ticket money with a payment processing account covers.

Prompt for Fai: "Show the payment accounts on <BRAND NAME> and help me connect one for payouts"

#### Then: Create your brand later

What an agent can do: Create the brand in the dashboard, from Brands. Fai can list your brands and switch between them.

### Find your way around the home page of your event dashboard

Slug `find-your-way-around-the-dashboard-home`. Guide: https://www.ticketfairy.com/guides/find-your-way-around-the-dashboard-home

Use Home in your event dashboard to follow first steps chosen for the events you run, start common jobs such as issuing guest tickets from Quick Actions, and replay the tour.

For: Getting started in the dashboard before your first event goes on sale.

What an agent can do: Fai can take you to the page behind any first step or Quick Action when you say what you want to do. You hide the welcome and correct your organisation type on Home in the dashboard.

Prompt for Fai: "Take me to the page where I set up a weekly series of club nights"

#### Then: Accept or decline an invitation

What an agent can do: Fai lists the invitations waiting for you, emails you the code, and accepts or declines the one you choose once you give her the code.

Prompt for Fai: "Show me the invitations waiting for me"

#### Then: Hide the welcome

What an agent can do: Hide the welcome on Home in the dashboard.

### Finish the event workspace your assistant prepared

Slug `finish-your-assistant-prepared-workspace`. Guide: https://www.ticketfairy.com/guides/finish-your-assistant-prepared-workspace

Review your account and brand, add an event draft if you want to, and choose how to receive ticket money before continuing in your dashboard.

For: You have an event workspace setup link from your assistant.

What an agent can do: You confirm your account, choose your brand and enter payout details in the dashboard. After you sign in, Fai can show your unfinished event drafts and the payment accounts connected to your brand. She asks for your approval before adding an unfinished draft to a brand, and you review and publish the event yourself.

Prompt for Fai: "Show my unfinished event drafts and the payment accounts connected to <BRAND NAME>, then help me choose my next step"

#### Then: Finish payout setup

What an agent can do: After sign-in, Fai can list your connected payment accounts and help you continue with setup. You complete provider sign-in, bank details and identity checks yourself.

Prompt for Fai: "Show the payment accounts on <BRAND NAME> and help me finish payout setup"

#### Then: Continue after an interrupted step

What an agent can do: Continue in your own browser using the same request. Ask your original assistant for a new setup link if this one expired. Fai does not redeem a personal setup link or create a replacement.

### Install the Ticket Fairy Promoter desktop app to manage your events

Slug `install-the-promoter-desktop-app`. Guide: https://www.ticketfairy.com/guides/install-the-promoter-desktop-app

Download the Ticket Fairy Promoter app for Mac or Linux, install it and sign in, then keep several events open in tabs while the app updates itself.

For: Running your events from the Ticket Fairy Promoter app on your Mac or Linux computer.

What an agent can do: You install the app on your computer yourself. Once you are signed in, you type to Fai in the app as you do in a browser, and in the app she can also move around the page you have open, reading it and using its controls with you.

Prompt for Fai: "Take me to the page where I change the ticket prices for <EVENT NAME>"

#### Then: Keep several events open in tabs

What an agent can do: Tabs and windows belong to the app on your computer, so you open them yourself.

#### Then: Install an update

What an agent can do: Updates install on your computer, so you answer the update question yourself.

#### Then: Open Fai from the keyboard

What an agent can do: Fai answers the same questions and makes the same changes in the app as in a browser, and in the app she can also work on the page with you.

### Invite promoters to your collective so they can sell tickets for your events

Slug `invite-people-to-your-collective`. Guide: https://www.ticketfairy.com/guides/invite-people-to-your-collective

Send invitations to your promoters, see who has not joined yet, and sort out a wrong email address or an invitation that never arrived, so every promoter can sell tickets for your events.

For: Running a street team, promoter group or production crew you deploy into other people's events.

What an agent can do: Fai can invite a promoter, list everyone who has not joined yet with the date each invitation last went out, send one again, or cancel it. She can also accept an invitation for you when you have the link but cannot get it to work.

Prompt for Fai: "Show me who I invited to my collective who has not joined yet, and send the invitation again to anyone still waiting"

### Invite your team to your events and choose what each person can do

Slug `invite-your-team`. Guide: https://www.ticketfairy.com/guides/invite-your-team

Give each person on your team the access their job needs, across the brand or for one event, and see who has accepted.

For: Giving each person on your team the access their job needs on your events.

What an agent can do: Fai can invite people to the brand or to one event with any role except owner, give an invited promoter the commission you name, send an invitation again, change a role and remove someone, after showing you the change and asking you to approve it. You make someone an owner in the dashboard.

Command line:

- Invite someone to the brand, or to one event with --event-id: `ticketfairy team invite <EMAIL> --role <ROLE>`
- List the team and the id of each membership: `ticketfairy team list`
- Change someone's role: `ticketfairy team update <ID> --role <ROLE>`
- Take someone's access away: `ticketfairy team revoke <ID> --force`

Prompt for Fai: "Invite <EMAIL ADDRESSES> to <BRAND OR EVENT NAME> as <ROLE>, then show me the team and who has not accepted yet"

#### Then: Send an invitation again

What an agent can do: Fai can send the brand's invitation email again. It goes to every address on the invitation list, people who already accepted included, so use Resend beside one person to reach that person. MCP and the CLI do not resend an invitation.

Prompt for Fai: "Show me who I invited to <BRAND NAME> and who has accepted, then send the invitation email again to the whole list"

#### Then: Cancel an invitation

What an agent can do: You cancel a pending invitation in the dashboard. Fai, MCP and the CLI can list the invitations but not cancel one.

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

What an agent can do: You manage the promoter join link in the dashboard. Fai invites promoters by address instead.

Prompt for Fai: "Invite <EMAIL ADDRESSES> to <BRAND NAME> as promoters and show me the team afterwards"

### Let people apply to promote your event and choose who joins your team

Slug `let-people-apply-to-promote-your-event`. Guide: https://www.ticketfairy.com/guides/let-people-apply-to-promote-your-event

Add an Apply to promote section to your event page, choose the questions applicants answer, and read each application with Fai's suggestion beside it. The people you approve join your team as promoters with their own link to sell tickets to your event.

For: Recruiting promoters who sell tickets for your events.

What an agent can do: Fai can turn applications on or off for your brand or one event, change the introduction, the questions and how you hear about new applications, read every application with her suggestion, approve or decline people for one event or all your events, with the commission you choose, a note in the email and a reason for your team, and ask people for more information. She can sort the list and filter it by her suggestion, decide on every application that matches, undo an approval in the first seconds, and turn on what the apply page shows promoters earn. She shows you each change and asks you to approve it first. The command line and MCP have no promoter application commands, so use the dashboard or Fai.

Prompt for Fai: "Turn on promoter applications for <EVENT NAME> with a yes or no question asking if they can hand out flyers, then show me who has applied and what you suggest for each one"

#### Then: Ask an applicant for more information

What an agent can do: Fai can ask one person, or up to 100 at once, for more information with your note and the questions they must answer, starting from her own draft when she suggested a closer look. She shows you who she will ask, the note and the questions, and asks you to approve it first.

Prompt for Fai: "Ask <APPLICANT NAME>, who applied to promote <EVENT NAME>, which events they promoted before and how many tickets they sold, and show me the request before you send it"

#### Then: Approve someone you declined

What an agent can do: Fai can find a declined application and approve it for one event or all your events, after showing you who it is and asking you to confirm.

Prompt for Fai: "Find <APPLICANT NAME> in the declined promoter applications for <EVENT NAME> and approve them for this event, and ask me before you do"

#### Then: Approve or decline several applications at once

What an agent can do: Fai can approve, decline or ask for more information on up to 100 applications in one go, or approve or decline every application that matches a filter (up to 5,000), such as everyone she suggests approving, and shows you what changes to confirm first.

Prompt for Fai: "Approve every promoter application for <EVENT NAME> that you suggest approving, and show me the list before you do"

#### Then: Stop taking applications

What an agent can do: Fai can turn applications off for your brand or one event, after showing you the change.

Prompt for Fai: "Stop taking promoter applications for <EVENT NAME>"

#### Then: Put an event back on your brand's settings

What an agent can do: Fai can put an event back on your brand's settings, after showing you the change.

Prompt for Fai: "Make <EVENT NAME> use our brand's promoter application settings again"

### Make statements of what you owe your promoters

Slug `make-statements-of-what-you-owe-your-promoters`. Guide: https://www.ticketfairy.com/guides/make-statements-of-what-you-owe-your-promoters

Mark each event ready to pay promoters once its sales and refunds are final, then make a statement of the commission you owe each promoter in each currency. A brand owner also approves the bank details your promoters send you.

For: Working out what you owe the promoters who sell your tickets.

What an agent can do: Fai can mark an event ready to pay promoters or undo it, make statements for one promoter, up to 100 at once or everyone with commission ready, cancel a statement waiting for approval, and approve or reject a promoter's bank details if you're a brand owner. She shows you each change and asks you to approve it first. When Vault asks you to confirm it's you, she sends you to the dashboard to finish. The command line and MCP have no promoter payout commands.

Prompt for Fai: "Mark <EVENT NAME> ready to pay promoters, then make statements for every promoter with commission ready to pay and show me who they cover before you make them"

#### Then: Approve a promoter's bank details

What an agent can do: Fai can approve or reject a promoter's bank details for a brand owner, after the 24-hour wait, and asks you to approve each decision. She never shows the full bank details. When Vault asks you to confirm it's you, she sends you to the dashboard to finish.

Prompt for Fai: "Show me the promoter bank details waiting for approval on <BRAND NAME> and approve <PROMOTER NAME>'s"

#### Then: Cancel a statement

What an agent can do: Fai can cancel a statement that is waiting for approval and asks you to confirm first.

Prompt for Fai: "Cancel <PROMOTER NAME>'s statement waiting for approval on <BRAND NAME>"

#### Then: Undo ready to pay on an event

What an agent can do: Fai can undo ready to pay on an event with your reason, and can cancel the statements waiting for approval that hold it. She asks you to approve first.

Prompt for Fai: "Undo ready to pay promoters on <EVENT NAME> because refunds are still coming in"

### Secure the account that runs your events

Slug `secure-your-account`. Guide: https://www.ticketfairy.com/guides/secure-your-account

Turn on sign-in protection so a stolen password alone can't open your events and ticket sales, and add a passkey to sign in with your face, fingerprint or device PIN.

For: Keeping the account behind your events safe from a stolen password.

What an agent can do: Fai can open Account Settings for you. Turning the authenticator app on needs your password and your authenticator app, so you complete the setup yourself in the dashboard.

Prompt for Fai: "Open my account settings so I can turn on sign-in protection"

#### Then: Add a passkey

What an agent can do: You add a passkey yourself in the dashboard, because your own device or password manager saves it. Fai can open Account Settings for you.

Prompt for Fai: "Open my account settings so I can add a passkey"

#### Then: Remove a passkey

What an agent can do: Remove a passkey in the dashboard, under Sign-in protection in Account Settings.

#### Then: Sign in on a shared or public computer

What an agent can do: You choose this yourself, on the sign-in page, before you sign in.

#### Then: Turn the authenticator app off

What an agent can do: Turning the authenticator app off needs your password, so you do it in the dashboard, in Account Settings.

#### Then: Delete your account

What an agent can do: Fai can tell you whether you can delete your account and open the Delete account section for you.

Prompt for Fai: "Open the Delete account section of my account settings"

#### Then: Confirm the deletion with your password

What an agent can do: Fai can tell you whether you can delete your account and what to do if you cannot, and open the Delete account section for you. Only you can confirm the deletion, with your password or the emailed code.

Prompt for Fai: "Can I delete my account?"

### See the commission you earn as a promoter

Slug `see-the-commission-you-earn`. Guide: https://www.ticketfairy.com/guides/see-the-commission-you-earn

Open My commission to see how you earn on each event you promote, what you have earned in each currency, and every earnings line behind it, including refunds and part refunds.

For: Promoters who sell tickets with their own link.

What an agent can do: Fai can tell you how you earn on an event, what you have earned, and why any order earned what it did. She can see only your own commission. The command line and MCP have no commission commands, so use the dashboard or Fai.

Prompt for Fai: "How much commission have I earned on <EVENT NAME>, and why did my last order earn less than the others?"

#### Then: Enter your payout details

What an agent can do: Enter your payout details in the dashboard, because they hold your bank account. Fai can show you what you have earned on each event.

Prompt for Fai: "Show me what I have earned on <EVENT NAME> and what is still to be paid"

### Set commission for your promoters

Slug `set-commission-for-your-promoters`. Guide: https://www.ticketfairy.com/guides/set-commission-for-your-promoters

Create the commission structures your promoters earn with, such as a percentage of ticket sales or a fixed amount per ticket, choose the default, give a promoter their own commission when you approve or invite them, and read what each promoter has earned.

For: Paying promoters a share of the tickets they sell.

What an agent can do: Fai can create, change, archive and restore commission structures, change the default, give one promoter or up to 100 promoters their own commission, and explain any promoter's earnings line by line. She shows you each change and asks you to approve it first. The command line and MCP have no commission commands, so use the dashboard or Fai.

Prompt for Fai: "Create a commission structure for <BRAND NAME> that pays 10% of each ticket's price, make it the default, and show me what each promoter has earned so far"

#### Then: Choose the commission when you approve an application

What an agent can do: Fai can approve applications with the commission you name, for one person or up to 100, and asks you to confirm first.

Prompt for Fai: "Approve every promoter application for <EVENT NAME> that you suggest approving, give them the <STRUCTURE NAME> commission, and show me the list before you do"

#### Then: Choose the commission when you invite a promoter

What an agent can do: Fai can invite promoters to your brand or one event with the commission you name, after showing you the invitation.

Prompt for Fai: "Invite <EMAIL ADDRESSES> to <BRAND NAME> as promoters with the <STRUCTURE NAME> commission"

#### Then: Change the commission of several promoters at once

What an agent can do: Fai can give up to 100 promoters the same commission in one change, after showing you who it covers.

Prompt for Fai: "Give every promoter on <BRAND NAME> who sold more than 50 tickets the <STRUCTURE NAME> commission and show me who it covers first"

#### Then: Read one promoter's earnings

What an agent can do: Fai can tell you a promoter's balance and explain every earnings line in plain words.

Prompt for Fai: "Why has <PROMOTER NAME> earned this much commission on <EVENT NAME>?"

#### Then: Change or archive a structure

What an agent can do: Fai can change, archive and restore a structure, and tells you how many people use it before you approve.

Prompt for Fai: "Change the <STRUCTURE NAME> commission structure to 12% from now on"

### Set up a brand kit for your events

Slug `set-up-your-brand-kit`. Guide: https://www.ticketfairy.com/guides/set-up-your-brand-kit

Set your brand's tone of voice, colours, fonts and logos once, so your Concierge widget and every new Website Builder site for your events use them.

For: Keeping one look and voice across every event you run.

What an agent can do: Fai can check the current kit and save its text fields or a complete colours, typography, logos or assets list. She checks the current list first, keeps entries you did not ask to remove, and asks you to confirm before saving. Upload files in the dashboard first because Fai cannot upload binary files. She can preserve or update a typography entry with a font-file URL even when its font name is blank, and she adds a new font file only after you tell her that your brand has the right to use the font.

Prompt for Fai: "Read the current Brand Guidelines for my current brand. Set the tagline to "[tagline]", the about text to "[about]", the tone of voice to "[tone]" and the usage guidelines to "[guidelines]". Keep the existing colours, fonts, logos and assets, show me the exact changes, then ask me to confirm before saving anything"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
