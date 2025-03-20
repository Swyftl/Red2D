import github
import requests
import zipfile
import os

def download_latest_release(repo_owner, repo_name, download_path):
    g = github.Github()
    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    latest_release = repo.get_latest_release()
    zip_url = latest_release.zipball_url

    response = requests.get(zip_url)
    zip_path = os.path.join(download_path, "Red2D.zip")

    with open(zip_path, "wb") as file:
        file.write(response.content)

    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(download_path)

    os.remove(zip_path)

def update_game_engine():
    repo_owner = "Swyftl"
    repo_name = "Red2D"
    download_path = "https://github.com/Swyftl/Red2D/releases/latest"
    
    download_latest_release(repo_owner, repo_name, download_path)
    print("Game engine updated to the latest version.")

# Example usage
if __name__ == "__main__":
    update_game_engine()

