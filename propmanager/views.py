from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from propmanager.models import *


class PropertiesList(TemplateView):
    template_name = "PropertyList.html"

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('go_edit'):
            return HttpResponseRedirect(reverse('add-property'))
        elif self.request.POST.get('main_menu'):
            return HttpResponseRedirect(reverse('main-menu'))

    def get_context_data(self, room_id=None, **kwargs):
        all_properties = Property.objects.all()

        context = {'properties': all_properties}

        return context


class EditPropertyDetails(TemplateView):
    template_name = "edit.html"

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('edit'):
            property_id = int(self.kwargs['property_id'])

            owner_pk = int(request.POST.get("owner", None))
            owner = Owner.objects.get(pk=owner_pk)

            type_pk = request.POST.get("type", None)
            type = PropertyType.objects.get(pk=type_pk)
            value = request.POST.get("value", None)

            edited_property = Property.objects.get(pk=property_id)
            edited_property.owner = owner
            edited_property.value = value
            edited_property.property_type = type

            edited_property.save(update_fields=['owner', 'value', 'property_type'])
            messages.success(request, 'Property details was successfully updated')

            return HttpResponseRedirect(f'/edit_property/{property_id}/')

        if self.request.POST.get('delete'):
            property_id = int(self.kwargs['property_id'])
            Property.objects.get(pk=property_id).delete()
            messages.success(request, 'Property was successfully deleted')
            return HttpResponseRedirect(reverse('properties-list'))
        if self.request.POST.get('list'):
            return HttpResponseRedirect(reverse('properties-list'))

        if self.request.POST.get('main'):
            return HttpResponseRedirect(reverse('main-menu'))

    def get_context_data(self, property_id=None, **kwargs):
        selected_property = Property.objects.get(pk=property_id)
        all_owners = Owner.objects.all()

        # All owners final excludes the owner which is linked to selected property, so no duplicates are displayed.
        all_owners_final = all_owners.exclude(pk=selected_property.owner.pk)
        all_property_types = PropertyType.objects.all()
        # All properties final excludes the property type which is linked to selected property, so no duplicates are displayed.

        all_property_types_final = all_property_types.exclude(name=selected_property.property_type.name)

        context = {'property': selected_property,
                   'owners': all_owners_final,
                   'property_types': all_property_types_final
                   }
        return context


class MainMenu(TemplateView):
    template_name = "main.html"

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('list'):
            return HttpResponseRedirect('properties-list/')
        elif self.request.POST.get('add_new'):
            return HttpResponseRedirect('add-property/')


class AddProperty(TemplateView):
    template_name = "new_property.html"

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('create_property'):
            address1 = request.POST.get("address1", None)
            address2 = request.POST.get("address2", None)
            city_town = request.POST.get("city_town", None)
            county = request.POST.get("county", None)
            post_code = request.POST.get("post_code", None)

            location = request.POST.get("location", None)
            value = request.POST.get("value", None)

            owner_pk = int(request.POST.get("owner", None))
            owner = Owner.objects.get(pk=owner_pk)

            type_pk = request.POST.get("type", None)
            type = PropertyType.objects.get(pk=type_pk)

            Property.objects.create(address_line_1=address1, address_line_2=address2, city_town=city_town,
                                    county=county,
                                    post_code=post_code, location=location, property_type=type, value=value,
                                    owner=owner)
            messages.success(request,
                             f'Property with address: {address1} {address2} {city_town} {county} {post_code} was added to the system.')
            return HttpResponseRedirect(reverse('properties-list'))
        elif self.request.POST.get('main_menu'):
            return HttpResponseRedirect(reverse('main-menu'))


    def get_context_data(self, **kwargs):
        all_properties = Property.objects.all()
        all_owners = Owner.objects.all()
        all_property_types = PropertyType.objects.all()

        context = {'properties': all_properties,
                   'owners': all_owners,
                   'property_types': all_property_types,
                   }
        return context
