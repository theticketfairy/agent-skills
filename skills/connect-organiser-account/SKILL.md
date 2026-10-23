---
name: connect-organiser-account
description: "Get a Ticket Fairy organiser credential for an AI agent, with the person's approval, and use it on the organiser API. Use when an agent must act for an organiser, for example to create events, read sales or copy an event's setup."
---

# Connect an organiser account

An agent acts for an organiser only with a token the organiser approves. The token carries the
person's team roles, so it reaches only the brands and events they can reach. The full protocol
is in https://www.ticketfairy.com/auth.md; this skill is the short path.

## Before you start

- The person needs a Ticket Fairy organiser account. If they have none, use
  `start-organising-events` if installed, or read its [published instructions](https://www.ticketfairy.com/.well-known/agent-skills/start-organising-events/SKILL.md).
  They can also start at https://manage.ticketfairy.com. Signup, legal terms and email
  verification happen in their browser.
- Tell the person what you will do with the access, and confirm that they want to continue.

## Pick a method

| Situation | Method |
| --- | --- |
| You know the person's email address, or can ask for it. Works from a hosted service. | Claim ceremony (below) |
| You run on the person's own computer and can open their browser | The CLI: ask first, then `npm install -g ticketfairy` and `ticketfairy login`. See the `manage-events-with-the-cli` skill. |
| Your runtime reads secrets from its environment or a secret store | A Personal Access Token the person creates at https://manage.ticketfairy.com/account (Personal Access Tokens section) and stores in `TICKET_FAIRY_API_KEY` themselves |

Never ask the person to paste a token into the chat, and never put one in a URL, a file you commit
or a log. A token in a conversation stays in its history. If the person has no secret store for
you, use the claim ceremony instead.

## Claim ceremony

1. Ask for access:

   ```http
   POST https://www.theticketfairy.com/api/agent/identity
   Content-Type: application/json

   {"type": "service_auth", "login_hint": "person@example.com", "agent_name": "Acme Assistant"}
   ```

   `agent_name` is what the person sees on the approval page. Keep `claim_token` from the response
   in memory only, and never put it in a URL. Keep `client_id` too: store it with the refresh token,
   because refreshing the access token needs it.

2. Send the person `claim.verification_uri` and `claim.user_code` in one message:

   > Open this link, sign in to Ticket Fairy, and enter this 6-digit code: **123456**

   The code goes into the page they open, not back to you.

3. Poll for the token every `claim.interval` seconds:

   ```http
   POST https://www.theticketfairy.com/api/oauth/access_token
   Content-Type: application/x-www-form-urlencoded

   grant_type=urn:workos:agent-auth:grant-type:claim&claim_token=clm_...
   ```

   `authorization_pending` means wait and poll again. `expired_token` means the 30-minute window
   closed; start again at step 1. On approval you get `access_token` and `refresh_token`. Store
   them securely.

## Use the token

Send `Authorization: Bearer <access_token>` and `Accept: application/vnd.api+json` on every
organiser request. Without that Accept header, some addresses answer 400 `NOT_LOGGED_IN`.

To check who the token acts for: `GET https://www.ticketfairy.com/api/v1/agent/identity`.

The organiser operations are described in https://www.theticketfairy.com/api/openapi.json:

| Operation | Request |
| --- | --- |
| Create an event (a draft needs only a name and `flagDraft: true`) | `POST https://www.theticketfairy.com/api/events` with an `Idempotency-Key` |
| Read an event's sales by day and by ticket type | `GET https://www.theticketfairy.com/api/events/{eventId}/relationships/performance?section=sales\|release_breakdown` |
| Find an event to copy the setup from | `GET https://www.theticketfairy.com/api/event/{eventId}/setup-copy/sources` |
| Preview a setup copy | `GET https://www.theticketfairy.com/api/event/{eventId}/setup-copy/preview?source_event_id=...` |
| Start a setup copy (answers 202 with a `Location`) | `POST https://www.theticketfairy.com/api/event/{eventId}/setup-copy/runs` |
| Follow a setup copy until `done`, `partly_done` or `failed` | `GET` the `Location` address |

Show the person what you will create or copy before you send it. Show a setup copy preview and
send only the parts they choose.

## Errors

| Answer | What to do |
| --- | --- |
| 401 | The token expired or was revoked. With a `refresh_token`, POST `grant_type=refresh_token&client_id=<client_id>&refresh_token=<refresh_token>` to the token endpoint. Otherwise ask the person again. |
| 403 | The person's role does not allow it. Tell them; do not retry. |
| 422 | Read the message and correct the request. `no_dashboard_access` means the account has no organiser access. |
| 429 | Wait for `Retry-After`. Do not retry in parallel. |

## Limits

- A token cannot buy tickets or pay for anything. Checkout, payment, bank and tax details and
  plan purchases stay in the person's browser.
- A Personal Access Token cannot create another Personal Access Token.
- The person can end your access at any time. To remove your own session, list the sessions with
  `GET https://www.theticketfairy.com/api/oauth/sessions`, find yours by the name you gave, then
  send `DELETE https://www.theticketfairy.com/api/oauth/sessions/<session_id>`. Remove only your
  own session.
