o
    �,cH'  �                   @   sR  d dl Z d dlZd dlmZmZ d dlmZ dZdZdZ	dZ
dZd	Zd
ZdZe jZe �d� e j�e jd�Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zdd� Zedv r�e�  ee� eee
 �Z eee	 �Z!eee � d e v r�ee �Z"e#e"j$�D ]	\Z%Z&ee&e%� q�nee �Z&ee&� eee � ee�Zedv s^dS dS )!�    N)�YouTube�Playlist)�safe_filenamezG______________________________________________________________________
ue  
                     ⠀⣀⣀⣤⣤⣶⣶⣶⣶⣦⣴⣶⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣬⢿⣿⣿⣿⣿⣿⣿⡙⢿⣿⣿⣿⣿⣿⣶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⣷⡍⠻⢷⠿⢿⠿⢧⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣆⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣆⣰⣶⣆⣀⣾⣿⣿⣿⣿⣿⣿⣿⡿⠿⣥⣾⣿⡀⠀⠀⠀⠀
⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠘⠻⣿⣿⣿⣦⡀⠀⠀
⠀⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠻⣿⣿⣿⣿⣿⣿⣿⣏⣡⣼⣿⣦⣄⠘⢿⣿⣿⣿⣿⡄⠀
⠀⣬⣿⣃⢨⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣼⣿⣿⣿⣿⡷⠀
⠀⠹⣿⣽⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⢿⣿⣿⣿⠁⠀
⠀⠀⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣽⣿⣿⣿⣇⠀⠀⠀⠀⢸⣿⣿⣿⠂⠀
⠀⠀⢹⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⣿⣿⣿⣿⣿⣿⣿⣶⠦⠀⣼⣿⣿⣿⣀⡀
⠀⢰⣧⣼⣿⣿⣿⠃⠀⢀⣠⡀⠀⠀⠀⠀⠀⠀⣆⢸⣿⣿⣿⣿⣿⠿⣷⣶⣶⡄⠈⣿⣿⣿⣸⣿
⠀⠘⣿⣿⡞⣿⡏⠀⠚⠛⠉⠙⣧⡀⠀⠀⠈⣦⣻⣾⣿⣿⣻⣿⢏⡴⠋⠁⠀⠀⠀⣿⣿⣿⣿⡿
⠀⠀⠙⢠⣷⢿⣧⠀⠀⢲⣿⣶⣿⣿⣦⡀⢀⣾⣿⣿⣿⣯⣟⣷⣯⣷⣶⣶⣾⣿⣦⣿⡏⣿⡔⠁
⠀⠀⢠⡼⣧⠘⡏⠀⠀⠀⠁⢹⣂⣤⣼⡿⢻⡟⠻⣿⣿⣿⣿⣹⠯⠖⣁⣿⣿⣿⠛⢻⢃⣿⠷⠀
⠀⠀⠀⢣⡨⠿⠉⠀⠀⠀⠀⣀⣈⠉⠁⠀⠀⠀⠀⢿⡃⢸⣿⣿⣿⣿⣿⣿⠋⠉⠀⠈⠾⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡿⠷⠖⠀⠀⠀⠀⢻⣿⣿⣿⣭⣿⣻⣿⣿⣶⡤⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣯⣇⠀⠀⠀⠀⣀⠀⠀⢸⣿⠇⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⠘⣿⣿⣶⣦⣄⣉⠳⠤⣿⣾⣿⣿⣿⠿⣿⡿⢫⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣆⠀⠀⠸⣿⡄⠈⠙⠛⠟⢿⠿⠏⠛⠉⠀⢠⣿⠁⡾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣄⠀⠀⠹⣿⡓⠲⠤⠀⠀⢀⡤⠴⠞⣻⣿⠃⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠢⠀⠀⠹⣷⣄⡀⡀⣀⢠⢠⣶⣷⡿⠃⠀⢀⢰⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡆⠈⢆⠀⠈⢿⣿⣶⣾⣿⣿⣿⡿⠀⠀⢀⡏⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠘⣆⠀⢀⡈⣻⣿⣿⣿⣷⣦⡀⠀⣾⠇⣼⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠘⣆⠀⠙⠛⠛⣻⠿⣿⣿⠇⣼⡟⣲⠋⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠘⢦⣀⣀⣴⣧⣴⣿⣟⣼⣿⡷⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⣈⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣟⡛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀WHOAMI-XD⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⠁⠀⠀⠀⠀⠀⠀

      YOUTUBE VIDEO/PLAYLIST DOWNLOADER
