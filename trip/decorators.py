from rest_framework.response import Response
from rest_framework.views import status


def validate_request_data(fn):
    """
      this function is to valida update input,
      but exist some libs to do this.
      #TODO improve this code
    """
    def decorated(*args, **kwargs):
        classification = args[0].request.data.get("classification", "")
        rate = args[0].request.data.get("rate", "")
        if rate and not classification:
            return Response(
                data={
                    "message": "You need to pass rate or classification"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if rate and rate not in [1, 2, 3, 4, 5]:
            return Response(
                data={
                    "message": "Rate is invalid, please use number between 1 and 5" # noqa
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        if classification and classification not in [1, 2, 3, 4]:
            return Response(
                data={
                    "message": "Classifications invalid"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)

    return decorated
