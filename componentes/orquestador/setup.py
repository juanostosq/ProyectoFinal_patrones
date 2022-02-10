import setuptools

with open("README.md") as f:
    README = f.read()

setuptools.setup(
    author="Sandro Bolanos",
    author_email="bsandrojavier@gmail.com",
    name="orquestador",
    url = "www.colosoft.com.co",
    description="orquestador del sistema",
    version="1.0",
    long_description = README,    
    packages = setuptools.find_namespace_packages(),   
    py_modules=['__main__'],
    zip_safe = False
)