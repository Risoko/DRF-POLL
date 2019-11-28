from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Choice, Question

class QuestionSerializer(serializers.ModelSerializer):
    choices = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date', 'choices']


class ChoiceSerializerMain(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Choice
        fields = ['id', 'url', 'question', 'choice_text', 'votes']


class ChoiceSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['question', 'choice_text']


class ChoiceSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['choice_text']


class VoteSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["id", 'choice_text']


class VoteSerializerVotes(serializers.Serializer):
    choice = serializers.IntegerField()
        
    def save(self, choice_object):
        choice_object.votes += 1
        choice_object.save()




    