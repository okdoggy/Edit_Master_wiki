#!/usr/bin/env bash
set -euo pipefail
LABEL="com.okdoggy.edit-master-wiki.raw-hourly"
DEST="$HOME/Library/LaunchAgents/$LABEL.plist"
if launchctl print "gui/$(id -u)/$LABEL" >/dev/null 2>&1; then
  launchctl bootout "gui/$(id -u)" "$DEST" >/dev/null 2>&1 || true
fi
rm -f "$DEST"
echo "Uninstalled $LABEL"
