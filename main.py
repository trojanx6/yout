import pytube
from os import system
class Tube():
    def __init__(self):
        """Video linki"""
        self.banner = """██    ██  ██████  ██    ██ ████████ 
 ██  ██  ██    ██ ██    ██    ██    
  ████   ██    ██ ██    ██    ██    
   ██    ██    ██ ██    ██    ██    
   ██     ██████   ██████     ██    
                                  """
        print(self.banner)
        self.link = str(input("video url:")).strip()


    def YouTube(self):
        try:
            main = pytube.YouTube(self.link)
            title = main.title
            view = main.views
            lenght = main.length ,"saniye"
            explanation = main.description
            download =main.streams.first()
            download.download(system("pwd"))
            print(f"""
<------------- YouTube ----------------->
[ + ] Video Title:> {title} <
[ + ] Video Views:> {view} <
[ + ] Video Second:> {lenght} <
[ + ] Video Explanation:> {str(explanation).strip()} <
<------------- YouTube ----------------->

  """)
        except Exception as cbk:
             print(cbk)


if __name__=="__main__":
    app = Tube()
    app.YouTube()




