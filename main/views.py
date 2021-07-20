from django.shortcuts import render
from .models import Composer
from .models import Composer1
from .models import Avtor_text
from .models import Artist
from .models import Translator
from .models import Song
from .models import Execution
from .models import Cvisit
from django.conf import settings


def index(request, comp_id):
    son = Song.objects.filter(comp_id=comp_id)

    exe = Execution.objects.filter(workfield2=comp_id).order_by('workfield')

    u = 0
    i = 0
    for e in exe:
        e.workfield3 = i
        i = i + 1
        e.workfield1 = 1
        if u == e.song_id_id:
            e.workfield1 = 2
        u = e.song_id_id

    uu = Composer.objects.get(pk=comp_id)

    pn = uu.name_composer + ' ' + uu.fam_composer

    comp = Composer.objects.filter(pk=comp_id)

    comp1 = Composer1.objects.filter()

    avt = Avtor_text.objects.all

    art = Artist.objects.all

    trans = Translator.objects.all

    context = {
        'comp': comp,
        'comp1': comp1,
        'avt': avt,
        'trans': trans,
        'art': art,
        'son': son,
        'exe': exe,
        'pn': pn
        }

    return render(request, 'main/index.html', context=context)


def index01(request):

        # indexx()

    si = Cvisit.objects.get(pk=1)

    if settings.SIGN_OF_VISIT == 0:

        settings.SIGN_OF_VISIT = 1

        si.count_visit = si.count_visit+1
       # si.save()

    si = Cvisit.objects.get(pk=1)

    comp = Composer.objects.filter().order_by('fam_composer')

    comp1 = Composer1.objects.filter()


    context = {
        'comp': comp,
        'comp1': comp1,
        'si': si,
        }

    return render(request, 'main/index01.html', context=context)

def index02(request,exec_id):
    exe = Execution.objects.get(pk=exec_id)
    context = {
        'exe': exe,
               }

    return render(request, 'main/index02.html', context=context)


def indexx():

    son = Song.objects.filter()
    for s in son:
        s.workfield = 0
        s.save()

    comp = Composer.objects.filter()

    for cc in comp:

        exe = Execution.objects.filter()
        for e in exe:
            s = Song.objects.get(pk=e.song_id_id)
            c = Composer.objects.get(pk=s.comp_id_id)

            e.workfield2 = c.pk
            e.workfield = c.fam_composer.strip() + str(s.name_song)
            e.save()
            s.workfield = s.workfield + 1
            s.save()

    return 0
