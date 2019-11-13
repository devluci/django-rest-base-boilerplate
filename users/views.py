from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response


@permission_classes((IsAuthenticated,))
def about_me(request: Request) -> Response:
    return Response(request.user.attribute, status=status.HTTP_200_OK)
