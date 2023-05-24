import rollers
objektum_nevek = rollers.Eroller("AKAI F10",25,250) 
print(f"{objektum_nevek.ToString()}")


roller_nev = input("Kérem a roller nevét: ")
rollers_max_sb = int(input("Kérem a roller max sebességét: "))
roller_telj = int(input("Kérem a rolle teljesíményét: "))

eroller1 = rollers.Eroller(roller_nev,rollers_max_sb,roller_telj)
print(eroller1.ToString())

eroller1.szoveg_be_ki()