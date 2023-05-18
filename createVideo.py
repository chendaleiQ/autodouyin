import os  # python标准库，不需要安装，用于系统文件操作相关
import cv2  # python非标准库，pip install opencv-python 多媒体处理
from PIL import Image  # python非标准库，pip install pillow，图像处理
import moviepy.editor as mov  # python非标准库，pip install moviepy，多媒体编辑
from moviepy.editor import VideoFileClip, AudioFileClip

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import cv2
import os

def images_to_video(images_folder:str, video_name:str, duration:int=30):
    """
    将一系列图片转换为视频

    Args:
        images_folder (str): 包含图片文件的文件夹路径
        video_name (str): 输出视频的名称
        duration (int, optional): 视频时长（秒）. Defaults to 5.

    Returns:
        None
    """
    # 获取所有图片文件的路径
    image_files = [os.path.join(images_folder, f) for f in os.listdir(images_folder) if f.endswith('.png')]
    image_files.sort() # 按文件名排序

    # 计算总帧数
    fps = len(image_files) / duration
    total_frames = int(fps * duration)

    # 读取第一张图片，获取图像大小信息
    img = cv2.imread(image_files[0])
    height, width, channels = img.shape

    # 创建视频写入器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    # 逐帧写入视频
    for i in range(total_frames):
        image_file = image_files[int(i * len(image_files) / total_frames)]
        img = cv2.imread(image_file)
        out.write(img)

    # 释放视频写入器并销毁所有窗口
    out.release()
    cv2.destroyAllWindows()


def add_audio_to_video(video_path:str, audio_path:str, output_path:str):
    # 读取视频和音频文件
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)

    # 提取音频子剪辑使其长度与视频一致
    if audio_clip.duration > video_clip.duration:
        start_time = 0
        end_time = video_clip.duration
        temp_audio_path = './temp_audio.mp3'
        ffmpeg_extract_subclip(audio_path, start_time, end_time, targetname=temp_audio_path)
        audio_clip = AudioFileClip(temp_audio_path)
    else:
        start_time = 0
        end_time = audio_clip.duration
        video_clip = video_clip.subclip(start_time, end_time)

    # 合并音频和视频
    video_with_audio = video_clip.set_audio(audio_clip)

    # 保存输出文件
    video_with_audio.write_videofile(output_path)

    # 删除临时文件
    if 'temp_audio_path' in locals():
        os.remove(temp_audio_path)



images_to_video('./output', './media.mp4')
add_audio_to_video('./media.mp4','./bgm.mp3','./output/music_video.mp4')