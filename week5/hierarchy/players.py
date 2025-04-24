class Player:
    """Базовый класс для всех плееров, предоставляющий основные функции воспроизведения и остановки."""

    def __init__(self, brand: str) -> None:
        """
        Инициализация плеера.
        
        Параметры:
            brand (str): Бренд плеера.
        """
        self.brand = brand              # Публичное поле
        self._current_status = "stopped"  # Защищённое поле
        self.__battery_level = 100       # Приватное поле

    def play(self, source: str) -> None:
        """
        Начать воспроизведение источника.
        
        Параметры:
            source (str): Название или путь к источнику.
        """
        self._current_status = "playing"
        print(f"{self.brand} воспроизводит {source}.")

    def stop(self) -> None:
        """Остановить воспроизведение."""
        self._current_status = "stopped"
        print(f"{self.brand} остановлен.")

    def _charge_battery(self) -> None:
        """Зарядить батарею (внутренний метод)."""
        self.__battery_level = 100

    def get_battery_level(self) -> int:
        """Получить текущий уровень заряда батареи."""
        return self.__battery_level


class AudioPlayer(Player):
    """Класс аудиоплеера с поддержкой настройки эквалайзера."""

    def __init__(self, brand: str) -> None:
        super().__init__(brand)
        self._equalizer_mode = "default"  # Защищённое поле
        self.__supported_formats = ["MP3", "WAV"]  # Приватное поле

    def play(self, audio_file: str) -> None:
        """
        Воспроизвести аудиофайл.
        
        Параметры:
            audio_file (str): Путь к аудиофайлу.
        """
        super().play(audio_file)
        print(f"Режим эквалайзера: {self._equalizer_mode}.")

    def set_equalizer(self, mode: str) -> None:
        """
        Установить режим эквалайзера.
        
        Параметры:
            mode (str): Название режима (например, 'Rock', 'Jazz').
        """
        self._equalizer_mode = mode
        print(f"Эквалайзер настроен на режим '{mode}'.")


class VideoPlayer(Player):
    """Класс видеоплеера с поддержкой субтитров."""

    def __init__(self, brand: str) -> None:
        super().__init__(brand)
        self._resolution = "1080p"          # Защищённое поле
        self.__subtitle_language = "None"   # Приватное поле

    def play(self, video_file: str) -> None:
        """
        Воспроизвести видеофайл.
        
        Параметры:
            video_file (str): Путь к видеофайлу.
        """
        super().play(video_file)
        print(f"Разрешение: {self._resolution}.")

    def set_subtitles(self, language: str) -> None:
        """
        Включить субтитры.
        
        Параметры:
            language (str): Язык субтитров (например, 'Russian', 'English').
        """
        self.__subtitle_language = language
        print(f"Субтитры: {language}.")


class DvdPlayer(VideoPlayer):
    """Класс DVD-плеера с возможностью сохранения позиции воспроизведения."""

    def __init__(self, brand: str) -> None:
        super().__init__(brand)
        self._current_position = 0    # Защищённое поле
        self.__region_code = 2         # Приватное поле

    def play(self, dvd_disc: str) -> None:
        """
        Воспроизвести DVD-диск.
        
        Параметры:
            dvd_disc (str): Название диска.
        """
        super().play(dvd_disc)
        self._current_position = 0
        print(f"Регион диска: {self.__region_code}.")

    def stop(self) -> None:
        """Остановить воспроизведение и сохранить позицию."""
        super().stop()
        print(f"Позиция сохранена: {self._current_position}.")

    def eject_dvd(self) -> None:
        """Извлечь DVD-диск."""
        print("Диск извлечён.")
