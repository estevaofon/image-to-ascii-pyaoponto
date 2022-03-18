import setuptools

# Get the long description from the README file
with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='image-to-ascii-pyaoponto',
    version='0.2',
    description='A Python module to transform image to ascii art',
    long_description=long_description,
    author='Python Direto ao Ponto',
    author_email='pyaoponto@gmail.com',
    license='MIT',
    url='https://github.com/estevaofon/image-to-ascii-pyaoponto',
    install_requires=['Pillow'],
    keywords=['ascii', 'image', 'art'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    )
