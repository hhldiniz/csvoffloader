from distutils.core import setup

setup(
    name="csvoffloader",
    packages=["csvoffloader"],
    version="1.0",
    license="MIT",
    description="A converter that consumes .csv files and outputs json onto many different targets.",
    author="Hugo Diniz",
    author_email="hhldiniz@gmail.com",
    url="https://github.com/hhldiniz/csvoffloader",
    download_url="https://github.com/hhldiniz/csvoffloader/archive/v1.0.tar.gz",
    keywords=["csv", "converter", "consumer"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9'
    ]
)