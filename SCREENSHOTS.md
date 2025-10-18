# 📸 Screenshot Generation Summary

This document explains how to create professional screenshots for your Gyokuro Theme.

## What's Been Set Up

✅ **Directory Structure**
```
gyokuro-theme/
├── images/              # ← Put final screenshots here
│   └── .gitkeep
└── screenshots/         # ← Development assets
    ├── README.md        # Detailed screenshot guide
    └── samples/         # Sample code for demos
        ├── sample.js
        ├── sample.py
        ├── sample.html
        └── sample.json
```

✅ **Sample Code Files** - Showcase syntax highlighting with:
- JavaScript/React (comments, JSX, async/await, classes)
- Python (type hints, decorators, async, dataclasses)
- HTML/CSS/JS (styling, grid layout, event handlers)
- JSON (configuration examples)

✅ **Documentation**
- Main [README.md](./README.md) - Usage instructions with screenshot placeholders
- [screenshots/README.md](./screenshots/README.md) - Detailed screenshot guide
- [QUICKSTART.md](./QUICKSTART.md) - Quick start guide for users

## How to Generate Screenshots

### Automated Approach (Not Available)

The `vscode-theme-screenshot` npm package mentioned in many guides **doesn't actually exist** in the npm registry. Most VS Code theme developers use manual screenshots instead.

### Manual Approach (Recommended) ⭐

**See the detailed guide:** [screenshots/README.md](./screenshots/README.md)

**Quick Steps:**

1. **Open VS Code** with Gyokuro theme active
2. **Open a sample file** from `screenshots/samples/`
3. **Adjust window** to ~1200-1600px wide
4. **Take screenshot**:
   - macOS: `Cmd + Shift + 4` → Space → Click window
   - Windows: `Win + Shift + S`
   - Linux: Use Flameshot or built-in tool
5. **Save to** `/images/` with proper naming:
   - `theme-desert.png`
   - `theme-desert-og.png`
   - `theme-dark.png`
   - `theme-light.png`
   - `accent-cyan-enhanced.png`
   - etc.

### Alternative Tools

1. **VS Code Built-in**:
   - Command Palette → "Developer: Screenshot Editor Contents to Clipboard"
   - Quick but doesn't capture full UI

2. **Browser-based** (if you have a preview site):
   - Chrome DevTools → Cmd/Ctrl+Shift+P → "Capture screenshot"
   - Good for consistent sizing

3. **Screen Recording → GIF**:
   - [Kap](https://getkap.co/) (macOS)
   - [ScreenToGif](https://www.screentogif.com/) (Windows)
   - Great for showing accent switching

## Screenshot Checklist

For professional results:

- [ ] Consistent window size across all screenshots (1200-1600px wide)
- [ ] Same font (Fira Code, JetBrains Mono, or Cascadia Code)
- [ ] Same zoom level
- [ ] Hide minimap and activity bar for cleaner look
- [ ] Show status bar to showcase accent colors
- [ ] Use sample files from `/screenshots/samples/`
- [ ] PNG format, <500KB per file
- [ ] Descriptive filenames

## What to Screenshot

### Base Themes (4 screenshots needed)
1. `theme-desert.png` - Gyokuro Desert
2. `theme-desert-og.png` - Gyokuro Desert OG
3. `theme-dark.png` - Gyokuro Dark
4. `theme-light.png` - Gyokuro Light

### Accent Examples (optional, 2-3 recommended)
- `accent-showcase.png` - 3-4 different accents side-by-side
- `accent-lime-enhanced.png` - Single accent example
- `accent-comparison.png` - Standard vs Enhanced comparison

## After Creating Screenshots

1. Add image files to `/images/` directory
2. Edit [README.md](./README.md) and uncomment the screenshot section (around line 110)
3. Verify images display correctly
4. Commit and push to repository
5. Screenshots will automatically show on GitHub and VS Code marketplace

## README Integration

The main README already has screenshot placeholders:

```markdown
### Gyokuro Desert
![Gyokuro Desert Theme](./images/theme-desert.png)

### Gyokuro Desert OG
![Gyokuro Desert OG Theme](./images/theme-desert-og.png)
```

Once you add the actual PNG files, just uncomment these lines!

## Tips for Great Screenshots

1. **Consistent samples** - Use the same code file for all theme variants
2. **Show variety** - Capture different languages to show versatility
3. **Highlight accents** - Make sure colored UI elements are visible
4. **Clean workspace** - Close unnecessary panels
5. **Good lighting** - If photographing screens (not recommended)
6. **Optimize size** - Use PNG compression tools to keep files under 500KB

## Questions?

- See [screenshots/README.md](./screenshots/README.md) for detailed instructions
- Check [VS Code Theme Publishing Guide](https://code.visualstudio.com/api/extension-guides/color-theme)
- Look at other popular themes for inspiration

---

**Ready to take screenshots?** Open one of the sample files and start capturing! 📸

