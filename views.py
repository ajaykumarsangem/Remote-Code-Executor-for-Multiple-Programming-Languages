from django.http import HttpResponse, JsonResponse
from django.contrib.auth import get_user_model, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
import json
from . import utils


User = get_user_model()

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            email = json_data.get("email")
            password = json_data.get("password")
            first_name = json_data.get("first_name")
            last_name = json_data.get("last_name")
            user_profile_image = utils.get_avatar()
            
            
            if email and password and last_name and first_name: 
                new_user = User.objects.create_user(email = email, password = password)
                new_user.first_name = first_name
                new_user.last_name = last_name
                new_user.user_profile_image = user_profile_image
                new_user.password = (make_password(password))
                new_user.save()
                login(request, new_user)
                response =  JsonResponse(utils.get_user_data(new_user), status=201)
                response.set_cookie('user', new_user.email, max_age=10000)
                return response
            
            else:
                return HttpResponse(e, status=400)
            
        except json.decoder.JSONDecodeError as e:
            return HttpResponse('Invalid JSON data', status=400)
    
@csrf_exempt
def login_user(request):
    if request.method == "POST":
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            email = json_data.get("email")
            password = json_data.get("password")
            
            if email and password:
                get_user = User.objects.get(email = email)
                user = check_password(password, get_user.password)
                print(user)
                if user is True:
                    login(request, get_user)
                    response = JsonResponse(utils.get_user_data(get_user))
                    response.set_cookie('user', get_user.email, max_age=10000)
                    return response
                else:
                    return HttpResponse("Invalid Credntials")
            else:
                return HttpResponse("email and password are required to be passed")
        except Exception as e: 
            return HttpResponse(e)
        
@csrf_exempt
def logout_user(request):
    if request.method == "POST":
        logout(request)
        return HttpResponse("Logout successful")
    
@csrf_exempt
def update_user(request):
    if request.method == "PUT":
        try:
            json_data = json.loads(request.body.decode('utf-8'))
            password = json_data.get("password")
            first_name = json_data.get("first_name")
            last_name = json_data.get("last_name")
            new_image = json_data.get("image")
            email = json_data.get("email")
            try:
                user = User.objects.get(email = email)
                if user is None:
                    return HttpResponse("User does not exist")
                if first_name is not None: 
                    user.first_name = first_name
                if last_name is not None:
                    user.last_name = last_name
                if new_image is not None: 
                    user.user_profile_image = new_image
                if password is not None:
                    user.set_password(password)
                user.save()
                login(request, user)
                response =  JsonResponse(utils.get_user_data(user), status=202)
                response.set_cookie('user', user.email, max_age=10000)
                return response
            except Exception as e:
                return HttpResponse(e)
            
        except:
            return HttpResponse("Invalid JSON data", status=400)
        
        
@csrf_exempt
def get_user_by_email(request):
    if request.method == "GET":
        try:
            email = request.GET.get('email', None)
            if email is not None:
                user = User.objects.get(email = email)
                print(user)
                return JsonResponse(utils.get_user_data(user), status=200)
            else:
                return HttpResponse("User does not exist")
        except Exception as e:
            print(e)
            return HttpResponse(e)        
        
        