from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Choice, Question
from .serializers import (QuestionSerializer, ChoiceSerializerMain, ChoiceSerializerCreate, 
                          ChoiceSerializerUpdate, VoteSerializerDetail, VoteSerializerVotes)

class QuestionViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class =  QuestionSerializer

    @action(methods=['GET', 'PUT'], detail=True)
    def vote(self, request, *args, **kwargs):
        pk_question = get_object_or_404(Question, pk=self.get_object().pk)
        if request.method == 'GET':
            all_choices = Choice.objects.filter(question=pk_question)
            serializer = VoteSerializerDetail(instance=all_choices, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'PUT':
            serializer = VoteSerializerVotes(data=request.data)
            if serializer.is_valid():
                choice_object = get_object_or_404(
                    klass=Choice, 
                    id=request.data['choice'], 
                    question=pk_question
                )
                serializer.save(choice_object=choice_object)
                return Response(status=status.HTTP_200_OK)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_serializer_class(self):
        if self.action == 'vote':
            return VoteSerializerVotes
        return super().get_serializer_class()

        

class ChoiceViewSet(ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializerMain

    def get_serializer_class(self):
        if self.action == 'create':
            return ChoiceSerializerCreate
        elif self.action == 'update':
            return ChoiceSerializerUpdate
        return self.serializer_class

        



