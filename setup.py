import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="oli", # Replace with your own username
    version="0.0.8",
    author="StanGirard",
    author_email="stan@primates.dev",
    description="One Liner Installer for Linux & MacOs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/StanGirard/OneLiners",
    packages=["oli","oli.macos"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
		'console_scripts':[
			'oli = oli.run:main',
		],
	},
)