from setuptools import setup
import subprocess
import os

# Get version from git
version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in version:
    # when not on tag, git describe outputs: "1.3.3-22-gdf81228"
    # pip has gotten strict with version numbers
    # so change it to: "1.3.3+22.git.gdf81228"
    # See: https://peps.python.org/pep-0440/#local-version-segments
    v, i, s = version.split("-")
    version = v + "+" + i + ".git." + s

assert "-" not in version
assert "." in version

# Write the version to a file (this can be used in your package)
with open(os.path.join("robustbase", "version.py"), "w", encoding="utf-8") as fh:
    fh.write("__version__ = '{}'\n".format(version))

setup()
