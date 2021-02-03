from django.shortcuts import render, HttpResponse
def index(request):
    # if 'num_visits' in request.session:
    #     print('key exists!')
    # else:
    #     print("key 'key_name' does NOT exist")
    
    return render(request, 'index.html')

def resultsPage(request):
    print(f"{request.method}")
    print(request.POST)
    context = {
        'submitinfo': request.POST
    }
    return render(request, 'submit.html', context)

def on_refreshbutton_clicked(self, widget):
    self.webview.back()