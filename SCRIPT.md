# Narration script

Record one file per scene and save them in `voice/` next to demo.py, named `s1.wav`, `s2.wav`, ...
(any format ffmpeg reads). Leading/trailing silence is trimmed automatically.
Paraphrase freely, but say each **cue**: typing starts on those words. Pausing between
sentences is fine; the video waits for you.

## s1.wav: s1_hook (draft voice 4.2s)

What if activating your dev environment was as simple as changing directories?

Cues: **changing directories**

## s2.wav: s2_auto (draft voice 7.5s)

With Flox auto-activation, it is. Say yes once, and whenever you come back, your environment activates automatically.

Cues: **say yes**

## s3.wav: s3_there (draft voice 3.3s)

Your packages, variables, and hooks are already there.

Cues: **your packages**, **variables**, **hooks**

## s4.wav: s4_services (draft voice 12.7s)

And it isn't just tools and variables. If your project declares services, you can have Flox start them with the environment. Nothing running. Your dev server is already listening when you cd in. No separate start script.

Cues: **isn't just**, **the environment**, **dev server**, **listening**

## s5.wav: s5_monorepo (draft voice 11.4s)

And this works the way you'd hope in a monorepo. Go deeper and environments stack. The inner one layers on top of the outer one, you get both. Come back out and they unwind, one layer at a time.

Cues: **monorepo**, **go deeper**, **come back out**, **one layer**

## s6.wav: s6_run (draft voice 5.8s)

Need something that isn't in the environment, or even installed on your machine? Just run it with Flox.

Cues: **even installed**, **just run it**

## s7.wav: s7_leave (draft voice 9.6s)

And when you leave, Flox deactivates the environment and shuts the server down with it. No stray process holding port 3000 because you forgot about it three days ago.

Cues: **when you leave**

## s8.wav: s8_remember (draft voice 11.5s)

Now, you saw Flox ask before activating that first environment. You don't have to answer that question every time. Allow it or deny it, and Flox remembers that directory. No more prompt.

Cues: **allow it**, **deny it**

## s9.wav: s9_config (draft voice 12.6s)

Or change how Flox behaves everywhere. Allowlist means Flox only activates projects you've already said yes to, and stops asking about new ones. Disabled turns the whole thing off. Your machine, your rules.

Cues: **behaves everywhere**
