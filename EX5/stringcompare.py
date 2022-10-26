n = "076432165"
wa_nr = "0764320165"
wa_nrs = ["0781111119", "0792653913", "0797763139", "0792793193", "0781139022", "0764320165"]
possible_nrs_for_juliet = []


#print("076432165" in "0764320165")
print(possible_nrs_for_juliet)

def arePhoneNumbersEquivalent(phone1, phone2):
    return phone1.replace('/[^0-9]+/g', '') == phone2.replace('/[^0-9]+/g', '')