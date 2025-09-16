"""
Person Models - Django Learning Guide

This module contains models for the Person/Student management system.
It demonstrates Django model concepts, relationships, and best practices.
"""

from django.db import models
from django.urls import reverse


class Faculty(models.Model):
    """
    Faculty model representing university faculties/departments.
    
    This demonstrates:
    - Basic model fields
    - String representation (__str__ method)
    - Model metadata (Meta class)
    """
    
    name = models.CharField(
        max_length=100, 
        help_text="Name of the faculty/department"
    )
    description = models.TextField(
        blank=True, 
        help_text="Description of the faculty"
    )
    established_date = models.DateField(
        null=True, 
        blank=True,
        help_text="Date when the faculty was established"
    )
    dean = models.CharField(
        max_length=100, 
        blank=True,
        help_text="Name of the faculty dean"
    )
    
    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"
        ordering = ['name']
    
    def __str__(self):
        """String representation of the faculty."""
        return self.name
    
    def get_absolute_url(self):
        """Get the URL for this faculty."""
        return reverse('faculty_detail', kwargs={'pk': self.pk})


class Student(models.Model):
    """
    Student model representing university students.
    
    This demonstrates:
    - Various field types (CharField, EmailField, DateField, etc.)
    - Foreign key relationships
    - Model validation
    - Custom methods
    """
    
    # Basic information
    first_name = models.CharField(
        max_length=50,
        help_text="Student's first name"
    )
    last_name = models.CharField(
        max_length=50,
        help_text="Student's last name"
    )
    email = models.EmailField(
        unique=True,
        help_text="Student's email address"
    )
    student_id = models.CharField(
        max_length=20,
        unique=True,
        help_text="Unique student identification number"
    )
    
    # Academic information
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        related_name='students',
        help_text="Faculty the student belongs to"
    )
    enrollment_date = models.DateField(
        help_text="Date when the student enrolled"
    )
    graduation_year = models.IntegerField(
        null=True,
        blank=True,
        help_text="Expected graduation year"
    )
    
    # Personal information
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        help_text="Student's date of birth"
    )
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        help_text="Student's phone number"
    )
    address = models.TextField(
        blank=True,
        help_text="Student's address"
    )
    
    # Status
    is_active = models.BooleanField(
        default=True,
        help_text="Whether the student is currently active"
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['last_name', 'first_name']
    
    def __str__(self):
        """String representation of the student."""
        return f"{self.first_name} {self.last_name} ({self.student_id})"
    
    def get_full_name(self):
        """Get the student's full name."""
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        """Get the URL for this student."""
        return reverse('student_detail', kwargs={'pk': self.pk})
    
    @property
    def age(self):
        """Calculate the student's age."""
        if self.date_of_birth:
            from datetime import date
            today = date.today()
            return today.year - self.date_of_birth.year - (
                (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
            )
        return None