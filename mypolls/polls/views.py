from .forms import CreatePollForm
from .models import Poll, Option
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import OptionFormSet

def home(request):
    poll = Poll.objects.all()
    context = {
        'poll': poll,
    }
    return render(request, 'polls/home.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    options = Option.objects.filter(poll=poll_id)

    context = {
        'poll': poll,
        'options': options
    }
    return render(request, 'polls/results.html', context)

def vote(request, poll_id):
    options = Option.objects.filter(poll=poll_id)
    poll = Poll.objects.get(pk=poll_id)
    if poll.type == 'text':
        if request.method == 'POST':
            option_text = request.POST['answer']
            filtered_options = Option.objects.filter(poll=poll_id, text__iexact=option_text)
            if filtered_options.exists():
                option = filtered_options.first()
                option.count += 1
                option.save()
                return redirect('home')
            else:
                option = Option()
                option.poll = poll
                option.text = option_text
                option.count = 1
                option.save()
                return redirect('home')
    elif poll.type == 'select_one':
        if request.method == 'POST':
            option_id = request.POST['poll']
            option = Option.objects.get(pk=option_id)
            option.count += 1
            option.save()
            return redirect('results', poll_id)
    else:
        if request.method == 'POST':
            for option in options:
                option_value = request.POST.get(str(option.id))
                if option_value is not None:
                    option.count += 1
                    option.save()
            return redirect('results', poll_id)

    context = {
        'options': options,
        'poll': poll,
        'poll_type': poll.type
    }
    return render(request, 'polls/vote.html', context)

def create(request):
    if request.method == 'POST':
        poll_form = CreatePollForm(request.POST)
        if poll_form.is_valid():
            poll = poll_form.save()
            poll_id = poll.id
            if (poll.type == 'select_one') or (poll.type == 'select_multiple'):
                context = {
                    'poll_form': poll_form,
                    'poll': poll,
                    'poll_id': poll_id
                }
                return redirect('create_options', poll_id)
            else:
                return redirect('home')
    else:
        poll_form = CreatePollForm()

    context = {
        'poll_form': poll_form,
    }
    return render(request, 'polls/create.html', context)


def create_options(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    if request.method == 'POST':
        formset = OptionFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                text = form.cleaned_data.get('text')
                if text:
                    Option(text=text, poll=poll).save()
            return redirect('home')
    else:
        formset = OptionFormSet()

    context = {
        'formset': formset,
        'poll': poll
    }
    return render(request, 'polls/create_options.html', context)


