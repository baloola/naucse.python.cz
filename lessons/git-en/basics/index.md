Unfortunately, you can only see different versions of a *single file*.
called *version control system* (VCS).
Real programs are rarely created by a single person.
Two heads are better than one, so it's better to work on a project in a team.

Each team member needs to be able to share their progress with others.
Git can be used exactly for that: you can set up a *shared repository* online that your team members will synchronize with.

[here]({{ lesson_url('git-en/install') }}).
*“Initial commit”* means that there is no commit stored yet.
## First commit
We need to make Git track each new file explicitly.
[master (root-commit) 1a009f4] First commit
This is referred to as a *commit message*. For now, a simple `First commit` will do.
    First commit
## Second commit
Finally, use `git commit` to create your second commit,
These two diagrams below visualize what each command demonstrated thus far does exactly,
and how the changes move from “not staged” to “commited” and back in case of need.

Diagram showing the process of viewing and committing changes:
    img=static('diagram.png'),
    alt="Diagram showing the process of viewing and committing changes"
Diagram showing the process of committing and resetting changes:

{{ figure(
    img=static('diagram2.png'),
    alt="Diagram showing the process of committing and resetting changes"
) }}


Now that we have created our first few commits in the repository,
    First commit