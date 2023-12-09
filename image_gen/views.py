from django.shortcuts import render
from .utils import generate_image

def generate_image_home(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt', '')
        try:
            generated_image_path = generate_image(prompt)
            return render(request, 'generate_image_home.html', {'generated_image_path': generated_image_path})
        except OSError as e:
            error_message = f"Image generation failed: {e}"
            return render(request, 'generate_image_home.html', {'error_message': error_message})
    else:
        return render(request, 'generate_image_home.html', {'generated_image_path': None})
