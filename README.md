# tumblecaesar



## Resources
- [Blog post relating to the challenge](https://www.harttraveller.com/Tumbler+Challenge)
- Clues might be posted in [Discord Server](https://discord.gg/ZDerehP6)
- Prize value can be viewed at [Public Wallet Address](https://algoexplorer.io/address/ZUECZQ67NIJNXED4V5HRZNGTQDHWHRW4SIBTOLRXDGHAZSTNGUDWVYWBYU)

Encoded wallet recovery phrase:

```
1zRiobx1tPhvqv32IoLAl7857cQYzKcIhNIPzJaQGpnJqFj6x7HTzIghdbvtrS7UOe1ts1bsZIxNCrMKOJER6KiO0FI0Nurf8z4yhmfj3shMUyIC0Vm2w18Si34HCD3qaax7aaCmc1MBeGcdem2idsuBtWikjSAqYwwSylJjyMAWUve-335475
```

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