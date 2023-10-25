from rest_framework import serializers

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """Сериализатор для модели пользователя"""
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email')


class CustomUserCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания нового пользователя"""
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email',
                  'first_name', 'last_name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            }
        }

    def validate_password(self, password):
        """Проверка длины пароля"""
        if len(password) < 8:
            raise serializers.ValidationError(
                'Пароль должен быть не меньше 8 символов')
        return password
