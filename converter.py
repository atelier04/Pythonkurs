from moviepy.editor import VideoFileClip


def convert_video_to_audio(moviesource: str):
    video = VideoFileClip(moviesource)
    audiosource = get_audio_filename(moviesource)
    video.audio.write_audiofile(audiosource)


def get_audio_filename(moviesource:str):
    dotindex = moviesource.index(".")
    audiosource =moviesource[:dotindex]
    return audiosource + ".mp3"

#convert_video_to_audio("Tom_and_Jerry_A_Night_Before_Christmas.mp4")
#convert_video_to_audio("Donald_Duck_-_The_Hockey_Champ_Part_2-590593.mp4")
