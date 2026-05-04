
from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="nadesiko3-python",
    version="6.0.0",
    description="Nadesiko3 Compatible Japanese Programming Language Module - Complete development environment for natural language programming",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Nadesiko Python Community",
    author_email="nadesiko-python@googlegroups.com",
    url="https://github.com/nadesiko3-python/nadesiko3-python",
    project_urls={
        "Documentation": "https://github.com/nadesiko3-python/nadesiko3-python/blob/main/docs/README.md",
        "Source": "https://github.com/nadesiko3-python/nadesiko3-python",
        "Tracker": "https://github.com/nadesiko3-python/nadesiko3-python/issues",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "requests>=2.25.0",
        "Pillow>=8.0.0",
        "numpy>=1.20.0",
        "pyyaml>=5.4.0",
    ],
    extras_require={
        "full": [
            "opencv-python>=4.5.0",
            "pandas>=1.3.0",
            "scikit-learn>=1.0.0",
            "matplotlib>=3.3.0",
            "pyautogui>=0.9.0",
            "pyperclip>=1.8.0",
            "pygame>=2.0.0",
            "qrcode>=6.1.0",
            "python-barcode>=0.15.0",
            "cryptography>=3.4.0",
            "openpyxl>=3.0.0",
        ],
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
    },
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Programming Languages :: Python",
        "Topic :: Software Development :: Internationalization",
        "Natural Language :: Japanese",
    ],
    keywords="nadesiko3 japanese programming education beginner natural-language gui bilingual",
    entry_points={
        "console_scripts": [
            "nadesiko-gui=start_gui:main",
            "nadesiko-designer=start_gui_designer:main",
        ],
    },
)
