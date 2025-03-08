# used for storing data in a configuration file for use across the game. This will be stored in a .env file

import os
import dotenv

class config:
    def __init__(self):
        # Check for the conf file, create a new one if it doesn't exist
        if not os.path.exists('./_internal/Assets/config'):
            os.mkdir('./_internal/Assets/config')
            with open('./_internal/Assets/config/config.env', 'w') as f:
                f.write("")
                f.close()
                self.config = ',/internal/Assets/config/config.env'
        else:
            self.config = ',/internal/Assets/config/config.env'


    def get(self, key):
        # Get the given part of the config file
        # It will return nul if the key is not found
        if os.getenv(key):
            return os.getenv(key)
        else:
            return "null"

    def set(self, key, value):
        # Set the given key to the given value
        # It will create the key if it doesn't exist
        if os.getenv(key):
            dotenv.set_key(self.config, key, value)
        else:
            dotenv.set_key(self.config, key, value)