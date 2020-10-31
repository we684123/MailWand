from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read().rstrip()

setup(
    name="MailCrawler",
    version="1.0.0",
    keywords=("mail", "email","crawler","embed","image"),
    description="link to crawler send email",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/we684123/MailCrawler",
    author="we684123",
    author_email="we684123@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['get_filename']
)
