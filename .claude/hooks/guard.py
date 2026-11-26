#!/usr/bin/env python3
# Run manually before committing to detect common secret files in the staged set.
import subprocess, sys
bad = (".env", ".env.", ".pem", ".key", "id_rsa", "credentials", "secrets/")
r = subprocess.run(["git", "diff", "--cached", "--name-only"], capture_output=True, text=True)
if r.returncode:
    sys.exit(r.returncode)
hits = [p for p in r.stdout.splitlines() if any(x in p.lower() for x in bad)]
if hits:
    print("Potential secret files staged:\n" + "\n".join(hits), file=sys.stderr)
    sys.exit(1)
