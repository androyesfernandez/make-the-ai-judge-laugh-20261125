# Make the AI Judge Laugh — office joke entry
#
# This program writes a single one-line joke about office life to
# /output/entry.txt. The joke is fixed: it was picked because it lands
# a true, relatable observation (the performance review that praises
# you and then explains why the praise is not worth a raise) and then
# twists it with a punchline about money already spent in the
# employee's head. One breath, no setup wasted, nothing to explain.
# The line is deliberately kept fixed: the program is a delivery
# vehicle for one tested joke, not a generator, so every run writes
# exactly the same text.

import os

JOKE = (
    "My manager opened my review by saying I was doing great, then spent "
    "forty minutes explaining why great wasn't good enough for the raise "
    "I had already spent in my head."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
