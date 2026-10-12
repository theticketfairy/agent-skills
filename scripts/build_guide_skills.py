#!/usr/bin/env python3
"""Build one skill per Ticket Fairy guide family from the guide catalogue.

The guide entries live in the Ticket Fairy platform repository under
resources/guides/entries. Export the published ones to JSON from that
repository's root:

    php -r '$o=[];foreach(glob("resources/guides/entries/*.php") as $f){$g=require $f;
      if(($g["published"]??true)===false)continue;$o[]=["slug"=>$g["slug"],"title"=>$g["title"],
      "summary"=>$g["summary"],"family"=>$g["family"]??"","audience"=>$g["audience"]??"",
      "agent_paths"=>$g["agent_paths"]??null];}echo json_encode($o,JSON_UNESCAPED_SLASHES|JSON_UNESCAPED_UNICODE);' > guides.json

Then run, from this repository's root:

    python3 scripts/build_guide_skills.py guides.json

Each skill lists the guides of its family, what an agent can do for each one,
and the command-line and MCP routes the guide names. The steps themselves stay
in the guides: an agent reads them live with the guides MCP server, so a skill
never carries a stale copy.
"""

import json
import sys
from pathlib import Path

GUIDES_URL = 'https://www.ticketfairy.com/guides/'

# family -> (skill name, title, description, what the area covers)
FAMILIES = {
    'event-setup': (
        'set-up-event-tickets',
        'Set up event tickets',
        'Set up a Ticket Fairy event: ticket types, release tiers, sessions, seating, add-ons, resale and '
        'transfer rules. Use when an organiser wants to create or change what their event sells.',
        'ticket types, release tiers, multi-day and timed entry, seating, resale and transfer rules',
    ),
    'checkout-and-orders': (
        'manage-orders-and-refunds',
        'Manage orders and refunds',
        'Find and manage Ticket Fairy orders: checkout questions, order approval, refunds, transfers, '
        'waiting lists and buyer support. Use when an organiser asks about an order, a refund or the checkout.',
        'checkout questions, order approval, refunds, transfers, waiting lists and buyer support',
    ),
    'pricing-and-promotions': (
        'run-promotions-and-discounts',
        'Run promotions and discounts',
        'Create Ticket Fairy promo codes, group discounts and promoter links. Use when an organiser wants '
        'to give some buyers a better price.',
        'promo codes, group discounts and promoter links',
    ),
    'referral-marketing-ticketing': (
        'grow-sales-with-referrals',
        'Grow sales with referrals',
        'Set up Ticket Fairy referral rewards and see who brought in each sale. Use when an organiser '
        'wants buyers to bring their friends.',
        'referral rewards for buyers who bring friends, and who brought in each sale',
    ),
    'invitations-and-guests': (
        'manage-invitations-and-guest-lists',
        'Manage invitations and guest lists',
        'Send Ticket Fairy invitations and guest tickets, and manage partner allocations and group '
        'bookings. Use when an organiser wants to give people tickets without a normal purchase.',
        'invitations, guest tickets, partner allocations and group bookings',
    ),
    'add-ons-and-extras': (
        'sell-add-ons-and-tables',
        'Sell add-ons and tables',
        'Sell Ticket Fairy add-ons beside tickets: merchandise, parking, donations, tables and '
        'accommodation. Use when an organiser wants to sell extras with their event.',
        'merchandise, parking, donations, tables and accommodation',
    ),
    'marketing-and-messaging': (
        'email-and-market-to-buyers',
        'Email and market to buyers',
        'Send Ticket Fairy emails and SMS to buyers, design emails, and build event websites and landing '
        'pages. Use when an organiser wants to reach their buyers or promote an event.',
        'messages to buyers, email design, event websites and landing pages',
    ),
    'advertising-pixels': (
        'track-advertising-campaigns',
        'Track advertising campaigns',
        'Connect advertising pixels and conversion tracking to Ticket Fairy and see which campaigns sold '
        'tickets. Use when an organiser runs paid ads for an event.',
        'advertising pixels, conversion tracking and which campaigns sold tickets',
    ),
    'integrations': (
        'connect-ticketfairy-integrations',
        'Connect integrations',
        'Connect Ticket Fairy to Mailchimp, Zapier and other tools an organiser already uses. Use when an '
        'organiser wants their ticket data in another tool.',
        'Mailchimp, Zapier and the other tools an organiser already uses',
    ),
    'payments-and-payouts': (
        'get-paid-for-ticket-sales',
        'Get paid for ticket sales',
        'Set up Ticket Fairy payment accounts, choose who pays the fees, pick currencies and follow '
        'payouts. Use when an organiser asks how and when they get their money.',
        'payment accounts, who pays the fees, currencies and payouts',
    ),
    'vault-and-capital': (
        'use-vault-and-capital',
        'Use Vault and Capital',
        'Use the Ticket Fairy Vault account, cards, transfers and invoices, and Capital working capital. '
        'Use when an organiser asks about their Vault balance, cards, transfers or funding.',
        'the Vault account, cards, transfers, invoices and working capital',
    ),
    'door-and-checkin': (
        'run-door-check-in',
        'Run door check-in',
        'Run Ticket Fairy check-in at the door: scanning, entry rules, live check-in reports and '
        'wristbands. Use when an organiser prepares or runs entry to an event.',
        'scanning, entry rules, live check-in reports and wristbands',
    ),
    'venues': (
        'manage-venue-pages',
        'Manage venue pages',
        'Claim a Ticket Fairy venue page and keep its details current. Use when a venue team wants to '
        'control what people read about their venue.',
        'venue pages: claiming one and keeping its details current',
    ),
    'team-and-brands': (
        'manage-brand-and-team',
        'Manage the brand and team',
        'Manage a Ticket Fairy brand kit, team roles, several brands, collectives and account security. '
        'Use when an organiser wants to add people, change roles or organise brands.',
        'brand kit, team roles, several brands, collectives and account security',
    ),
    'reports-and-analytics': (
        'read-event-reports',
        'Read event reports',
        'Read Ticket Fairy event reports: sales, page views, buyers and what each figure counts. Use when '
        'an organiser asks how an event is selling or what a report means.',
        'the dashboard reports, what each one counts and how to use the figures',
    ),
    'fai-and-intelligence': (
        'work-with-fai',
        'Work with Fai',
        'Use Fai, the assistant inside the Ticket Fairy dashboard, for questions, the inbox and the buyer '
        'concierge. Use when an organiser wants Fai to do work for them.',
        'Fai in the dashboard, inbox handling and the buyer concierge',
    ),
    'event-os': (
        'run-event-production',
        'Run event production',
        'Run event production in Ticket Fairy Event Management: budgets, schedules, artists, crew, '
        'sponsors, traders, volunteers and compliance. Use when an organiser plans or runs the show itself.',
        'budgets, schedules, artists, crew, sponsors, traders, volunteers and compliance',
    ),
    'developers': (
        'build-with-the-ticketfairy-api',
        'Build with the Ticket Fairy API',
        'Use Ticket Fairy access tokens, API keys and webhooks, and sell from your own app. Use when a '
        'developer integrates with Ticket Fairy.',
        'access tokens, API keys, webhooks and selling from your own app',
    ),
    'workflows': (
        'run-event-workflows',
        'Run event workflows',
        'Follow Ticket Fairy start-to-finish workflows: on-sale day, repeating last year\'s event, and '
        'changing plans. Use when an organiser faces one of these moments.',
        'on-sale day, repeating last year\'s event, and changing plans',
    ),
    'playbooks': (
        'follow-event-type-playbooks',
        'Follow event-type playbooks',
        'Follow the Ticket Fairy order of work for festivals, club nights, tours, conferences and other '
        'event types. Use when an organiser plans a whole event of one type.',
        'the order of work for festivals, club nights, tours, conferences and more',
    ),
    'answers': (
        'solve-ticketing-problems',
        'Solve ticketing problems',
        'Solve common event ticketing problems with Ticket Fairy: queues, no-shows, reports, marketing and '
        'access. Use when an organiser describes a problem rather than a feature.',
        'queues, no-shows, reports, marketing and access',
    ),
}

