
echo "🌌 Migrating media files to Git LFS..."

# Step 1: Make sure LFS is tracking these types
git lfs track "*.mp3" "*.wav" "*.jpg" "*.jpeg" "*.png"

# Step 2: Find and migrate media files
find . -type f \( -iname "*.mp3" -o -iname "*.wav" -o -iname "*.jpg" -o -iname "*.png" -o -iname "*.jpeg" \) | while read file; do
    echo "🎵 Processing: $file"
    git rm --cached "$file"
    git add "$file"
done

# Step 3: Add .gitattributes
git add .gitattributes

# Step 4: Commit and push
git commit -m "🌠 Move media files to Git LFS"
git push space main