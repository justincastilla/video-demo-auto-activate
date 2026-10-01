"""terminal-demo-video spec for "Video 5: Flox environments are ready when you are (Auto Activate full)".

Every typed command matches SCRIPT.md exactly. Things the script cuts past between shots (leaving a
directory, clearing the screen) happen off camera with hidden(). The sample projects in sample/ are
copied into a fresh directory per recording, which uses its own Flox config dir, so allow/deny
decisions and `flox config --set` never touch the real ~/.config/flox.

Render:  ~/.claude/skills/terminal-demo-video/scripts/tdv draft .
"""

import os
import subprocess

from engine import Event, cmd, hidden, key, sleep, type_, wait

SLUG = "tanja"
BASE_ROOT = "/tmp"
HERE = os.path.dirname(os.path.abspath(__file__))

SCENES = {
    "s1_hook": "What if activating your dev environment was as simple as changing directories?",
    "s2_auto": "With Flox auto-activation, it is. Say yes once, and whenever you come back, your environment "
               "activates automatically.",
    "s3_there": "Your packages, variables, and hooks are already there.",
    "s4_services": "And it isn't just tools and variables. If your project declares services, you can have Flox "
                   "start them with the environment. Nothing running. Your dev server is already listening when "
                   "you cd in. No separate start script.",
    "s5_monorepo": "And this works the way you'd hope in a monorepo. Go deeper and environments stack. The inner "
                   "one layers on top of the outer one, you get both. Come back out and they unwind, one layer at "
                   "a time.",
    "s6_run": "Need something that isn't in the environment, or even installed on your machine? Just run it with Flox.",
    "s7_leave": "And when you leave, Flox deactivates the environment and shuts the server down with it. No stray "
                "process holding port 3000 because you forgot about it three days ago.",
    "s8_remember": "Now, you saw Flox ask before activating that first environment. You don't have to answer that "
                   "question every time. Allow it or deny it, and Flox remembers that directory. No more prompt.",
    "s9_config": "Or change how Flox behaves everywhere. Allowlist means Flox only activates projects you've "
                 "already said yes to, and stops asking about new ones. Disabled turns the whole thing off. Your "
                 "machine, your rules.",
}

WAIT_ESTIMATES = {"activate": 2.0, "in1": 2.0, "mono": 1.5, "deeper": 1.5, "run": 1.5}

HIDDEN_SETUP = ["source {build}/setup.sh {base}"]
HIDDEN_TEARDOWN = ["cd /", "flox services stop -d {base}/my-project >/dev/null 2>&1; true"]

SETUP = """\
# Sourced off camera in the recording shell: $1 = fresh base dir.
B="$1"
rsync -a --exclude '.flox/cache' --exclude '.flox/log' "{fixtures}/" "$B/"
export FLOX_CONFIG_DIR="$B/.flox-config"
mkdir -p "$FLOX_CONFIG_DIR"
flox config --set hide_default_prompt true >/dev/null
(cd "$B/monorepo" && flox activate allow >/dev/null 2>&1)
(cd "$B/monorepo/services/api" && flox activate allow >/dev/null 2>&1)
export RIPGREP_CONFIG_PATH="$B/ripgreprc"      # the script shows rg output without line numbers
flox run rg -- --version >/dev/null 2>&1 </dev/null   # resolve rg once here, not on camera
# Any in-place activation installs Flox's prompt hook; an env named 'default' is hidden from the prompt.
flox init -d "$B/.hook" -n default >/dev/null 2>&1
export PS1='\\[\\e[1;35m\\]$\\[\\e[0m\\] '
eval "$(flox activate -d "$B/.hook")"
# After the on-camera y/N answer, the script never shows Flox's "You are now using the environment"
# lines, so later shots run the hook with its messages silenced.
# Silence the hook's messages ("You are now using the environment ...") while it keeps working.
# Activations prepend fresh `_flox_hook;` calls to PROMPT_COMMAND and may redefine the function,
# so wrap the function once and lock the wrapper; every call then goes through it.
quiet_flox_hook() {
  [ "$(type -t _flox_hook_loud)" = function ] && return
  eval "$(declare -f _flox_hook | sed '1s/_flox_hook/_flox_hook_loud/')"
  _flox_hook() { _flox_hook_loud 2>/dev/null; }
  readonly -f _flox_hook
}
# The allow/deny shot shows only the two commands, so their confirmations are silenced there.
quiet_flox() { flox() { command flox "$@" >/dev/null 2>&1; }; }
cd "$B"
"""


