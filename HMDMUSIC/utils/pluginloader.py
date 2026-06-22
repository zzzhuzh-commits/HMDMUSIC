from pathlib import Path
import importlib

def load_plugins():
    plugins = Path("HMDMUSIC/plugins")

    for plugin in plugins.glob("*.py"):
        if plugin.stem.startswith("_"):
            continue

        importlib.import_module(
            f"HMDMUSIC.plugins.{plugin.stem}"
        )
