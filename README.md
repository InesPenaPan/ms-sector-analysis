# 📊 Microservicio de Análisis Sectorial

Este microservicio ofrece una API construida con FastAPI para obtener y procesar datos de tendencias de búsqueda de Google y métricas actuales de mercado para ETF sectoriales, utilizando `pytrends` y `yfinance` como fuentes de datos.

## 💻 Funcionalidades Principales

El microservicio expone dos endpoints principales:

### 1. Datos de Mercado Sectorial (`/market/{ticker}`)

Este endpoint recupera métricas en tiempo real para un **ETF Sectorial**: 

* **Precio Acual** `last_close_price`: Indica el valor de mercado actual del sector. Refleja el rendimiento colectivo de las principales empresas dentro de esa industria.

* **Capitalización de Mercado** `market_cap`: Mide el tamaño total de los activos bajo gestión del ETF. Ayuda a entender la escala y la magnitud de la inversión total en ese sector.

* **Volumen** `volume`: Muestra la actividad y el nivel de interés de los inversores en el sector. Un volumen alto sugiere que el sector está "en movimiento" o es objeto de mucha atención (compra/venta).

### 2. Sugerencias de Palabras Clave (`/trends/{ticker}`)

Este endpoint consulta Google Trends para encontrar palabras clave y temas relacionados con el nombre del sector.

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

