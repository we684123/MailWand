from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read().rstrip()

setup(
    name="mailwand",
    version="1.0.0",
    keywords=("mail", "email", "embed", "image", "mailsender", "mailwand"),
    description="easy to send email",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/we684123/MailWand",
    author="we684123",
    author_email="we684123@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[
        'get_filename>=1.0',
        'coloredlogs>=14.0',
        'humanfriendly >= 7.1'
    ],
    python_requires='>=3.5',
)
