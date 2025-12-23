from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = f.read().strip().split("\n")

setup(
    name="lojinet",
    version="2.0.0",
    description="Profesyonel Lojistik Yönetim Sistemi",
    author="İXİR Bilişim",
    author_email="info@ixirbilisim.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
