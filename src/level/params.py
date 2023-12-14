from drf_yasg import openapi

get_level = [
            openapi.Parameter('level', openapi.IN_QUERY, description="Level id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('organization', openapi.IN_QUERY, description="Organization id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('date_from', openapi.IN_QUERY, description="Start date", type=openapi.TYPE_STRING),
            openapi.Parameter('date_to', openapi.IN_QUERY, description="End date", type=openapi.TYPE_STRING),
            openapi.Parameter('region', openapi.IN_QUERY, description="Region id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('district', openapi.IN_QUERY, description="District id", type=openapi.TYPE_INTEGER),
        ]