import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="epyrogram",
    version="0.0.2",
    author="stefanodvx",
    author_email="pp.stefanodvx@gmail.com",
    description="EPyrogram: extend the functionality of Pyrogram by enhancing it with new features.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stefanodvx/epyrogram",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["pyrogram"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)