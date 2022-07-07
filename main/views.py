from django.shortcuts import render
from .models import Composer
from .models import Composer1
from .models import Avtor_text
from .models import Artist
from .models import Translator
from .models import Song
from .models import Execution
import socket

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

    art = Artist.objects.filter(pk=art_id)
    for a in art:
        t = a.fam_artist[0:1]
        if t in '12':
            pn = a.name_artist + ' ' + a.fam_artist[1:]
        else:
            pn = a.name_artist + ' ' + a.fam_artist

    son = Song.objects.filter()

    if t == "1":
        exe = Execution.objects.filter(note__contains="1").order_by('workfield')
    else:
        exe = Execution.objects.filter(artist_id=art_id).filter(sco=0).order_by('workfield')

    u = 0
    i = 0
    for e in exe:
        tt = e.note[0:1]
        if tt in '12':
            e.note = e.note[1:]
        e.workfield3 = i
        i = i + 1
        e.workfield1 = 1
        if u == e.song_id_id:
            e.workfield1 = 2
        u = e.song_id_id

    comp = Composer.objects.filter()

    comp1 = Composer1.objects.filter()

    avt = Avtor_text.objects.all

    if t == "1":
        art = Artist.objects.filter()
    else:
        art = Artist.objects.filter(pk=art_id)

    for a in art:
        tt = a.fam_artist[0:1]
        if tt in '12':
            a.fam_artist = a.fam_artist[1:]

    trans = Translator.objects.all

    context = {
        'comp': comp,
        'comp1': comp1,
        'avt': avt,
        'trans': trans,
        'art': art,
        'son': son,
        'exe': exe,
        't': t,
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
    if "DESKTOP" in socket.gethostname():
        indexx()

    comp = Composer.objects.filter(sco=1).order_by('orderr')

    comp1 = Composer1.objects.filter()

    context = {
        'comp': comp,
        'comp1': comp1
              }

    return render(request, 'main/index01.html', context=context)


def fon(request):

    if "DESKTOP" in socket.gethostname():
        indexx()

    comp = Composer.objects.filter(sco=1).order_by('orderr')

    comp1 = Composer1.objects.filter()

    art = Artist.objects.filter(sco=2)
    for a in art:
        t = a.fam_artist[0:1]
        if t in '12':
            a.fam_artist = a.fam_artist[1:]

    exe = Execution.objects.filter(sco=0)
    context = {
        'exe': exe,
        'comp': comp,
        'art': art,
        'comp1': comp1
         }

    return render(request, 'main/fon.html', context=context)


def index02(request, exec_id):
    avt = Avtor_text.objects.all
    exe = Execution.objects.get(pk=exec_id)
    son = Song.objects.filter(name_song=exe.song_id)

    context = {
         'avt': avt,
         'son': son,
         'exe': exe,
               }

    return render(request, 'main/index02.html', context=context)


def indexx():
    arr = Artist.objects.filter()
    for a in arr:
        a.sco = 0
        a.save()

    exe = Execution.objects.filter()
    for e in exe:

        a = Artist.objects.get(pk=e.artist_id_id)

        ll = a.fam_artist[0]

        if ll in "12" and not ("1" in e.note):
            e.note = '1'+e.note
            print()
            e.save()

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
