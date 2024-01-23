from django.contrib import messages
from django.shortcuts import render
from job_application.forms import ApplicationForm
from .models import Form
from django.core.mail import EmailMessage


def index(request):
    if request.method == "POST":
        # ApplicationForm is inherited all features from forms.Form that's why we need to add argument
        form = ApplicationForm(request.POST)
        # Check form is exist
        if form.is_valid():
            # cleaned_data extract only value from dictionary , user input
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]
            # Add user input to our db using object method
            Form.objects.create(first_name=first_name, last_name=last_name, email=email,
                                date=date, occupation=occupation)

            # Message configuration
            message_body = f"A new job application was submitted. Thank you.\n{first_name} {last_name}"
            email_message = EmailMessage("Form submission confirmation.", message_body, to=[email])
            email_message.send()

            messages.success(request, "Form submitted successfully")
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact_us.html')
