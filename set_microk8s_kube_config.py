import shutil
from pathlib import Path
import os

def check_microk8s_kube_config_file():
    """
    Copy microk8s kuber config to ~/.kube/config
    """
    kube_config_file_location = Path(os.path.expanduser("~/.kube/config"))

    if not kube_config_file_location.exists():
        kube_dir = os.path.dirname(kube_config_file_location)

        if not os.path.exists(kube_dir):
            os.makedirs(kube_dir)

        try:
            shutil.copy(Path("/var/snap/microk8s/current/credentials/client.config"), kube_config_file_location)
        except FileNotFoundError:
            print("No Kubernetes config file found at ~/.kube/config")


check_microk8s_kube_config_file()
