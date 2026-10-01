# Flox environments are ready when you are

Try Flox auto-activation yourself: `cd` into a project and its environment (packages, variables,
hooks, even a dev server) is ready, then `cd` out and it all goes away. This repo holds the sample
projects from the "Flox environments are ready when you are" video, so you can follow along step by
step.

## What you need

- [Flox](https://flox.dev/download) (made with Flox 1.17.0)
- `curl`
- Port 3000 free (the sample's dev server listens there)

## One-time setup: the Flox prompt hook

Auto-activation runs from a small hook in your shell's prompt. Any in-place activation installs it,
so if your shell startup file already has a line like `eval "$(flox activate ...)"`, you're set.

If not, add your FloxHub default environment to your shell startup file (`~/.zshrc`, `~/.bashrc`, ...),
as the Flox docs suggest:

```bash
eval "$(flox activate -D)"
```

Or, without FloxHub, activate an empty local environment named `default` and keep it out of your prompt:

```bash
flox init -d ~/.flox-hook -n default
flox config --set hide_default_prompt true
# then in your shell startup file:
eval "$(flox activate -d ~/.flox-hook)"
```

Open a new terminal, then clone this repo:

```bash
git clone https://github.com/justincastilla/video-demo-auto-activate.git
cd video-demo-auto-activate/sample
```

## 1. `cd` in, say yes once

```bash
cd my-project
```

The first time, Flox asks:

```
! Auto-activate the environment in '/path/to/video-demo-auto-activate/sample/my-project'? (y/N)
```

Type `y`. Flox remembers the answer for this directory, activates the environment, and your prompt changes:

```
✔ You are now using the environment 'my-project'
flox [my-project] $
```

The first activation also downloads Node.js, so give it a moment.

## 2. Everything is already there

```console
flox [my-project] $ node --version
v22.11.0
flox [my-project] $ echo $NODE_ENV
development
flox [my-project] $ echo $API_URL
http://localhost:3000
```

All of it comes from `my-project/.flox/env/manifest.toml`: the `[install]` section pins Node, and
`[vars]` sets the variables.

## 3. Services start too

The same manifest declares a service and opts in to starting it automatically:

```toml
[services]
auto-start = true

api.command = "node server.js"
```

Without `auto-start = true` the service is declared but stays stopped until you run
`flox services start`. With it, the dev server in `server.js` is already listening:

```console
flox [my-project] $ curl localhost:3000
{"status":"ok","service":"api"}
```

Now step out and try the same command:

```console
flox [my-project] $ cd ..
$ curl localhost:3000
curl: (7) Failed to connect to localhost port 3000 after 0 ms: Couldn't connect to server
```

Leaving the directory deactivated the environment and stopped the server: no stray process holding
port 3000. `cd my-project` again and it's back, with no question this time.

## 4. Monorepos: environments stack

`monorepo/` has its own environment, and so does `monorepo/services/api/` inside it:

```
monorepo
├── .flox
└── services
    └── api
        └── .flox
```

Answer `y` the first time Flox asks about each one:

```console
$ cd monorepo
flox [monorepo] $ cd services/api
flox [api monorepo] $
```

Both environments are active, innermost first. Climb back out and they unwind one layer at a time:

```console
flox [api monorepo] $ cd ../..
flox [monorepo] $ cd ..
$
```

## 5. One more tool, without installing it

Need a tool that isn't in the environment, or even installed on your machine? Run it with Flox:

```console
$ cd my-project
flox [my-project] $ flox run rg -- TODO notes.txt
2:beta TODO fix
```

`flox run` finds the package that provides `rg` (ripgrep) in the Flox catalog and runs it without
adding it to the environment. The first run resolves and downloads it. (In the video, ripgrep is
configured to hide line numbers; `export RIPGREP_CONFIG_PATH=$PWD/../ripgreprc` does the same here.)

## 6. Decide up front

You don't have to wait for the question. From inside a project directory, settle it either way:

```console
$ flox activate allow
✔ Auto-activation allowed for 'my-project'.

$ flox activate deny
✔ Auto-activation denied for 'my-project'.
```

Flox stores these decisions in your user config under `auto_activate_environments`; run
`flox config` to see them.

## 7. Change the default everywhere

One setting controls how Flox treats directories you haven't decided about yet:

```bash
flox config --set auto_activate allowlist
```

| Value | Behaviour |
|---|---|
| `prompt` | Ask about new projects (the default) |
| `allowlist` | Only activate projects you've already allowed; never ask |
| `disabled` | Auto-activation off entirely |

To go back to the default: `flox config --set auto_activate prompt`.

## What's in the sample

| Path | What it is |
|---|---|
| `sample/my-project/` | Flox environment with Node.js 22.11.0, `NODE_ENV` and `API_URL`, and an auto-started `api` service |
| `sample/my-project/server.js` | The dev server: answers `{"status":"ok","service":"api"}` on port 3000 |
| `sample/my-project/notes.txt` | Text for the `flox run rg` step |
| `sample/monorepo/`, `sample/monorepo/services/api/` | Nested environments for the stacking step |
| `sample/ripgreprc` | Optional ripgrep config that hides line numbers |

`SCRIPT.md` and `demo.py` are the video's production script and the spec used to record its
terminal footage.

Learn more in the [Flox docs](https://flox.dev/docs) or with `man flox-activate` (see the
AUTO-ACTIVATION section).
