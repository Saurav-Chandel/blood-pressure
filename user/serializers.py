from rest_framework import serializers
from .models import *
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import (
    DjangoUnicodeDecodeError,
    force_str,
    smart_bytes,
    smart_str,
)

from buisness.models import Buisness
from buisness.serializers import BuisnessSerializer

class UserSignupSerializer(serializers.ModelSerializer):
    # buisness_owner=BuisnessSerializer(read_only=True)
    class Meta:
        model=User
        fields="__all__"

    # def validate(self,validated_data):
    #     username = validated_data.get('username')
    #     password = validated_data.get('password')

    #     if 
  

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            user_type=validated_data['user_type']
        )
        user.set_password(validated_data['password'])
        user.save()
        print(user)
        print(user.user_type.id)

        if user.user_type.id==2:
           print("___________")
           profile_obj=Profile.objects.create(user_id=user)
           profile_obj.save()

        if user.user_type.id==3:
            buisness_obj=Buisness.objects.create(buisness_owner=user)
            buisness_obj.save()
        
        return user

        # if User.objects.get(user_type__role="buisness",id=):
        #    print("______________")
        #    buisness_obj=Buisness.objects.create(buisness_owner=user)
        #    buisness_obj.save()
        # return user   

    # def create(self,validated_data):
    #     u=User.objects.create_user(**validated_data)
    #     return u

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model=User
#         fields = "__all__"
#         # fields=("email","password")
#         extra_kwargs = {
#             "password": {"write_only": True},
#         }         

class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True
    )
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ["password", "token", "uidb64"]

    def validate(self, attrs):
        try:
            password = attrs.get("password")
            token = attrs.get("token")
            uidb64 = attrs.get("uidb64")
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
  
                raise AuthenticationFailed("The reset link is invalid", 401)

            user.set_password(password)
            user.save()

            return user
        except Exception as e:

            raise AuthenticationFailed("The reset link is invalid", 401)
        return super().validate(attrs)


class TeamScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeamScore
        fields="__all__"



class ProfileSerializer(serializers.ModelSerializer):
    # user_id=UserSerializer(read_only=True)
    class Meta:
        model=Profile
        fields="__all__"
        # exclude=""


class UserSerializer(serializers.ModelSerializer):
    profile=ProfileSerializer()
    class Meta:
        model=User
        fields = "__all__"
        # exclude=('last_login',)
        # fields=("email","password")
        extra_kwargs = {
            "password": {"write_only": True},
        }         

class UserTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model=UserType
        fields = ("role",)

class UserSerializer1(serializers.ModelSerializer):
    user_type=UserTypeSerializer()
    class Meta:
        model=User
        fields = ("user_type",)
        # exclude=('last_login',)
        # fields=("email","password")
        extra_kwargs = {
            "password": {"write_only": True},
        } 


class Team1PlayerSerializer(serializers.ModelSerializer):
    # player=ProfileSerializer(read_only=True)

    class Meta:
        model=Team1Players
        fields="__all__"

class Team2PlayerSerializer(serializers.ModelSerializer):
    # player=ProfileSerializer(read_only=True)
    
    class Meta:
        model=Team2Players
        fields="__all__"    


#this serializer is used with create or update hostmatch API's.
class HostMatchSerializer(serializers.ModelSerializer):
    # user_id=ProfileSerializer(read_only=True)
    class Meta:
        model=HostMatch
        fields="__all__"   

    
    # def update(self, instance, validated_data):
    #     instance.hostmatch = validated_data.get('hostmatch', instance.hostmatch)
    #     return instance


#this serializer is used by get hostmatch list or get hostmatch by id  API's.
class GetHostMatchSerializer(serializers.ModelSerializer):
    # host_player_1=Team1PlayerSerializer(read_only=True,many=True)
    # host_player_2=Team2PlayerSerializer(read_only=True,many=True)
    
    # hostmatch=HostInvitationSerializer(many=True)
    host_score=TeamScoreSerializer(read_only=True,many=True)
    class Meta:
        model=HostMatch
        fields="__all__"

class HostInvitationSerializer(serializers.ModelSerializer):


    # hostmatch_id=GetHostMatchSerializer(read_only=True)      
    # user_invited=ProfileSerializer(read_only=True)
    class Meta:
        model=HostInvitation
        fields="__all__"


class TeamScoreSerializer(serializers.ModelSerializer):
    # host_match=GetHostMatchSerializer(read_only=True)
    
    class Meta:
        model=TeamScore
        fields="__all__"


class GetProfileSerializer(serializers.ModelSerializer):
    total_host_match=serializers.SerializerMethodField(method_name='total_hostmatch')
    hostmatch_profile=HostMatchSerializer(read_only=True,many=True)
    user_id=UserSerializer(read_only=True)
    class Meta:
        model=Profile
        fields="__all__"

    def total_hostmatch(self,obj):
        queryset = HostMatch.objects.filter(user_id=obj.id).count()   
        return queryset 

    # def update(self,)   



    
class ContactUsSerializer(serializers.ModelSerializer):
    user_id=UserSerializer1()
    class Meta:
        model=ContactUs
        fields="__all__"
    def create(self,validated_data):
        C=ContactUs.objects.create(**validated_data)
        return C        

class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AboutUs
        fields="__all__"
    def create(self,validated_data):
        C=AboutUs.objects.create(**validated_data)
        return C 


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification
        fields="__all__"
          