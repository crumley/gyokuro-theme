# Gyokuro Theme Workspace Accents

Workspace accent themes to make each VS Code window easily distinguishable. Perfect for managing multiple projects with different personalities!

## 🎨 Color Palette (12 Colors)

**Original Accents:**
- **Cyan** - Aqua teal vibes
- **Pink** - Hot pink energy

**Neon/Street Art Collection:**
- **Orange** - Electric neon orange
- **Lime** - Radioactive neon green
- **Purple** - Electric violet
- **Blue** - Cobalt electric blue
- **Magenta** - Pure hot magenta
- **Yellow** - Acid yellow highlighter
- **Red** - Blood crimson
- **Coral** - Neon coral pink-orange

**High Contrast:**
- **White** - Pure white minimalist
- **Black** - Deep black stealth

## 📦 Variations

Each color comes in **two variations**:

### Standard (`*-standard.jsonc`)
Customizes core UI elements:
- Status bar
- Activity bar
- Title bar
- Panel titles
- Focus borders
- Buttons
- Remote indicators

### Enhanced (`*-enhanced.jsonc`)
Everything in standard, PLUS:
- **Editor tabs** (active/inactive colors and borders)
- **Sidebar section headers** (Explorer, Search, etc.)
- **Editor gutter** (line numbers background)
- **Text selections** (editor highlighting)
- **Input fields** (borders and backgrounds)
- **Badges** (notification counts)
- **Scrollbars** (thumb and hover states)
- **Lists/trees** (hover and selection states)

Enhanced versions create maximum window differentiation!

## 🚀 How to Use

1. **Open VS Code Settings** (`Cmd/Ctrl + ,`)
2. **Click the `{}` icon** (top right) to open `settings.json`
3. **Copy the contents** of your chosen accent file
4. **Paste into your workspace settings** or user settings

### For Workspace-Specific Accents (Recommended)
Create a `.vscode/settings.json` in your project:
```json
{
  "workbench.colorCustomizations": {
    // Paste accent colors here
  }
}
```

### Quick Workflow
For different projects:
- **Frontend** → `lime-enhanced.jsonc` (radioactive green)
- **Backend** → `blue-enhanced.jsonc` (electric blue)
- **Admin panel** → `red-enhanced.jsonc` (blood red)
- **Documentation** → `cyan-enhanced.jsonc` (aqua teal)
- **Experiments** → `magenta-enhanced.jsonc` (hot magenta)

## 💡 Tips

- **Mix and match**: Try standard for cleaner looks, enhanced for maximum personality
- **High contrast themes** (white/black) work great for focused work
- **Neon themes** are perfect for that graffiti/street art/punk aesthetic
- **Each window = different color** makes switching projects instant and visual
- **Use with base themes**: These accents overlay on your Gyokuro Dark/Desert themes

## 🎯 File Naming Convention

```
{color}-{variation}.jsonc

Examples:
- cyan-standard.jsonc
- purple-enhanced.jsonc
- red-standard.jsonc
```

---

**Total:** 24 accent themes (12 colors × 2 variations each)

Choose your vibe and make each project window instantly recognizable! 🎨✨