def prepare(build):
    fx = os.path.join(build, "fixtures")
    os.makedirs(fx, exist_ok=True)
    subprocess.run(["rsync", "-a", "--exclude", ".flox/cache", "--exclude", ".flox/log",
                    os.path.join(HERE, "sample") + "/", fx + "/"], check=True)
    # Build every environment now (and fetch ripgrep) so nothing builds or downloads on camera.
    for d in ("my-project", "monorepo", "monorepo/services/api"):
        subprocess.run(["flox", "activate", "--no-start-services", "-d", os.path.join(fx, d), "--", "true"],
                       check=True, capture_output=True)
    subprocess.run(["flox", "run", "rg", "--", "--version"], check=True, capture_output=True, stdin=subprocess.DEVNULL)
    open(os.path.join(build, "setup.sh"), "w").write(SETUP.replace("{fixtures}", fx))


def events():
    return [
        # 0:00-0:05 Hook: plain terminal, `$ cd my-project`
        Event("s1_hook", "changing directories", lambda: cmd("cd my-project", settle=0.6)),

        # 0:05-0:12 Auto-activate: answer the one-time question with a deliberate y
        Event("s2_auto", "say yes", lambda: [sleep(0.3), type_("y"), sleep(0.4), key("Enter"), wait("activate")]),

        # 0:12-0:19 Everything is there (new shot: the environment is live)
        Event("s3_there", "START", lambda: [hidden("quiet_flox_hook; clear")]),
        Event("s3_there", "your packages", lambda: cmd("node --version", "node"), hard=False),
        Event("s3_there", "variables", lambda: cmd("echo $NODE_ENV", "env1"), hard=False),
        Event("s3_there", "hooks", lambda: cmd("echo $API_URL", "env2"), hard=False),

        # 0:19-0:29 Services: cut to the manifest's [services] block
        Event("s4_services", "isn't just", lambda: [hidden("clear; tail -n 4 .flox/env/manifest.toml")]),
        # Before state: outside the environment, nothing is listening
        Event("s4_services", "the environment",
              lambda: [hidden("cd ..", "clear")] + cmd("curl localhost:3000", "curl1"), hard=False),
        # Now cd in, and run the same command
        Event("s4_services", "dev server", lambda: [hidden("quiet_flox_hook; clear")] + cmd("cd my-project", "in1")),
        Event("s4_services", "listening", lambda: cmd("curl localhost:3000", "curl2"), hard=False),

        # 0:29-0:39 Monorepos: descend...
        Event("s5_monorepo", "START", lambda: [hidden("cd ..", "quiet_flox_hook; clear")]),
        Event("s5_monorepo", "monorepo", lambda: cmd("cd monorepo", "mono")),
        Event("s5_monorepo", "go deeper", lambda: cmd("cd services/api", "deeper")),
        # ...and climb back out
        Event("s5_monorepo", "come back out", lambda: [hidden("clear")] + cmd("cd ..", "up1")),
        Event("s5_monorepo", "one layer", lambda: cmd("cd ..", "up2"), occurrence=2, hard=False),

        # 0:39-0:45 One more tool
        Event("s6_run", "START", lambda: [hidden("cd ../my-project", "quiet_flox_hook; clear")]),
        Event("s6_run", "even installed", lambda: [type_("flox run rg -- TODO notes.txt")], hard=False),
        Event("s6_run", "just run it", lambda: [key("Enter"), wait("run")]),

        # 0:45-0:50 Back out
        Event("s7_leave", "START", lambda: [hidden("clear")]),
        Event("s7_leave", "when you leave", lambda: cmd("cd ..", "leave")),

        # 0:50-0:58 Decide up front, from inside the project (plain prompt: activation paused off camera)
        Event("s8_remember", "START",
              lambda: [hidden("flox config --set auto_activate disabled", "cd my-project", "quiet_flox; clear")]),
        Event("s8_remember", "allow it", lambda: cmd("flox activate allow", "allow")),
        Event("s8_remember", "deny it", lambda: cmd("flox activate deny", "deny"), hard=False),

        # 0:58-1:05 Or change the default
        Event("s9_config", "START", lambda: [hidden("clear")]),
        Event("s9_config", "behaves everywhere", lambda: cmd("flox config --set auto_activate allowlist", "config")),
    ]
