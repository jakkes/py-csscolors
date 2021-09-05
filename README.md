# CSS Colors
[![Build Status](http://drone.jakke.se/api/badges/jakkes/py-csscolors/status.svg)](http://drone.jakke.se/jakkes/py-csscolors)
Simply all css colors easily accessible in hex color code.

```python
>>> import csscolors
>>> csscolors.RED
'#ff0000'
```

Also allows for iteration:
```python
>>> import csscolors
>>> for color_name, hex_code in csscolors.iterator():
...     print(color_name, hex_code)
ALICE_BLUE #f0f8ff
ANTIQUEWHITE #faebd7
AQUA #00ffff
AQUAMARINE #7fffd4
AZURE #f0ffff
BEIGE #f5f5dc
BISQUE #ffe4c4
BLACK #000000
BLANCHED_ALMOND #ffebcd
BLUE #0000ff
...
...
...
```

## Install
Install through `pip`:
```bash
pip install csscolors
```
