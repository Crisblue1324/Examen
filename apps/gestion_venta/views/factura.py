from django.http import JsonResponse
from django.urls import reverse_lazy
from apps.gestion_venta.forms.factura import FacturaForm
from apps.gestion_venta.models import Factura, DetalleFactura, Producto
from apps.security.mixins.mixins import ListViewMixin,CreateViewMixin,UpdateViewMixin,DeleteViewMixin,PermissionMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
import json

class FacturaListView(PermissionMixin,ListViewMixin,ListView):
    model: Factura
    template_name = 'facturas/list.html'
    context_object_name = 'facturas'
    permission_required="view_factura"
    # paginate_by = 3
    # query=None
    
    def get_queryset(self):
        return self.model.objects.all().order_by('id')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Facturas'
        context['create_url'] = reverse_lazy('gestion_venta:factura_create')
        context['permission_add'] = context['permissions'].get('add_factura','')
        return context
    
class FacturaCreateView(PermissionMixin,CreateViewMixin,CreateView,):
    model = Factura
    template_name = 'facturas/form.html'
    form_class = FacturaForm
    success_url = reverse_lazy('gestion_venta:factura_list')
    permission_required="add_factura"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Factura'
        context['back_url'] = self.success_url
        context['productos'] = Producto.objects.all().order_by('id')
        context['detail_producto'] =[]
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.get_form()
        #data = form.save(commit=False)
        if not form.is_valid():
            print("form:",form.errors) 
            return JsonResponse({},status=400)
        data = request.POST
        cliente_id = data['cliente']
        fecha = data['fecha']
        subtotal = data['subtotal']
        iva = data['iva']
        total = data['total']
        cabecera = Factura.objects.create(
            cliente_id=cliente_id,
            fecha=fecha,
            subtotal=subtotal,
            iva=iva,
            total=total,
        )
        details = json.loads(request.POST['detail'])
        for detail in details:
            DetalleFactura.objects.create(
                factura_id=cabecera.id,
                producto_id=detail['id_producto'],
                cantidad=detail['cant'],
                precio=detail['prec'],
                subtotal=detail['subtotal']
            )
        return JsonResponse({'id':cabecera.id})
    
class FacturaUpdateView(PermissionMixin,UpdateViewMixin,UpdateView):
    model = Factura
    template_name = 'facturas/form.html'
    form_class = FacturaForm
    success_url = reverse_lazy('gestion_venta:factura_list')
    permission_required="change_factura"
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Factura'
        context['back_url'] = self.success_url
        return context
    
class FacturaDeleteView(PermissionMixin,DeleteViewMixin,DeleteView):
    model = Factura
    success_url = reverse_lazy('gestion_venta:factura_list')
    permission_required="delete_factura"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Eliminar Factura'
        context['back_url'] = self.success_url
        return context