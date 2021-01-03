def get_absolute_uri(request, file_field):
    field_raw_url = file_field.url
    field_url = request.build_absolute_uri(field_raw_url)
    return field_url
