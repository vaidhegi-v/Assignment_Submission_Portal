# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User, Assignment
import jwt
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

secret_key = "user"


def home(request):
    return render(request, 'home.html')

class RegisterUser(APIView):
    def get(self, request):
        if request.method == "POST":
            us = request.POST.get('username')
            pw = request.POST.get('password')
            return render(request,'login.html')
        elif request.method == "POST":
            ad = request.POST.get('is_admin')
            return render(request,'admin.html')
        return render(request, 'register.html')

class LoginUser(APIView):
    def get(self, request):
        return render(request, 'login.html')

class UploadAssignment(APIView):
    def get(self, request):
        return render(request, 'upload.html')

@login_required
def admin_assignments(request):
    admin_username = request.user.username
    assignments = Assignment.objects.filter(admin=admin_username)
    
    context = {
        'admin_username': admin_username,
        'assignments': assignments
    }
    return render(request, 'admin_assignments.html', context)

def accept_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    assignment.status = 'Accepted'
    assignment.save()
    
    context = {
        'assignment': assignment
    }
    return render(request, 'accept_assignment.html', context)

def reject_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)
    assignment.status = 'Rejected'
    assignment.save()
    
    context = {
        'assignment': assignment
    }
    return render(request, 'reject_assignment.html', context)

def generate_token(username):
    token = jwt.encode({'username': username}, secret_key, algorithm='HS256')
    return token
