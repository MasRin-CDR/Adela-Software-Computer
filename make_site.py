from pathlib import Path
import re
import shutil

root = Path(r"E:\Adela Software & Computer")
source = root / "Adela Software & Computer.html"
if not source.exists():
    raise FileNotFoundError(source)

text = source.read_text(encoding="utf-8")
style_match = re.search(r"<style>(.*?)</style>", text, re.S)
script_match = re.search(r"<script>(.*?)</script>", text, re.S)
if not style_match or not script_match:
    raise RuntimeError("Could not find style/script blocks")

(root / "css").mkdir(exist_ok=True)
(root / "js").mkdir(exist_ok=True)
(root / "css" / "style.css").write_text(style_match.group(1).strip() + "\n", encoding="utf-8")
(root / "js" / "script.js").write_text(script_match.group(1).strip() + "\n", encoding="utf-8")

new_text = text.replace(style_match.group(0), '  <link rel="stylesheet" href="css/style.css">', 1)
new_text = new_text.replace(script_match.group(0), '  <script src="js/script.js" defer></script>', 1)
(root / "index.html").write_text(new_text, encoding="utf-8")

print("Created index.html, css/style.css, js/script.js")
