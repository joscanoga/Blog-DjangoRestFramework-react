from apps.category.models import Category
from apps.category.serializers import CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.pagination import PageNumberPagination

class ListCategoriesView(APIView):
    """
    listar las cateogrias
    """
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        if Category.objects.all().exists():
            categories = Category.objects.all()
            results = []
            for category in categories:
                if not category.parent:
                    item = {}
                    item["id"]=category.id
                    item["name"]=category.name
                    item["thumbnail"]=category.thumbnail.url
                    item["subcategories"] = []
                    
                    for cat in categories:
                        if cat.parent and cat.parent.id == category.id:
                            subitem = {}
                            subitem["id"]=cat.id
                            subitem["name"]=cat.name
                            subitem["thumbnail"]=cat.thumbnail.url
                            item["subcategories"].append(subitem)
                    results.append(item)
            return Response({'categories': results}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'No categories found'}, status=status.HTTP_404_NOT_FOUND)
       

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)