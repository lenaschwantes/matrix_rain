# Matrix Digital Rain

Efeito de chuva digital do Matrix feito com Pygame.

![Matrix Rain Effect](screenshot.png)

## 🚀 Rodar
```bash
# Com uv (recomendado)
uv run --with pygame matrix-rain.py

# Ou com pip
pip install pygame
python matrix-rain.py
```

## ✨ Features

- Caracteres katakana autênticos do Matrix
- Trail effect com fade gradual
- Velocidades variadas para depth effect
- 30 FPS smooth rendering

## 🛠️ Stack

- Python 3.11+
- Pygame 2.5+

## 📝 Como funciona

O efeito de trail é criado sobrepondo uma surface preta semi-transparente (alpha=25) a cada frame, fazendo os caracteres antigos fadearem gradualmente ao invés de limpar a tela completamente.

## 🎨 Customização

Edite as constantes no código:
- `FONT_SIZE`: tamanho dos caracteres
- `alpha` na Surface: intensidade do trail (quanto menor, mais longo)
- `CHARS`: conjunto de caracteres exibidos

