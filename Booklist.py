from matplotlib import pyplot as plt
bookdict = {"Divine Comedy" : 928, "Alice in Wonderland" : 130, "The Phantom Tollbooth" : 272,
 "The Tempest" : 80, "Josefine" : 132, "The Importance of Being Earnest" : 64,
  "Moby Dick" : 378, "Oliver Twist" : 262, "For Esme" : 100, "The Crying of Lot 49" : 194,
  "La Peste" : 320, "The Vane Sisters" : 300, "The U.S.A. Trilogy" : 1500,
  "Mrs Dalloway" : 224, "Madame Bovary" : 384, "Orlando": 384, "Wuthering Heights" : 500,
  "The Hunchback of Notre Dame" : 600, "King Lear" : 144, "The Vicar of Wakefield" : 112,
  "The Bear's Famous Ivasion" : 150, "Anna Karenina" : 600, "Waiting for Godot" : 128,
  "Native Son" : 554, "The Odyseey" : 541, "Robinson Crusoe" : 158, "Walden" : 196,
  "Doctor Faustus" : 160, "Lolita" : 317}
sum = 0
numlist = []
for i in bookdict:
    sum += bookdict[i]
    numlist.append(bookdict[i])
print(sum)
plt.hist(numlist, color = "c")
plt.show()
