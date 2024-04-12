from drf_standardized_errors.formatter import ExceptionFormatter
from drf_standardized_errors.types import ErrorResponse
from rest_framework import exceptions
from drf_spectacular.utils import OpenApiExample
from drf_standardized_errors.openapi import AutoSchema

class CustomExceptionFormatter(ExceptionFormatter):
    def format_error_response(self, error_response: ErrorResponse):
        errors = error_response.errors
        return {
            "errors":{
                "detalhes":[
                    {
                        "type": error_response.type,
                        "code": error.code,
                        "message": error.detail,
                        "field_name": error.attr
                    }
                    for error in errors
                ]
            }
        }
    

class CustomAutoSchema(AutoSchema):
    def get_examples(self):
        errors = [
            exceptions.APIException(),
            exceptions.ValidationError(),
            exceptions.PermissionDenied(), 
            exceptions.NotFound(),
            exceptions.ParseError(), 
            exceptions.AuthenticationFailed(),
            exceptions.NotAuthenticated(), 
            exceptions.NotAcceptable(),
            exceptions.Throttled()
        ]
        return [get_example_from_exception(error) for error in errors]


def get_example_from_exception(exc: exceptions.APIException):
    return OpenApiExample(
        exc.__class__.__name__,
        value={
            "errors": {
                "detalhes": [
                    {
                        "type": "cliente_error",
                        "code": exc.get_codes(),
                        "message": exc.detail,
                        "field_name": None
                    }
                ]
            }
        },
        response_only=True,
        status_codes=[str(exc.status_code)],
    )