# Week 5 — Python environment for notebooks

This folder uses a **virtual environment** at `week5/.venv` so `pip install` works (Homebrew’s system Python blocks installs with PEP 668).

The repo root also has **`.venv` → `week5/.venv`** (symlink) so Cursor / VS Code can discover the same environment as a normal workspace `.venv`.

## One-time setup (or if `.venv` is missing)

From the repo root:

```bash
python3 -m venv week5/.venv
ln -sf week5/.venv .venv
week5/.venv/bin/python -m pip install -U pip
week5/.venv/bin/python -m pip install -r week5/requirements.txt
week5/.venv/bin/python -m ipykernel install --user --name hcde530-week5 --display-name "Python (hcde530 week5)"
```

## In Cursor

1. **Python: Select Interpreter** → choose **`.venv/bin/python`** at the repo root, or **`week5/.venv/bin/python`** (same env).  
   Workspace **`.vscode/settings.json`** defaults the interpreter to **`.venv/bin/python`**.
2. Open a `.ipynb` → **Select Kernel**:
   - Easiest: under **Python Environments**, pick **`.venv` (Python 3.14.x)** at the **repo root**, or **`Enter Interpreter Path…`** and paste  
     `<repo>/hcde530/.venv/bin/python` (your full clone path).
   - Optional: **Select Another Kernel…** → **Jupyter Kernels** → **Python (hcde530 week5)** (only if that list appears; it reads from `jupyter kernelspec list`).
3. Run cells with **Shift+Enter**.

If the kernel list is empty or stuck loading, run **Developer: Reload Window**, then try **Enter Interpreter Path…** with `.venv/bin/python` (that path always works when `ipykernel` is installed in that venv).

## Reinstall packages

Always use the venv’s pip:

```bash
week5/.venv/bin/python -m pip install <package>
```
