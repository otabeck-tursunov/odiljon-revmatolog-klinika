from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.serializers import *

from .models import *

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenObtainPairSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'role': self.user.last_name})
        data.update({"token": data.pop('access')})
        # and everything else you want to send in the response
        return data

class BemorSerializer(ModelSerializer):
    class Meta:
        model = Bemor
        fields = '__all__'

    def to_representation(self, instance):
        data = super(BemorSerializer, self).to_representation(instance)
        hozirgi_bemor = Bemor.objects.get(id=data.get('id'))
        joylashishlar = Joylashtirish.objects.filter(bemor_id=hozirgi_bemor)
        serializer_ = JoylashtirishSerializer(joylashishlar, many=True)
        tolovlari = Tolov.objects.filter(bemor_id=hozirgi_bemor)
        serializer = TolovReadBemorUchun(tolovlari, many=True)
        data.update({'tolovlar': serializer.data, 'joylashishlar': serializer_.data})
        return data

class YollanmaSerializer(ModelSerializer):
    class Meta:
        model = Yollanma
        fields = '__all__'

    def to_representation(self, instance):
        data = super(YollanmaSerializer, self).to_representation(instance)
        subs = SubYollanma.objects.filter(yollanma_id=instance)
        ser = SubYollanmaSerializer(subs, many=True)
        data.update({"subyollanmalar": ser.data})
        return data

class SubYollanmaSerializer(ModelSerializer):
    class Meta:
        model = SubYollanma
        fields = '__all__'

class TolovSerializer(ModelSerializer):
    class Meta:
        model = Tolov
        fields = '__all__'

class XonaSerializer(ModelSerializer):
    class Meta:
        model = Xona
        fields = '__all__'

class JoylashtirishSerializer(ModelSerializer):
    class Meta:
        model = Joylashtirish
        fields = '__all__'

class JoylashtirishReadSerializer(ModelSerializer):
    xona_id = XonaSerializer(read_only=True)
    class Meta:
        model = Joylashtirish
        fields = '__all__'

class TolovReadSerializer(ModelSerializer):
    subyollanma_idlar = SubYollanmaSerializer(read_only=True, many=True)
    yollanma_id = YollanmaSerializer(read_only=True)
    joylashtirish_id = JoylashtirishReadSerializer(read_only=True)
    class Meta:
        model = Tolov
        fields = '__all__'

class TolovReadBemorUchun(ModelSerializer):
    yollanma_id = YollanmaSerializer(read_only=True)
    subyollanma_idlar = SubYollanmaSerializer(read_only=True, many=True)
    class Meta:
        model = Tolov
        fields = '__all__'

class XulosaSerializer(ModelSerializer):
    class Meta:
        model = Xulosa
        fields = '__all__'

class XulosaReadSerializer(ModelSerializer):
    tolov_id = TolovReadSerializer(read_only=True)
    class Meta:
        model = Xulosa
        fields = '__all__'


class TolovQaytarishSerializer(ModelSerializer):
    class Meta:
        model = TolovQaytarish
        fields = '__all__'

class TolovPatchLab(Serializer):
    xulosa_holati = serializers.CharField(allow_blank=True, allow_null=True)

class TolovPatchChegirma(Serializer):
    chegirma = serializers.IntegerField()

class TolovPatch(Serializer):
    tolov_qaytarildi = serializers.BooleanField(allow_null=True, default=False)
    izoh = serializers.CharField(allow_blank=True, allow_null=True)

class UserReadSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id",'username', 'password', "first_name"]

    def to_representation(self, instance):
        data = super(UserReadSerializer, self).to_representation(instance)
        hozirgi_user = User.objects.get(username=data.get('username'))
        data.update({'role': hozirgi_user.last_name})
        return data

class UserSerializer(Serializer):
    username = serializers.CharField(max_length=30)
    password = serializers.CharField(max_length=30)
    ism_familiya = serializers.CharField(max_length=30)
    role = serializers.CharField(max_length=30)

class ChekSerializer(ModelSerializer):
    class Meta:
        model = Chek
        fields = '__all__'

class YollanmaReadSerializer(ModelSerializer):
    class Meta:
        model = Yollanma
        fields = '__all__'

class TolovAdminSerializer(ModelSerializer):
    joylashtirish_id = JoylashtirishReadSerializer()
    yollanma_id = YollanmaReadSerializer()
    class Meta:
        model = Tolov
        fields = '__all__'

    def to_representation(self, instance):
        data = super(TolovAdminSerializer, self).to_representation(instance)
        data.update({'ism': instance.bemor_id.ism, 'familiya': instance.bemor_id.familiya,
                     "tel": instance.bemor_id.tel})
        return data

class BemorMaxsus(ModelSerializer):
    class Meta:
        model = Bemor
        fields = ['id','ism', 'familiya']

class JoylashtirishMaxsusSerializer(ModelSerializer):
    bemor_id = BemorMaxsus()
    class Meta:
        model = Joylashtirish
        fields = '__all__'

    def to_representation(self, instance):
        data = super(JoylashtirishMaxsusSerializer, self).to_representation(instance)
        tolov = Tolov.objects.get(joylashtirish_id__id=data.get("id"))
        serializer = TolovSerializer(tolov)
        data.update({"tolovi": serializer.data})
        return data

class XonaJoylashuvlariSerializer(ModelSerializer):
    class Meta:
        model = Xona
        fields = '__all__'

    def to_representation(self, instance):
        data = super(XonaJoylashuvlariSerializer, self).to_representation(instance)
        joylashishlar = Joylashtirish.objects.filter(ketish_sanasi__isnull=True, xona_id__id=data.get("id"))
        joy = JoylashtirishMaxsusSerializer(joylashishlar, many=True)
        data.update({"joylashtirishlar": joy.data})
        return data

