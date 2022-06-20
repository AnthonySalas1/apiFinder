from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    lastname = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    category = serializers.ChoiceField(choices=User.CATEGORIES_CHOICES)
    release_date = serializers.DateField()
    

    def create(self, validated_data):
        """
        Create and return a new `Serie` instance, given the validated data.
        """
        return User.objects.create(**validated_data)


    def update(self, instance, validated_data):
        """
        Update and return an existing `Serie` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.lastname = validated_data.get('lastname', instance.lastname)
        instance.age = validated_data.get('age', instance.age)
        instance.category = validated_data.get('category', instance.category)
        instance.release_date = validated_data.get(
            'release_date', instance.release_date)
        instance.save()
        return instance
