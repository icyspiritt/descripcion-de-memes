meme = {
  "XDD":"algo entre raro y gracioso"
  "REAL":"algo con lo que te puedes relacionar"
}
word = input("palabra?:").upper()
if word in meme.keys():
  print(meme[word])
else:
  print("palabra no encontrada")
