---
name: manage-events-with-the-cli
description: "Manage Ticket Fairy events, tickets, orders, customers, invitations, promotions, check-in and webhooks with the official ticketfairy CLI or its MCP server. Use when an organiser wants an agent or a script to work on their own Ticket Fairy account."
---

# Manage events with the CLI

`ticketfairy` is the official command-line tool for organisers. It gives scripts and agents
stable JSON output, documented exit codes and safe retries. It acts as the signed-in person, with
the same permissions they have in the dashboard.

## Set up

Ask the person before you install anything. The CLI needs Node.js 20 or newer.

```sh
npm install -g ticketfairy
ticketfairy --version
```

Sign in with one of these:

| Where you run | How |
| --- | --- |
| The person's own computer, with a browser | `ticketfairy login` (opens the browser, supports 2FA, keeps the token in the system keychain) |
| CI, a server or a hosted agent | A Personal Access Token in `TICKET_FAIRY_API_KEY`. The person creates it at https://manage.ticketfairy.com/account or with `ticketfairy auth tokens create "<name>"`. |

Then check the account and pick the brand:

```sh
ticketfairy auth status
ticketfairy brand list
ticketfairy brand use <BRAND_ID>
```

## Rules for agents

- Pass `--output json --non-interactive` on every command. Read data from stdout; logs go to
  stderr.
- Branch on the exit code: `0` success, `2` usage, `3` network, `4` authentication, `5` not
  found, `6` conflict or verification required, `7` rate limited.
- Errors in JSON mode are `{"error": {"code", "message", "hint", "request_id"}}`. Follow `hint`.
- Use `--dry-run` to show the person a change before you make it. Destructive commands need an
  explicit `--force`; pass it only after the person agrees.
- For a retry across separate runs, pass the same `--idempotency-key <uuid>` so the server does
  not create a duplicate.
- `ticketfairy <command> --help --output json` returns a command's schema.
  `ticketfairy manifest` returns the whole command tree.
- `VERIFICATION_REQUIRED` (exit 6) on `event publish`, `messaging send` or `invitation send`
  means the person must run `ticketfairy account verify` and finish identity verification in
  their browser.

## Common tasks

| Task | Command |
| --- | --- |
| List events on the active brand | `ticketfairy event list` |
| Open one event | `ticketfairy event get <EVENT_ID>` |
| Sales and performance | `ticketfairy event stats <EVENT_ID> --metric sales` |
| Create or change an event from a file | `ticketfairy event create --from-file event.json` |
| Copy an event | `ticketfairy event clone <EVENT_ID>` |
| Publish or unpublish | `ticketfairy event publish <EVENT_ID>`, `ticketfairy event unpublish <EVENT_ID>` |
| Ticket types | `ticketfairy ticket list <EVENT_ID>` |
| Orders, filtered by status | `ticketfairy order list <EVENT_ID> --status paid` |
| Export orders to CSV | `ticketfairy order export <EVENT_ID> --format csv --file orders.csv` |
| Customers | `ticketfairy customer search <TERM>` |
| Promotions | `ticketfairy promotion list <EVENT_ID>` |
| Send invitations from a CSV | `ticketfairy invitation send <EVENT_ID> --from-csv guests.csv --ticket-type <TICKET_TYPE_ID>` |
| Check-in status | `ticketfairy checkin status <EVENT_ID> --breakdown ticket-types` |
| Webhooks | `ticketfairy webhook list` |
| Team | `ticketfairy team list` |
| Any other API endpoint, with authentication attached | `ticketfairy api <PATH> -X <METHOD>` |

Run `ticketfairy <group> --help` for every flag. The guide skills, such as
`manage-orders-and-refunds`, list the exact command for each guide.

## MCP server

The CLI is also an MCP server. Add it to the client configuration:

```json
{
  "mcpServers": {
    "ticketfairy": {
      "command": "ticketfairy",
      "args": ["mcp", "--read-only"]
    }
  }
}
```

It uses the same sign-in as the CLI. `--read-only` exposes read tools only; start there and drop
it only when the person wants you to make changes. The client asks the person to approve
destructive actions.

## Limits

- The CLI cannot take payment, enter bank or tax details or buy a plan. Those stay in the
  person's browser.
- Vault commands are read-only and work only for brands enrolled in Vault.
- Event Management commands (`ticketfairy event-os`) need Event Management on the brand.

More: https://www.npmjs.com/package/ticketfairy and https://www.ticketfairy.com/developers
