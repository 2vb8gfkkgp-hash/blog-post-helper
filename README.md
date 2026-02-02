# Blog Post Helper

This repository provides a helper app for writing and researching blog posts. The instructions below include setup and troubleshooting tips, including how to resolve the Windows error where `git` is not recognized.

> Note: `README.md` is a text document. Don’t run it in PowerShell. Open it in a text editor or on GitHub.

## Quick Start (Windows PowerShell)

1. **Install Git** (required to clone the repo):
   - Download and install **Git for Windows** from https://git-scm.com/download/win.
   - During installation, keep the default option **"Git from the command line and also from 3rd-party software"** so `git` is available in PowerShell.
   - After installation, **close and reopen PowerShell**.
   - Verify:
     ```powershell
     git --version
     ```

2. **Clone the repo**:
   ```powershell
   cd C:\Users\<your-user>\Downloads
   git clone https://github.com/2vb8gfkkgp-hash/blog-post-helper.git
   cd blog-post-helper
   ```

3. **If Git is already installed but `git` is not recognized**:
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

## Next Steps

Once the repo includes the application files, follow the instructions in the project docs for installing dependencies and running the app.
