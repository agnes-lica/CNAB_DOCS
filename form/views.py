from django.shortcuts import render, redirect
from .form import UploadFileForm
from .utils import utils


def transactionsPage(request):
    
    stores = utils.db_stores()
            
    return render(request, 'transactionPage.html', {'stores': stores})

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            utils.handle_uploaded_file(request.FILES['file'])
            return redirect(transactionsPage)
    else:
        form = UploadFileForm()
        
    return render(request, 'upload.html', {'form': form})