# Python Triangle Helper

This is a Python script to start up a Flask server. This server has one '/triangle' endpoint that calculates what type of triangle the user submits.

## Prerequisites

The script runs with Python 3.8. See the [requirements](requirements.txt) for what third-party requirements you will need to have installed.

You can install all requirements by using pip:

```
pip3 install -U -r requirements.txt
```

## Example

To run the Flask server, run the following command:

```
FLASK_ENV=development FLASK_APP=server.py python3 -m flask run
```

## License

Copyright (c) 2022  Mike Voets

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the [LICENSE.md](LICENSE.md) file for details.
