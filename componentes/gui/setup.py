import setuptools

with open("README.md") as f:
    README = f.read()

setuptools.setup(
    author="Cristhian Martinez, Juan Ostos, Jose Quintero",
    author_email="camilofour1@gmail.com, jmostosq@correo.udistrital.edu.co, jolquinteroc@correo.udistrital.edu.co",
    name="gui",
    description="interfaces del sistema",
    version="1.0",
    data_files=[('',['configuracion.inf'])],
    long_description = README,   
    packages= setuptools.find_namespace_packages(),    
    zip_safe=False
)


