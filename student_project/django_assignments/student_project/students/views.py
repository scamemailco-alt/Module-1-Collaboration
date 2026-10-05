from django.shortcuts import render


def student_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        student_id = request.POST.get('student_id', '').strip()
        major = request.POST.get('major', '')
        standing = request.POST.get('standing', '')
        languages = request.POST.getlist('languages')
        grad_year = request.POST.get('grad_year', '')
        comments = request.POST.get('comments', '').strip()

        if not name:
            return render(request, 'students/form.html', {
                'error': 'Student Name cannot be blank.',
                'name': name,
                'student_id': student_id,
            })

        if not student_id:
            return render(request, 'students/form.html', {
                'error': 'Student ID cannot be blank.',
                'name': name,
                'student_id': student_id,
            })

        context = {
            'name': name,
            'student_id': student_id,
            'major': major,
            'standing': standing,
            'languages': ', '.join(languages) if languages else 'None selected',
            'grad_year': grad_year,
            'comments': comments,
        }
        return render(request, 'students/results.html', context)

    return render(request, 'students/form.html')


def student_results(request):
    return render(request, 'students/results.html')