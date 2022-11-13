from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UploadfileSerializer
from rest_framework import status
from rest_framework.decorators import action
from .utils import (
    handle_uploaded_file,
    one_rendom_line,
    long_hundred_lines,
    fetch_random_line,
    twenty_longestline,
)


class UploadViewSet(viewsets.GenericViewSet):
    serializer_class = UploadfileSerializer

    def create(self, request):
        serializer_class = UploadfileSerializer(data=request.data)
        if "file" not in request.FILES or not serializer_class.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            files = request.FILES.getlist("file")

            for f in files:
                handle_uploaded_file(f)

            return Response("Files Uploaded!", status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["get"])
    def one_rendomline(self, request):
        response = one_rendom_line()
        return Response(response, status=status.HTTP_200_OK)

    @action(detail=False, methods=["post"])
    def one_rendomline_backward(self, request):
        line_number = request.data["line_number"]
        response = fetch_random_line(line_number)
        return Response(response, status=status.HTTP_202_ACCEPTED)

    @action(detail=False, methods=["get"])
    def longest_hundred_lines(self, request):
        response = long_hundred_lines()
        return Response(response, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def twenty_longestline_onefile(self, request):
        response = twenty_longestline()
        return Response(response, status=status.HTTP_200_OK)
