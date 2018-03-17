from django.views import generic


class MainPageView(generic.TemplateView):
    template_name = 'main_page.html'


class ContactsView(generic.TemplateView):
    template_name = 'contacts.html'


class ProfileView(generic.TemplateView):
    template_name = 'profile.html'
