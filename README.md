# 🎨 ErrorArt

ErrorArt makes Python errors **fun and creative** by replacing tracebacks with **ASCII art, haikus, or sarcastic remarks**.

## ✨ Features
- Replace boring errors with fun outputs
- Modes: `ascii`, `haiku`, `sarcasm`
- Easy to use with just `import errorart`

## 🚀 Usage
```python
import errorart
errorart.set_mode("haiku")

print(1 / 0)   # triggers fancy ZeroDivisionError
