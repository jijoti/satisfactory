Data trix: https://docs.google.com/spreadsheets/d/11v_oKu4j1ryVhaxRbgkW3rEiYod8qI0NVKEDzZbEXmk/edit#gid=1908851257

Run with: `python3 optimize_generate.py`


All of the "trades" that I've unlocked in my game are added in satisfactory_data.py. Comment out or add alternative "trades" that you've unlocked in `StaticSatisfactoryDataLoader._loadTrades()`.

All of the "resources" that I've unlocked are in `StaticSatisfactoryDataLoader._loadResources()`. If I do not know their sink_points then I've set it to 0. Liquids are also set to 0.

In order to change the input of raw resources open optimize_generate.py and change the values set into `available_resources`.

`optimize_generate.py` generates a system of equations that look like those more explicitly laid out in `optimize.py`. I suggest reading `optimize.py` first.

Currently time, buildings and energy are ignored.
