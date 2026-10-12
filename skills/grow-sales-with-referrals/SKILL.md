---
name: grow-sales-with-referrals
description: "Set up Ticket Fairy referral rewards and see who brought in each sale. Use when an organiser wants buyers to bring their friends."
---

# Grow sales with referrals

This skill covers referral rewards for buyers who bring friends, and who brought in each sale on Ticket Fairy. It lists the 4 published guides for this area and what an agent can do for each one.

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
     you run; the commands below leave them out to stay short.
   - **MCP.** `ticketfairy mcp --read-only` starts the CLI's MCP server with read tools. Drop
     `--read-only` only when the organiser wants you to make changes.
   - **Fai.** Fai is the assistant inside the organiser's dashboard. When a task is not on the
     command line, give the organiser the suggested prompt to paste into Fai.
   - **Dashboard.** Otherwise, send the organiser the guide link and walk them through it.
4. **Keep secrets out of the chat.** Codes, passwords and tokens that the organiser receives go
   into the dashboard page that asks for them, never into the conversation.
5. **Confirm before you change anything.** Show the organiser what you will create, change, send,
   refund or cancel, and wait for their yes. You can do only what their team role allows.
6. **Never take payment.** Buyers pay in the browser checkout. Bank, tax and payout details stay
   in the organiser's own browser.

## Guides

- [Choose how your buyers share your event](#choose-how-your-buyers-share-your-event)
- [Choose who wins a prize at your event](#choose-who-wins-a-prize-at-your-event)
- [Offer prizes your fans can win at your event](#offer-prizes-your-fans-can-win-at-your-event)
- [Reward buyers who bring friends to your event](#reward-buyers-who-bring-friends-to-your-event)

### Choose how your buyers share your event

Slug `choose-how-your-buyers-share-your-event`. Guide: https://www.ticketfairy.com/guides/choose-how-your-buyers-share-your-event

Set the message your buyers start with, the apps they can share to, and the share card each of them gets, from the Rewards page.

For: Turning word of mouth into ticket sales.

What an agent can do: Fai can read how your buyers share, change the message, the apps and the drawn cards on an event, and set the brand's budget and default look. You see every change, and what drawing costs, before it is saved.

Prompt for Fai: "On this event, offer WhatsApp, Instagram Stories and Copy link only, and draw a Neon card for each buyer, up to 200 cards"

### Choose who wins a prize at your event

Slug `choose-who-wins-a-prize-at-your-event`. Guide: https://www.ticketfairy.com/guides/choose-who-wins-a-prize-at-your-event

Give out a prize with no target on it: name the buyer you already know won, or draw winners at random from every buyer who has paid, then confirm what the draw came up with.

For: Giving out a prize you decide the winner of.

What an agent can do: Fai can name the winner you tell her to, or draw winners for you. A draw gives nobody anything on its own: she reads out who came up and how many buyers were in the draw, then waits for you to say whether to give the prizes out.

Prompt for Fai: "For this event, draw 2 winners for the prize Best costume on the night, tell me who came up and how many buyers were in the draw, then ask me before you give the prizes out"

### Offer prizes your fans can win at your event

Slug `offer-prizes-your-fans-can-win`. Guide: https://www.ticketfairy.com/guides/offer-prizes-your-fans-can-win

Put an upgrade, merch, an experience or a table on your event, set what a fan has to do to win it, and give each prize out from Influencers.

For: Rewarding the fans who fill your event.

What an agent can do: Fai can add a prize, change one, name or draw the winner of a prize you judge yourself, tell you who has won and mark a prize as delivered. You see the whole change before it is made.

Prompt for Fai: "For this event, add a prize called Front row upgrade for every buyer who refers 5 tickets, awarded as soon as they reach it"

### Reward buyers who bring friends to your event

Slug `reward-buyers-for-referrals`. Guide: https://www.ticketfairy.com/guides/reward-buyers-for-referrals

Give every buyer of an eligible paid ticket their own referral link, and return part of their ticket price when their friends buy through it.

For: Turning word of mouth into ticket sales.

What an agent can do: Before ticket sales start, Fai can turn referral rewards on, set all three tiers and show the reward offer on your event ticket page. You review the complete change before it is applied.

Prompt for Fai: "For this event, enable referral rewards at 10% after 2 referred sales, 30% after 5 and 100% after 8, and show the referral reward offer on the ticket page"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
