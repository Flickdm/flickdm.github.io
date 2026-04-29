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
    # autocrlf = false # Required for EDK2 (committing as CRLF)
    autocrlf = true # for any other repo
    editor = code --wait
[pull]
    rebase = true
[init]
    defaultBranch = main
[fetch]
    prune = true
[diff]
    tool = vscode
[difftool "vscode"]
    cmd = code --wait --diff $LOCAL $REMOTE
[rebase]
    autoStash = true
[merge]
    conflictstyle = diff3
[alias]
    c = "commit --signoff"
    amend = "commit --amend --no-edit"
    nah = "git reset --hard && git clean -df"
    update = "pull --rebase origin main"
    uncommit = "reset --soft HEAD~1"
    last-touch = "log -1 --oneline --"
    tree = "log --graph --decorate --oneline --all"
    recent = "log -10 --pretty=format:'%h %ad | %s | %an' --date=short"
    st = "status -sb"

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

#### `git last-touch`

```
log -1 --oneline --
```

Retrieves the commit that last touched a given file.

#### `git tree`

```
log --graph --decorate --oneline --all
```

Shows a visual, one-line graph of your commit history.

#### `git recent`

```
log -10 --pretty=format:'%h %ad | %s | %an' --date=short
```

Shows the last 10 commits with their dates and authors.

#### `git st`

```
status -sb
```

A minimalist, short version of `git status`.


### Pro-Tip: Using `.gitattributes`

If you want to ensure that specific files (or all files) always use a certain line ending in the repository, regardless of individual user settings, you can use a `.gitattributes` file in your project root.

For example, to force all files to be committed with CRLF:
```text
* text=auto eol=crlf
```

This is often more reliable than relying on individual `git config` settings.
