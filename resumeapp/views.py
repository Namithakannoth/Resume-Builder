from django.shortcuts import render,redirect
from resumeapp.models import Resume
from easy_pdf.views import PDFTemplateResponseMixin
from django.views.generic import DetailView


# Create your views here.

def fetchResumeData(request,id):
    resumedetail = Resume.objects.get(id=id)
    context = {
        'resumedetail': resumedetail
    }
    return render(request, "resume.html", context)



class PDFUserDetailView(PDFTemplateResponseMixin, DetailView):
    model = Resume
    template_name = 'user_detail.html'

def home(request):
    resume = Resume.objects.all()
    context = {
        'resume': resume
    }
    return render(request, "home.html", context)


def createResume(request):
    if request.method == "POST":
        myname = request.POST.get('name')
        myage = request.POST.get('age')
        myemail = request.POST.get('emailid')
        myphone = request.POST.get('phoneno')
        mygender = request.POST.get('gender')
        myaddress = request.POST.get('address')
        mydob = request.POST.get('dob')
        mytechnical = request.POST.get('technicalskills')
        myprojects = request.POST.get('projects')
        myinternship = request.POST.get('internship')
        myschoolname = request.POST.get('schoolname')
        myschoolqualification = request.POST.get('schoolqualification')
        myschoolduration = request.POST.get('schoolduration')
        myschoolpercentage=request.POST.get('schoolpercentage')
        mycollegename = request.POST.get('collegename')
        mycollegequalification = request.POST.get('collegequalification')
        mycollegeduration = request.POST.get('collegeduration')
        mycollegepercentage=request.POST.get('collegepercentage')
        mygraduatecollegename = request.POST.get('graduatecollegename')
        mygraduatecollegequalification = request.POST.get('graduatecollegequalification')
        mygraduatecollegeduration = request.POST.get('graduatecollegeduration')
        mygraduatepercentage=request.POST.get('graduatepercentage')
        myhobbies = request.POST.get('hobbies')
        mylanguages = request.POST.get('languages')
        mynationality = request.POST.get('nationality')
        mycertification = request.POST.get('certification')
        mystate = request.POST.get('state')
        mymarital = request.POST.get('maritalstatus')
        mysummary = request.POST.get('summary')

        r = Resume(name=myname, age=myage, emailid=myemail, gender=mygender, phoneno=myphone,
                   address=myaddress, dob=mydob, technicalskills=mytechnical, projects=myprojects,
                   internship=myinternship, schoolname=myschoolname, schoolqualification=myschoolqualification,
                   schoolduration=myschoolduration,schoolpercentage=myschoolpercentage, collegename=mycollegename, collegequalification=mycollegequalification,
                   collegeduration=mycollegeduration,collegepercentage=mycollegepercentage, graduatedcollegename=mygraduatecollegename,
                   graduatequalification=mygraduatecollegequalification, graduateduration=mygraduatecollegeduration,graduatepercentage=mygraduatepercentage,
                   hobbies=myhobbies, languagesknown=mylanguages, nationality=mynationality, certification=mycertification,
                   state=mystate, maritalstatus=mymarital, summary=mysummary)
        r.save()
        return redirect("/home")

    return render(request, "create.html")