# Gyokuro Theme Quick Start Guide

Get up and running with Gyokuro Theme in 5 minutes! 🚀

## Step 1: Install the Theme

**From VS Code Extensions:**
1. Press `Cmd/Ctrl + Shift + X`
2. Search "Gyokuro Theme"
3. Click Install

**From VSIX file:**
1. Download `.vsix` from Releases
2. Extensions → `...` menu → Install from VSIX

## Step 2: Activate a Base Theme

1. Press `Cmd/Ctrl + Shift + P`
2. Type "Color Theme"
3. Select one:
   - **Gyokuro Desert** (recommended) - Warm desert tones
   - **Gyokuro Desert OG** - Classic desert variant
   - **Gyokuro Dark** - Pure dark theme
   - **Gyokuro Light** - Light theme variant

## Step 3: Add a Workspace Accent (Optional)

Make each project window instantly recognizable!

### Quick Method

1. Open your project
2. Create `.vscode/settings.json` in project root
3. Browse `/accents` folder in this repo
4. Pick an accent (e.g., `lime-enhanced.jsonc`)
5. Copy the entire content
6. Paste into your settings file

**Example:** For a neon lime accent:

```json
{
  "workbench.colorCustomizations": {
    "statusBar.background": "#39FF14",
    "statusBar.foreground": "#001F00",
    "activityBar.background": "#2D8B00",
    "activityBar.foreground": "#E0FFB3",
    "titleBar.activeBackground": "#39FF14",
    "titleBar.activeForeground": "#001F00",
    "panelTitle.activeBorder": "#7FFF00",
    "focusBorder": "#7FFF00"
  }
}
```

## Step 4: Choose Your Accent

**12 Colors Available:**

**Neon Collection** (Street art vibes):
- `lime` 🟢 - Radioactive green
- `orange` 🟠 - Electric orange
- `purple` 🟣 - Electric violet
- `blue` 🔵 - Cobalt blue
- `magenta` 🟣 - Hot magenta
- `yellow` 🟡 - Acid yellow
- `red` 🔴 - Blood crimson
- `coral` 🟠 - Neon coral

**Original**:
- `cyan` 🔵 - Aqua teal
- `pink` 💗 - Hot pink

**High Contrast**:
- `white` ⚪ - Pure white
- `black` ⚫ - Deep black

**Two Variations:**
- `-standard.jsonc` - Core UI only (cleaner)
- `-enhanced.jsonc` - Maximum customization (tabs, gutters, selections)

## Step 5: Multi-Project Setup

Use different accents for different types of projects:

```
📁 my-frontend/      → lime-enhanced.jsonc
📁 my-backend/       → blue-enhanced.jsonc
📁 my-admin/         → red-enhanced.jsonc
📁 my-docs/          → cyan-enhanced.jsonc
📁 my-experiments/   → magenta-enhanced.jsonc
```

Now you can instantly tell which window is which! 🎨

## Tips

✨ **Mix and Match**: Combine base themes with any accent
🎯 **Per-Project**: Each project gets its own `.vscode/settings.json`
🔄 **Easy Switch**: Change accents anytime by editing the settings file
🗑️ **Remove**: Delete the `workbench.colorCustomizations` section to reset

## Next Steps

- Read the full [README](./README.md)
- Browse all [Accent Options](./accents/README.md)
- Check out [Sample Code](./screenshots/samples/) for theme previews

---

**Need Help?**
- [GitHub Issues](https://github.com/crumley/gyokuro-theme/issues)
- [VS Code Theme Docs](https://code.visualstudio.com/api/extension-guides/color-theme)

Happy coding! 🍵

