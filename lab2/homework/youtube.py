from youtube_dl import YoutubeDL

# options ={
#     'format': 'bestaudio/audio'
# }
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=WHK5p7JL7g4'])
# dl.download(['https://www.youtube.com/watch?v=wNVIn-QS4DE', 'https://www.youtube.com/watch?v=JZjRrg2rpic'])

# dl.download(['https://www.youtube.com/watch?v=JZjRrg2rpic'])
dl.download(['I hate you I love you'])
