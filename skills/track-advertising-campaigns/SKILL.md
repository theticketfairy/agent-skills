---
name: track-advertising-campaigns
description: "Connect advertising pixels and conversion tracking to Ticket Fairy and see which campaigns sold tickets. Use when an organiser runs paid ads for an event."
---

# Track advertising campaigns

This skill covers advertising pixels, conversion tracking and which campaigns sold tickets on Ticket Fairy. It lists the 15 published guides for this area and what an agent can do for each one.

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

- [Connect advertising pixels to your ticket sales](#connect-advertising-pixels-to-your-ticket-sales)
- [Measure ticket sales with Google Analytics](#measure-ticket-sales-with-google-analytics)
- [See which ads sold tickets](#see-which-ads-sold-tickets)
- [Set up a Meta pixel to track your ticket sales](#set-up-a-meta-pixel-to-track-your-ticket-sales)
- [Track ticket sales with your Amazon DSP pixel](#track-ticket-sales-with-your-amazon-dsp-pixel)
- [Track ticket sales with your ChatGPT pixel](#track-ticket-sales-with-your-chatgpt-pixel)
- [Track ticket sales with your Google Ads pixel](#track-ticket-sales-with-your-google-ads-pixel)
- [Track ticket sales with your LinkedIn pixel](#track-ticket-sales-with-your-linkedin-pixel)
- [Track ticket sales with your Microsoft Bing pixel](#track-ticket-sales-with-your-microsoft-bing-pixel)
- [Track ticket sales with your Pinterest pixel](#track-ticket-sales-with-your-pinterest-pixel)
- [Track ticket sales with your Reddit pixel](#track-ticket-sales-with-your-reddit-pixel)
- [Track ticket sales with your Snapchat pixel](#track-ticket-sales-with-your-snapchat-pixel)
- [Track ticket sales with your Spotify pixel](#track-ticket-sales-with-your-spotify-pixel)
- [Track ticket sales with your TikTok pixel](#track-ticket-sales-with-your-tiktok-pixel)
- [Track ticket sales with your X pixel](#track-ticket-sales-with-your-x-pixel)

### Connect advertising pixels to your ticket sales

Slug `connect-meta-and-network-pixels`. Guide: https://www.ticketfairy.com/guides/connect-meta-and-network-pixels

Connect Meta and your other advertising networks at brand level so you can see which campaigns led to ticket sales.

For: Buying ads for an event.

What an agent can do: Complete the Meta sign-in in your browser, then ask Fai, the assistant inside your dashboard, to turn on Meta tracking and add your other advertising pixels. She asks you to approve each change before she makes it. You can also add them in the dashboard.

Prompt for Fai: "Show me which tracking pixels this brand has, then turn Meta conversion tracking on for the pixel we advertise with and add our TikTok pixel <your TikTok pixel ID>"

#### Then: Add a pixel to one event only

What an agent can do: Fai, the assistant inside your dashboard, can list, add, change and remove the pixels for one event, and asks you to approve each change. Picking a pixel from your Meta ad accounts needs your Facebook sign-in, so give Fai the Meta pixel ID or use the dashboard for that part.

Prompt for Fai: "Show me the tracking pixels on <EVENT NAME>, including the brand pixels that already track it, then add our TikTok pixel <TIKTOK PIXEL ID> to this event only"

### Measure ticket sales with Google Analytics

Slug `set-up-a-google-analytics-pixel`. Guide: https://www.ticketfairy.com/guides/set-up-a-google-analytics-pixel

Add your complete Google Analytics measurement ID once to measure event page visits, checkout starts and completed ticket sales.

For: Measuring event traffic and ticket sales in Google Analytics.

What an agent can do: You can import the complete measurement ID in the dashboard. Fai can also add it after asking you to approve the change. Keep the G- at the start whichever path you use.

Prompt for Fai: "Add Google Analytics to this brand with measurement ID <your Google Analytics ID>"

### See which ads sold tickets

Slug `see-which-ads-sold-tickets`. Guide: https://www.ticketfairy.com/guides/see-which-ads-sold-tickets

Compare your advertising by the ticket orders each campaign brought in rather than by clicks, so you know where to spend next.

For: Deciding where your advertising budget should go next.

What an agent can do: Fai can read the campaign figures back to you and say which campaign brought in each sale. Changing a budget is yours to do.

Command line:

- Show the event statistics: `ticketfairy event stats <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "For <EVENT NAME>, which advertising campaign brought in the most ticket sales, and what did each sale cost"

#### Then: Trace a sale back further than the campaign

What an agent can do: Fai can open the tracking links for the event. What each one brought in is read in the dashboard today.

Command line:

- Show the event statistics: `ticketfairy event stats <EVENT_ID>`

CLI MCP tools that read: `select_event`, `get_event`.

Prompt for Fai: "Open the tracking links for <EVENT NAME>"

### Set up a Meta pixel to track your ticket sales

Slug `set-up-a-meta-pixel`. Guide: https://www.ticketfairy.com/guides/set-up-a-meta-pixel

Connect Meta to your brand and choose which pixel records your ticket sales, so you can see which Facebook and Instagram campaigns sold tickets.

For: Running Meta ads for an event.

What an agent can do: Fai, the assistant inside your dashboard, can do this for you, and stops to ask you before she changes anything. Complete the Meta sign-in in your browser, then let Fai take it from there. You can also add the pixel in the dashboard.

Prompt for Fai: "I have connected Meta and want to see the pixels on our ad account, then turn conversion tracking on for the one we advertise with"

### Track ticket sales with your Amazon DSP pixel

Slug `set-up-an-amazon-dsp-pixel`. Guide: https://www.ticketfairy.com/guides/set-up-an-amazon-dsp-pixel

Add your Amazon DSP pixel once for your brand, and see which campaigns sold tickets.

For: Running campaigns in Amazon DSP.

What an agent can do: Give Fai the complete snippet from Amazon DSP, and she can add the pixel after asking you to approve the change. You can also add it in the dashboard.

Prompt for Fai: "Add an Amazon DSP tracking pixel to this brand using this complete snippet: <paste the snippet>"

### Track ticket sales with your ChatGPT pixel

Slug `set-up-a-chatgpt-pixel`. Guide: https://www.ticketfairy.com/guides/set-up-a-chatgpt-pixel

Add your ChatGPT pixel once for your brand, and see which campaigns sold tickets.

For: Running ChatGPT ads for an event.

What an agent can do: Fai can add this pixel after asking you to approve the change. You still need the pixel ID from ChatGPT. You can also add it in the dashboard.

Prompt for Fai: "Add a ChatGPT tracking pixel to this brand with ID <your ChatGPT pixel ID>"

### Track ticket sales with your Google Ads pixel

Slug `set-up-a-google-ads-pixel`. Guide: https://www.ticketfairy.com/guides/set-up-a-google-ads-pixel

Add your Google Ads pixel once for your brand, and see which campaigns sold tickets.

For: Running campaigns in Google Ads.

What an agent can do: Give Fai the complete snippet from Google Ads, and she can add the pixel after asking you to approve the change. You can also add it in the dashboard.

Prompt for Fai: "Add a Google Ads tracking pixel to this brand using this complete snippet: <paste the snippet>"

### Track ticket sales with your LinkedIn pixel

Slug `set-up-a-linkedin-pixel`. Guide: https://www.ticketfairy.com/guides/set-up-a-linkedin-pixel

Add your LinkedIn pixel once for your brand, and see which campaigns sold tickets.

For: Running LinkedIn ads for an event.

What an agent can do: Give Fai the complete snippet from LinkedIn, and she can add the pixel after asking you to approve the change. You can also add it in the dashboard.

Prompt for Fai: "Add a LinkedIn tracking pixel to this brand using this complete snippet: <paste the snippet>"

### Track ticket sales with your Microsoft Bing pixel

Slug `set-up-a-microsoft-bing-pixel`. Guide: https://www.ticketfairy.com/guides/set-up-a-microsoft-bing-pixel

Add your Microsoft Bing pixel once for your brand, and see which campaigns sold tickets.

For: Running Microsoft Bing ads for an event.

What an agent can do: Fai can add this pixel after asking you to approve the change. You still need the pixel ID from Microsoft Bing. You can also add it in the dashboard.

Prompt for Fai: "Add a Microsoft Bing tracking pixel to this brand with ID <your Microsoft Bing pixel ID>"

### Track ticket sales with your Pinterest pixel

Slug `set-up-a-pinterest-pixel`. Guide: https://www.ticketfairy.com/guides/set-up-a-pinterest-pixel

Add your Pinterest pixel once for your brand, and see which campaigns sold tickets.

For: Running Pinterest ads for an event.

What an agent can do: Fai can add this pixel after asking you to approve the change. You still need the pixel ID from Pinterest. You can also add it in the dashboard.

Prompt for Fai: "Add a Pinterest tracking pixel to this brand with ID <your Pinterest pixel ID>"

### Track ticket sales with your Reddit pixel

Slug `set-up-a-reddit-pixel`. Guide: https://www.ticketfairy.com/guides/set-up-a-reddit-pixel

Add your Reddit pixel once for your brand, and see which campaigns sold tickets.

For: Running Reddit ads for an event.

What an agent can do: Fai can add this pixel after asking you to approve the change. You still need the pixel ID from Reddit. You can also add it in the dashboard.

Prompt for Fai: "Add a Reddit tracking pixel to this brand with ID <your Reddit pixel ID>"

### Track ticket sales with your Snapchat pixel

Slug `set-up-a-snapchat-pixel`. Guide: https://www.ticketfairy.com/guides/set-up-a-snapchat-pixel

Add your Snapchat pixel once for your brand, and see which campaigns sold tickets.

For: Running Snapchat ads for an event.

What an agent can do: Fai can add this pixel after asking you to approve the change. You still need the pixel ID from Snapchat. You can also add it in the dashboard.

Prompt for Fai: "Add a Snapchat tracking pixel to this brand with ID <your Snapchat pixel ID>"

### Track ticket sales with your Spotify pixel

Slug `set-up-a-spotify-pixel`. Guide: https://www.ticketfairy.com/guides/set-up-a-spotify-pixel

Add your Spotify pixel once for your brand, and see which campaigns sold tickets.

For: Running Spotify ads for an event.

What an agent can do: Give Fai the complete snippet from Spotify, and she can add the pixel after asking you to approve the change. You can also add it in the dashboard.

Prompt for Fai: "Add a Spotify tracking pixel to this brand using this complete snippet: <paste the snippet>"

### Track ticket sales with your TikTok pixel

Slug `set-up-a-tiktok-pixel`. Guide: https://www.ticketfairy.com/guides/set-up-a-tiktok-pixel

Add your TikTok pixel once for your brand, and see which campaigns sold tickets.

For: Running TikTok ads for an event.

What an agent can do: Fai can add this pixel after asking you to approve the change. You still need the pixel ID from TikTok. You can also add it in the dashboard.

Prompt for Fai: "Add a TikTok tracking pixel to this brand with ID <your TikTok pixel ID>"

### Track ticket sales with your X pixel

Slug `set-up-an-x-twitter-pixel`. Guide: https://www.ticketfairy.com/guides/set-up-an-x-twitter-pixel

Add your X pixel once for your brand, and see which campaigns sold tickets.

For: Running X ads for an event.

What an agent can do: Fai can add this pixel after asking you to approve the change. You still need the pixel ID from X. You can also add it in the dashboard.

Prompt for Fai: "Add an X tracking pixel to this brand with ID <your X pixel ID>"

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
