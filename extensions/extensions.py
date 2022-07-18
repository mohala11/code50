def main():
    text = "File name: "
    file_name = str.lower(input(text).strip())
    result = check(file_name)
    print(result)


def check(file_name):
    if file_name.endswith(".gif"):
        return "image/gif"
    elif file_name.endswith(".jpg"):
        return "image/jpeg"
    elif file_name.endswith(".png"):
        return "image/png"
    elif file_name.endswith(".pdf"):
        return "application/pdf"
    elif file_name.endswith(".txt"):
        return "text/plain"
    elif file_name.endswith(".zip"):
        return "application/zip"
    else:
        return "application/octet-stream"


main()