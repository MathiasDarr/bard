from setuptools import setup, find_packages

setup(
    name="bard",
    version="3.9.11",
    description="Packaging a Flask application",
    author="Mathias Darr",
    author_email="dakobedbard@gmail.com",
    url="https://github.com/MathiasDarr/dakobed_flask",
    packages=find_packages(exclude=["ez_setup", "examples", "test"]),
    namespace_packages=[],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points={
        "console_scripts": ["bard = bard.manage:cli"],
    },
)

