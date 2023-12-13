from drf_yasg import openapi


default_and_date_params = [
            openapi.Parameter('date_from', openapi.IN_QUERY, description="Start date", type=openapi.TYPE_STRING),
            openapi.Parameter('date_to', openapi.IN_QUERY, description="End date", type=openapi.TYPE_STRING),
            openapi.Parameter('category', openapi.IN_QUERY, description="Category id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('region', openapi.IN_QUERY, description="Region id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('district', openapi.IN_QUERY, description="District id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('organization', openapi.IN_QUERY, description="Organization id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('social_type', openapi.IN_QUERY, description="Social type id", type=openapi.TYPE_INTEGER),
        ]


filter_default_params = [
            openapi.Parameter('category', openapi.IN_QUERY, description="Category id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('region', openapi.IN_QUERY, description="Region id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('district', openapi.IN_QUERY, description="District id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('organization', openapi.IN_QUERY, description="Organization id", type=openapi.TYPE_INTEGER),
            openapi.Parameter('social_type', openapi.IN_QUERY, description="Social type id", type=openapi.TYPE_INTEGER),
        ]