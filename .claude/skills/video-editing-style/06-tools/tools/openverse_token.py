#!/usr/bin/env python3
"""Exchange a registered Openverse client for a 12 h bearer token (2026-11-27).
   OPENVERSE_CLIENT_ID and OPENVERSE_CLIENT_SECRET must be set in the environment; prints the token's lifetime, writes the token to ./openverse_token.txt (keep it out of git)."""
import os, sys, json, urllib.parse, urllib.request
body = urllib.parse.urlencode({"client_id": os.environ["OPENVERSE_CLIENT_ID"], "client_secret": os.environ["OPENVERSE_CLIENT_SECRET"], "grant_type": "client_credentials"}).encode()
req = urllib.request.Request("https://api.openverse.org/v1/auth_tokens/token/", data=body, headers={"User-Agent": "sfx-research-client/1.0"})
r = json.load(urllib.request.urlopen(req, timeout=40)); open("openverse_token.txt", "w").write(r["access_token"]); os.chmod("openverse_token.txt", 0o600)
print("token ok, expires_in", r.get("expires_in"), "s")
