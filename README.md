# Login Dashboard — Git Practice Project

A small Python FastAPI login/dashboard app made for practicing Git commands.

## 1. Requirements
- Python 3.10+
- Git
- VS Code (recommended)

## 2. Run the starter project
Open this folder in VS Code, then in the terminal:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000

**Demo credentials**
- Username: `admin`
- Password: `admin123`

This is a learning demo. Authentication is intentionally simple and uses an in-memory demo account; do not use it in production.

## 3. Start Git tracking
Run these commands from the project root:

```bash
git init
git status
git add .
git commit -m "Initial login dashboard"
git branch
```

## 4. Practice tasks

Apply one patch at a time. Each patch contains a realistic code modification.
On Windows, Git Bash is convenient for applying patches:

```bash
git apply git-practice/patches/01-add-login-validation.patch
git diff
git status
git add .
git commit -m "Add login validation"
```

Then repeat for patches 02–04. Read each patch before applying it.

### Git command checklist
1. `git status` — inspect changed files.
2. `git diff` — inspect unstaged code changes.
3. `git add app/main.py` — stage one file.
4. `git diff --staged` — inspect staged changes.
5. `git commit -m "..."` — save a snapshot.
6. `git log --oneline` — inspect history.
7. `git switch -c feature/profile-card` — create a branch.
8. `git switch main` — return to main (your default branch may be `master`).
9. `git merge feature/profile-card` — merge a branch.
10. `git stash`, `git stash list`, `git stash pop` — temporarily put changes aside.
11. `git restore <file>` — discard unstaged changes (be careful).
12. `git revert <commit-id>` — create a new commit that reverses an earlier commit.

### Suggested practice sequence
- Patch 01: add validation and better error messages.
- Patch 02: add a profile section to the dashboard.
- Patch 03: add a logout button and route.
- Patch 04: add a dashboard summary card.

### Branch and merge exercise
After applying patches 01 and 02 and committing them:
```bash
git switch -c feature/dashboard-summary
```
Apply patch 04, commit it, then:
```bash
git switch main
git merge feature/dashboard-summary
```
If your initial branch is called `master`, replace `main` with `master`.

### Stash exercise
Edit the welcome heading in `app/templates/dashboard.html`, but do not commit.
```bash
git stash
git status
git stash pop
```

### Merge-conflict exercise
Create two branches from the same commit. On each branch, change the dashboard heading to a different value and commit. Merge one branch into the other. Resolve the conflict in the file, then:
```bash
git add app/templates/dashboard.html
git commit
```

## 5. Patch files
Patch files are in `git-practice/patches/`. Apply them from the project root, in numeric order. If you want to restart, unzip a fresh copy of this project.
