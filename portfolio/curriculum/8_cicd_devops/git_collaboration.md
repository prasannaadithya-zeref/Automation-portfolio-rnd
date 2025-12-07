# 🐙 Git for Teams: Beyond "Push & Pull"
*You know `git push`, but do you know how to work in a team of 10?*

## 1. The Golden Rule: Never Commit to Main
Always use a "Feature Branch".
```bash
git checkout -b feature/login-page
# Make changes...
git add .
git commit -m "Added login page"
```

## 2. Merging vs Rebasing (The Hot Topic)
*   **Merge**: Combines history. Safe. Creates a "Merge Commit".
    *   `git merge feature/login-page`
*   **Rebase**: Rewrites history. Clean linear line. Dangerous if shared.
    *   `git rebase main`

## 3. Handling Conflicts ⚔️
When two people edit the same line, Git panics.
1.  Open the file. Look for `<<<<<<< HEAD`.
2.  Delete the code you don't want.
3.  Delete the marker lines.
4.  `git add .` and `git commit`.

## 4. Stashing (The "Save Game" Button)
You are working on a bug, but need to switch branches? Don't commit broken code.
```bash
git stash        # Saves current changes to a clipboard
git checkout other-branch
# ... do stuff ...
git checkout original-branch
git stash pop    # Brings your changes back
```

## 5. Cherry Picking 🍒
You want *just one specific commit* from another branch.
```bash
git cherry-pick <commit-hash>
```
