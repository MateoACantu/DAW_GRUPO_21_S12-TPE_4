# DAW_GRUPO_21_S12-TPE_4

# Sitio Web de Oferta de Cursos

Proyecto académico desarrollado para la asignatura **Desarrollo de Aplicaciones Web**, correspondiente al Grupo 21 de la Universidad Estatal de Milagro (UNEMI).

El proyecto consiste en una aplicación web desarrollada con **Django y PostgreSQL**, que permite gestionar docentes y cursos mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar). También incluye una página principal informativa y una interfaz desarrollada con HTML, CSS y Bootstrap.

## Tecnologías utilizadas

| Tecnología            | Versión         | Descripción                         |
| --------------------- | --------------- | ----------------------------------- |
| Python                | 3.13.5          | Lenguaje de programación            |
| Django                | 6.1.3           | Framework web                       |
| PostgreSQL            | —               | Sistema gestor de base de datos     |
| psycopg               | 3.3.9           | Adaptador de PostgreSQL             |
| Pillow                | 13.0.0          | Procesamiento de imágenes           |
| HTML, CSS y Bootstrap | Bootstrap 5.3.3 | Diseño de interfaces                |
| Git y GitHub          | —               | Control de versiones y colaboración |

## Funcionalidades

### Página principal

- Menú de navegación Home, Docentes y Cursos.
- Presentación de los cinco estudiantes.
- Secciones informativas de docentes y cursos.
- Enlaces de acceso a los módulos.

### Módulo de docentes

- Registrar docentes con sus datos personales y fotografía.
- Consultar el listado de docentes.
- Editar información existente.
- Eliminar registros mediante confirmación.
- Validar campos como correo electrónico y cédula.

### Módulo de cursos

- Registrar cursos con nombre, créditos, nivel, horas semanales, jornada e imagen.
- Asignar un docente a cada curso.
- Consultar los cursos registrados.
- Editar y eliminar cursos.
- Visualizar el docente asociado a cada curso.

La relación entre cursos y docentes se implementa mediante una clave foránea (`ForeignKey`). Un docente puede tener varios cursos asignados.

## Instalación y configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/MateoACantu/DAW_GRUPO_21_S12-TPE_4.git
cd DAW_GRUPO_21_S12-TPE_4
```

### 2. Crear el entorno virtual

En Windows:

```powershell
py -3.13 -m venv .venv313
.\.venv313\Scripts\Activate.ps1
```

### 3. Instalar las dependencias

```bash
python -m pip install -r requirements.txt
```

### 4. Configurar PostgreSQL

Es necesario disponer de PostgreSQL instalado y en ejecución.

Crear una base de datos para el proyecto, por ejemplo:

```sql
CREATE DATABASE sitio_cursos_db;
```

Configurar en `sitio_cursos/settings.py` los parámetros de conexión correspondientes al entorno local:

- Motor: `django.db.backends.postgresql`
- Base de datos: `sitio_cursos_db`
- Usuario: usuario con permisos sobre la base
- Contraseña: contraseña del usuario
- Servidor: `localhost`
- Puerto: `5432`

**Importante:** no publicar contraseñas ni claves secretas en GitHub. Se recomienda administrar las credenciales mediante variables de entorno.

### 5. Aplicar las migraciones

```bash
python manage.py check
python manage.py migrate
```

Verificar las migraciones aplicadas:

```bash
python manage.py showmigrations
```

### 6. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## Rutas principales

| Ruta               | Descripción              |
| ------------------ | ------------------------ |
| `/`                | Página principal         |
| `/docentes/`       | Listado de docentes      |
| `/docentes/nuevo/` | Registrar docente        |
| `/materias/`       | Listado de cursos        |
| `/materias/crear/` | Registrar curso          |
| `/admin/`          | Administración de Django |

## Estructura del proyecto

```text
DAW_GRUPO_21_S12-TPE_4/
├── docentes/
│   ├── migrations/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── materias/
│   ├── migrations/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── sitio_cursos/
│   ├── settings.py
│   ├── urls.py
│   └── views.py
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

## Trabajo colaborativo

El proyecto se desarrolló mediante Git y GitHub, utilizando ramas para organizar los aportes y Pull Requests para integrar los cambios.

La distribución de responsabilidades fue:

| Rol   | Responsabilidad                         |
| ----- | --------------------------------------- |
| Rol 1 | Entorno Django y repositorio GitHub     |
| Rol 2 | Configuración PostgreSQL y aplicaciones |
| Rol 3 | Diseño base y página principal          |
| Rol 4 | CRUD de docentes                        |
| Rol 5 | CRUD de cursos                          |
| Rol 6 | Integración, pruebas y entrega final    |

## Verificación del proyecto

Para comprobar la configuración y las migraciones:

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py showmigrations
python manage.py migrate
```

Las verificaciones funcionales comprenden la navegación, las operaciones CRUD de docentes y cursos, la visualización de imágenes, la persistencia en PostgreSQL y las relaciones entre modelos.

## Autores

**Grupo 21 — Desarrollo de Aplicaciones Web**

- Mateo Alexander Cantuña Intriago
- Jhonatan Christian Catota Verdezoto
- Pablo Andres Farro Vera
- Juan Carlos Izurieta Cisneros
- Jorge Marcelo Lojano Novillo
- Joseph Salvatore Vallejo Rodriguez
