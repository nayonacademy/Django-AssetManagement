from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from assetapp.forms import DistributionForm
from .forms import MemberForm, AssetForm

from .models import Member, Asset, Distribution


# MEMBER LIST PAGE
def members(request):
    queryset = Member.objects.all()
    context = {
        "object_list": queryset,
        "title": "list"
    }
    return render(request, 'assetapp/members.html', context)


# ADD MEMBER LIST
def addmembers(request):
    form = MemberForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "form": form,
    }
    return render(request, 'assetapp/addmembers.html', context)


def membersupdate(request, id=None):
    instance = get_object_or_404(Member, id=id)
    form = MemberForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form,
        "instance": instance
    }
    return render(request, 'assetapp/addmembers.html', context)


# ASSET LIST
def assets(request):
    queryset = Asset.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'assetapp/assets.html', context)


# ADD ASSET
def addasset(request):
    form = AssetForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "form": form,
    }
    return render(request, 'assetapp/addasset.html', context)


# DISTRIBUTION

def distribution(request):
    form = DistributionForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form,
    }
    return render(request, 'assetapp/add_distribution.html', context)


def index(request):
    queryset = Distribution.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, 'assetapp/show_distribution.html', context)


def distributionupdate(request, id=False):
    instance = get_object_or_404(Distribution, id=id)
    form = DistributionForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form,
        "instance": instance
    }
    return render(request, 'assetapp/add_distribution.html', context)


def membersdetails(request, id):
    instance = get_object_or_404(Member, pk=id)
    context = {
        "title": "Hello",
        "more": instance
    }
    return render(request, 'assetapp/details.html', context)


def assetsdetails(request, id):
    instance = get_object_or_404(Asset, pk=id)
    context = {
        "title": "Hello",
        "more": instance
    }
    return render(request, 'assetapp/assetdetails.html', context)


def assetupdate(request, id=None):
    instance = get_object_or_404(Asset, id=id)
    form = AssetForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        "form": form,
        "instance": instance
    }
    return render(request, 'assetapp/addasset.html', context)


def membersdelete(request, id=None):
    instance = get_object_or_404(Member, id=id)
    # message.success(request, "Successfully Deleted")
    instance.delete()

    return render(request, 'assetapp/members.html')


def assetdelete(request, id):
    instance = get_object_or_404(Asset, id=id)
    # message.success(request, "Successfully Deleted")
    instance.delete()

    return redirect('assets')  # render(request, 'assetapp/assets.html')


def distributiondelete(request, id=None):
    instance = get_object_or_404(Distribution, id=id)
    instance.delete()
    return render(request, 'assetapp/show_distribution.html')
