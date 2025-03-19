# Get the version of the engine, and check it against the repo for the latest version

import github
import dotenv
import os

import github.Repository

def check_for_updates():
    dotenv.load_dotenv('./Red2D/engine.env')
    if os.getenv('version'):
        print(os.getenv('version'))
        repo = github.Github().get_repo('Swyftl/Red2D')
        latest_version = repo.get_latest_release().tag_name
        if latest_version != os.getenv('version'):
            print(latest_version+" of Red2D is available, you are running "+os.getenv('version'))
        else:
            print('No updates are available for Red2D')
    else:
        print('engine config not found')
        print('if this is a packaged game, please ignore this')