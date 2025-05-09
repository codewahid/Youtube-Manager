import json
def get_videos():
    try:
        with open('data.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def save_all_videos(video):
    with open('data.txt','w') as file:
        json.dump(video,file)
        

def list_videos(videos):
    print('\n')
    print('*' * 70)
    for index,video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, Duraion: {video['time']}")
    print('\n')
    print('*' * 70)

def add_video(videos):
    name = input("Enter your video name: ")
    time = input("Enter your video time: ")
    videos.append({'name': name, 'time': time})
    save_all_videos(videos)



def update_video(videos):
    list_videos(videos)
    index =int(input("Enter the Video Index to update"))
    if 1 <= index <= len(videos):
        name = input("Enter New Video Name: ")
        duration = input("Enter New Video Duration: ")
        videos[index-1] = {'name': name, 'time': duration}
        save_all_videos(videos)
    else:
        print("Invalid Input")

def delete_video(videos):
    list_videos(videos)
    index =int(input("Enter the Video Index to delete"))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_all_videos(videos)
    else:
        print("Invalid Input")

    
def main():
    while True:
        videos = get_videos()
        print("1. All Videos List")
        print("2. Add a Video")
        print("3. Update a video")
        print("4. Delete a video")
        chioce = input("Give your chioce : ")
        match chioce:
            case '1':
                list_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case _:
                return
            
if __name__ == '__main__': main()
        