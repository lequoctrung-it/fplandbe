from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response

from hello.models import Hello


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def get_name(request):
    try:
        query_set = get_object_or_404(Hello, key="name")
    except Http404 as e:
        return Response(data=e, status=status.HTTP_404_NOT_FOUND)
    return Response(data={"name": query_set.value}, status=status.HTTP_200_OK)
