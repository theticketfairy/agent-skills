---
name: get-paid-for-ticket-sales
description: "Set up Ticket Fairy payment accounts, choose who pays the fees, pick currencies and follow payouts. Use when an organiser asks how and when they get their money."
---

# Get paid for ticket sales

This skill covers payment accounts, who pays the fees, currencies and payouts on Ticket Fairy. It lists the 3 published guides for this area and what an agent can do for each one.

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

- [Check the payout for your event](#check-the-payout-for-your-event)
- [Choose who pays the booking fee on your event](#choose-who-pays-the-booking-fee-on-your-event)
- [Take ticket money with a payment processing account](#take-ticket-money-with-a-payment-processing-account)

### Check the payout for your event

Slug `check-your-payout`. Guide: https://www.ticketfairy.com/guides/check-your-payout

See what your event has earned, whether the money has been released to you, which account it goes to and when to expect it.

For: Waiting on the money from an event you have run.

What an agent can do: Fai, the assistant inside your dashboard, reads the same figures back to you, and where you have a connected card account she lists the most recent payouts sent from it, with the date each one was due to land. She has no next payout to give you, and cannot tell you a payout reached your bank: nothing records either. When Vault is switched on for your brand, she also reads each event's payout from Vault: expected, on hold, paid or paid in advance, with the expected dates. Releasing the money is ours to do.

Prompt for Fai: "For <EVENT NAME>, what did it earn, and what has our card account paid out recently"

### Choose who pays the booking fee on your event

Slug `set-who-pays-the-fees`. Guide: https://www.ticketfairy.com/guides/set-who-pays-the-fees

Decide before your first ticket type whether buyers pay the booking fee on top, you absorb it from the ticket price, or buyers see it at checkout, and know what each choice does to the price on your page and the amount you receive.

For: Deciding how booking fees appear on an event before tickets go on sale.

What an agent can do: Fai, the assistant inside your dashboard, can set who pays the booking fee on an event and explains what each choice does to the price and your payout. She refuses a switch between Added and Absorbed once ticket types exist and asks you to approve any change first. The whole workflow is also in the dashboard.

Command line:

- Set the fee choice on an event that has no ticket types yet. The value is forward for Added, absorb for Absorbed and forward_checkout for Added Later: `ticketfairy event update <EVENT_ID> --body '{"feeMode": "<FEE_MODE>"}'`

Prompt for Fai: "For <EVENT NAME>, tell me which booking fee choice is set and what a <PRICE> ticket would cost the buyer and pay me under each choice, then set it to <ADDED OR ABSORBED> if that is still possible"

### Take ticket money with a payment processing account

Slug `connect-a-payment-account`. Guide: https://www.ticketfairy.com/guides/connect-a-payment-account

Link the account that takes card payments for your brand, make it the one new events use, and know when it is ready to take money.

For: Setting up the account that takes card payments for a brand.

What an agent can do: Fai, the assistant inside your dashboard, lists the accounts linked to a brand, renames an account, makes one the default, archives one, and puts a first account on every event that has not sold yet, if you ask for that as she links it. She starts a Stripe (classic) account or a Xendit invite; a Managed Account is started here, on the Payments page. She asks you to approve every change first, and a new account still needs you to open the link and finish the setup with the payment company.

Command line:

- List the payment processing accounts on a brand, with the account type, status and which one is the default: `ticketfairy api /api/organizations/<BRAND_ID>/brand-payment-methods --output json`

Prompt for Fai: "List the payment processing accounts on <BRAND NAME>, say which one new events will use, and tell me whether any of them still needs its setup finished"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
