import multiprocessing
import os
import subprocess

from typing import Callable
import matplotlib as mpl
import matplotlib.animation as anim


class MplAnimator(object):

    def __init__(self,
                 fig: mpl.pyplot,
                 animate: Callable[[int], None],
                 nframes: int,
                 filename: str,
                 fps: int = 60,
                 nproc: int = 4,
                 initialize: Callable[[], None] = lambda: None):

        """
        Animator for Matplotlib.Pyplot using multiprocessing
        """

        self.figure         = fig
        self.num_frames     = nframes
        self.num_fps        = fps
        self.name_outfile   = filename
        self.num_processes  = nproc
        self.func_animation = animate
        self.func_init      = initialize
        self.cwd            = os.path.dirname(os.path.realpath(__file__))

    def __create_file(self,
                      frame_start: int,
                      frame_stop: int,
                      file_part: int):

        moviewriter = anim.FFMpegWriter(fps=self.num_fps, codec='libx264')
        fname = self.cwd + "/p_{:02}.mp4".format(file_part)
        moviewriter.setup(self.figure, fname, dpi=100)

        for j in range(frame_start, frame_stop):
            self.func_animation(j)
            moviewriter.grab_frame()

        moviewriter.finish()

    def __multi_processing(self):
        list_processes = []
        num_partframes = int(self.num_frames / self.num_processes)
        for num_process in range(self.num_processes):
            list_processes.append(
                multiprocessing.Process(
                    target=self.__create_file,
                    args=(
                        num_partframes * num_process,
                        num_partframes * (num_process + 1),
                        num_process
                    )
                )
            )

            list_processes[num_process].start()
            print("started proc #{:02}, with frames {} to {}".format(
                num_process,
                num_partframes*num_process,
                num_partframes*(num_process+1)-1
            ))

        for process in list_processes:
            process.join()

    def __cleanup_files(self):

        str_parts = ""
        for i in range(self.num_processes):
            str_parts += "file " + self.cwd + "/p_{:02}.mp4".format(i) + "\n"

        with open(self.cwd +"/temp", 'w') as f:
            f.write(str_parts)

        cmd_concat = ["ffmpeg", "-f", "concat", "-safe", "0", "-i", "temp", "-y", "-c", "copy", "{}.mp4".format(self.name_outfile)]
        cmd_cleanup_parts = ["find", self.cwd, "-name", "p_[0-9][0-9].mp4", "-delete"]
        cmd_cleanup_temp = ['rm', self.cwd + '/temp']

        pipe = subprocess.Popen(cmd_concat)
        pipe.wait()

        subprocess.call(cmd_cleanup_parts)
        subprocess.call(cmd_cleanup_temp)

    def start(self):
        self.__multi_processing()
        self.__cleanup_files()