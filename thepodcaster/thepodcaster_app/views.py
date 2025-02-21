from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import logout
from django.db.models.query import Q
from . import extensions, models, rss_extension
from django.http import HttpResponse
import uuid

# Create your views here.
@login_required(login_url=reverse_lazy("login"))
def dashboard(request):
    return render(request, "thepodcaster_app/dashboard.html")

def index(request):
    return redirect(reverse_lazy("dashboard"))

@login_required(login_url=reverse_lazy("login"))
def log_out(request):
    logout(request)
    return redirect(reverse_lazy("index"))

@login_required(login_url=reverse_lazy("login"))
def shows(request):
    shows = models.Show.objects.filter(Q(user = request.user)).all()
    return render(request, "thepodcaster_app/shows.html", context={"shows":shows})

@login_required(login_url=reverse_lazy("login"))
def episodes(request):
    shows = models.Show.objects.filter(Q(user = request.user)).all()

    episodes: [models.Episode] = []
    for show in shows:
        episodes += models.Episode.objects.filter(Q(show=show)).all()
    return render(request, "thepodcaster_app/episodes.html", context={"episodes":episodes})

def get_rss(request, id):
    show = models.Show.objects.get(id=id)
    episodes = models.Episode.objects.filter(Q(show=show)).all()
    generated_rss = rss_extension.rss_generate_for_show(show, episodes)
    return HttpResponse(generated_rss, content_type='application/rss+xml')

@login_required(login_url=reverse_lazy("login"))
def add_show(request):
    if request.method == "POST" and request.FILES["cover_file"]:
        file = request.FILES["cover_file"]
        if not extensions.check_if_photo(file.name):
            return render(request, "thepodcaster_app/add_show.html", context={"error": "Invalid file type!"})
        new_filename = extensions.generate_uuid_namefile(file.name)
        fss = FileSystemStorage()
        fn = fss.save(new_filename, file)
        url = fss.url(fn)

        title = request.POST["title"]
        description = request.POST["description"]
        category = request.POST["category"]
        key_words = request.POST["keywords"]
        copyright = request.POST["copyright"]
        lang_code = request.POST["lang_code"]

        models.Show.objects.create(user = request.user,title=title, description=description, category=category, keywords= key_words, copyright=copyright, language=lang_code, cover_url = url)

        return redirect(reverse_lazy("dashboard"))
    else:
        return render(request, "thepodcaster_app/add_show.html")

@login_required(login_url=reverse_lazy("login"))
def add_episode(request):
    shows = models.Show.objects.filter(Q(user = request.user)).all()
    if request.method == "POST" and request.FILES["audio_file"]:
        file = request.FILES["audio_file"]
        mimetype = ""
        if extensions.check_if_mp3(file.name):
            mimetype = "audio/mpeg"
        elif extensions.check_if_wav(file.name):
            mimetype =  "audio/wav"
        else:
            return render(request, "thepodcaster_app/add_episode.html", context={"shows":shows, "error":"Invalid file format!"})
        
        filename = extensions.generate_uuid_namefile(file.name)
        filesize = len(file.read())
        duration = request.POST["duration"]
        title = request.POST["title"]
        description = request.POST["description"]
        guid = uuid.uuid4()
        show = models.Show.objects.get(id = request.POST["show_select"])

        fss = FileSystemStorage()
        f = fss.save(filename, file)
        url = fss.url(f)

        models.Episode.objects.create(show = show, title=title, description=description, media_url = url, media_size = filesize, media_type = mimetype, duration=duration, guid=guid)


        return redirect(reverse_lazy("dashboard"))
    else:
        return render(request, "thepodcaster_app/add_episode.html", context={"shows":shows})


class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']


class CreateAccountView(CreateView):
    form_class = CustomUserForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")