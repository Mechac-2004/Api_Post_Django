from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from post.models import Comment, Post
from post.serializers import CommentSerializer

class CommentView(APIView):
    def get(self, request):
        comment = Comment.objects.all()
        serializer = CommentSerializer(comment, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
           serializer.save() 
           return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CommentDetailView(APIView):
    def get(self, request, pk):
        comment = Comment.objects.all(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        comment = Comment.objects.all(pk=pk)

        # Vérifie si l'utilisateur est l'auteur du commentaire.
        if comment.author != request.user:
            return Response({"detail": "Vous n'êtes pas autorisé à modifier ce commentaire."},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        comment = Comment.objects.all(pk=pk)

        # Vérifie la permission.
        if comment.author != request.user:
            return Response({"detail": "Vous n'êtes pas autorisé à modifier ce commentaire."},
                            status=status.HTTP_403_FORBIDDEN)
                            
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        comment = Comment.objects.all(pk=pk)

        # Vérifie la permission.
        if comment.author != request.user:
            return Response({"detail": "Vous n'êtes pas autorisé à supprimer ce commentaire."},
                            status=status.HTTP_403_FORBIDDEN)
                            
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
