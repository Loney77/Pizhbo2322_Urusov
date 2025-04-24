from players import Player, AudioPlayer, VideoPlayer, DvdPlayer

def main():
    # Создание объектов
    audio = AudioPlayer("Sony Audio")
    video = VideoPlayer("Panasonic Video")
    dvd = DvdPlayer("Philips DVD")

    # Тестирование AudioPlayer
    audio.play("track.mp3")
    audio.set_equalizer("Rock")
    audio.stop()

    # Тестирование VideoPlayer
    video.play("movie.mp4")
    video.set_subtitles("Russian")
    video.stop()

    # Тестирование DvdPlayer
    dvd.play("The Matrix")
    dvd.stop()
    dvd.eject_dvd()

if __name__ == "__main__":
    main()
