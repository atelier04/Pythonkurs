import tkinter as tk
from tkVideoPlayer import TkinterVideo

video_list = ["Tom_and_Jerry_A_Night_Before_Christmas.mp4", "KriechendeSchnecke.mp4", "Schneeballblume.mp4"]

video: TkinterVideo = None

count = 0


def forward_video():
    global video
    if video is not None:
        video.destroy()
    video = TkinterVideo(master=root, scaled=True)
    global count

    count = count + 1
    if len(video_list)-1 >= count >= 0:
        video.load(video_list[count])
        print(f"count {count}")

        video.grid(row=0,columnspan=2,ipadx=190, ipady=100, padx=30)
        video.play()
    else:
        count = 0
        video.load(video_list[count])
        video.grid(row=0,columnspan=2,ipadx=190, ipady=100, padx=30)
        video.play()


def backward_video():
    global video
    if video is not None:
        video.destroy()
    global count
    count = count -1
    video = TkinterVideo(master=root, scaled=True)
    if len(video_list)-1 >= count >= 0:
        video.load(video_list[count])
        video.grid(row=0,columnspan=2,ipadx=190, ipady=100, padx=30)
        video.play()
    else:
        count = len(video_list) - 1
        print(f"{count}")
        video.load(video_list[count])
        video.grid(row=0,columnspan=2,ipadx=190, ipady=100, padx=30)
        video.play()


def pause():
    global video
    if not video.is_paused():
        video.pause()


def play():
    global video
    if video.is_paused():
        video.play()


root = tk.Tk()
root.title("Video Slider")
root.geometry("600x600")
video = TkinterVideo(master=root, scaled=True)
video.load(video_list[0])
video.grid(row=0,columnspan=2,ipadx=190, ipady=100, padx=30)
video.play()
button_forward = tk.Button(root, text=">>", command=forward_video)
button_forward.grid(column=0, row=1, ipady=20,ipadx=112, pady=20, padx=10)
button_backward = tk.Button(root, text="<<", command=backward_video )
button_backward.grid(column=1, row=1, ipady=20, ipadx=108, padx=10)

# Pause Button
button_pause = tk.Button(root, text="Pause", command=pause)
button_pause.grid(column=0, row=2,ipady=20,ipadx=105, padx=10)

button_play = tk.Button(root, text="Play", command=play)
button_play.grid(column=1, row=2,ipady=20,ipadx=105, padx=10)

root.resizable(height=False, width=False)
root.mainloop()
