extensions = [".gif", ".jpg" , ".jpeg", ".png", ".pdf", ".txt", ".zip"]

x = input("File name: ").strip()

def suffix(x):
    for suffix in extensions:
        if suffix in x:
            return f"image/{suffix[1:]}"
    
    return "application/octet-stream"

print(suffix(x))
    
