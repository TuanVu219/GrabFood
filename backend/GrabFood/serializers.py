from rest_framework import serializers
from .models import User, Role,Customer,Restaurant,TypeFood,MenuFood,ReviewMenu,Shipper,Cart,CartItem,FavoriteMenu,Voucher
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirmation = serializers.CharField(write_only=True, required=True)
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirmation', 'role','email','first_name','last_name')

    def validate(self, data):
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Passwords must match.")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        
        role = validated_data.pop('role', None) or Role.objects.filter(role_name="Customer").first()
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            role=role,

        )

    
        customer = Customer.objects.create(user=user)
        if role:
            user.role = role
        
        user.save()
        customer.save()
        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("username","password","email","first_name","last_name")
        
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("id","username","password")
        

class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name', allow_blank=True, required=False)
    last_name = serializers.CharField(source='user.last_name', allow_blank=True, required=False)
    email = serializers.EmailField(source='user.email', allow_blank=True, required=False)
    class Meta:
        model=Customer
        fields=("age","phone","address","email","first_name","last_name")
        
class RegisterRestaurant(serializers.ModelSerializer):
    class Meta:
        model=Restaurant
        fields=("user","restaurant_name","phone_restaurant","address_restaurant")

class Serializer_FoodType(serializers.ModelSerializer):
    class Meta:
        model=TypeFood
        fields=("type_name",)

class Serializer_Menu(serializers.ModelSerializer):
    food_type = serializers.PrimaryKeyRelatedField(queryset=TypeFood.objects.all())
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    class Meta:
        model=MenuFood
        fields=("restaurant","price","food_type","food_name")

class Serializer_ReviewMenu(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    menu = serializers.PrimaryKeyRelatedField(queryset=MenuFood.objects.all())
    class Meta:
        model=ReviewMenu
        fields=("user","menu","rating","comments")

class Serializer_Shipper(serializers.ModelSerializer):
    class Meta:
        model=Shipper
        fields=('user','age','cccd','license_plate','address','phone','vehicle')
class Serializer_Cart(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=('restaurant','customer','created_at','updated_at')
class Serializer_CartItem(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=('cart','food','quantity')
class Serializer_FavouriteMenu(serializers.ModelSerializer):
    class Meta:
        model=FavoriteMenu
        fields=('customer','menu')
class Serializer_Voucher(serializers.ModelSerializer):
    class Meta:
        model=Voucher
        fields=('restaurant','value','minimum_order_value','expiration_date')