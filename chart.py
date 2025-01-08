import yaml

from client import HelmClient

class HelmChart:
    url: str
    path: str
    client: HelmClient

    def __init__(self, path_or_url: str, client: HelmClient):
        if self._is_url(path_or_url):
            self.url = path_or_url
        else:
            self.path = path_or_url

        self.client = client


    def _is_url(self, s: str):
        protocols = ('https://', 'oci://')
        return s.startswith(protocols)

    def package(self):
        pass

    def template(self):
        pass

class HelmChartValues:
    pass
