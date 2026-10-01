# Video 5: Flox environments are ready when you are (Auto Activate full)

Terminal footage for the long-form auto-activation video (speaker: Tanja, ~1:05). The production
script is in [SCRIPT.md](SCRIPT.md).

- `sample/` holds the code the video runs against:
  - `my-project/`: Flox env with Node 22.11.0, `NODE_ENV`/`API_URL`, and an auto-started `api`
    service (`node server.js`) that answers `{"status":"ok","service":"api"}` on port 3000;
    `notes.txt` for the `flox run rg` beat.
  - `monorepo/` and `monorepo/services/api/`: nested environments for the stacking beat.
  - `ripgreprc`: makes `rg` print matches without line numbers, as the script shows.
- `demo.py` is the [terminal-demo-video](https://github.com/justincastilla/flox-demo-video-skill) spec:
  every typed command matches the script, timed to the narration's cue words.

## Render

```bash
~/.claude/skills/terminal-demo-video/scripts/tdv draft .   # draft.mp4 + script.md (macOS draft voice)
~/.claude/skills/terminal-demo-video/scripts/tdv sync .    # final.mp4 from voice/s1.wav ... voice/s9.wav
```

Recordings run in a fresh `/tmp/tanja-N` copy of `sample/` with their own Flox config directory,
so `flox activate allow|deny` and `flox config --set` never change your real `~/.config/flox`.

## Where the screen differs from SCRIPT.md

Every typed command and every line of command output matches the script, except these, which come
from Flox itself or from the script:

- **Auto-activate prompt (0:05).** Flox prints `! Auto-activate the environment in '/private/tmp/tanja-N/my-project'? (y/N)`;
  after `y` it redraws the line as `> … Yes` and prints `✔ You are now using the environment 'my-project'`.
  The script shows `? … '/home/tanja/my-project'? (y/N) y`. `/home/tanja` can't be created on macOS
  (`/home` is system-managed), and the recording path shows as `/private/tmp/...`.
- **Climbing out of the monorepo (0:29).** The script ends `cd ..`, `cd ..` at `$`, but from
  `monorepo/services/api` two `cd ..` land in `monorepo/`, which is still inside the monorepo
  environment, so the real prompt is `flox [monorepo] $`. Either `cd ../..` then `cd ..`, or three
  `cd ..`, reaches `$`.

Presentation choices (real commands still run):

- After the on-camera y/N answer, Flox's "You are now using the environment" lines are silenced, as
  the script never shows them.
- In the allow/deny shot, auto-activation is paused off camera so the prompt stays `$` inside the
  project, and the commands' confirmations ("✔ Auto-activation allowed for 'my-project'.") are
  silenced, so the shot is just the two commands.
- Scene changes the script cuts past (leaving a directory, clearing the screen) happen off camera.
