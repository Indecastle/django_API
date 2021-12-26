import coreapi
import coreschema
from drf_yasg import openapi
from drf_yasg.openapi import Schema
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.schemas import AutoSchema
from rest_framework.views import APIView

from .view_models.translate_result_vm import LanguageSerializer

from deep_translator import GoogleTranslator
# Translator = GoogleTranslator(source='auto', target='ru')
# translated = GoogleTranslator(source='auto', target='de').translate("keep it up, you are awesome")  # output -> Weiter so, du bist großartig



class DeviceViewSchema(AutoSchema):
    """
    Schema customizations for DeviceViewSet
    """

class TranslateView(APIView):
    schema = DeviceViewSchema()

    #param_get_source = openapi.Parameter('source', in_=openapi.IN_QUERY, description='source language', type=openapi.TYPE_STRING, required=True )
    param_get_source = openapi.Parameter('source', openapi.IN_QUERY, 'source language', type=openapi.TYPE_STRING, required=True)
    param_get_target = openapi.Parameter('target', openapi.IN_QUERY, 'target language', type=openapi.TYPE_STRING, required=True)
    param_get_text = openapi.Parameter('text', openapi.IN_QUERY, 'text to translate', type=openapi.TYPE_STRING, required=True)
    user_response = openapi.Response('response description', LanguageSerializer)

    @swagger_auto_schema(manual_parameters=[param_get_source, param_get_target, param_get_text], responses={200: user_response})
    @action(detail=True, methods=['get'])
    def get(self, request):
        source = request.query_params.get('source')
        target = request.query_params.get('target')
        text = request.query_params.get('text')

        translated = GoogleTranslator(source='auto', target=target).translate(text)

        result = {"text": translated}
        serializer = LanguageSerializer(result, many=False)
        return Response(serializer.data)


    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'source': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'target': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
            'text': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        },
        responses={
            status.HTTP_200_OK: Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'text': Schema(
                        type=openapi.TYPE_STRING
                    )
                }
            )
        }
    ))
    @action(detail=True, methods=['post'])
    def post(self, request):
        source = request.data.get('source')
        target = request.data.get('target')
        text = request.data.get('text')

        translated = GoogleTranslator(source='auto', target=target).translate(text)

        result = {"text": translated}
        serializer = LanguageSerializer(result, many=False)
        return Response(serializer.data)

