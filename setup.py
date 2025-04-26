from pathlib import Path
from setuptools import find_namespace_packages, setup
from fincash import __version__


BASE_DIR = Path(__file__).parent
long_description = (BASE_DIR / "README.md").read_text()

# Load packages from requirements.txt
with open(Path(BASE_DIR, "requirements.txt")) as file:
    required_packages = [ln.strip() for ln in file.readlines() if not ln.startswith("#")]


test_packages = [
    "pytest"
]

dev_packages = [
    "ruff",
    "ipykernel",
    "ipywidgets>=7.0,<8.0",
    "python-dotenv"
]

docs_packages = [
    "mkdocs",
    "mkdocstrings[python]",
    "mkdocs-material",
    "mkdocs-gen-files",
    "mkdocs-literate-nav",
    "mkdocs-section-index",
    "mkdocs-jupyter"
]


setup(
    name='fincash',
    packages=find_namespace_packages(),
    version=__version__,
    description='A short description of the project.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Diego Canales",
    python_requires=">=3.8",
    entry_points={
        'console_scripts': ['fincash=fincash.cli:main'],
    },
    install_requires=[required_packages],
    extras_require={
        "test": test_packages,
        "dev": test_packages + dev_packages + docs_packages,
        "docs": docs_packages,
    }
)