HOW_TO_WORK = """## How to work

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
"""


def bullet_list(items):
    return '\n'.join(f'- {item}' for item in items)


def guide_section(guide):
    paths = guide.get('agent_paths') or {}
    lines = [
        f"### {guide['title']}",
        '',
        f"Slug `{guide['slug']}`. Guide: {GUIDES_URL}{guide['slug']}",
        '',
        guide['summary'],
    ]
    if guide.get('audience'):
        lines += ['', f"For: {guide['audience']}."]
    if paths.get('summary'):
        lines += ['', f"What an agent can do: {paths['summary']}"]
    cli = paths.get('cli') or {}
    commands = cli.get('commands') or []
    if commands:
        lines += ['', 'Command line:', '']
        lines += [f"- {command['does'].rstrip('.')}: `{command['run']}`" for command in commands]
    if paths.get('mcp_tools'):
        tools = ', '.join(f'`{tool}`' for tool in paths['mcp_tools'])
        mode = 'reads and writes' if paths.get('mcp_writes') else 'reads'
        lines += ['', f'CLI MCP tools ({mode}): {tools}.']
    if paths.get('fai_prompt'):
        lines += ['', f"Prompt for Fai: \"{paths['fai_prompt']}\""]
    return '\n'.join(lines)


def build_skill(family, guides):
    name, title, description, covers = FAMILIES[family]
    guides = sorted(guides, key=lambda guide: guide['title'].lower())
    index = bullet_list(f"[{guide['title']}](#{anchor(guide['title'])})" for guide in guides)
    body = '\n\n'.join(guide_section(guide) for guide in guides)

    return f"""---
name: {name}
description: {json.dumps(description, ensure_ascii=False)}
---

# {title}

This skill covers {covers} on Ticket Fairy. It lists the {len(guides)} published guides for this area and what an agent can do for each one.

{HOW_TO_WORK}
## Guides

{index}

{body}

## More

- All guides: https://www.ticketfairy.com/guides
- Guides MCP server: https://www.ticketfairy.com/docs/mcp (tools `search_guides` and `get_guide`)
- CLI reference: https://www.npmjs.com/package/ticketfairy
- Developer documentation: https://www.ticketfairy.com/developers
- Support: support@ticketfairy.com
"""


def anchor(title):
    kept = ''.join(char for char in title.lower() if char.isalnum() or char in ' -')
    return kept.strip().replace(' ', '-')


def main():
    if len(sys.argv) != 2:
        sys.exit('Usage: build_guide_skills.py <guides.json>')
    guides = json.loads(Path(sys.argv[1]).read_text())
    by_family = {}
    for guide in guides:
        by_family.setdefault(guide.get('family', ''), []).append(guide)

    unknown = sorted(set(by_family) - set(FAMILIES))
    if unknown:
        sys.exit('Guide families with no skill: ' + ', '.join(unknown))

    skills_dir = Path(__file__).resolve().parent.parent / 'skills'
    for family, family_guides in by_family.items():
        name = FAMILIES[family][0]
        target = skills_dir / name / 'SKILL.md'
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(build_skill(family, family_guides))
        print(f'{target.relative_to(skills_dir.parent)}: {len(family_guides)} guide(s)')


if __name__ == '__main__':
    main()
