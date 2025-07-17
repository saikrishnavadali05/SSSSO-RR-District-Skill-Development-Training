with open(r'C:\Users\saisr\OneDrive\Desktop\SSSSO-RR-District-Skill-Development-Training\may_2025_contributions\PY-M-27_Venkatapuram_Sai_Srujan_Submissions\The_Whisper_of_File_Modes.txt',"r+") as f:
    data=f.readlines()
    print("No of lines:",len(data))
    n=str(len(data))
    f.write(n)