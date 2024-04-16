import pygame

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

# Sử dụng hàm play_audio để phát audio từ file
audio_file_path = "example.mp3"  # Đường dẫn tới file audio
play_audio(audio_file_path)
