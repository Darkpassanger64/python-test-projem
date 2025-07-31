def selam_ver(isim: str) -> str:
    """This function greets a name."""
    mesaj = f"Merhaba, {isim}!"
    print(mesaj)
    return mesaj


if __name__ == "__main__":
    selam_ver("Dünya")
