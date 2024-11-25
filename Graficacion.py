import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
file_path = '\\Users\\sonic\\OneDrive\\Documentos\\7to\\Mineria\\Proyecto\\MD_Proyecto.csv'
data = pd.read_csv(file_path)

# Limpiar los datos: eliminar columnas irrelevantes y NaN
cleaned_data = data[['Marca', 'Total de telefonos']].dropna()

# Gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(cleaned_data['Marca'], cleaned_data['Total de telefonos'], color='skyblue', edgecolor='black')
plt.title('Total de Teléfonos por Marca', fontsize=16)
plt.xlabel('Marca', fontsize=14)
plt.ylabel('Total de Teléfonos', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(cleaned_data['Total de telefonos'], labels=cleaned_data['Marca'], autopct='%1.1f%%', colors=plt.cm.tab10.colors)
plt.title('Distribución de Teléfonos por Marca', fontsize=16)
plt.tight_layout()
plt.show()
