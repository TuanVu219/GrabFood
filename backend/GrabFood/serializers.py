from rest_framework import serializers
from .models import User, Role,Customer,Restaurant,TypeFood,MenuFood,ReviewMenu,Shipper
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirmation = serializers.CharField(write_only=True, required=True)
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'password_confirmation', 'role')

    def validate(self, data):
        # Kiểm tra nếu mật khẩu và xác nhận mật khẩu khớp
        if data['password'] != data['password_confirmation']:
            raise serializers.ValidationError("Passwords must match.")
        return data
    
    def create(self, validated_data):
        # Xóa trường 'password_confirmation' vì không cần lưu vào database
        validated_data.pop('password_confirmation')
        
        # Lấy các giá trị từ validated_data
        role = validated_data.pop('role', None) or Role.objects.filter(role_name="Customer").first()
        # Tạo người dùng mới với mật khẩu đã được mã hóa
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            role=role,

        )
        if Customer.objects.filter(phone=validated_data.get('phone')).exists():
            raise serializers.ValidationError("This phone number is already registered.")
    
         # Tạo đối tượng Customer cho người dùng mới (nếu không có số điện thoại trùng lặp)
        customer = Customer.objects.create(user=user)
        # Gán vai trò nếu có
        if role:
            user.role = role
        
        # Lưu người dùng
        user.save()
        customer.save()
        return user
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("username","password")
        
class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("id","username","password")
        

class CustomerSerializer(serializers.ModelSerializer):
    name=serializers.CharField(source='user.first_name',allow_blank=True,required=False)
    class Meta:
        model=Customer
        fields=("name","age","phone","address")
        
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
