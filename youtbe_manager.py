import sqlite3

conn = sqlite3.connect('youtbe_manger.db')
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL,
               url TEXT NOT NULL
               )
""")    
        

def list_videos():
    print('\n')
    print('*' * 70)
    cursor.execute("SELECT * FROM videos")
    for video in cursor:
        print(f"{video}")
    print('\n')
    print('*' * 70)

def add_video(name,time,url):
    cursor.execute("INSERT INTO videos (name,time,url) VALUES (?,?,?)",(name,time,url))
    conn.commit()
    

def update_video(Video_Id,name,time,url):
    cursor.execute("UPDATE videos SET name = ?, time = ? , url = ? WHERE id = ?",(name,time,url,Video_Id))
    conn.commit()

def delete_video(video_Id):
    cursor.execute("DELETE FROM videos WHERE id = ?",(video_Id,))

    
def main():
    while True:
        print("1. All Videos List")
        print("2. Add a Video")
        print("3. Update a video")
        print("4. Delete a video")
        chioce = input("Give your chioce : ")
        if chioce == '1':
            list_videos()
        elif chioce == '2':
            name = input("Enter the Video name : ")
            time = input("Enter the Video time : ")
            url = input("Enter the Video URL : ")
            add_video(name, time, url)
        elif chioce == '3':
            list_videos()
            video_Id = input("Enter the VIDEO ID to Update : ")
            name = input("Enter the Video name : ")
            time = input("Enter the Video time : ")
            url = input("Enter the Video URL : ")
            update_video(video_Id,name, time, url)
        elif chioce == '4':
            list_videos()
            video_Id = input("Enter the VIDEO ID to Delete : ")
            delete_video(video_Id)
        else: 
            print("Invalid Input")
    conn.close()

            
if __name__ == '__main__': main()
        