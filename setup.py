"""
DataBot - Package d'installation
"""

from setuptools import setup, find_packages
import os

# Lire le README
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Lire les requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="databot-ai",
    version="1.0.0",
    author="Votre Nom",
    author_email="votre.email@domain.com",
    description="Assistant IA pour l'analyse commerciale",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/votre-username/DataBot-TFC",
    project_urls={
        "Documentation": "https://github.com/votre-username/DataBot-TFC/docs",
        "Source Code": "https://github.com/votre-username/DataBot-TFC",
        "Bug Tracker": "https://github.com/votre-username/DataBot-TFC/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: French",
        "Framework :: Streamlit",
    ],
    packages=find_packages(include=["src", "src.*"]),
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "databot=src.main:main",
            "databot-web=webapp.app_streamlit:main",
        ],
    },
    package_data={
        "src": ["data/*.csv", "data/*.db", "templates/*.html"],
    },
    include_package_data=True,
    keywords=[
        "ai",
        "business-intelligence",
        "data-analysis",
        "llm",
        "chatbot",
        "streamlit",
        "langchain",
        "mistral-ai",
    ],
    license="MIT",
    platforms=["any"],
    options={
        "bdist_wheel": {"universal": True},
        "build_exe": {
            "packages": ["pandas", "streamlit", "plotly"],
            "include_files": ["data/", "webapp/"],
        },
    },
    scripts=["scripts/databot-cli.py"],
)