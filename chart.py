from typing import Optional, Any
import yaml

from client import HelmClient
from errors import *

class HelmChart:
    url: str
    path: str
    client: HelmClient
    chart: dict[str, Any]


    def __init__(self, path_or_url: str, client: Optional[HelmClient] = None, load: bool = False):
        if self._is_url(path_or_url):
            self.url = path_or_url
            self.remote = True
        else:
            self.path = path_or_url
            self.remote = False

        if client:
            self.client = client
        else:
            self.client = HelmClient()

        if load:
            self.load()


    def _is_url(self, s: str):
        protocols = ('https://', 'oci://')
        return s.startswith(protocols)


    def load(self):
        if self.remote:
            self.pull()
        try:
            with open(f"{self.path}/Chart.yaml", 'r') as f:
                self.chart = yaml.safe_load(f)
        except FileNotFoundError:
            raise ChartLoadError(f"Chart.yaml not found in {self.path}")
        except yaml.YAMLError:
            raise ChartLoadError(f"Error parsing Chart.yaml in {self.path}")


    def package(self):
        pass

    def template(self):
        pass

    def pull(self,
             username: Optional[str] = None,
             password: Optional[str] = None,
             path: Optional[str] = None
             ):
        self.client.pull(self.url, username, password, untardir=path)
        pass

class HelmChartValues:
    pass
