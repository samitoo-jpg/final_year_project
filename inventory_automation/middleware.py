import json
import logging
from django.http import JsonResponse
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)

# Middleware to catch unhandled exceptions in Django
class CustomExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
            return response
        except Exception as e:
            logger.error(f"Unhandled error: {str(e)}", exc_info=True)
            return JsonResponse({"error": "Internal Server Error"}, status=500)

# DRF Custom Exception Handler
def custom_exception_handler(exc, context):
    """
    Custom exception handler for DRF.
    """
    response = exception_handler(exc, context)

    if response is not None:
        response.data['error_message'] = str(exc)  # Add error message to response

    return response

