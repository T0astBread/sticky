## What is this?

Two tools (`sticky` and `diary`) for daily note-taking and time
tracking.

## How do I use this?

Run `sticky` to launch an editor for your sticky notes. The file
(`sticky.md`) is checked right into your copy of this Git repo to
keep things simple.

The `diary` script is for daily activity- and time tracking and
functions similarly to the `sticky` script but with a more "defined"
structure: One top-level heading per day which it will insert
automatically when it is first started each day.

Additionally, you can track time ranges (for example when you worked)
in the heading line and `diary` will automatically calculate the
total time for that day. Headings with time ranges should conform to
the following format:

```markdown
# YYYY-mm-dd: (HH:MM - HH:MM, HH:MM - HH:MM)
```

Where the amount of `HH:MM - HH:MM` ranges is variable. The line can
end with an open-ended time range:

```markdown
# YYYY-mm-dd: (HH:MM - HH:MM, HH:MM - HH:MM, HH:MM)
```

In which case the current time will be used as the end time in
calculation.
