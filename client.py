import subprocess
from typing import Optional


class HelmClient:
    client_version: str = ""
    client_path: str = "helm"


    def __init__(self, path: str = ""):
        if path:
            self.client_path = path

        version = self.version()
        self.client_version = version


    def version(self) -> str:
        if self.client_version:
            return self.client_version

        stdout, _ = self._run("version", "--short")

        return stdout.rstrip()


    def pull(self,
             chart: str,
             username: Optional[str] = None,
             password: Optional[str] = None,
             repo: Optional[str] = None,
             untardir: Optional[str] = None,
             untar: bool = True, 
             *args,
             **kwargs
             ):
        flags = []
        if username:
            flags.append(f"--username={username}")
        if password:
            flags.append(f"--password={password}")
        if repo:
            flags.append(f"--repo={repo}")
        if untar:
            flags.append("--untar")
        if untardir:
            flags.append(f"--untardir={untardir}")

        stdout, stderr = self._run("pull", chart, flags)

    def _run(self, args: list[str] | str, *flags) -> tuple[str, str]:
        cmd = [self.client_path]
        
        if type(args) is list:
            cmd.extend(args)
        elif type(args) is str:
            cmd.append(args)
        else:
            raise TypeError

        cmd.extend(flags)

        # TODO: error handling
        r = subprocess.run(cmd, capture_output=True, text=True)

        return r.stdout, r.stderr

