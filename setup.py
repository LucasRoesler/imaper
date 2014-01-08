from setuptools import setup

setup(
    name="imaper",
    version="1.0.1",
    author="Lucas Roesler",
    author_email="lucas@jobdash.com",
    url="https://github.com/jobdash/imaper",
    description="IMAP made easy.",
    long_description="See documentation at http://pythonhosted.org/imaper/",
    license='MIT',
    packages=["imaper"],
    install_requires=[
        "IMAPClient==0.10.2",
    ],
    classifiers=[
        "Topic :: Utilities",
    ],
)
