---
name: answer-ticketfairy-questions
description: "Answer how-to questions about Ticket Fairy from the official guides, with the guides MCP server. Use when someone asks how to do something on Ticket Fairy, such as add a promo code, refund an order or scan tickets at the door."
---

# Answer Ticket Fairy questions

Answer "how do I ... on Ticket Fairy?" from the published guides, not from memory. The guides
cover event setup, checkout and orders, promotions, guest lists, add-ons, messaging, payouts,
check-in, teams, reports and event production.

## Connect

The guides MCP server needs no account and no key:

- Endpoint: `https://www.ticketfairy.com/docs/mcp` (Streamable HTTP)
- Server card: https://www.ticketfairy.com/docs/mcp/server-card

It has two read-only tools.

| Tool | Input | Returns |
| --- | --- | --- |
| `search_guides` | `query`: what the person wants to do, in plain words (2 to 500 characters) | At most 5 guides, best match first, each with `guide_slug`, `title`, `summary`, `screen`, `url` and `agent_tools` |
| `get_guide` | `guide`: a `guide_slug` from a search, or a guide link such as `https://www.ticketfairy.com/guides/create-an-event` | One guide as plain text: `audience`, `intro`, `before_you_start`, `steps`, `questions`, `agent_summary` and `related_guides` |

Without an MCP client, POST JSON-RPC to the endpoint with `Content-Type: application/json` and
`Accept: application/json, text/event-stream`:

```sh
curl -sS https://www.ticketfairy.com/docs/mcp \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json, text/event-stream' \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"search_guides","arguments":{"query":"add a promo code"}}}'
```

## Answer a question

1. Call `search_guides` with the person's question in their own words.
2. Pick the guide whose `title` and `summary` match what they want. If two are close, ask which
   one they mean.
3. Call `get_guide` with its `guide_slug`.
4. Answer from the guide:
   - Check `before_you_start` first. Tell the person if they need a role, a setting or something
     ready before the steps work.
   - Give the steps in order, with the page names the guide uses.
   - Use `questions` for the follow-up questions people usually ask.
   - End with the guide's `url`, so they can open it.
5. If the person wants the work done for them, read `agent_summary`. It says what Fai, the
   assistant in their dashboard, the command-line tool or MCP can do for that task.

## Rules

- Quote the guide; do not invent menu names, settings or limits.
- If no guide matches, say so and point to https://www.ticketfairy.com/guides or
  support@ticketfairy.com.
- Guides describe the organiser dashboard. A ticket buyer with an order question should contact
  the event organiser, whose details are on their ticket email.
- The tools only read guides. They cannot change an account, an event or an order.

## Related skills

- Skills for each area, such as `manage-orders-and-refunds` and `run-promotions-and-discounts`,
  list every guide of that area with its command-line and MCP routes.
- `find-event-tickets` finds public events for a ticket buyer.
