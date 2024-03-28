---
tags:
  - Terminal
  - Zsh
  - Linux
---

# Zsh

To get your currently set keybindings:

```sh
bindkey -L
```

For interpreting what these bindings mean:
- `^[` means the ESC key
- `[A`, `[B`, `[C`, `[D` are the "up", "down", "right" and "left" keys
- `^` means the control key, unless it's part of the `^[` "escape key" sequence

To get the list of macros that can be bound to a keybinding:

```sh
zle -al
```

Note: `zle` stands for "Zsh Line Editor". It has pretty expansive documentation, but it's pretty dense.