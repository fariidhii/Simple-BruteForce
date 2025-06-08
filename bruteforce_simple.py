import pyzipper

def main():
    zip_path = input("Masukkan lokasi file ZIP: ")
    wordlist_path = input("Masukkan lokasi file wordlist: ")

    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as words:
        for candidate in words:
            pwd = candidate.strip()
            try:
                with pyzipper.AESZipFile(zip_path) as archive:
                    archive.extractall(pwd=pwd.encode('utf-8'))
                print(f"[BERHASIL] Password: {pwd}")
                return
            except Exception:
                print(f"[SALAH] {pwd}")

    print("Password tidak ditemukan di wordlist.")

if __name__ == "__main__":
    main() 