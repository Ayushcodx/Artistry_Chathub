from django.http import HttpResponse
from django.shortcuts import render
from .utils import generate_image

def generate_image_home(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')  # Get the prompt from the form
        generated_image_content = generate_image(prompt)

        # Return the image content as an HTTP response
        return HttpResponse(generated_image_content, content_type="image/png")
    else:
        return render(request, 'generate_image_home.html', {'generated_image_path': None})
