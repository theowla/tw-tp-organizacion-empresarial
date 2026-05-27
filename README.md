# tw-tp-organizacion-empresarial

#Trabajo Práctico: Gestión Colaborativa, Control de Versiones y Organización Empresarial (Git, GitHub y Jira) 

#Escenario B – Análisis de Ventas de una Pequeña Empresa 

#Alumno: Theo Wlasiczuk
#Roles:
*HUGO (Rol: Líder y Organizador)
*PACO (Rol: Desarrollador Técnico)
*LUIS (Rol: Revisor y QA)

tw-tp-organizacion-empresarial/ 
│ 
├── datos/ 
│   └── dataset.csv 
│ 
├── resultados/ 
│   └── evolucion_ventas.png
│ 
├── scripts/ 
│   └── analisis_datos.py 
│ 
├──.gitignore
│ 
├── README.md

#dataset: El dataset fue tomado desde kaggle.com y su autor es ShreyanshVerma27, este contiene un listado de ventas. Son alrededor de 232 productos unicos contando con estos tipos de datos Id, fecha, categoria, nombre del producto, cantidad, precio por unidad, precio total, region y metodo de pago

#como utilizar el programa:
paso 1: clonar el repositorio y entrar en el mismo
  git clone https://github.com/theowla/tw-tp-organizacion-empresarial.git
  cd tw-tp-organizacion-empresarial
paso 2: cargar el set de datos
  meter un archivo csv con nombre dataset.csv dentro de la carpeta datos o utilizar el ya implementado
paso 3: ejecutar el programa
  python scripts/analisis_datos.py
