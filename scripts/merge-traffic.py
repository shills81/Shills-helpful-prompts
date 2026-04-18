"""
Fetches GitHub traffic stats for this repo and merges them into
data/traffic-log.json on the traffic-data branch.

Called by .github/workflows/fetch-traffic.yml.
Usage: python scripts/merge-traffic.py <path-to-traffic-log.json>
"""

import json
import os
import sys
import urllib.request
from datetime import datetime, timezone


def gh(path, token):
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "traffic-logger-bot",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())


def main():
    log_path = sys.argv[1] if len(sys.argv) > 1 else "data/traffic-log.json"
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY", "shills81/Shills-helpful-prompts")

    if not token:
        print("ERROR: GITHUB_TOKEN or GH_TOKEN environment variable required")
        sys.exit(1)

    print(f"Fetching traffic for {repo}...")

    repo_data = gh(f"/repos/{repo}", token)
    views_data = gh(f"/repos/{repo}/traffic/views", token)
    clones_data = gh(f"/repos/{repo}/traffic/clones", token)
    referrers = gh(f"/repos/{repo}/traffic/referrers", token)
    paths = gh(f"/repos/{repo}/traffic/popular/paths", token)

    # Load existing log
    try:
        with open(log_path) as f:
            log = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        log = {"views": {}, "clones": {}, "repo_snapshots": [], "referrers": [], "popular_paths": []}

    # Ensure all keys exist (handle old format)
    log.setdefault("views", {})
    log.setdefault("clones", {})
    log.setdefault("repo_snapshots", [])
    log.setdefault("referrers", [])
    log.setdefault("popular_paths", [])

    # Merge daily views (keyed by date string — existing entries are never overwritten)
    for entry in views_data.get("views", []):
        d = entry["timestamp"][:10]
        if d not in log["views"]:
            log["views"][d] = {"count": entry["count"], "uniques": entry["uniques"]}

    # Merge daily clones
    for entry in clones_data.get("clones", []):
        d = entry["timestamp"][:10]
        if d not in log["clones"]:
            log["clones"][d] = {"count": entry["count"], "uniques": entry["uniques"]}

    # Replace referrers and popular paths with latest snapshot (they're 14-day aggregates)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    log["referrers"] = [
        {"referrer": r.get("referrer", ""), "count": r.get("count", 0), "uniques": r.get("uniques", 0)}
        for r in referrers
    ]
    log["popular_paths"] = [
        {"path": p.get("path", ""), "title": p.get("title", ""), "count": p.get("count", 0), "uniques": p.get("uniques", 0)}
        for p in paths
    ]

    # Append daily repo snapshot (stars, forks, watchers)
    snapshots_by_date = {s["date"]: s for s in log["repo_snapshots"]}
    snapshots_by_date[today] = {
        "date": today,
        "stars": repo_data.get("stargazers_count", 0),
        "forks": repo_data.get("forks_count", 0),
        "watchers": repo_data.get("subscribers_count", 0),
    }
    log["repo_snapshots"] = sorted(snapshots_by_date.values(), key=lambda x: x["date"])

    os.makedirs(os.path.dirname(log_path) or ".", exist_ok=True)
    with open(log_path, "w") as f:
        json.dump(log, f, indent=2)

    total_views = sum(v["count"] for v in log["views"].values())
    total_uniques = sum(v["uniques"] for v in log["views"].values())
    print(f"Done. {len(log['views'])} days tracked. Total views: {total_views}, unique visitors: {total_uniques}")
    print(f"Top path: {log['popular_paths'][0]['path'] if log['popular_paths'] else 'none'}")


if __name__ == "__main__":
    main()
