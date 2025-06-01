# api/renderers.py

from rest_framework.renderers import BaseRenderer
import pandas as pd
from io import BytesIO, StringIO
from datetime import datetime
import dateutil.parser

class CSVRenderer(BaseRenderer):
    media_type = 'text/csv'
    format = 'csv'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if not data:
            return ''
        
        if isinstance(data, dict) and 'results' in data:
            data = data['results']  # suporte para paginadores

        df = pd.DataFrame(data)

        # Parâmetros adicionais
        csv_buffer = StringIO()
        df.to_csv(
                  csv_buffer, 
                  index=False, 
                  sep=';',
                  na_rep='',
                  encoding='utf-8',
                  header=True,
                  decimal='.'
                  )  # separador ; e encoding compatível com Excel

        # df = pd.DataFrame(data)
        # csv_buffer = StringIO()
        #df.to_csv(csv_buffer, index=False)
        response = csv_buffer.getvalue()
        return response

class XLSXRenderer(BaseRenderer):
    media_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    format = 'xlsx'
    charset = None

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if not data:
            return b''

        if isinstance(data, dict):
            data = data.get('results', data)

        # Garante estrutura de lista
        if not isinstance(data, list):
            data = [data]

        # Corrige o campo datetime manualmente: transforma em string legível
        for item in data:
            if isinstance(item, dict) and "applied" in item:
                try:
                    dt = dateutil.parser.parse(item["applied"])
                    item["applied"] = dt.replace(tzinfo=None).strftime("%Y-%m-%d %H:%M:%S")
                except Exception:
                    pass

        # Garante string para listas e dicts
        for row in data:
            for key, value in row.items():
                if isinstance(value, (list, dict)):
                    row[key] = str(value)

        df = pd.DataFrame(data)

        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Consulta')

            # Ajusta largura automática das colunas
            worksheet = writer.sheets['Consulta']
            for column_cells in worksheet.columns:
                values = [str(cell.value) for cell in column_cells if cell.value is not None]
                max_length = max((len(val) for val in values), default=10)
                worksheet.column_dimensions[column_cells[0].column_letter].width = max_length + 2

        return output.getvalue()