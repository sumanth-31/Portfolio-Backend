from django.core import serializers

def object_to_dictionary(obj):
    return serializers.serialize("python",[obj,])[0]
