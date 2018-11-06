from django.shortcuts import render,get_object_or_404

from .models import Person, File



def index(request):
    context = {}
    return render(request,'ancestors/home.html',context)

def search_person(request):
    filter = request.GET.get('search')
    personsByName = Person.objects.filter(name__icontains=filter)
    personsBySurname = Person.objects.filter(surname__icontains=filter)
    personsByIdNumber = Person.objects.filter(id_number__icontains=filter)
    context = {
        "personsByName":personsByName,
        "personsBySurname": personsBySurname,
        "personsByIdNumber": personsByIdNumber
    }

    return render(request, 'ancestors/search_results.html', context)

def show_person(request,person_id):
    person = get_object_or_404(Person,pk=person_id)

    context = {"person":person}
    return render(request, 'ancestors/person_details.html', context)


def show_file(request,person_id,file_id):
    person = get_object_or_404(Person,pk=person_id)
    file = get_object_or_404(File,pk=file_id)

    context = {"file":file}
    return render(request, 'ancestors/file_details.html',context)
