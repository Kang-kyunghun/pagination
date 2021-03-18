import json

from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from .models                import Product

class ProductsView(View):   
    def get(self, request):    
        offset = int(request.GET.get("offset",0))
        limit  = int(request.GET.get("limit",141))
        
        products = Product.objects.all()
        data = {
            "count"  : products.count(),
            "result" : [{
                            "id"          : product.id,
                            "name"        : product.name,
                            "image_url"   : product.image_url,
                            "description" : product.description
                        } for product in products[offset:offset+limit]]
        }
        
        return JsonResponse({'products': data}, status=200)
