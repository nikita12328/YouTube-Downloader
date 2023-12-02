from pytube import YouTube
from tqdm import tqdm
from pytube import Playlist
from pytube.cli import on_progress
import os


def download_video():
    video_link = input('[/] Enter the link for download: ')
    video = YouTube(video_link, on_progress_callback=on_progress)
    video.streams.get_highest_resolution().download()


def download_playlist():
    playlist = Playlist(input('[/] Enter the link for download: '))
    folder_name = f'videos/{playlist.title}'
    if not os.path.exists(folder_name):
        os.mkdir('videos')
        os.mkdir(folder_name)
        print(f'Folder created: {folder_name}')
    else:
        print(f'Folder already exists: {folder_name}')
    print(f'Downloading playlist: {playlist.title}')
    print(f'Videos in playlist: {playlist.length}')

    with tqdm(total=playlist.length) as pbar:
        for video in playlist.videos:
            pbar.update(1)
            print(f'Downloading: {video.title}')
            video.streams.get_highest_resolution().download(output_path=folder_name)


def main():
    while True:
        print('├── MENU:')
        print('\t├── 1 - Video download')
        print('\t├── 2 - Playlist download')
        print('\t└── 0 - Exit')

        menu_choice = input('\nEnter your choice: ')

        match menu_choice:
            case '1':
                download_video()
            case '2':
                download_playlist()
            case '0':
                print('Good choice :)')
                break
            case _:
                print('*' * 30)


if __name__ == '__main__':
    main()
