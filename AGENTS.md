# Data Engineering Roadmap — Working Rules

These rules apply whenever an assistant works in this project.

## Session start

1. Read `LEARNING_PROGRESS.md` before proposing a lesson or exercise.
2. Briefly tell the learner:
   - the last completed roadmap item;
   - the current item;
   - the next recommended action.
3. Continue from the recorded current item unless the learner explicitly chooses another topic.
4. Never mark an item complete merely because it was opened or discussed.

## During a learning session

1. Teach with a realistic data-engineering business context.
2. For code topics, include a practical exercise, let the learner attempt it, then explain the solution.
3. Record important decisions, errors, corrections, and useful commands.
4. Keep roadmap item names identical to the names used in `index.html` whenever possible.

## Session end

1. Update `LEARNING_PROGRESS.md` after the learner confirms an item or exercise is complete.
2. Record:
   - date and session summary;
   - completed items;
   - current item and status;
   - exercises and files used;
   - important notes;
   - exact next step.
3. Show the learner a short visual recap of which roadmap checkbox(es) should now be checked.
4. Do not commit or publish `LEARNING_PROGRESS.md`; it is personal and ignored by Git.

## Browser limitation

The progress file is the source of truth for learning sessions. Reading it does not directly change the localStorage of the public Vercel page. If browser checkboxes differ, report the exact items the learner should check or uncheck rather than claiming they were changed.
