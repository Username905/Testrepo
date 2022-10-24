prisoner_245 = {
    "Name" : "Areg",
    "Lastname" : "Shahumyan",
    "Age" : 19,
    "Birthday" : 11.02,
    "Year" : 2003,
    "Height" : 182,
    "Eyes" : "Brown",
    "Hair" : "Dark",
    "Convicted" : "Fight",
    "Term" : "6 Months",
    "Article" : 116,
    "Prison" : "KOSH"
}

prisoner_245.update({"Name" : "Narek"})
prisoner_245.update({"Lastname" : "Alaverdyan"})
prisoner_245.update({"Age" : 20})
prisoner_245.update({"Birthday" : 27.07})
prisoner_245.update({"Year" : 2002})
prisoner_245.update({"Height" : 175})
prisoner_245.update({"Eyes" : "Green"})
prisoner_245.update({"Hair" : "Ginger"})
prisoner_245["Convicted"] = "None"
prisoner_245["Term"] = "None"
prisoner_245["Article"] = "None"
prisoner_245["Prison"] = "None"
print(prisoner_245)