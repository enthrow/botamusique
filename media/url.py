import youtube_dl
import variables as var


def get_url_info(index=-1):
    ydl_opts = {
        'noplaylist': True
    }
    var.playlist[index]['duration'] = 0
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        for i in range(2):
            try:
                print(var.playlist)
                info = ydl.extract_info(var.playlist[index]['url'], download=False)
                var.playlist[index]['duration'] = info['duration'] / 60
                var.playlist[index]['title'] = info['title']
            except youtube_dl.utils.DownloadError:
                pass
            except KeyError:
                return True
            else:
                return True
    return False
