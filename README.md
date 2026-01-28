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

Utiliza la función de sugerencias de Google Trends para proponer palabras clave y temas relacionados con el sector. Devuleve una collección `suggestions` donde cada elemento contine:

* `title`: Término o frase sugerida por Google Trends.
* `type`: Categoría de la entidad.

### Análisis de Popularidad

`GET /time-series/{keyword}`

Proporciona una serie temporal que muestra la popularidad relativa de un término de búsqueda en Google. Permitie definir un horizonte temporal personalizado mediante rangos de fechas ajustables. Devuleve una colección de puntos de datos que conforman la serie temporal, donde cada regsitro contiene:

* `date`: Fecha del registro.
* `interest_level`: Índice de popularidad relativa (escala de 0 a 100).

### ⚡ Ejecución

Navega hasta el directorio raíz del proyecto y ejecuta el siguiente comando en tu terminal:

```bash
docker compose up --build -d
```
Una vez levantado el contenedor, la API estará disponible en el puerto `8080`. Puedes verificar el funcionamiento realizando peticiones a través de tu navegador, cURL o Postman:

| Endpoint | URL Ejemplo |
| :--- | :--- |
| Análisis de ETFs | `http://localhost:8081/market/XLK` |
| Análisis de Tendencias | `http://localhost:8081/trends/XLE` |
| Análisis de Popularidad | `http://localhost:8081/time-series/Cloud%20Computing?start_date=2024-01-01&end_date=2024-12-31` |

**Nota:** Puedes buscar los símbolos de los ETFs (ej: XLK, XLF, XLE) en [Yahoo! Finance](https://finance.yahoo.com/).



