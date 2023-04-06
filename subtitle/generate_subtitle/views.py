from django.shortcuts import render
import os
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
import whisper
from whisper.utils import WriteSRT

# Create your views here. 

def generate_subtitles(request):
    if request.method == 'POST':

        #load the model
        model = whisper.load_model("small")

        #get the uploaded video file
        video_file = request.FILES['video']
        
        #create a path for the uploaded video
        video_path = os.path.join(os.getcwd(), video_file.name)
        
        #save the uploaded video to the media directory
        with open(video_path, 'wb+') as destination:
            for chunk in video_file.chunks():
                destination.write(chunk)
                
        #load audio from the video file
        audio = whisper.load_audio(video_path)

        #transcribe
        transcribe = model.transcribe(audio=audio, task='translate')

        #create subtitle directory
        subtitle_dir = os.path.join('media', 'subtitles')
        os.makedirs(subtitle_dir, exist_ok=True)
        
        #create subtitle file path
        subtitle_path = os.path.join(subtitle_dir, os.path.splitext(video_file.name)[0] + '.srt')

        #write srt object
        srt_writer = WriteSRT('')

        #write subtitles to file
        with open(subtitle_path, 'w', encoding="utf-8") as result:
            srt_writer.write_result(transcribe, result)

        #get the SRT file and create a file response to offer it for download
        with open(subtitle_path, 'rb') as srt_file:
            response = HttpResponse(srt_file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'attachment; filename="{os.path.basename(subtitle_path)}"'
            return response
    
    return render(request, 'upload_video.html')
