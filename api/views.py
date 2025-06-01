from django.shortcuts import render

# Create your views here.
from django.db import connections
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework import status
import pandas as pd
from django.http import HttpResponse
from .permissions import RequireGroup

from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from .renderers import CSVRenderer, XLSXRenderer
import os
from django.conf import settings
#from .custom_permission import IsConsultaUser

class IsInConsultaGroup(BasePermission):
    def has_permission(self, request, view):
        #print(f"Usuário: {request.user}")
        #print(f"Autenticado? {request.user.is_authenticated}")
        #print(f"Grupos: {[g.name for g in request.user.groups.all()]}")
        #print("grupos:", list(request.user.groups.values_list("name", flat=True)))
        return (
                request.user and 
                request.user.is_authenticated and 
                request.user.groups.filter(name="Consulta").exists()
                
        )


class ConsultaSQLView(APIView):
     
    # permission_classes = [IsAuthenticated, IsConsultaUser]
    permission_classes = [IsAuthenticated, IsInConsultaGroup]
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer, CSVRenderer, XLSXRenderer]
    # permission_classes = [type("ConsultaPermission", (RequireGroup,), {"required_group": "Consulta"})]


    def get(self, request):
        # 🗂️ Caminho do arquivo SQL
        sql = os.path.join(settings.BASE_DIR, 'api', 'sql', 'consulta_migracoes.sql')

        with open(sql, 'r', encoding='utf-8') as f:
            sql_query = f.read()

        with connections['readonly'].cursor() as cursor:
            cursor.execute(sql_query)
            columns = [col[0] for col in cursor.description]

            results = cursor.fetchall()

        #df = pd.DataFrame(results, columns=columns)

        data = [dict(zip(columns, row)) for row in results]

        response = Response(data)

        # 👉 Define o nome do arquivo, se for exportação
        export_format = request.query_params.get('format')
        filename = request.query_params.get('filename', 'consulta')

        if export_format == 'csv':
            response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'
        elif export_format == 'xlsx':
            response['Content-Disposition'] = f'attachment; filename="{filename}.xlsx"'

        return response
        #return Response(df.to_dict(orient="records"), status=status.HTTP_200_OK)