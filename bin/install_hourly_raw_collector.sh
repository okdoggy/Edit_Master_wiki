#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
LABEL="com.okdoggy.edit-master-wiki.raw-hourly"
SRC="$ROOT/launchd/$LABEL.plist"
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"
mkdir -p "$HOME/Library/LaunchAgents" "$ROOT/.omx/logs" "$ROOT/raw/hourly"
cp "$SRC" "$DEST"

if launchctl print "gui/$(id -u)/$LABEL" >/dev/null 2>&1; then
  launchctl bootout "gui/$(id -u)" "$DEST" >/dev/null 2>&1 || true
fi
launchctl bootstrap "gui/$(id -u)" "$DEST"
launchctl enable "gui/$(id -u)/$LABEL" || true
launchctl kickstart -k "gui/$(id -u)/$LABEL" || true

echo "Installed $LABEL"
echo "Plist: $DEST"
echo "Logs: $ROOT/.omx/logs/hourly_raw_collector.out.log"
