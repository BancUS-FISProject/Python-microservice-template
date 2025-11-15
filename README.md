# Estructura del proyecto

```bash
service_name/
├── .github/                      # CI/CD (Integración Continua)
│   └── workflows/
│       └── ci.yml                # GitHub Action: instala, corre tests, chequea formato
│
├── .dockerignore                 # Archivos a ignorar en la build de Docker
├── .env.example                  # Plantilla de variables de entorno (para copiar a .env)
├── .gitignore
│
├── Dockerfile                    # Construcción de la imagen del servicio
├── docker-compose.yml            # Servicio + MongoDB para desarrollo
├── README.md                     # Documentación del microservicio
│
└── src/
    └── accounts_service/
        ├── __init__.py
        │
        ├── api/                  # 1. Capa de API (HTTP)
        │   ├── __init__.py
        │   ├── v1/               # Versionado /v1/
        │   │   ├── __init__.py
        │   │   └── accounts_blueprint.py  # Endpoints
        │   ├── auth.py           # Autenticaciones
        │
        ├── core/                 # 2. Configuración
        │   ├── __init__.py
        │   ├── config.py         # Carga variables de entorno
        │   └── extensions.py     # Configuracion de comunicaciones 
        │                         #  (base dedatos, otros microservicios)
        │
        ├── db/                   # 3. Base de datos
        │   ├── __init__.py
        │   ├── database.py       # Conexión a MongoDB (Motor)
        │   └── account_repository.py # Operaciones DB
        │
        ├── models/               # 4. Modelos Pydantic
        │   ├── __init__.py
        │   ├── account.py        # AccountCreate, AccountView…
        │
        ├── services/             # 5. Lógica de negocio
        │   ├── __init__.py
        │   └── account_service.py # crear, debitar, actualizar, etc.
        │
        ├── comms/               # 6. Comunicación
        │   ├── __init__.py
        │   ├── publisher.py      # Publica eventos (RabbitMQ, etc.)
        │   └── consumer.py       # Consume eventos externos
        │
        └── app.py               # Punto de entrada (FastAPI)
        
