from django.shortcuts import render, redirect

from app.forms.comment import CommentForm
from app.forms.pet import PetCreateForm
from app.models.comment import Comment
from app.models.like import Like
from app.models.pet import Pet
from app.views.shared import visualise_view


def pet_list(req):
    pets = Pet.objects.all()
    context = {
        'pets': pets
    }

    return render(req, 'pet_list.html', context=context)


def pet_detail(req, pk):
    pet = Pet.objects.get(pk=pk)

    if req.method == 'GET':
        comment_form = CommentForm()

        return visualise_view(req, comment_form, 'pet_detail.html', pet=pet)

    else:
        comment_form = CommentForm(req.POST)

        if comment_form.is_valid():
            comment = Comment()
            comment.comment = comment_form.cleaned_data['comment']
            comment.pet = pet
            comment.save()
            return redirect('pet detail', pk)

        return visualise_view(req, comment_form, 'pet_detail.html', pet=pet)


def pet_like(req, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like()
    like.pet = pet
    like.save()
    return redirect('pet list')


def pet_create(req):
    if req.method == 'GET':
        form = PetCreateForm()
        return visualise_view(req, form, 'pet_create.html')

    else:
        form = PetCreateForm(req.POST)

        if form.is_valid():
            form.save()
            return redirect('pet list')

        return visualise_view(req, form, 'pet_create.html')


def pet_edit(req, pk):
    pet = Pet.objects.get(pk=pk)
    if req.method == 'GET':
        form = PetCreateForm(instance=pet)

        return visualise_view(req, form, 'pet_edit.html')

    else:
        form = PetCreateForm(req.POST,
                             instance=pet)

        if form.is_valid():
            form.save()
            return redirect('pet detail', pk)

        return visualise_view(req, form, 'pet_edit.html')


def pet_delete(req, pk):
    pet = Pet.objects.get(pk=pk)

    if req.method == 'GET':
        context = {
            'pet': pet,
        }

        return render(req, 'pet_delete.html', context=context)
    else:
        pet.delete()
        return redirect('pet list')
