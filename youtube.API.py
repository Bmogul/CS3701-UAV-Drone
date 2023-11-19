from pytube import YouTube

video1 = YouTube('https://youtu.be/DhmZ6W1UAv4')
video2 = YouTube('https://youtu.be/YrydHPwRelI')

video1.streams.get_highest_resolution().download(output_path='./videos', filename_prefix='drone1')
video2.streams.get_highest_resolution().download(output_path='./videos', filename_prefix='drone2')