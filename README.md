# XSLICE README
https://mybinder.org/v2/gh/tbui0525/XSLICE-GODAS/HEAD?labpath=%2Fvoila%2Frender%2FXSLICE_Lite.ipynb
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tbui0525/XSLICE-GODAS/HEAD?labpath=voila%2Frender%2FXSLICE_Lite.ipynb)
###  Feel free to clone and experiment with adding new features and widgets in a separate branch


- `pip3 install --upgrade pip`
- Install pip-tools `pip3 install pip-tools`
- Update dev requirements: `pip-compile --output-file=requirements.dev.txt requirements.dev.in`
- Update requirements: `pip-compile --output-file=requirements.txt requirements.in`
- Install dev requirements `pip3 install -r requirements.dev.txt`
- Install requirements `pip3 install -r requirements.txt`


## Update versions

`pip-compile --output-file=requirements.dev.txt requirements.dev.in --upgrade`
`pip-compile --output-file=requirements.txt requirements.in --upgrade`


