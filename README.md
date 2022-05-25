# tumblecaesar

The original blog post relating to the challenge can be found by [clicking here](https://www.harttraveller.com/Tumbler+Challenge)

## Installation

If you want to install the program as a module to use, you can do so with the `pip install git+` command. 
```
pip install git+https://github.com/harttraveller/tumblecaesar.git
```

## Quickstart

```python
# import the tumbler
from tumblecaesar import Tumbler
import string

# define the text you want to encode
text = "WhatIsTheAirspeedVelocityOfAnUnladenSwallow"

# instantiate the tumbler with the appropriate seed and layers
tumbler = Tumbler(seed=2, layers=2)

# pass the text to the .enc() method on the tumbler, returning the encoded text
enc = tumbler.enc(text)
# > 4dy0GgWRfia5vZqqdzLMMrZfeiGNBg0faZiDWS4Xt8r-14728

# pass the encoded text to the .dec() method on the tumbler, returning the decoded text
dec = tumbler.dec(enc)
# > WhatIsTheAirspeedVelocityOfAnUnladenSwallow
```