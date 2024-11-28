from rest_framework import serializers
from accounts.models import CustomUser
from .models import ContractType, Function, Question, Skill, Extra, Vacancy, Language, ApplyVacancy


class ContractTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractType
        fields = ['contract_type']


class FunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Function
        fields = ['function']


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['language']


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill', 'category']


class ExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extra
        fields = ['extra']


class VacancySerializer(serializers.ModelSerializer):
    contract_type = serializers.PrimaryKeyRelatedField(queryset=ContractType.objects.all(), many=False)
    function = serializers.PrimaryKeyRelatedField(queryset=Function.objects.all(), many=False)
    skill = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), many=True)
    language = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all(), many=True)

    class Meta:
        model = Vacancy
        fields = ['title', 'contract_type', 'function', 'location', 'skill', 'week_day', 'salary', 'description',
                  'language', 'question']


class ApplySerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all(), many=False)
    vacancy = serializers.PrimaryKeyRelatedField(queryset=Vacancy.objects.all(), many=False)

    class Meta:
        model = ApplyVacancy
        fields = ['user', 'vacancy']
