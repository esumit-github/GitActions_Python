import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0."

REPO_NAME = "IPYNBRENDERER"
AUTHOR_USER_NAME = "sumit.mitra"
SRC_REPO = "IPYNBRENDERER"
AUTHOR_EMAIL = "email@rmail.com"
AUTHOR_PAT=

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package",
    long_description=long_description,
    long_description_content="text/markdown",
    #url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    #url=f"https://{AUTHOR_USER_NAME}:{AUTHOR_PAT}@github.rsym-cicd.blr.rsicdcdns.lab/sumit-mitra/{REPO_NAME}",
    url=f"http.proxy=http://192.168.50.3:3128 https://{AUTHOR_USER_NAME}:{AUTHOR_PAT}@github.rsym-cicd.blr.rsicdcdns.lab/sumit-mitra/{REPO_NAME}",
    
    project_urls={
        #"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        "Bug Tracker": f"github.rsym-cicd.blr.rsicdcdns.lab/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
