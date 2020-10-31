from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read().rstrip()

setup(
    name="MailSender",
    version="1.0.2",
    keywords=("mail", "email", "embed", "image", "MailSender"),
    description="easy to send email",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    url="https://github.com/we684123/MailSender",
    author="we684123",
    author_email="we684123@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=['get_filename', 'coloredlogs'],
    python_requires=">=3.4"
)
