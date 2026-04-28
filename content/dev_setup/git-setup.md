---
title: "Git Setup"
description: "Guide for setting up Git for development"
date: 2026-04-27
---

## Git Configuration


```ini
# ~/.gitconfig

[user]
    email = <my email>
    name = <my name>
[core]
    autocrlf = true
[pull]
    rebase = true
[init]
    defaultBranch = main
[core]
    editor = code --wait
[diff]
    tool = vscode
[difftool "vscode"]
    cmd = code --wait --diff $LOCAL $REMOTE
[rebase]
    autoStash = true
[merge]
    conflictstyle = diff3
[alias]
    c = commit --signoff
    amend = commit --amend --no-edit
    nah = amend reset --hard && git clean -df
    update = pull --rebase origin main
    uncommit = reset --soft HEAD~1
```


### Aliases

#### `git c`

```
commit --signoff
```

Creates a commit with a sign-off line at the bottom of the message.

#### `git amend`

```
commit --amend --no-edit
```

Updates the last commit without changing the message.

#### `git nah`

```
reset --hard && git clean -df
```

Discards all working tree changes and removes untracked files.

#### `git update`

```
pull --rebase origin main
```

Rebases your changes onto the latest `main` branch.

#### `git uncommit`

```
reset --soft HEAD~1
```

Unstages the last commit, keeping your changes in the working tree.
