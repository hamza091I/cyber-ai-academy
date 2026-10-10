from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Course, Enrollment
from .forms import EnrollmentForm, ContactForm

def home_view(request):
    courses = Course.article.all() if hasattr(Course, 'article') else Course.objects.all()[:3]
    context = {'courses': courses}
    return render(request, 'academy/home.html', context)

def courses_view(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'academy/courses.html', context)

def course_detail_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    context = {'course': course}
    return render(request, 'academy/course_detail.html', context)

def enroll_view(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully enrolled in the course!')
            return redirect('courses')
    else:
        form = EnrollmentForm()
    context = {'form': form}
    return render(request, 'academy/enroll.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Your message has been sent successfully. We will contact you soon!')
            return redirect('contact')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'academy/contact.html', context)