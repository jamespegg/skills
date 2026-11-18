---
name: teardown
description: Guide a user-led walkthrough of a repository or subtree by voice or chat. Use when the user wants to explore a codebase step by step, dictate their own review notes, and produce a single review for another agent session to discuss.
license: Apache-2.0
metadata:
  author: jamespegg
  version: "2.1.0"
---

# Teardown

Guide the user through the repository at their pace and record their assessment. Use brief, factual observations to orient them, such as what a directory contains, where a file is used, or what a section appears to do. Give technical opinions or solutions only if the user asks. Leave repository files untouched apart from the review if the user chooses to store it there.

## Start or resume

- Use the repository, revision, and scope the user names. When the current repository is the obvious target, identify it and start at its root unless the user narrows the scope. Clarify only when several targets are plausible or the requested scope is unclear.
- Preview the immediate children and suggest a starting point using the repository's structure or entry points. Default to a recursive walkthrough, one meaningful unit at a time. A unit can be a directory, a file, or a section of a large file. Introduce one short path or section at a time and leave room for the user to speak.
- Create a single Markdown review at a stable, user-accessible path and share that path. Prefer a writable shared location outside the reviewed repository. Use the same file for checkpoints and the final handoff. Keep separate reviews for independent walkthroughs. If no durable writable location is available, tell the user and keep a copyable Markdown checkpoint in the conversation.
- Record the repository identifier, revision when available, whether local changes were present, and the agreed scope. If resuming, open the existing review, restore its traversal position and coverage, and check whether the source changed. Flag any revision or working-tree differences you can establish that affect prior notes or the remaining walkthrough. Preserve prior notes with their original source context.

## Navigate and capture

- Treat natural speech as the interface. “Next” advances through the current branch, “go deeper” opens the current item, “up” goes to its parent, and “back” returns to the previous location. Honor direct jumps, revisits, and requests to skip a file or branch. Remember where a detour left off so the user can pick up the original branch. Treat a jump outside scope as a detour unless the user expands the scope.
- Combine notes and navigation in one turn. For “this retry logic worries me, skip the rest,” first record the concern against the current section, then mark and leave the unreviewed remainder. Treat tentative mentions of other paths as comments unless the user is directing a jump. Clarify ambiguous speech only when it would materially change the note, its location, or the next stop.
- Record the user's observations, questions, preferences, and decisions under the relevant repository-relative paths. Add line or symbol anchors when known. Lightly clean up transcription while preserving intent, uncertainty, and emphasis. Distinguish questions from conclusions. Apply corrections to the affected note, and avoid duplicating notes on revisits. Keep any requested agent commentary explicitly attributed.
- Save updates after each meaningful turn, including when the user pauses or changes direction. Track the current location, the next likely stop, any detour return point, and enough coverage to resume without replaying the walk. Distinguish items reviewed by the user, partially reviewed, explicitly skipped, and still unvisited. Opening or listing an item only establishes that it was seen. Track skipped or unvisited branches compactly and record exceptions when the user revisits a descendant. A glance at a directory or file does not establish coverage of its children or sections.
- When a branch runs out, move to the next in-scope sibling or return up the tree. Flag unreadable content and any exclusions that affect coverage. Keep acknowledgments short. When the user pauses, share the saved location and where they can resume.

## Finish and hand off

- On “wrap up” or equivalent, finish from whatever scope and coverage the user reached. Re-read the saved notes and organize them into one self-contained review with the repository identity and source revision, scope and coverage, notes grouped by path, and any open questions the user raised. Preserve concrete details and source anchors when consolidating related comments.
- Make skipped branches, partial reviews, remaining work, and source changes that matter explicit. Include the current position and next likely stop if the walkthrough is incomplete. Summarize themes only when the user's notes support them, and attribute any requested agent observations.
- Save the consolidated review at the same path. Give the user the link so they can open the review in another session and discuss it with access to the repository context.
