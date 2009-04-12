from atento.contato.models import Contact
from django import forms
from django.shortcuts import render_to_response
 
def main(request):
 
  # initialize variables to sent to template
  message = ''
  submit_action = 'Add'
  edit_id = ''
 
  # generate default form
  ContactForm = forms.form_for_model(Contact)
  f = ContactForm()
 
  # handle edit and delete events
  if request.method == 'GET':
    if request.has_key('edit_id'):
      # replace default form with form based on row to edit
      contact = Contact.objects.get(pk=request.GET['edit_id'])
      ContactForm = forms.form_for_instance(contact)
      f = ContactForm()
      submit_action = 'Update'
      edit_id = request.GET['edit_id']
      message = 'Editing contact ID ' + request.GET['edit_id']
 
    if request.has_key('delete_id'):
      Contact.objects.get(pk=request.GET['delete_id']).delete()
      message = 'Contact deleted.'
 
  # handle add and update events
  if request.method == 'POST':
    if request.POST['submit_action'] == 'Add':
      # attempt to do add
      add_f = ContactForm(request.POST)
      if add_f.is_valid():
        add_f.save()
        message = 'Contact added.'
      else:
        # validation failed: show submitted values in form
        f = add_f
 
    if request.POST['submit_action'] == 'Update':
      # attempt to do update
      contact = Contact.objects.get(pk=request.POST['edit_id'])
      ContactForm = forms.form_for_instance(contact)
      update_f = ContactForm(request.POST.copy())
      if update_f.is_valid():
        update_f.save()
        message = 'Contact updated.'
      else:
        # validation failed: prepare form for new update attempt
        submit_action = 'Update'
        edit_id = request.POST['edit_id']
        f = update_f
 
  # get existing contacts
  contact_list = Contact.objects.all()
 
  # return rendered HTML page
  return render_to_response(
    'contacts.html',
    { 'request': request,
      'message': message,
      'contact_list': contact_list,
      'form': f.as_table(),
      'submit_action': submit_action,
      'edit_id': edit_id
    }
  )
