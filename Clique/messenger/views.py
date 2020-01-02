from django.shortcuts import render

# Create your views here.
def inbox(request):
    return render(request, 'messenger/inbox.html')

def community(request):
    return render(request, 'messenger/inbox.html')






# This sets the post form to have the current logged in user. OVERRIDE
# def form_valid(self, form):
#     form.instance.author = self.request.user
#     return super().form_valid(form)