zV for video, or A for audio : zWrite the link : zLoading, please wait...
zDONE !z0Type Q to exit or R to download another video : �RZyt_dlsc                  C   s&   t jdkrt �d�} d S t �d�} d S )N�nt�cls�clear)�os�name�system)�_� r   �/sdcard/Download/main.pyr   6   s   
r   c                 C   �"   t d| j�� d d� � d�� d S )Nu   ╔═ Video titled [�2   z] started downloading��print�title�upper��varr   r   r   �startdl=   �   "r   c                   C   �   t d� d S )Nu+   ╟──── Downloaded original file(s)�r   r   r   r   r   �finished_original_downloadA   �   r   c                   C   r   )Nu7   ╟──── Converting file(s) to the proper formatr   r   r   r   r   �startConvertingE   r   r   c                   C   r   )Nu*   ╟──── Converting file(s) is doner   r   r   r   r   �finishConvertingI   r   r   c                 C   r   )Nu   ╚═ Video titled [r   z] has been downloaded
r   r   r   r   r   �finishdlM   r   r   c                 C   s�   t | � | jjdd��d��� }|jtdd� t�  t�  d}t	�
d|j� dt|j�� d	|� �� t	�d|j� �� t�t� d
t|j�� d�t� d
t|j�� d�� t�  t| � d S )NT�Z
only_audio�abrz	original �Zfilename_prefix�-v error -hide_banner -nostatszffmpeg -i "original z" "z.mp3" �/z.mp3)r   �streams�filter�order_by�last�download�current_folderr   r   r	   r   �default_filenamer   r   �remove�shutil�move�dl_pathr   r   )r   Z	audiofile�optionsr   r   r   �
vid_to_audR   s   $0r1   c                 C   sn   t dkst dkr't| � | jjddd��d��� jt|� d�d� t| � d S t d	ks/t d
kr5t	| � d S d S )N�v�VZmp4T)Zsubtype�progressive�
resolutionz) r"   �a�A)
�
the_formatr   r%   r&   r'   r(   r)   r/   r   r1   )r   �video_indexr   r   r   �
dl_from_ple   s   *�r:   c              
   C   s�  t dkst dkr�| j}g }|jdd��d�D ]}|j|vr#|�|j� qtdt d � t|dd	i� td
�}tt� |jdd|d�}|rVt	| � |d �
t� t| � d S t	| � |jd|d��d��� }|j
dd� |jdd��d��� }|j
dd� t�  t�  t|j�}d|j� �}	d|j� �}
d}t�d|	� d|
� d|� d|� �� t�|	� t�|
� t�t� d|� d�t� d|� d�� t�  t| � d S t dks�t dkr�t| � d S d S )Nr2   r3   �video)�typer5   �
z,Here's all the available video resolutions :�sepz,    z"Choose a resolution (e.g. 1080p) :T)r<   r4   r5   r   )Z
only_videor5   Zfilesize_approxz
videofile r"   r    r!   z
audiofile r#   zffmpeg -i "z" -i "z" -c copy "z.mp4" r$   z.mp4r6   r7   )r8   r%   r&   r'   r5   �appendr   �	blankline�inputr   r)   r/   r   �firstr   r   r   r   r+   r	   r   r,   r-   r.   r*   r   r1   )r   Zall_streamsZvideo_resolutions�streamZchosen_resoZvideo_streamsZ	videoFileZ	audioFileZvideo_titleZinput_file_videoZinput_file_audior0   r   r   r   �dl_a_vido   sH   
�
"

$�rD   )r   �rzplaylist?list)'r	   r-   Zpytuber   r   Zpytube.helpersr   r@   ZwelcomeTextZvid_aud_msgZlink_msgZloading_msgZdone_msgZexit_msgZexit_command�curdirr*   �makedirs�path�joinr/   r   r   r   r   r   r   r1   r:   rD   r   rA   �urlr8   Zplaylist�	enumerateZvideosr9   r;   r   r   r   r   �<module>   sP   !

@��