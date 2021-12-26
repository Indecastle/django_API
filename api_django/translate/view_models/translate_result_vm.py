from rest_framework import serializers


# class LanguageVM:
#     text = serializers.CharField(max_length=500)


class LanguageSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=500)
