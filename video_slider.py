import tkinter as tk
from tkVideoPlayer import TkinterVideo
import pygame
from converter import get_audio_filename

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()

video_list = ["Tom_and_Jerry_A_Night_Before_Christmas.mp4", "Tom_And_Jerry_Casanova_Cat_part_1-573536.mp4",
              "Donald_Duck_-_The_Hockey_Champ_Part_2-590593.mp4"]

video: TkinterVideo = None

count = 0


def forward_video():
    global video
    if video is not None:
        video.destroy()
    video = TkinterVideo(master=root, scaled=True)
    pygame.mixer.music.unload()
    global count
    count = count + 1
    if len(video_list) - 1 >= count >= 0:
        video.load(video_list[count])
        video.grid(row=0, columnspan=2, ipadx=190, ipady=100, padx=30)
        play_audio(video_list[count])
        video.play()
    else:
        count = 0
        video.load(video_list[count])
        video.grid(row=0, columnspan=2, ipadx=190, ipady=100, padx=30)
        play_audio(video_list[count])
        video.play()


def backward_video():
    global video
    if video is not None:
        video.destroy()
    global count
    count = count - 1
    video = TkinterVideo(master=root, scaled=True)
    pygame.mixer.music.unload()
    if len(video_list) - 1 >= count >= 0:
        video.load(video_list[count])
        video.grid(row=0, columnspan=2, ipadx=190, ipady=100, padx=30)
        play_audio(video_list[count])
        video.play()
    else:
        count = len(video_list) - 1
        video.load(video_list[count])
        video.grid(row=0, columnspan=2, ipadx=190, ipady=100, padx=30)
        play_audio(video_list[count])
        video.play()


def pause():
    global video

    if not video.is_paused():
        video.pause()
        pygame.mixer.music.pause()


def play():
    global video
    if video.is_paused():
        video.play()
        pygame.mixer.music.unpause()


def play_audio(videosource):
    audiosource = get_audio_filename(videosource)
    pygame.mixer.music.load(audiosource)
    pygame.mixer.music.play()


def loop_video(event):
    global video
    pygame.mixer.music.unload()
    print("Audio stopped")


root = tk.Tk()
root.title("Video Slider")
root.geometry("600x600")
video = TkinterVideo(master=root, scaled=True)
video.load(video_list[0])
video.grid(row=0, columnspan=2, ipadx=190, ipady=100, padx=30)
play_audio(video_list[0])
video.play()
button_forward = tk.Button(root, text=">>", command=forward_video)
button_forward.grid(column=0, row=1, ipady=20, ipadx=112, pady=20, padx=10)
button_backward = tk.Button(root, text="<<", command=backward_video)
button_backward.grid(column=1, row=1, ipady=20, ipadx=108, padx=10)

# Pause Button
button_pause = tk.Button(root, text="Pause", command=pause)
button_pause.grid(column=0, row=2, ipady=20, ipadx=105, padx=10)

button_play = tk.Button(root, text="Play", command=play)
button_play.grid(column=1, row=2, ipady=20, ipadx=105, padx=10)

root.resizable(height=False, width=False)

video.bind('<<Ended>>', loop_video)
root.mainloop()
