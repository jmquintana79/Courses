# README

## How to install SCIPOPT (framework)

- Descargar instalador (SH file) de la libreria necesaria con fines NO COMERCIALES [aqui](https://scipopt.org/index.php#download).
- Mover el instalador a `~/` y ejecutar. En las opciones, no extraer directamente en la carpeta actual para que te cree la carpeta correspondiente de la libreria.
- Modificar el nombre de la carpeta para que sea mas simple (por ejemplo: `SCIPOptSuite7`).
- Añadir la libreria al path del sistema: `export PATH=$PATH:~/SCIPOptSuite7`.
- Instalar la correspondiente libreria python con Conda (en este caso en el entorno virutal *optimization*): `conda install -n "optimization" --channel conda-forge pyscipopt` 

## How to install PYOMO (framework) and GLPK (open source solver)

- Instalacion del solver GLPK en MacOs es inmediata: `brew install glp`.
- Revisar donde ha sido instalado: `which glpsol`.
> NOTA: Al haber sido instalado con *brew*, deberia estar aqui: */usr/local/bin/glpsol*.
- Incluir en el path del sistema: `export PATH=$PATH:/usr/local/bin/glpsol`.
- Para revisar que se ha instalado correctamente: `glpsol —help`
- Instalacion del framework PYOMO con Conda (en este caso en el entorno virutal *optimization*): `conda install -n "optimization" -c conda-forge pyomo`.

## Hot to install PuLP (framework):
- Basta con instalar las siguientes librerias de Python. Usando Conda (env *optimization*):
	- Cython: `conda install -n optimization -c anaconda cython`.
        - PuLP: `conda install -n optimization -c conda-forge pulp`.


## Intall Cbc (solver):

> NOTA: Si lo instalas desde un entorno virtual activado, la libreria se instalara en dicho entorno virtual.
- brew tap coin-or-tools/coinor
- brew install cbc 
