import setuptools

with open("README.md") as f:
    README = f.read()

setuptools.setup(
    author="Sandro Bolanos",
    author_email="bsandrojavier@gmail.com",
    name="gui",
    url = "www.colosoft.com.co",
    description="interfaces del sistema",
    version="1.0",
    data_files=[('',['configuracion.inf'])],
    long_description = README,   
    packages= setuptools.find_namespace_packages(),    
    zip_safe=False
)


