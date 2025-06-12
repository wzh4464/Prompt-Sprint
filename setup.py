from setuptools import setup, find_packages

setup(
    name="prompt-sprint",
    version="0.1.0",
    author="Your Name",
    description="Prompt-Sprint utilities and experiments",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
) 