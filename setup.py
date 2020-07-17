from setuptools import setup, find_packages

readme = open('README', 'r')
README_TEXT = readme.read()
readme.close()

setup(
    name="doi2bib",
    version="0.4.0",
    packages=find_packages(exclude=["build", ]),
    scripts=["doi2bib/bin/doi2bib"],
    long_description=README_TEXT,
    install_requires=["requests", "future", "bibtexparser"],
    include_package_data=True,
    license="MIT",
    description="Generate a bibtex given a doi",
    author="Bruno Messias",
    author_email="messias.physics@gmail.com",
    download_url="https://github.com/bibcure/doi2bib/archive/0.4.0.tar.gz",
    keywords=["bibtex", "science", "scientific-journals"],

    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Topic :: Text Processing :: Markup :: LaTeX",
    ],
    url="https://github.com/bibcure/doi2bib"
)
