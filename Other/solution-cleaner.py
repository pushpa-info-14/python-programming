import os
import shutil

# Specify the root folder (the solution folder)
ROOT_DIRS = [
    "C:\\Projects\\transvirtual-web-v1\\Actions",
    "C:\\Projects\\transvirtual-web-v1\\ThirdPartyWebServices",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.AspNet.Owin",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Common",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Common.Legacy",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Common.Tests",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.ConsoleTester",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Deployment",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Infra",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.ServerUtility",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Service.Commander",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Service.Common",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Service.Host",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Service.Manager",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Services.Tests",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Tcp",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Web",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Web.Common",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Web.Controllers",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Web.Models",
    "C:\\Projects\\transvirtual-web-v1\\TransVirtual.Web.Tests",
]

# Folder names to delete
TARGET_FOLDERS = ["bin", "obj", ".vs"]


def delete_folder(path):
    """Safely delete a folder and handle errors."""
    try:
        shutil.rmtree(path)
        print(f"✅ Deleted: {path}")
    except Exception as e:
        print(f"⚠️ Failed to delete {path}: {e}")


def clean_build_folders(root_dir):
    """Walk through the directory tree and delete target folders."""
    for current_dir, dirs, files in os.walk(root_dir, topdown=True):
        for folder in list(dirs):
            if folder.lower() in TARGET_FOLDERS:
                folder_path = os.path.join(current_dir, folder)
                delete_folder(folder_path)
                # Remove from traversal to prevent further walk
                dirs.remove(folder)


if __name__ == "__main__":
    for f in ROOT_DIRS:
        print(f"🧹 Cleaning build folders under: {f}")
        clean_build_folders(f)
    print("\n✅ Cleanup complete!")
