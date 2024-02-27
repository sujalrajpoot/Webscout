from setuptools import setup, find_packages

# Parse version from your project's __init__.py file
version = None
with open("webscout/version.py") as version_file:
    exec(version_file.read())

with open("README.md", encoding="utf-8") as f:
    README = f.read()

setup(
    name="webscout",
    version="1.0.7",
    description="Search for words, documents, images, videos, news, maps and text translation using the DuckDuckGo.com, yep.com, phind.com and you.com Also containes AI models",
    long_description=README,
    long_description_content_type="text/markdown",
    author="OEvortex",
    author_email="helpingai5@gmail.com",  # Replace with your email
    url="https://github.com/OE-LUCIFER/Webscout",
    packages=find_packages(),
    classifiers=[
        "Development Status ::  5 - Production/Stable",
        "License :: OSI Approved :: HelpingAI Simplified Universal License",  # Updated license classifier
        "Operating System :: OS Independent",
        "Programming Language :: Python ::  3",
        "Programming Language :: Python ::  3 :: Only",
        "Programming Language :: Python ::  3.8",
        "Programming Language :: Python ::  3.9",
        "Programming Language :: Python ::  3.10",
        "Programming Language :: Python ::  3.11",
        "Programming Language :: Python ::  3.12",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP :: Indexing/Search",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "docstring_inheritance>=2.1.2",
        "click>=8.1.7",
        "curl_cffi>=0.6.0b7",
        "lxml>=5.1.0",
        "nest-asyncio>=1.6.0",
        "selenium>=4.1.3",
        "tqdm>=4.64.0",
        "webdriver-manager>=3.5.4",
        "halo>=0.0.31",
    ],
    entry_points={
        "console_scripts": [
            "WEBS = webscout.cli:cli",
            "webscout-ai-phindsearch = webscout.AI:phindsearch",
            "webscout-ai-yepchat = webscout.AI:yepchat",
            "webscout-ai = webscout.AI:cli",      
        ],
    },
    extras_require={
        "dev": [
            "ruff>=0.1.6",
            "pytest>=7.4.2",
        ],
    },
    license='HelpingAI Simplified Universal License',  
)
