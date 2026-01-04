# Pipeline de Datos de Ventas

Un proyecto de portafolio de ingeniería de datos profesional que demuestra procesos ETL, limpieza de datos con Pandas y análisis SQL.

## Resumen del Proyecto

Este proyecto simula un pipeline de datos del mundo real:
1.  **Ingesta**: Genera datos de ventas crudos con inconsistencias intencionales (formatos de fecha mixtos, valores faltantes, duplicados).
2.  **Procesamiento (ETL)**: Un script de Python limpia, transforma y enriquece los datos.
3.  **Análisis**: Consultas SQL derivan insights de negocio a partir de los datos procesados.

## Tecnologías Utilizadas

-   **Python 3.x**
-   **Pandas**: Para manipulación y limpieza de datos.
-   **NumPy**: Para operaciones numéricas.
-   **SQL**: Para consultas de análisis de datos (compatible con MySQL).

## Estructura de Archivos

-   `scripts/genera data.py`: Script para crear el dataset crudo (`data/raw data.csv`).
-   `scripts/processor.py`: Script principal ETL para producir `data/clean data.csv`.
-   `sql/analysis_queries.sql`: Consultas SQL para preguntas de negocio.
-   `data/raw data.csv`: Datos de entrada generados.
-   `data/clean data.csv`: Datos de salida procesados.

## Cómo Ejecutar

1.  **Instalar Dependencias**:
    ```bash
    pip install pandas numpy
    ```

2.  **Generar Datos**:
    ```bash
    python "scripts/genera data.py"
    ```
    Esto crea `data/raw data.csv` con errores simulados.

3.  **Ejecutar Pipeline**:
    ```bash
    python scripts/processor.py
    ```
    Este script realizará lo siguiente:
    -   Estandarizar fechas a `YYYY-MM-DD`.
    -   Imputar precios faltantes usando medianas por categoría.
    -   Calcular `Total_Revenue` (Ingresos Totales).
    -   Eliminar duplicados.
    -   Guardar datos limpios en `data/clean data.csv`.

## Análisis SQL

Puedes ejecutar las consultas en `sql/analysis_queries.sql` contra los datos limpios (asumiendo que están cargados en una base de datos SQL llamada `sales_data`).

1.  **Producto con Mayores Ingresos**
2.  **Promedio de Ventas por Categoría**
3.  **Top 5 Clientes por Gasto**
