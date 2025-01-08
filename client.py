import subprocess


class HelmClient:
    client_version: str = ""
    client_path: str = "helm"

    def __init__(self, path: str | None) -> None:
        if path:
            self.client_path = path

        version = self.version()
        self.client_version = version

    def version(self) -> str:
        if self.client_version:
            return self.client_version

        cmd = ["helm", "version", "--short"]
        o = subprocess.run(cmd, capture_output=True, text=True)

        o.check_returncode()
        return o.stdout.rstrip()

    def _run(self, args: list[str] | str, *flags: list[str]):
        pass 
