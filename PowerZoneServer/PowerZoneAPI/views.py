from .models import Locale, Presa, Recensione
from .serializers import LocaleSerializer, PresaSerializer, RecensioneSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class ListaLocali(generics.ListAPIView):
    queryset = Locale.objects.all()
    serializer_class = LocaleSerializer

    def post(self, request, format=None):
        serializer = LocaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DettaglioLocale(generics.RetrieveUpdateDestroyAPIView):
    queryset = Locale.objects.all()
    serializer_class = LocaleSerializer


class ListaPrese(generics.ListAPIView):
    queryset = Presa.objects.all()
    serializer_class = PresaSerializer

    def post(self, request, format=None):
        serializer = PresaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DettaglioPresa(generics.RetrieveUpdateDestroyAPIView):
    queryset = Presa.objects.all()
    serializer_class = PresaSerializer


class ListaRecensioni(generics.ListAPIView):
    queryset = Recensione.objects.all()
    serializer_class = RecensioneSerializer

    def post(self, request, format=None):
        serializer = RecensioneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DettaglioRecensione(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recensione.objects.all()
    serializer_class = RecensioneSerializer


class RecensioniPresa(generics.ListAPIView):
    serializer_class = RecensioneSerializer

    def get_queryset(self):
        """
        Questa view ritorna la lista delle recensioni di una presa
        :return:
        """

"""
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Locale
from .serializers import LocaleSerializer


class ListaLocali(APIView):
    # ritorna tutti i locali
    def get(self,request, format=None):
        locali= Locale.objects.all()
        serializer = LocaleSerializer(locali, many=True)
        return Response(serializer.data)
    # Crea nuovo locale
    def post(self,request, format=None):
        serializer=LocaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DettaglioLocale(APIView):

    # Ricerca elemento
    def get_object(self, pk):
        try:
            return Locale.objects.get(pk=pk)
        except Locale.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        locale = self.get_object(pk)
        serializer = LocaleSerializer(locale)
        return Response(serializer.data)

    # Update locale
    def put(self, request, pk, format=None):
        locale=self.get_object(pk)
        serializer= LocaleSerializer(locale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Cancellazione locale
    def delete(self,request,pk,format=None):
        locale= self.get_object(pk)
        locale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
