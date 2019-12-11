from .models import Student
#from .models import collageCareer


from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# class collegeCareerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=collageCareer
#         fields='__all__'
