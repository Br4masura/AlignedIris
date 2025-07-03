#!/bin/bash

echo "🔧 Refactoring for Hugging Face deployment..."

# Step 1: Create new folders
mkdir -p reflections
mkdir -p iris_assets/audio
mkdir -p iris_assets/visuals
mkdir -p iris_assets/prompts
mkdir -p training

# Step 2: Move key files into place
mv aligned_iris_mvp/app3.py app.py
mv aligned_iris_mvp/reflections.py reflections/reflections.py
mv media/level1/audio/meditations.mp3 iris_assets/audio/
mv media/level1/visuals/stars1.jpg iris_assets/visuals/
mv iris_training_set1.json1 training/iris_training_set1.json1

echo "✅ Files moved to Hugging Face–ready structure."

# Optional: Suggest Git commands
echo ""
echo "📦 Ready to push:"
echo "   git add ."
echo "   git commit -m 'Restructure for Hugging Face Space deployment'"
echo "   git push origin main"