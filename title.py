'''
We will use the art by Joan Stark as the logo:
           ____()()
          /      @@
jgs `~~~~~\_;m__m._>o

Game Title

Name: Bassam Batch
SID: 310229251
unikey: bbat2575

'''

def main():
      title = 'Mousehunt'
      
      logo = '''
       ____()()
      /      @@
`~~~~~\_;m__m._>o'''
      
      author = 'An INFO1110/COMP9001 Student'

      credits = f'''
Inspired by Mousehunt© Hitgrab
Programmer - {author}
Mice art - Joan Stark and Hayley Jane Wakenshaw
'''

      print(f"{title}\n{logo}\n{credits}")


# Using the following condition so that file is not automatically run when imported
if __name__ == '__main__':
      main()
