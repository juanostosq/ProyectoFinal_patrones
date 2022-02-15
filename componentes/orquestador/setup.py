import setuptools

with open("README.md") as f:
    README = f.read()

setuptools.setup(
    author="Cristhian Martinez, Juan Ostos, Jose Quintero",
    author_email="camilofour1@gmail.com, jmostosq@correo.udistrital.edu.co, jolquinteroc@correo.udistrital.edu.co",
    name="orquestador",
    description="orquestador del sistema",
    version="1.0",
    long_description = README,    
    packages = setuptools.find_namespace_packages(),   
    py_modules=['__main__'],
    zip_safe = False
)