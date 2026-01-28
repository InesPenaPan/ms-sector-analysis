# 📊 Microservicio de Análisis Sectorial

**Componente del Trabajo de Fin de Máster (TFM)** > *Máster en Ingeniería de Software y Sistemas Informáticos (MSSI)*

Microservicio construido con **FastAPI** que que automatiza la monitorización del entorno macroeconómico y competitivo de sectores específicos. Automatiza la ingesta de datos financieros mediante Yahoo! Finance (`yfinance`) para analizar ETFs sectoriales y caputra las tendencias de búsqueda a tarvés de Google Trends (`pytrends`).

## 🛠️ Stack 
El microservicio está desarrollado con las siguientes tecnologías y librerías clave:

* `FastAPI`: Framework principal utilizado para construir la API.
* `uvicorn`: Servidor ASGI de alta velocidad encargado de ejecutar la aplicación.
* `pydantic`: Utilizado para la validación de datos y la gestión de esquemas mediante modelos de Python.
* `yfinance`: Librería encargada de la extracción de datos financieros y de mercado desde la API de Yahoo! Finance.
* `pytrends`: Interfaz para la descarga de informes de tendencias y popularidad de palabras clave en Google.
* `NumPy`: Soporte para el procesamiento eficiente de grandes estructuras de datos y cálculos numéricos.
* `py-eureka-client`: Cliente para la integración con **Netflix Eureka**.

## 🌐 Endpoints

### Análisis de ETFs

`GET /market/{ticker}`

Recupera métricas bursátiles de un ETF representativo para diagnosticar el estado actual, el tamaño y el nivel de actividad de un determinado sector.

* `last_close_price`: Indica el valor de mercado del sector. Refleja el rendimiento colectivo de las principales empresas de esa industria.
* `market_cap`: Mide el tamaño total de los activos bajo gestión del ETF. Ayuda a entender la escala y la magnitud de la inversión total en el sector.
* `volume`: Muestra la actividad y el nivel de interés de los inversores.

### Análisis de Tendencias

`GET /trends/{ticker}`

Este endpoint consulta Google Trends para encontrar palabras clave y temas relacionados con el nombre del sector.

### Análisis de Popularidad


### 3. Interés de Búsqueda a lo Largo del Tiempo (`/time-series/{ticker}`)

Este endpoint recupera datos históricos que muestran la popularidad relativa de un término de búsqueda en Google a lo largo de un rango de fechas.

### ⚡ Ejecutar el servicio

### Pasos

1. **Situarse en el Directorio**: Abre tu terminal y navega hasta el directorio raíz del proyecto.

2. **Construir e Iniciar**: Ejecuta el siguiente comando para construir la imagen e iniciar el contenedor:

```bash
docker compose up --build -d
```

3. **Acceder a la API**: El microservicio estará accesible en el puerto `8081` (definido en el docker-compose.yml). Utiliza tu navegador o una herramienta como cURL o Postman para realizar las siguientes peticiones:

| Endpoint | URL Ejemplo |
| :--- | :--- |
| Datos de Mercado | `http://localhost:8081/market/XLK` |
| Sugerencias | `http://localhost:8081/trends/XLE` |
| Interés | `http://localhost:8081/time-series/Cloud%20Computing?start_date=2024-01-01&end_date=2024-12-31` |

### Ejemplos de Tickers

Utiliza los siguientes símbolos bursátiles para probar tu API:

| Ticker | Sector |
| :--- | :--- |
| **XLK** | Technology |
| **XLF** | Finance |
| **XLE** | Energy |
| **XLV** | Healthcare |

