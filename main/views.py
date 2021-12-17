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


def fonp(request, comp_id):

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

    return render(request, 'main/fonp.html', context=context)


def poart(request, art_id):

    son = Song.objects.filter()

    exe = Execution.objects.filter(artist_id=art_id).filter(sco=0).order_by('workfield')

    u = 0
    i = 0
    for e in exe:
        e.workfield3 = i
        i = i + 1
        e.workfield1 = 1
        if u == e.song_id_id:
            e.workfield1 = 2
        u = e.song_id_id

    uu = Artist.objects.get(pk=art_id)

    pn = uu.name_artist + ' ' + uu.fam_artist

    comp = Composer.objects.filter()

    comp1 = Composer1.objects.filter()

    avt = Avtor_text.objects.all

    art = Artist.objects.filter(pk=art_id)

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

    return render(request, 'main/poart.html', context=context)


def fonpg(request):

    son = Song.objects.filter()

    exe = Execution.objects.filter(sco=0).order_by('workfield')

    u = 0
    i = 0
    for e in exe:
        e.workfield3 = i
        i = i + 1
        e.workfield1 = 1
        if u == e.song_id_id:
            e.workfield1 = 2
        u = e.song_id_id

    comp = Composer.objects.filter()

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
                }

    return render(request, 'main/fonpg.html', context=context)


def index01(request):

    #indexx()

    comp = Composer.objects.filter(sco=1).order_by('orderr')

    comp1 = Composer1.objects.filter()

    context = {
        'comp': comp,
        'comp1': comp1
              }

    return render(request, 'main/index01.html', context=context)


def fon(request):

    #indexx()

    comp = Composer.objects.filter(sco=1).order_by('orderr')

    comp1 = Composer1.objects.filter()

    art = Artist.objects.filter(sco=2)

    context = {
        'comp': comp,
        'art': art,
        'comp1': comp1
         }

    return render(request, 'main/fon.html', context=context)


def index02(request, exec_id):

    exe = Execution.objects.get(pk=exec_id)
    son = Song.objects.filter(name_song=exe.song_id)

    context = {
         'son': son,
         'exe': exe,
               }

    return render(request, 'main/index02.html', context=context)


def indexx():
    arr = Artist.objects.filter()
    for a in arr:
        a.sco = 0
        a.save()


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
            if cc.pk == c.pk:
                e.workfield2 = c.pk
                a = Artist.objects.get(pk=e.artist_id_id)
                dd = c.fam_composer[:20]+c.name_composer[:15]+str(s.name_song)[:40]
                e.workfield = dd + '9'
                e.sco = cc.sco
                if c.fam_composer.strip() == a.fam_artist.strip() and c.name_composer.strip() == a.name_artist.strip():
                    e.workfield = dd+'0'
                else:
                    if c.sco != 1:
                        a.sco = 2
                        a.save()

                e.save()
                s.workfield = s.workfield + 1
                s.save()

    return


def sco(request):
    return render(request, 'main/sco.html')
