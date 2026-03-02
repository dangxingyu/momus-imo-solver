"""
Setup script for IMO Solver package
"""

from setuptools import setup, find_packages


# Read README file
def read_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "AI agents for solving International Mathematical Olympiad problems"


# Read requirements
def read_requirements():
    try:
        with open("requirements.txt", "r", encoding="utf-8") as f:
            return [
                line.strip() for line in f if line.strip() and not line.startswith("#")
            ]
    except FileNotFoundError:
        return ["requests", "pyyaml"]


setup(
    name="momus-imo-solver",
    version="0.1.0",
    author="Xingyu Dang, Rohit Agarwal, Rodrigo Porto, Anirudh Goyal, Liam H Fowl, Sanjeev Arora",
    description="Official implementation of the Momus IMO pipeline",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://arxiv.org/abs/2602.16793",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov",
            "black",
            "flake8",
        ],
    },
    entry_points={
        "console_scripts": [
            "imo-solve=imo_solver.cli:main",
            "imo-test=imo_solver.cli:test_main",
            "imo-parallel=imo_solver.cli:parallel_main",
        ],
    },
    package_data={
        "imo_solver": [
            "config/*.yaml",
            "prompts/*.yaml",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="artificial-intelligence machine-learning olympiad mathematics proof-solving",
    project_urls={"Paper": "https://arxiv.org/abs/2602.16793"},
)
