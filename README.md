# Gyokuro Theme Collection

A collection of VS Code themes by [cupofcrumly.com](https://cupofcrumly.com) featuring soothing color palettes and 24 vibrant workspace accent variations.

## ✨ Features

- **4 Base Themes** - Desert, Desert OG, Dark, and Light variants
- **24 Workspace Accents** - 12 colors × 2 variations (standard & enhanced)
- **Graffiti/Street Art Vibes** - Neon colors inspired by urban art
- **High Contrast Options** - Pure white and black accents available
- **Maximum Window Differentiation** - Instantly recognize which project you're in

## 🎨 Themes

- **Gyokuro Desert** - Desert theme with green tea inspired accents
- **Gyokuro Desert OG** - Classic desert theme with warm orange highlights  
- **Gyokuro Dark** - Dark theme variant
- **Gyokuro Light** - Light theme variant

## 🚀 Installation

### From VS Code Marketplace (Recommended)

1. Open **Extensions** in VS Code (`Cmd/Ctrl + Shift + X`)
2. Search for **"Gyokuro Theme"**
3. Click **Install**
4. Click **Reload** to activate

### Manual Installation from VSIX

1. Download the latest `.vsix` file from [Releases](https://github.com/crumley/gyokuro-theme/releases)
2. Open VS Code
3. Go to **Extensions** (`Cmd/Ctrl + Shift + X`)
4. Click the `...` menu at the top
5. Select **Install from VSIX...**
6. Choose the downloaded `.vsix` file

## 🎯 Getting Started

### Activate a Base Theme

1. Open **Command Palette** (`Cmd/Ctrl + Shift + P`)
2. Type **"Preferences: Color Theme"**
3. Select your preferred Gyokuro theme:
   - `Gyokuro Desert`
   - `Gyokuro Desert OG`
   - `Gyokuro Dark`
   - `Gyokuro Light`

### Apply Workspace Accents

Workspace accents let you customize the UI colors (status bar, activity bar, etc.) to give each project window a unique personality.

#### Quick Start

1. Open your project in VS Code
2. Create or open `.vscode/settings.json` in your project root
3. Choose an accent from the `/accents` folder (e.g., `cyan-enhanced.jsonc`)
4. Copy its entire `workbench.colorCustomizations` object
5. Paste into your workspace settings:

```json
{
  "workbench.colorCustomizations": {
    // Paste accent colors here
    "statusBar.background": "#39FF14",
    "activityBar.background": "#2D8B00",
    // ... etc
  }
}
```

#### Available Accents (12 Colors)

**Original Collection:**
- 🔵 **Cyan** - Aqua teal vibes
- 💗 **Pink** - Hot pink energy

**Neon/Street Art Collection:**
- 🟠 **Orange** - Electric neon orange
- 🟢 **Lime** - Radioactive neon green
- 🟣 **Purple** - Electric violet
- 🔵 **Blue** - Cobalt electric blue
- 🟣 **Magenta** - Pure hot magenta
- 🟡 **Yellow** - Acid yellow highlighter
- 🔴 **Red** - Blood crimson
- 🟠 **Coral** - Neon coral pink-orange

**High Contrast:**
- ⚪ **White** - Pure white minimalist
- ⚫ **Black** - Deep black stealth

Each color comes in **standard** and **enhanced** variations:
- **Standard** (`*-standard.jsonc`) - Core UI elements only
- **Enhanced** (`*-enhanced.jsonc`) - Maximum customization including tabs, gutters, selections, scrollbars

See the full [Accents Guide](./accents/README.md) for detailed information.

## 💼 Multi-Project Workflow

Use different accents for different projects to instantly recognize which window you're in:

```
Frontend Project    → lime-enhanced.jsonc    (radioactive green)
Backend API         → blue-enhanced.jsonc    (electric blue)  
Admin Panel         → red-enhanced.jsonc     (blood red)
Documentation       → cyan-enhanced.jsonc    (aqua teal)
Experiments         → magenta-enhanced.jsonc (hot magenta)
```

This creates instant visual recognition when switching between windows!

## 📸 Screenshots

<!-- Add screenshots after generating them -->
<!-- Uncomment and add actual screenshot files to /images directory

### Gyokuro Desert
![Gyokuro Desert Theme](./images/theme-desert.png)

### Gyokuro Desert OG
![Gyokuro Desert OG Theme](./images/theme-desert-og.png)

### Gyokuro Dark
![Gyokuro Dark Theme](./images/theme-dark.png)

### Gyokuro Light
![Gyokuro Light Theme](./images/theme-light.png)

### Accent Showcase
![Workspace Accents](./images/accent-showcase.png)

-->

**Note:** To generate screenshots, see the [Screenshot Guide](./screenshots/README.md).

## 📦 What's Included

```
gyokuro-theme/
├── themes/               # 4 base color themes
│   ├── gyokuro-desert.json
│   ├── gyokuro-desert-og.json
│   ├── gyokuro-dark.json
│   └── gyokuro-light.json
├── accents/             # 24 workspace accent themes
│   ├── cyan-standard.jsonc
│   ├── cyan-enhanced.jsonc
│   ├── pink-standard.jsonc
│   ├── pink-enhanced.jsonc
│   ├── ... (20 more)
│   └── README.md
└── screenshots/         # Sample code for theme demos
    └── samples/
```

## 🎨 Customization Tips

### Fine-tune Accent Colors

You can mix and match or modify any accent. In your workspace `.vscode/settings.json`:

```json
{
  "workbench.colorCustomizations": {
    "statusBar.background": "#39FF14",     // Lime
    "activityBar.background": "#FF6600",   // Orange
    "titleBar.activeBackground": "#00CED1" // Cyan
  }
}
```

### Combine with Base Themes

Accents work best when layered on top of the base Gyokuro themes. The colors are designed to complement the Desert and Dark variants.

### Reset to Default

To remove accent customizations:
1. Open `.vscode/settings.json` in your project
2. Delete the `workbench.colorCustomizations` section
3. Save the file

## 🛠️ Development

To package the theme:

```bash
# Install vsce if you haven't
npm install -g @vscode/vsce

# Package the extension
vsce package
```

This generates a `.vsix` file you can install manually or publish to the marketplace.

## 📖 Documentation

- [Workspace Accents Guide](./accents/README.md) - Detailed accent usage and examples
- [Screenshot Guide](./screenshots/README.md) - How to generate theme screenshots
- [VS Code Theme Guide](https://code.visualstudio.com/api/extension-guides/color-theme) - Official documentation

## 🙏 Credits

Hat tip to the [desert-ex-syntax](https://github.com/casualjim/desert-ex-syntax) repository for the beautiful color palette that inspired the desert variants.

Special thanks to Hans Fugal, the original creator of the Vim desert color scheme, for the timeless design that continues to inspire developers.

## 📄 License

MIT License - see [LICENSE](./LICENSE) file for details.

---

Made with 🍵 by [cupofcrumly](https://cupofcrumly.com)
