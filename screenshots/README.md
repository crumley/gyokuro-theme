# Screenshot Generation Guide

This directory contains sample code files for generating theme screenshots.

## 📸 Taking Screenshots

### Method 1: Manual (Recommended for Quality)

1. **Open VS Code** with the Gyokuro theme active
2. **Open sample files** from the `samples/` directory
3. **Adjust window size** to ~1200-1600px wide for good visibility
4. **Hide unnecessary UI elements**:
   - Hide minimap: `View > Show Minimap` (toggle off)
   - Hide activity bar (optional): `View > Appearance > Activity Bar`
   - Adjust zoom for clarity: `Cmd/Ctrl + =` or `-`

5. **Take screenshots** using:
   - **macOS**: `Cmd + Shift + 4` (then space to capture window)
   - **Windows**: `Windows + Shift + S` (select area)
   - **Linux**: Use built-in screenshot tool or Flameshot

6. **Save screenshots** to the `../images/` directory with naming:
   - `theme-desert.png`
   - `theme-desert-og.png`
   - `theme-dark.png`
   - `theme-light.png`
   - `accent-cyan-enhanced.png`
   - `accent-lime-enhanced.png`
   - etc.

### Method 2: VS Code Command (Quick & Dirty)

Use the built-in screenshot command:
1. Open Command Palette (`Cmd/Ctrl + Shift + P`)
2. Type: `Developer: Screenshot Editor Contents to Clipboard`
3. Paste into image editor and save

### Method 3: Browser DevTools (For Documentation Sites)

If you have a theme preview site:
1. Open in Chrome/Edge
2. F12 to open DevTools
3. `Cmd/Ctrl + Shift + P` → "Capture screenshot"
4. Choose full size or node screenshot

## 📝 Sample Files

The `samples/` directory contains:
- `sample.js` - JavaScript/React code
- `sample.py` - Python with various syntax features
- `sample.html` - HTML with CSS and JavaScript
- `sample.json` - JSON configuration example

These files are designed to showcase:
- Syntax highlighting
- Comments
- Strings and template literals
- Keywords and operators
- Functions and classes
- Regular expressions
- JSX/HTML tags
- Color values

## 🎨 Screenshot Checklist

For each theme variant, capture:
- [ ] Full editor view with sample code
- [ ] Show some UI elements (status bar, title bar with accent color)
- [ ] Multiple syntax elements visible
- [ ] Consistent window size across all screenshots
- [ ] Clean, focused composition

### Accent Screenshots

For accent showcases, consider capturing:
- Side-by-side comparisons of 2-3 accents
- Focus on status bar and activity bar differences
- Enhanced vs standard comparison

## 📐 Recommended Dimensions

- **Width**: 1200-1600px
- **Height**: 800-1000px
- **Format**: PNG (better quality for UI screenshots)
- **Compression**: Light compression to keep file size reasonable (<500KB per image)

## 🔧 Tools for Screenshot Editing

If you need to annotate or crop screenshots:
- **Figma** (free, web-based)
- **Preview** (macOS built-in)
- **Paint.NET** (Windows, free)
- **GIMP** (Cross-platform, free)
- **Kap** (macOS, for GIF recordings)

## 💡 Pro Tips

1. **Use a consistent code sample** across all theme screenshots for easy comparison
2. **Disable ligatures temporarily** if they cause confusion: `"editor.fontLigatures": false`
3. **Use a standard font** like Fira Code, JetBrains Mono, or Cascadia Code
4. **Capture during the day** with good lighting if photographing physical screens
5. **Consider creating a GIF** showing accent switching for the README

## 🎬 Creating Comparison GIFs

For animated comparisons:
1. Install [Kap](https://getkap.co/) (macOS) or [ScreenToGif](https://www.screentogif.com/) (Windows)
2. Record switching between accents or themes
3. Keep duration short (3-5 seconds)
4. Export as optimized GIF (<2MB)
5. Save to `../images/theme-demo.gif`

