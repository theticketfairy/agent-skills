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

#### Then: Set the brand's monthly budget and default look

What an agent can do: Fai can read the brand's budget, spend and default look, and change the budget and the look after you confirm the amount.

Prompt for Fai: "Set this brand's monthly budget for drawn share cards to 80 dollars and make Collage the default look"

### Choose who wins a prize at your event

Slug `choose-who-wins-a-prize-at-your-event`. Guide: https://www.ticketfairy.com/guides/choose-who-wins-a-prize-at-your-event

Give out a prize with no target on it: name the buyer you already know won, or draw winners at random from every buyer who has paid, then confirm what the draw came up with.

For: Giving out a prize you decide the winner of.

What an agent can do: Fai can name the winner you tell her to, or draw winners for you. A draw gives nobody anything on its own: she reads out who came up and how many buyers were in the draw, then waits for you to say whether to give the prizes out.

Prompt for Fai: "For this event, draw 2 winners for the prize Best costume on the night, tell me who came up and how many buyers were in the draw, then ask me before you give the prizes out"

#### Then: Give out a prize that runs across a brand's events

What an agent can do: Fai can draw for a brand prize and give the prizes out, the same as on an event. She reads out who came up and asks you to approve the moment they win.

Prompt for Fai: "For the brand <BRAND NAME>, draw 1 winner for the prize <PRIZE NAME>, tell me who came up, then ask me before you give the prize out"

#### Then: Ask each winner for what you need to send the prize

What an agent can do: Fai can add or change the questions a prize asks its winners. You see the questions before they are saved.

Prompt for Fai: "On the prize <PRIZE NAME> for this event, ask each winner for their postal address and their t-shirt size"

### Offer prizes your fans can win at your event

Slug `offer-prizes-your-fans-can-win`. Guide: https://www.ticketfairy.com/guides/offer-prizes-your-fans-can-win

Put an upgrade, merch, an experience or a table on your event, set what a fan has to do to win it, and give each prize out from Influencers.

For: Rewarding the fans who fill your event.

What an agent can do: Fai can add a prize, change one, name or draw the winner of a prize you judge yourself, tell you who has won and mark a prize as delivered. You see the whole change before it is made.

Prompt for Fai: "For this event, add a prize called Front row upgrade for every buyer who refers 5 tickets, awarded as soon as they reach it"

#### Then: Make referrals count for more for a while

What an agent can do: Fai can read your boosts, add one and take one away. You see the dates and the multiplier before anything is saved.

Prompt for Fai: "For this event, make referrals count double towards prizes from Friday 6pm to Monday 9am and call it Launch weekend"

#### Then: Let friends refer together as a pack

What an agent can do: Fai can turn packs on for an event and read the packs your fans have started, with the people in each one.

Prompt for Fai: "Turn packs on for this event so friends can pool the tickets they refer, then show me the packs so far"

#### Then: Count the friends your fans' friends bring

What an agent can do: Fai can turn this on or off for an event. You see the change before it is saved.

Prompt for Fai: "Count friends of friends towards prizes on this event"

#### Then: Read the wins across a whole brand

What an agent can do: Fai can read a brand's winners and mark a prize delivered, undone or called off, the same as on an event. She shows you the winner and the prize and asks you to approve each change.

Prompt for Fai: "For the brand <BRAND NAME>, show me who has won its prizes and mark <PRIZE NAME> delivered to <WINNER>. Show me the winner and the prize, then ask me to approve it"

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
