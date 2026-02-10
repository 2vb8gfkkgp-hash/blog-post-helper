# Blog Post Helper

This repository provides a helper app for writing and researching blog posts. The instructions below include setup and troubleshooting tips, including how to resolve the Windows error where `git` is not recognized.

> Note: `README.md` is a text document. Don’t run it in PowerShell. Open it in a text editor or on GitHub.

## Run the app locally

You will run two servers in separate terminals: the FastAPI backend and the Next.js frontend.

### 1) Backend (FastAPI)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API will be available at http://127.0.0.1:8000/health.

### 2) Frontend (Next.js)

```bash
cd frontend
npm install
npm run dev
```

The web UI will be available at http://localhost:3000.

## Quick Start (Windows PowerShell)

1. **Install Git** (required to clone the repo):
   - Download and install **Git for Windows** from https://git-scm.com/download/win.
   - During installation, keep the default option **"Git from the command line and also from 3rd-party software"** so `git` is available in PowerShell.
   - After installation, **close and reopen PowerShell**.
   - Verify:
     ```powershell
     git --version
     ```

2. **Clone the repo** (use the base repo URL, not a `/tree/...` page):
   ```powershell
   cd C:\Users\<your-user>\Downloads
   git clone https://github.com/2vb8gfkkgp-hash/blog-post-helper.git
   cd blog-post-helper
   ```

3. **If you need a specific branch** (example: `codex/build-full-stack-app-newsroomkit`):
   ```powershell
   git fetch --all
   git checkout codex/build-full-stack-app-newsroomkit
   ```

4. **If Git is already installed but `git` is not recognized**:
   - Reopen PowerShell (PATH updates require a new shell).
   - If that fails, ensure `C:\Program Files\Git\cmd` is in your PATH:
     ```powershell
     $env:Path
     ```
   - You can temporarily add it for the current session:
     ```powershell
     $env:Path += ";C:\Program Files\Git\cmd"
     git --version
     ```

## If you see “repository not found”

That error usually means the **clone URL is wrong**. Make sure you are **not** cloning a URL that contains `/tree/...`.

✅ Correct (clone this):
```
https://github.com/2vb8gfkkgp-hash/blog-post-helper.git
```

❌ Incorrect (do NOT clone this):
```
https://github.com/2vb8gfkkgp-hash/blog-post-helper/tree/codex/build-full-stack-app-newsroomkit/
```

If you need a branch, clone the base repo first, then run `git checkout <branch>` as shown above.

## Alternative: Download ZIP (No Git Required)

If you can’t install Git, use the ZIP download:
1. Open https://github.com/2vb8gfkkgp-hash/blog-post-helper
2. Click **Code → Download ZIP**
3. Extract the ZIP, then open the folder in your terminal.

## If the repo looks empty

If you only see `.gitkeep` (and no `backend`, `frontend`, or other files), it means the repository doesn’t contain the application code yet. You can confirm with:
```powershell
dir
```

**What to do next:**
- Make sure you cloned the correct repo and branch.
- If you expected app files, share the output of `dir` so the project structure can be verified and the next steps provided.
