from django.db import models

from django.contrib import auth
from django.urls import reverse
from django.contrib.auth.models import User


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Calculation(models.Model):
    """Track a calculation and its results"""
    EQUATION_FIBONACCI = 'FIB'
    EQUATIONS = ((EQUATION_FIBONACCI, 'Fibonacci'),)

    STATUS_PENDING = 'PENDING'
    STATUS_ERROR = 'ERROR'
    STATUS_SUCCESS = 'SUCCESS'
    STATUSES = (
        (STATUS_PENDING, 'Pending'),
        (STATUS_ERROR, 'Error'),
        (STATUS_SUCCESS, 'Success'),
    )

    equation = models.CharField(max_length=3, choices=EQUATIONS)
    input = models.IntegerField()
    output = models.IntegerField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=8, choices=STATUSES)
    message = models.CharField(max_length=110, blank=True)

class ToDoList(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Item(models.Model):
	todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	complete = models.BooleanField()

	def __str__(self):
		return self.text