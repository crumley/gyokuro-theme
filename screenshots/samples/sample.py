"""
Gyokuro Theme - Python Sample
Demonstrates syntax highlighting for Python code
"""

from typing import List, Dict, Optional
import asyncio
import json
from datetime import datetime
from dataclasses import dataclass


@dataclass
class ThemeConfig:
    """Configuration for Gyokuro theme settings"""
    name: str
    variant: str
    accent: Optional[str] = None
    enhanced: bool = False


class ThemeManager:
    """Manages VS Code theme configurations"""
    
    VALID_ACCENTS = ['cyan', 'pink', 'orange', 'lime', 'purple', 
                     'blue', 'magenta', 'yellow', 'red', 'coral']
    
    def __init__(self, default_theme: str = 'gyokuro-desert'):
        self.theme = default_theme
        self._configs: Dict[str, ThemeConfig] = {}
        self.applied_at = datetime.now()
    
    async def apply_accent(self, color: str, enhanced: bool = False) -> ThemeConfig:
        """
        Apply an accent color to the current theme
        
        Args:
            color: The accent color name
            enhanced: Whether to use enhanced variant
            
        Returns:
            ThemeConfig object with the new settings
            
        Raises:
            ValueError: If color is not in VALID_ACCENTS
        """
        if color not in self.VALID_ACCENTS:
            raise ValueError(f"Invalid accent: {color}. "
                           f"Valid options: {', '.join(self.VALID_ACCENTS)}")
        
        variation = 'enhanced' if enhanced else 'standard'
        config = ThemeConfig(
            name=self.theme,
            variant=variation,
            accent=color,
            enhanced=enhanced
        )
        
        self._configs[color] = config
        await self._save_config(config)
        
        return config
    
    async def _save_config(self, config: ThemeConfig) -> None:
        """Save configuration to file"""
        filename = f"{config.accent}-{config.variant}.json"
        data = {
            'theme': config.name,
            'accent': config.accent,
            'enhanced': config.enhanced,
            'timestamp': datetime.now().isoformat()
        }
        
        # Simulate async I/O
        await asyncio.sleep(0.1)
        print(f"✓ Saved configuration: {filename}")
    
    def list_configs(self) -> List[str]:
        """Return list of configured accents"""
        return [f"{c.accent}-{c.variant}" 
                for c in self._configs.values()]


def calculate_theme_stats(configs: Dict[str, ThemeConfig]) -> Dict[str, int]:
    """Calculate statistics about theme usage"""
    stats = {
        'total': len(configs),
        'enhanced': sum(1 for c in configs.values() if c.enhanced),
        'standard': sum(1 for c in configs.values() if not c.enhanced)
    }
    return stats


# Example usage
if __name__ == '__main__':
    manager = ThemeManager('gyokuro-desert')
    
    # List comprehension and lambda examples
    accent_files = [f"{acc}-standard.jsonc" for acc in manager.VALID_ACCENTS]
    sorted_accents = sorted(manager.VALID_ACCENTS, key=lambda x: len(x))
    
    # F-string formatting
    print(f"🎨 Gyokuro Theme Manager")
    print(f"📦 Available accents: {len(manager.VALID_ACCENTS)}")
    print(f"⏰ Initialized at: {manager.applied_at.strftime('%Y-%m-%d %H:%M:%S')}")

