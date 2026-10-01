🎥 Video 5 Flox environments are ready when you are (Auto Activate full) by Tanja 
Speaker: Tanja
Recording session: Tanja — 2026
Recording date: Unknown — not yet scheduled
Original script source: Drafted in this repository; not imported from a document
Recording source: Not yet recorded
Length: ~1:05
Format: Horizontal + vertical
Script and production directions
This is the long-form version. It is a single continuous script: no optional beats, no branches, shoot it top to bottom.
03-auto-activate-short.md is the ~28-second cut of the same material — the first half of this video, roughly. Use that one for social; use this one for the docs page, a release post, or YouTube proper.

Pronunciation guide
Written
Say it
Notes
Flox
FLOKS
One syllable, rhymes with "box."
cd
see-dee
Spelled out.
curl
CURL
As the word.
ripgrep
RIP-grep
The command is rg (ARR-GEE) — see the note in beat 6.
allowlist
ah-LOW-list
One word.
config
CON-fig
flox config is said "flox config," not "configuration."
monorepo
MONO-repo


localhost
LOCAL-host


NODE_ENV
N-O-D-E env
Read the variable as "node env."
API_URL
A-P-I U-R-L
Spelled out.

Spoken in this script: Flox, cd, curl, ripgrep, allowlist, config, monorepo, localhost. On screen only: NODE_ENV, API_URL, auto_activate.

0:00–0:05 | Hook
Production: Open on a plain terminal. No Flox prompt yet.
TANJA: What if activating your dev environment was as simple as changing directories?
Terminal: Just this (illustrative):
$ cd my-project

0:05–0:12 | Auto-activate
Terminal: The prompt appears verified wording:
? Auto-activate the environment in '/home/tanja/my-project'? (y/N) y
Production: Type the y deliberately. This is a one-time decision and the video should make that feel like a small, safe thing.
TANJA: With Flox auto-activation, it is.
Say yes once, and whenever you come back, your environment activates automatically.

0:12–0:19 | Everything is there
TANJA: Your packages, variables, and hooks are already there.
Terminal: The environment is live (illustrative):
flox [my-project] $ node --version
v22.11.0

flox [my-project] $ echo $NODE_ENV
development

flox [my-project] $ echo $API_URL
http://localhost:3000
Production: Note the prompt has changed to show the active environment. Worth a beat — it's the visual proof that something happened.
On-screen:
cd in → environment active

0:19–0:29 | Services start too
TANJA: And it isn't just tools and variables.
Terminal: Cut to the manifest (verified):
[services]
auto-start = true

api.command = "node server.js"
Production: Highlight auto-start = true for a beat — that one line is the opt-in; without it the service is declared but stays stopped until you run flox services start.
TANJA: If your project declares services, you can have Flox start them with the environment.
Production: Show the before state first. Step out of the environment and prove nothing is running — this is what makes the next shot mean something.
Terminal: Outside the environment (verified):
$ curl localhost:3000
curl: (7) Failed to connect to localhost port 3000 after 0 ms: Couldn't connect to server
TANJA: Nothing running.
Terminal: Now cd in, and run the same command (verified):
$ cd my-project
flox [my-project] $ curl localhost:3000
{"status":"ok","service":"api"}
Production: Same command, two results. Keep the curl text in the same screen position across both shots so the only thing that changes is the response.
TANJA: Your dev server is already listening when you cd in. No separate start script.
On-screen:
cd in → service running

0:29–0:39 | Monorepos: environments stack
TANJA: And this works the way you'd hope in a monorepo.
Terminal: A hierarchy of environments (illustrative):
monorepo
├── .flox
└── services
    └── api
        └── .flox
Production: A file-tree graphic reads better than real tree output at speed. The point is only that environments sit inside environments.
Terminal: Descend into the hierarchy (illustrative):
$ cd monorepo
flox [monorepo] $ cd services/api
flox [api monorepo] $
Production: The prompt is the whole shot. Frame on it. [monorepo] becomes [api monorepo] — both environments are live, innermost first.
TANJA: Go deeper and environments stack. The inner one layers on top of the outer one — you get both.
Terminal: And climbing back out unwinds them:
flox [api monorepo] $ cd ..
flox [monorepo] $ cd ..
$
TANJA: Come back out and they unwind, one layer at a time.
On-screen:
nested repos → environments stack

0:39–0:45 | One more tool
TANJA: Need something that isn't in the environment — or even installed on your machine?
Terminal: flox run rg, not flox run ripgrep — see the appendix:
flox [my-project] $ flox run rg -- TODO notes.txt
beta TODO fix
TANJA: Just run it with Flox.

0:45–0:50 | Back out
Terminal: Leave the directory (illustrative):
flox [my-project] $ cd ..
$
Production: Show the prompt reverting to the plain shell. The absence of the Flox prompt is the payoff — hold it for a beat. This is also where the service stops; one cd .. shot carries both.
TANJA: And when you leave, Flox deactivates the environment and shuts the server down with it.
No stray process holding port 3000 because you forgot about it three days ago.
On-screen:
cd in. Get to work. cd out. Done.

0:50–0:58 | Don't ask me every time
Production: Shift in register here — the demo is over, this is the reassurance section. Slow down slightly.
TANJA: Now — you saw Flox ask before activating that first environment.
You don't have to answer that question every time.
Terminal: Decide up front, from inside the project (verified):
$ flox activate allow
$ flox activate deny
Production: Show them as a pair. The symmetry is the point: this isn't a way to say yes, it's a way to settle the question either way.
TANJA: Allow it or deny it, and Flox remembers that directory. No more prompt.
On-screen:
answered once → remembered

0:58–1:05 | Or change the default
TANJA: Or change how Flox behaves everywhere.
Terminal: One setting, three values (verified):
$ flox config --set auto_activate allowlist
Production: Show the three values as an overlay rather than typing all three — six seconds of near-identical text reads as filler. Hold on the overlay while Tanja explains.
On-screen:
prompt — ask about new projects (default) allowlist — only ones you already allowed, never ask disabled — off entirely
TANJA: Allowlist means Flox only activates projects you've already said yes to, and stops asking about new ones.
Disabled turns the whole thing off.
TANJA: Your machine, your rules.
On-screen:
Your environment. Ready when you are. flox.dev
