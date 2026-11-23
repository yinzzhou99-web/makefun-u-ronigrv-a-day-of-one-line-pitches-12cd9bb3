"""A Day of One-Line Pitches.

Writes one sentence convincing a friend who has never coded to let an AI
agent build their first app idea on make.fun to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output). Standard library only.
The line is judged on making the case in one read, persuasion with a
concrete low-risk reason to say yes now, clarity in plain words, truth
with no overpromising, and warmth.

Chosen pitch: one sentence, a concrete first step (describe the idea),
the builder named (an AI agent), and the risk removed — your $5 only goes
to the best one. Plain words, no jargon, sounds like a friend talking.
"""

import os

LINE = "Give me one sentence about your app idea and I\u2019ll turn it into a make.fun bounty \u2014 an AI agent builds the first version, and your $5 only goes to the best one."


def main() -> None:
    text = LINE.strip()
    if not text or len(text) > 240:
        raise SystemExit("entry line must be 1 to 240 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    tmp = target + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(tmp, 0o644)  # readable by the grader even under a strict umask
    os.replace(tmp, target)


if __name__ == "__main__":
    main()
