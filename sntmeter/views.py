from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse,JsonResponse
from django.utils.timezone import localtime
from rest_framework import viewsets
import pandas as pd
from openpyxl import Workbook
from .models import Meter,Con_method,Model,Vendor
from . forms import MeterForm
from .serializers import MeterSerializer,ConMethodSerializer,ModelSerializer,VendorSerializer
from . import lectura

# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def home(request):
    return render(request, 'home.html',{})

#crear folder views para tener views normales y views ajax, en ajax poner la accion de lectura
#la accion de lectura debe estar con objeto meter y direccionado a lectura.py
@login_required
def meter(request):
    if request.method == 'GET':
        medidores = Meter.objects.all().order_by('name')
        return render(request, 'sntmeter/meter.html', {'medidores':medidores,})
    else: return home(request)
    
def ajax_ver_med(request):
    if is_ajax(request=request):
        if request.method == 'POST':
            meter_name = request.POST.get('meter')
            medidor = Meter.objects.get(name = meter_name)
            hist = medidor.history.all()
            return render(request,'sntmeter/response_ver.html', {'historial':hist})
        else:return JsonResponse({'msg':'Metodo invalido'})
    else:return JsonResponse({'msg':'Metodo invalido'})
    
def ajax_lectura_simple(request):
    if is_ajax(request=request):
        if request.method == 'POST':
            meter_name = request.POST.get('meter')
            medidor = Meter.objects.get(name = meter_name)
            hist = medidor.history.last()
            medidor = lectura.simple_de_medidor(medidor)
            medidor.save()
            medidorl = Meter.objects.get(name = meter_name)
            return render(request,'sntmeter/response.html', {'medidor':medidorl,'hist':hist})
        else:return JsonResponse({'msg':'Metodo invalido'})
    else:return JsonResponse({'msg':'Metodo invalido'})

def ajax_editar_med(request, name):
    medidor = get_object_or_404(Meter, name = name )
    if is_ajax(request=request):
        if request.method == 'POST':
            form = MeterForm(request.POST, instance=medidor)
            if form.is_valid():
                form.save()
                return JsonResponse({'success': True})
        else:
            form = MeterForm(instance=medidor)
            return render(request, 'sntmeter/edit_med.html', {'form': form})
    else:return JsonResponse({'msg':'Metodo invalido'})
    return home(request)

def ajax_nuevo_med(request):
    if is_ajax(request=request):
        if request.method == 'POST':
            form = MeterForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'success': True})
        else:
            form = MeterForm()
            return render(request, 'sntmeter/new_med.html', {'form': form})
    else:return JsonResponse({'msg':'Metodo invalido'})
    return home(request)

def ajax_quitar_med(request):
    if is_ajax(request=request):
        if request.method == 'POST':
            meter_name = request.POST.get('meter_name')
            medidor = Meter.objects.get(name = meter_name)
            medidor.delete()
            return JsonResponse({'success': True})
        else:return JsonResponse({'msg':'Metodo invalido'})
    else:return JsonResponse({'msg':'Metodo invalido'})



def report(request):
    if request.method == 'POST':
        medidores = request.POST.getlist('medidores')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        # Lógica para generar el reporte personalizado (como se explicó anteriormente)
        # Obtener las lecturas filtradas
        lecturas = Meter.history.filter(
            id__in=medidores, 
            history_date__range=(fecha_inicio, fecha_fin)
        )
        for lectura in lecturas:
            lectura.history_date = lectura.history_date.strftime("%Y-%m-%d %H:%M")

            print(lectura.history_date)
        
        # Crear el DataFrame de pandas
            df = pd.DataFrame(lecturas.values())

            # Crear el libro de trabajo de Excel
            workbook = Workbook()
            sheet = workbook.active
            sheet.title = "Reporte Personalizado"

            # Escribir el DataFrame al archivo Excel
            sheet.append(list(df.columns))
            for index, row in df.iterrows():
                sheet.append(row.tolist())

            # Crear la respuesta HTTP
            response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = f'attachment; filename="reporte_personalizado_{fecha_inicio}_{fecha_fin}.xlsx"'


            # Guardar el libro de trabajo en la respuesta
            workbook.save(response)

        return response
    else:
        medidores = Meter.objects.all()
        return render(request, 'sntmeter/report.html', {'medidores': medidores})




def reporte_mensual(request, anio, mes):
    # Obtener todas las lecturas del mes
    lecturas = Meter.history.filter(history_date__year=anio, history_date__month=mes)

    # Crear un DataFrame de pandas
    df = pd.DataFrame(lecturas.values())

    # Crear el libro de trabajo de Excel
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = f"Reporte Mensual {anio}-{mes}"

    # Escribir el DataFrame al archivo Excel
    sheet.append(list(df.columns))
    for index, row in df.iterrows():
        sheet.append(row.tolist())

    # Crear la respuesta HTTP
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="reporte_mensual_{anio}_{mes}.xlsx"'
    
    workbook.save(response)
    return response

#ViewSets---------------------------------

class MeterViewSet(viewsets.ModelViewSet):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer

class ConMethodViewSet(viewsets.ModelViewSet):
    queryset = Con_method.objects.all()
    serializer_class = ConMethodSerializer

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

#Custom API para obtener los medidores segun su tipo de
#conexion, solo hay tres opciones hdlc, serial, tcp
def medidor_con(request,con):
    try:
        print(con)
        medidores = Meter.objects.filter(con_method__type__icontains=con)
        serializer = MeterSerializer(medidores, many=True)
        print(serializer.data)
        return JsonResponse({'medidores': serializer.data}, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, safe=False, status=500)