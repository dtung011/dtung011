from youtube_dl import YoutubeDL
dl = YoutubeDL()

#1 download single video:
# dl.download(['https://www.youtube.com/watch?v=yL0RzgUpGjk'])

#2 download multiple videos:
# dl.download(['https://www.youtube.com/watch?v=yL0RzgUpGjk','https://www.youtube.com/watch?v=tUWHyFpnIwE'])

#3 download only audio:
# options = {'format': 'bestaudio/audio'}
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=yL0RzgUpGjk'])

#4 search and then download the first video:
# options = {'default_search': 'ytsearch', 'max_downloads': 1}
# dl = YoutubeDL(options)
# dl.download (['porco rosso trailer'])

#5 search and then download the first video's audio:
options = {'default_search': 'ytsearch', 'max_downloads': 1, 'format': 'bestaudio/audio'}
dl = YoutubeDL(options)
dl.download (['Cant take my eyes of you'])