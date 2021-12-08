# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import subprocess


def exercise1():
    command = ["ffmpeg", "-flags2", "+export_mvs", "-i", "BBB_cut.mp4", "-vf", "codecview=mv=pf+bf+bb",
               "BBB_macrob_motionv.mp4"]  # showing motion vector and motion blocks
    subprocess.call(command)

    command2 = ["ffplay", "BBB_macrob_motionv.mp4"]  # we reproduce the cut we have done
    subprocess.call(command2)


def exercise2():
    original_input = "bbb.mp4"
    subprocess.call(["ffmpeg", "-ss", str(0), "-i", original_input, "-c",
                     "copy", "-t", str(60), "BBB_new_cut.mp4"])  # 1 minute cutting

    subprocess.call(["ffmpeg", "-i", "BBB_new_cut.mp4", "-vn", "-c:a",
                     "libmp3lame", "BBB_mp3_stereo.mp3"])  # mp3 stereo conversion

    subprocess.call(["ffmpeg", "-i", "BBB_new_cut.mp4", "-vn", "-c:a",
                     "aac", "-b:a", "64k", "BBB_aac.aac"])  # acc conversion

    subprocess.call(["ffmpeg", "-i", "BBB_new_cut.mp4", "-i", "BBB_mp3_stereo.mp3",
                     "-i", "BBB_aac.aac", "-c:v", "copy", "-c:a",
                     "copy", "-map", "0:0", "-map", "1:a", "-map", "2:a",
                     "BBB_all.mp4"])  # putting it all together

    command2 = ["ffplay", "BBB_all.mp4"]  # we reproduce what we have done
    subprocess.call(command2)


def exercise4():
    command = ["ffmpeg", "-i", "BBB_new_cut.mp4", "-vf",
               "subtitles=TomHollandSubtitles.srt", "BBB_sub.mp4"]  # we put the subtitles on the video
    subprocess.call(command)
    command2 = ["ffplay", "BBB_sub.mp4"]  # we reproduce what we have done
    subprocess.call(command2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    opt = int(input("Please, select the exercise you want"
                    "\n\n\t 1 -Macroblocks and Motion vectors"
                    "\n\n\t 2 -BBB container"
                    "\n\n\t 3 -Broadcasting standard"
                    "\n\n\t 4 -Spider-man Subtitles  \n\n\t"))

    if opt == 1:
        exercise1()
    elif opt == 2:
        exercise2()
    elif opt == 3:
        print("Sorry, did not know how to implement it:(")
    elif opt == 4:
        exercise4()

    else:
        print("Please, choose a correct number")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
