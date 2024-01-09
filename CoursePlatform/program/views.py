from django.shortcuts import render, redirect, get_object_or_404

from program.forms import CourseModelForm, ModuleModelForm, LessonModelForm
from program.models import Course, Lesson, Module


def start_list_view(request):

    courses = Course.objects.all()
    modules = Module.objects.all()
    lessons = Lesson.objects.all()
    context = {'courses': courses,
               'modules': modules,
               'lessons': lessons,
               }
    return render(request, 'course/start_list.html', context)

# module_title = Module.objects.select_related('course').get(slug=slug).course.title
# {'course_title': module_title}
def detail_course_view(request, slug):
    course = Course.objects.get(slug=slug)
    modules = course.course.all()
    courses = Course.objects.all()
    context = {"course": course,
               'modules': modules,
               "courses": courses}

    return render(request, 'course/detail.html', context)

def create_course_view(request):

    form = CourseModelForm()
    context = {'form': form}

    if request.method == 'POST':
        form = CourseModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('start_list')
        else:
            context['form'] = form
    return render(request, 'course/create.html', context)


def update_course_view(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseModelForm(instance=course)
    if request.method == 'POST':
        form = CourseModelForm(request.POST, instance=course)

        if form.is_valid():
            form.save()
            return redirect('course_detail', course.slug)
        else:
            form = CourseModelForm(instance=course)
    context = {'form': form}

    return render(request, 'course/update.html', context)

def delete_course_view(request, slug):
    course = get_object_or_404(Course, slug=slug)

    if request.method == 'POST':
        course.delete()
        return redirect('course_detail', course.slug)

    context = {'course': course}
    return render(request, 'course/delete.html', context)


def detail_module_view(request, slug):
    module = get_object_or_404(Module, slug=slug)
    modules = Module.objects.all()
    context = {'module': module,
               'modules': modules
               # 'courses': courses
    }

    return render(request, 'module/detail.html', context)

def create_module_view(request):

    form = ModuleModelForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ModuleModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('start_list')
        else:
            context['form'] = form
    return render(request, 'module/create.html', context)


def update_module_view(request, slug):
    module = get_object_or_404(Module, slug=slug)
    form = ModuleModelForm(instance=module)
    if request.method == 'POST':
        form = ModuleModelForm(request.POST, instance=module)

        if form.is_valid():
            form.save()
            return redirect('module_detail', module.slug)
        else:
            form = ModuleModelForm(instance=module)
    context = {'form': form}

    return render(request, 'module/update.html', context)


def delete_module_view(request, slug):
    module = get_object_or_404(Module, slug=slug)

    if request.method == 'POST':
        module.delete()
        return redirect('start_list')

    context = {'module': module}
    return render(request, 'module/delete.html', context)



def detail_lesson_view(request, slug):
    lesson = Lesson.objects.select_related('module').get(slug=slug)
    course_title = lesson.module.course.title
    lessons = Lesson.objects.all()
    context = {'lesson': lesson,
               'lessons': lessons,
               'course': course_title}

    return render(request, 'lesson/detail.html', context)


def create_lesson_view(request):

    form = LessonModelForm()
    context = {'form': form}

    if request.method == 'POST':
        form = LessonModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('start_list')
        else:
            context['form'] = form
    return render(request, 'lesson/create.html', context)


def update_lesson_view(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)
    form = LessonModelForm(instance=lesson)
    if request.method == 'POST':
        form = LessonModelForm(request.POST, instance=lesson)

        if form.is_valid():
            form.save()
            return redirect('lesson_detail', lesson.slug)
        else:
            form = LessonModelForm(instance=lesson)
    context = {'form': form}

    return render(request, 'lesson/update.html', context)



def delete_lesson_view(request, slug):
    lesson = get_object_or_404(Lesson, slug=slug)

    if request.method == 'POST':
        lesson.delete()
        return redirect('start_list')

    context = {'lesson': lesson}
    return render(request, 'lesson/delete.html', context)