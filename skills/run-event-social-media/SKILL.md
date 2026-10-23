---
name: run-event-social-media
description: "Connect Instagram and TikTok to Ticket Fairy, draft and schedule posts, answer comments and messages, and run follower presales. Use when an organiser promotes events on social media."
---

# Run event social media

This skill covers connected accounts, posts, replies, auto-replies and follower presales on Ticket Fairy. It lists the 7 published guides for this area and what an agent can do for each one.

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

- [Answer what ticket buyers ask you on social](#answer-what-ticket-buyers-ask-you-on-social)
- [Connect the social accounts that promote your events](#connect-the-social-accounts-that-promote-your-events)
- [Let the Social Assistant draft your event posts and replies](#let-the-social-assistant-draft-your-event-posts-and-replies)
- [Post an update to fans when your event changes](#post-an-update-to-fans-when-your-event-changes)
- [Run a ticket presale for your Instagram followers](#run-a-ticket-presale-for-your-instagram-followers)
- [Schedule the social posts that sell your tickets](#schedule-the-social-posts-that-sell-your-tickets)
- [Send fans your ticket link automatically when they comment or message](#send-fans-your-ticket-link-automatically-when-they-comment-or-message)

### Answer what ticket buyers ask you on social

Slug `read-what-your-audience-says-on-social`. Guide: https://www.ticketfairy.com/guides/read-what-your-audience-says-on-social

Answer every comment on your event posts and every direct message from ticket buyers in one Inbox. Tell a buyer from a passer-by, reply in public or in private, hide touts several at a time, and share each conversation with your team.

For: Answering the buyers who comment on your event posts and message your accounts.

What an agent can do: Fai reads you the comments, drafts an answer, and posts it in public or sends it as a private message. She hides up to 25 comments at once, and she asks before every reply or hide, because fans see the result. Hide a single comment from its menu in Comments.

Prompt for Fai: "What are buyers asking under our posts for <BRAND NAME>, and which ones need an answer today"

#### Then: Answer a direct message as a team

What an agent can do: Fai lists your conversations, reads you the fan's recent orders and comments, gives a conversation an owner, adds a note for your team, replies to the fan, and marks the to-do done or opens it again. She asks before each change, and a reply goes out only while the fan's reply window is open.

Prompt for Fai: "Which instagram messages for <BRAND NAME> are still to do, and who owns each one"

#### Then: Set how quickly your team replies

What an agent can do: Fai tells you your team's reply time and changes it or turns it off for an owner or admin. She asks before she saves it.

Prompt for Fai: "Set our social reply time to 30 minutes"

#### Then: Find a comment again later

What an agent can do: Fai searches the comments and reads you the matches. You unhide a comment yourself in Comments.

Prompt for Fai: "Find the comments for <BRAND NAME> that mention refunds"

### Connect the social accounts that promote your events

Slug `connect-your-social-accounts`. Guide: https://www.ticketfairy.com/guides/connect-your-social-accounts

Bring your Instagram and TikTok accounts into Ticket Fairy and say whether each one promotes your whole brand, an event series, a venue or one event, so you can run posts, replies and presales for your Instagram accounts from your dashboard.

For: Running the social accounts that promote your events.

What an agent can do: Fai lists the ways to connect that are open to your brand and the accounts already connected, with what each one is for and whether it needs reconnecting. She cannot sign in to Instagram, Facebook or TikTok for you, so you make the connection itself on the Accounts page. Once an account is connected she can change what it is for and refresh its posts and comments, and she asks you to approve each change first.

Prompt for Fai: "Which social accounts are connected to <BRAND NAME>, what is each one for, and does any of them need reconnecting"

#### Then: Reconnect an account before it stops working

What an agent can do: Fai tells you which accounts need reconnecting and when. Reconnecting is a sign-in with Instagram, Facebook or TikTok, so you do it from the card.

Prompt for Fai: "Do any of the social accounts on <BRAND NAME> need reconnecting"

#### Then: Link the Facebook Page to an Instagram account

What an agent can do: Fai tells you which Instagram accounts are missing competitor lookup, hashtag search and mentions. Linking the Page is a Facebook sign-in, so you do it from the card.

Prompt for Fai: "Which Instagram accounts on <BRAND NAME> can't use hashtag search or mentions yet"

#### Then: Change what an account is for

What an agent can do: Fai changes what an account is for, including the series, venue or event it belongs to, and asks you to approve the change first.

Prompt for Fai: "Set the Instagram account @<ACCOUNT HANDLE> on <BRAND NAME> to promote the <SERIES NAME> event series"

#### Then: Disconnect an account you no longer use

What an agent can do: Fai cannot disconnect an account. Use Disconnect on the account's card.

### Let the Social Assistant draft your event posts and replies

Slug `let-the-social-assistant-draft-your-event-posts-and-replies`. Guide: https://www.ticketfairy.com/guides/let-the-social-assistant-draft-your-event-posts-and-replies

The Social Assistant watches your events, ticket sales and fan comments, and drafts the next social post for each event, answers to ticket buyers' questions and messages to fans who have not bought yet. It hides ticket scams in your comments, and your team approves, edits or dismisses everything else in one list.

For: Running the social accounts that promote your events.

What an agent can do: Fai lists what the Social Assistant has ready and explains why it suggested each draft. She approves a draft as it is or with your changes to the words, the time or the accounts, dismisses one, undoes a comment the assistant hid, and says what happened to any suggestion. She also approves every draft for one event in one go, after telling you the counts by kind and the drafts she leaves for you. She asks before every change, and you add a new image on the Assistant page yourself.

Prompt for Fai: "What has the social assistant got ready for <EVENT NAME>, and why"

#### Then: Approve every draft for one event

What an agent can do: Fai approves every draft waiting for one event, 50 at a time, after telling you the counts by kind, the posts that go out at once and the drafts she leaves for you. She asks before she approves them.

Prompt for Fai: "Approve everything the social assistant has ready for <EVENT NAME>"

#### Then: Delete a reply the assistant posted

What an agent can do: Delete the reply on the Done list of the Assistant page.

#### Then: Choose what the assistant does on its own

What an agent can do: Fai reads what each job is set to and changes a job's mode for an owner or admin. She asks before she saves.

Prompt for Fai: "Set the social assistant to answer questions automatically but keep asking me first about event posts"

#### Then: Ask the assistant to check your events now

What an agent can do: Fai starts a check for event posts, replies, the scam guard or fan follow-up, and asks before she starts it.

Prompt for Fai: "Ask the social assistant to check our events for new posts now"

#### Then: Review the drafts from Social Home

What an agent can do: Fai lists your upcoming events with the drafts waiting for each one and the next post the assistant drafts.

Prompt for Fai: "Which of our upcoming events have social drafts waiting for me"

### Post an update to fans when your event changes

Slug `post-an-update-when-your-event-changes`. Guide: https://www.ticketfairy.com/guides/post-an-update-when-your-event-changes

Tell every fan who follows your social accounts what changed about your event in one step. With Post an update, we pause the event's scheduled promotional posts, draft an update post for each account for you to approve, and save a reply your team can send when fans ask. You resume the posts when it's over.

For: Telling fans on social what changed about your event.

What an agent can do: Fai tells you what an update would pause and which accounts get a draft, then posts the update for you with your words and the steps you choose. She asks before she starts it and before she resumes the posts, because both change posts your team scheduled. The update drafts wait in the Assistant for your approval.

Prompt for Fai: "The <EVENT NAME> show is postponed because of the storm, post an update and pause the promo posts"

#### Then: Resume the promotional posts

What an agent can do: Fai resumes an event's paused promotional posts and tells you how many came back scheduled, waiting for approval or as drafts. She asks before she resumes them.

Prompt for Fai: "The <EVENT NAME> update is over, resume the promo posts"

### Run a ticket presale for your Instagram followers

Slug `run-a-follower-only-presale`. Guide: https://www.ticketfairy.com/guides/run-a-follower-only-presale

Fans comment a word under your Instagram post, follow your account and reply with their email to join the presale list for your event. When you launch, each of them gets a personal link to buy tickets before the public on-sale.

For: Selling early tickets to the fans who follow you on Instagram.

What an agent can do: Fai sets up the presale list from your event's ready-made auto-replies with your words and messages, switches it on, tells you where every fan on the list has got to, and launches it. She asks you to approve the auto-reply, switching it on and the launch, and the launch sends real emails and messages that cannot be called back.

Prompt for Fai: "Set up a followers-only presale on our Instagram for <EVENT NAME>: fans who comment PRESALE get asked to follow and reply, then asked for their email"

#### Then: Invite the fans who joined after the launch

What an agent can do: Fai tells you how many fans have become ready since the launch and launches to them, after you approve the email and message she will send.

Prompt for Fai: "How many fans are ready in the followers-only presale for <EVENT NAME>? Launch to them with the same email and message as last time"

#### Then: Stop taking sign-ups

What an agent can do: Fai switches the presale auto-reply off after you approve it.

Prompt for Fai: "Switch off the followers-only presale auto-reply for <EVENT NAME>"

### Schedule the social posts that sell your tickets

Slug `schedule-your-social-posts`. Guide: https://www.ticketfairy.com/guides/schedule-your-social-posts

Plan the posts that sell your event's tickets in one sitting. Add each one to the queue at its account's next free posting time, or choose the exact minute, and send it for approval where your team needs it.

For: Running the social accounts that sell your tickets.

What an agent can do: Fai drafts a post for your event and adds it to the queue at the next free posting time, or at the time you give her. She shows you the post and asks before it goes into the queue, and a post on an account that needs approval still waits for an owner or admin. Add a new photo or video in the New post dialog.

Prompt for Fai: "Draft a last chance post for <EVENT NAME> on our instagram and add it to the queue"

#### Then: Move a post to another day

What an agent can do: Fai moves a scheduled post to another date and keeps its time, after you approve the change.

Prompt for Fai: "Move our lineup post for <EVENT NAME> to friday at the same time"

#### Then: See the tickets a post sold

What an agent can do: Fai lists your event's posts with the tickets and revenue each one brought in through its link.

Prompt for Fai: "Which of our facebook posts for <EVENT NAME> sold the most tickets"

#### Then: Choose the times Add to queue uses

What an agent can do: Fai reads an account's posting times and changes them, including switching to the suggested times. She asks before she saves, and she changes them only for an owner or admin.

Prompt for Fai: "Set our instagram posting times to 6pm on weekdays and 11am on saturdays"

#### Then: Clear the posts waiting on you

What an agent can do: Fai lists the posts waiting for approval and approves one you have read and agreed to. She asks first, because approving sends it to a public audience.

Prompt for Fai: "Show me the posts waiting for approval for <BRAND NAME>"

#### Then: Deal with a post that did not go out

What an agent can do: Fai lists the posts that did not go out and tells you what each one said. You send one again from the queue.

Prompt for Fai: "Which posts for <BRAND NAME> did not go out, and why"

### Send fans your ticket link automatically when they comment or message

Slug `send-fans-your-ticket-link-automatically`. Guide: https://www.ticketfairy.com/guides/send-fans-your-ticket-link-automatically

Turn on an auto-reply for your event, and every fan who comments TICKETS under your event posts gets the ticket link in a private message, with the waiting list instead once the event sells out. You can also use ready-made auto-replies for a presale list, a guest list, answers from your event details and a thank-you for story mentions, and see how many tickets fans bought through each one's link.

For: Selling tickets to the fans who comment on and message your social accounts.

What an agent can do: Fai lists the auto-replies made for your event, sets one up with your changes to the keywords, the posts it watches and the messages, and turns it on. She shows you the auto-reply and asks before she creates it and again before she turns it on, because it messages real fans.

Prompt for Fai: "Set up the ticket link auto-reply for <EVENT NAME> on our instagram and turn it on"

#### Then: See the tickets an auto-reply sold

What an agent can do: Fai tells you what an auto-reply did and sold: the fans it answered, the messages it sent, the tickets and revenue from its link, and what happened for each fan.

Prompt for Fai: "How many tickets has the ticket link auto-reply for <EVENT NAME> sold"

#### Then: Turn on an auto-reply the assistant suggests

What an agent can do: Fai lists the auto-replies the assistant suggests and approves one, which sets it up and turns it on. She asks before she approves it.

Prompt for Fai: "Has the social assistant suggested any auto-replies for <EVENT NAME>"

#### Then: Pause an auto-reply

What an agent can do: Fai pauses an auto-reply, or turns one back on, after you approve it.

Prompt for Fai: "Pause the ticket link auto-reply for <EVENT NAME>"

#### Then: Change or delete an auto-reply

What an agent can do: Fai changes an auto-reply's keywords, posts, messages and options, or deletes it. She shows you the change and asks before she saves it or deletes the auto-reply.

Prompt for Fai: "Change the ticket link auto-reply for <EVENT NAME> so it also answers the word TIX"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
