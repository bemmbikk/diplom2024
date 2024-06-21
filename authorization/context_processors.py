from .forms import UserRegisterForm

def register_form(request):
    form = UserRegisterForm()
    return {'register_form': form}
