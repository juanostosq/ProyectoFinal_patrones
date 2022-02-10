import setuptools

with open("README.md") as f:
    README = f.read()

setuptools.setup(
    author="Sandro Bolanos",
    author_email="bsandrojavier@gmail.com",
    name="api",
    url = "www.colosoft.com.co",
    description="interfaces del sistema",
    version="1.0",
    long_description = README,    
    packages= setuptools.find_namespace_packages(),    
    zip_safe=False
)


