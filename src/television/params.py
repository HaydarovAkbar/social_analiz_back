from drf_yasg import openapi

file_input_params = [
    openapi.Parameter('file', openapi.IN_BODY, description="Choose file", type=openapi.TYPE_FILE, required=True),
    # openapi.Parameter('organiztion', openapi.IN_BODY, description="Start date", type=openapi.TYPE_INTEGER,
    #                   required=True),
    # openapi.Parameter('post_date', openapi.IN_BODY, description="Post date", type=openapi.TYPE_STRING, required=True),
    # openapi.Parameter('television_type', openapi.IN_BODY, description="Television type", type=openapi.TYPE_INTEGER,
    #                   required=True),
    # openapi.Parameter('content', openapi.IN_BODY, description="Content", type=openapi.TYPE_STRING),
]
