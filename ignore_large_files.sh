#!/bin/bash

# 50MB in bytes
MAXSIZE=$((50 * 1024 * 1024))

# Find all files in the current directory and its subdirectories
# that are larger than the specified size
# and append them to .gitignore

find . -type f -size +${MAXSIZE}c ! -path "./.git/*" -exec sh -c '
  for file do
    # Convert the full path to a relative path
    relative_path=$(realpath --relative-to=. "$file")
    # Append the relative path to .gitignore if not already present
    grep -qxF "$relative_path" .gitignore || echo "$relative_path" >> .gitignore
  done
' sh {} +
